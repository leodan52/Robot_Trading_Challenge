import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf
from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime, timedelta, timezone

def main():

	robot = RobotTrading()

	robot.importar_base_bitcoin()
	robot.extraer_tendencias()
	robot.limpieza_datos()
	robot.tomar_decisiones()
	robot.visualizacion()

class RobotTrading:

	def __init__(self):
		self.__df_bitcoin = pd.DataFrame()
		self.__precio_actual = 0
		self.__tendencia = ''
		self.__media_bitcoin = 0
		self.__algoritmo_decision = ''

		self.__df_bitcoin_limpio = pd.DataFrame()
		self.__df_bitcoin_limpio_caja = pd.DataFrame()

	@property
	def precio_actual(self):
		return self.__precio_actual

	@property
	def decision(self):
		return self.__algoritmo_decision

	def ejecutar(self):
		self.importar_base_bitcoin()
		self.extraer_tendencias()
		self.limpieza_datos()
		self.tomar_decisiones()

	def importar_base_bitcoin(self):

		''' Importa el histórico de los precios del BitCoin de los últimos 7 días en intervalos de 5 minutos'''

		end_day = datetime.today()
		period = timedelta(days = 7)
		start_day = end_day - period

		ticker = yf.Ticker('BTC-USD')

		self.__df_bitcoin = ticker.history(start = start_day, end = end_day, interval = '5m')


	def extraer_tendencias(self):

		''' Extrae el precio actual y la tendencia a la 'baja' o a la 'alza' del BitCoin'''

		headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'}
		url = 'https://coinmarketcap.com/'

		respuesta = requests.get(url, headers)
		#print(respuesta.status_code)
		soup = BeautifulSoup(respuesta.content, features = 'lxml')

		filas = soup.find_all('tr')

		for f in filas:
			names = f.findAll('p', {'class' : "sc-4984dd93-0 kKpPOn"})
			actual_prices = f.findAll('div', {'class' : "sc-a0353bbc-0 gDrtaY"})
			tendencias = f.findAll('span', {'class' : "sc-d55c02b-0"})

			if not (len(names) == 1 and len(actual_prices) == 1 and len(tendencias) == 3):
				continue

			dict_datos = RobotTrading.__procesar(names[0], actual_prices[0], tendencias)

			if 'Bitcoin' in dict_datos:
				break

		try:
			self.__precio_actual = dict_datos['Bitcoin']['precio_actual']
			self.__tendencia = dict_datos['Bitcoin']['tendencia1h']
		except KeyError:
			print('Error al extraer precio actual y tendencia')

	@staticmethod
	def __procesar(nombre, precio_actual, tendencias) -> dict:

		clase_tendencia = {
			'icon-Caret-down' : 'baja',
			'icon-Caret-up' : 'alza'
		}

		salida = {
			nombre.text : {
			'precio_actual' : float(re.sub('[$,]', '', precio_actual.text)),
			'tendencia1h' : clase_tendencia[tendencias[0].span['class'][0]],
			'tendencia24h' : clase_tendencia[tendencias[1].span['class'][0]],
			'tendencia7d' : clase_tendencia[tendencias[2].span['class'][0]]
			}
  		}

		return salida

	def limpieza_datos(self):

		# Crear un duplicado
		df_bitcoin_limpio = self.__df_bitcoin.copy()

		# Tratar duplicados en el índice (Datetime)

		df_bitcoin_limpio = df_bitcoin_limpio[~df_bitcoin_limpio.index.duplicated()]

		#  Valores nulos en Close

		df_bitcoin_limpio = df_bitcoin_limpio[df_bitcoin_limpio.Close.notna()]

		# Valores de Volume mayores a 0

		df_bitcoin_limpio = df_bitcoin_limpio.query('Volume > 0')

		# Eliminar outliers

		Q1 = df_bitcoin_limpio.Close.quantile(0.25)
		Q3 = df_bitcoin_limpio.Close.quantile(0.75)
		IQR = Q3 - Q1
		min_close = Q1 - 1.5 * IQR
		max_close = Q3 + 1.5 * IQR

		self.__df_bitcoin_limpio = df_bitcoin_limpio.query('Close >= @min_close & Close <= @max_close')

		# Seleccionar los datos de Close entre Q1 y Q3
		self.__df_bitcoin_limpio_caja = df_bitcoin_limpio.query('Close >= @Q1 & Close <= @Q3')

		# Promedio de los datos de Close entre Q1 y Q3
		self.__media_bitcoin = self.__df_bitcoin_limpio_caja.Close.mean()

	def tomar_decisiones(self):

		if self.__precio_actual >= self.__media_bitcoin and self.__tendencia == 'baja':
			self.__algoritmo_decision = 'Vender'
		elif self.__precio_actual < self.__media_bitcoin and self.__tendencia == 'alza':
			self.__algoritmo_decision = 'Comprar'
		else:
			self.__algoritmo_decision = 'Mantener'

	def visualizacion(self, rango : str = '7d', qt : bool = False):

		color_legend = {
			'baja' : 'r',
			'alza' : 'g'
		}

		# Se agrega el promedio a una columna
		self.__df_bitcoin['Promedio'] = self.__media_bitcoin

		# Se calcula para obtener el histórico según `rango`
		hoy = self.__df_bitcoin.index.max()

		if rango.startswith('24h'):
			date_inicio = hoy - timedelta(days = 1, hours = 2)
		elif rango.startswith('1h'):
			date_inicio = hoy - timedelta(hours = 1, minutes = 10)
		else:
			date_inicio = hoy - timedelta(days = 8)

		df = self.__df_bitcoin[['Close', 'Promedio']].query('Datetime >= @date_inicio')

		# Se calculan las coordenadas para mostrar la tendencia en la gráfica
		maximo_index = df.index.max()
		ultimo_close = df.tail(1).Close

		if not qt:
			self.__figure = plt.figure()

		plt.title('Costo histórico del Bitcoin (USD)')
		plt.annotate(f'A la {self.__tendencia}', (maximo_index, ultimo_close), color = color_legend[self.__tendencia])
		plt.xlabel('Hora y fecha')
		plt.ylabel('Costo')
		sns.lineplot(data = df, palette = {'Close' : 'b', 'Promedio' : 'r'})

		if not qt:
			plt.show()

if __name__ == "__main__":
	main()