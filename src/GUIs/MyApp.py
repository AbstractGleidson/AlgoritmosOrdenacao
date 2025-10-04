# Cria de fato a interface da aplicacao
# Para futuras modificacao, e interessante implementar um esquema de navegacao usando QStackedWidget
from PySide6.QtWidgets import QMainWindow, QWidget, QCheckBox, QListWidget, QStyle, QFileDialog # Principais widgets
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from .widgets.smallWidgets import inputValue, messageDialog, buttonMainMenu
from constants import ICON2_PATH, WINDOW_HEIGTH, WINDOW_WIDTH
#from datetime import datetime
import sys

# Herda QMainWindow para ter acesso a alguns componentes da janela em si, como title e icon 
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Algoritmos de Ordenação")
        self.setFixedSize(WINDOW_HEIGTH, WINDOW_WIDTH)
        self.setWindowIcon(QIcon(ICON2_PATH)) # Troca o icone da janela
        self.showMainMenu()  # Mostra a primeira janela


    # Renderiza o menu principal da aplicacao 
    def showMainMenu(self):
        CENTER = Qt.AlignmentFlag.AlignCenter # Cria um centralizacao 

        widget = QWidget() # Widget generico
        layout = QVBoxLayout() # Box vertical

        # Plota os gráficos usando os dados de ordenação
        button_view_graph = buttonMainMenu("Visualizar gráficos de desempenho")
        # button_view_graph.clicked.connect() # Adiciona funcao para esse botao
        
        # Reinicia os testes dos algorítmos de ordenação
        button_restart_tests = buttonMainMenu("Reiniciar testes de algorítmos")
        # button_restart_tests.clicked.connect(self.restartTests) # Adiciona funcao para esse botao
        
        # Compara Algoritmos
        button_compare_algorithms = buttonMainMenu("Comparar Algorítmos")
        # button_compare_algorithms.clicked.connect() # Adiciona funcao para esse botao
        
        # Sai da aplicacao
        button_report = buttonMainMenu("Sair")
        button_report.clicked.connect(self.exitAplication) # Adiciona funcao para esse botao

        # Adiciona os botoes no layout
        layout.addWidget(button_view_graph, alignment=CENTER)
        layout.addWidget(button_restart_tests, alignment=CENTER)
        layout.addWidget(button_compare_algorithms, alignment=CENTER)
        layout.addWidget(button_report, alignment=CENTER)
        
        widget.setLayout(layout) # Adiciona o layout no widget generico

        self.setCentralWidget(widget)  # Renderiza esse widget generico que foi criado 

    # Sai da aplicacao
    def exitAplication(self):
        sys.exit()
    