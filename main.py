# Descripcion

from UI.ventana_madre import *
import numpy as np
import matplotlib.pyplot as plt
import threading, time
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from models.robot import RobotTrading
from PyQt5.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

	''' Ventana principal, donde se hace la magia '''

	def __init__(self, *args, **kwargs):

		QtWidgets.QMainWindow.__init__(self, *args)
		self.setupUi(self)

		self.__robot = RobotTrading()
		self.__rango = '7d'

		# Creamos un lambda
		self.layout_plt = QtWidgets.QVBoxLayout(self.plt_container)

		# Creamos una figura plt
		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)
		self.toolbar = NavigationToolbar(self.canvas, self)
		self.traducir_tooltip_toolbar()

		# Agregamos la figura en el layout
		self.layout_plt.addWidget(self.toolbar)
		self.layout_plt.addWidget(self.canvas)

		# Creamos un nuevo hilo para el loop de actualización

		self.cronometro = 60
		self.timer_runs = threading.Event()
		self.timer_runs.set()

		# Conectamos botones
		self.GrupoBoton_mostrar.buttonClicked.connect(self.seleccionar_limites_mostrar)
		self.pushButton_iniciar.clicked.connect(self.timer)
		self.pushButton_detener.clicked.connect(self.stop_timer)

	def plot(self):
		''' Se ejecuta la visualización '''

		self.figure.clear()
		self.__robot.visualizacion(rango = self.__rango, qt = True)
		self.canvas.draw()

	def seleccionar_limites_mostrar(self):
		''' Se cambia los límites de visualización en 7 días, 24h o 1h '''

		self.__rango = self.GrupoBoton_mostrar.checkedButton().text().replace(' ', '').lower()
		try:
			self.plot()
		except TypeError:
			pass

	def timer(self):
		''' Abrimos un hilo para ejecutar un loop que actualiza los datos y la gráfica '''

		self.pushButton_detener.setEnabled(True)
		self.pushButton_iniciar.setEnabled(False)

		t = threading.Thread(target = self.iniciar)
		t.start()

	def stop_timer(self):
		''' Detiene la función en el hilo secundario iniciada por `self.timer()` '''

		self.pushButton_detener.setEnabled(False)
		self.pushButton_iniciar.setEnabled(True)
		self.timer_runs.clear()

	def iniciar(self):

		''' Ejecuta la captura de datos del RobotTrading y la visualización de datos '''

		while self.timer_runs.is_set():
			self.__robot.ejecutar()
			self.plot()

			precio_actual = self.__robot.precio_actual
			decision = self.__robot.decision

			self.label_info.setText(f'Precio actual: 1 BTC = {precio_actual:,.2f} USD')
			self.label_recomendacion.setText(f'Se recomienda: {decision}')
			self.label_recomendacion.setAlignment(Qt.AlignRight)

			print('Mensaje: Actualización de datos realizada')

			time.sleep(self.cronometro)


	def traducir_tooltip_toolbar(self):

		traductor = {
			'Reset original view' : 'Reiniciar a vista original',
			'Back to previous view' : 'Ir a vista anterior',
			'Forward to next view'  : 'Ir a la vista siguiente',
			'Left button pans, Right button zooms\nx/y fixes axis, CTRL fixes aspect' :
			 		'Botón izquierdo desplaza, Botón derecho hace zoom',
			'Zoom to rectangle\nx/y fixes axis' : 'Zoom in o Zoom out a la selección',
			'Configure subplots' : 'Configura subplots',
			'Edit axis, curve and image parameters' : 'Editar ejes, curva y parámetros de imagen',
			'Save the figure' : 'Guardar figura',
			'' : ''
		}

		for action in self.toolbar.actions():

			if not action.isSeparator():
				original = action.toolTip()
				nuevo = traductor[original]

				action.setToolTip(nuevo)

	def closeEvent(self, event):
		event.ignore()
		self.stop_timer()
		event.accept()

if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	Ventana = MainWindow()
	Ventana.show()
	app.exec_()