# Cria de fato a interface da aplicacao
# Para futuras modificacao, e interessante implementar um esquema de navegacao usando QStackedWidget
from PySide6.QtWidgets import QMainWindow, QWidget, QCheckBox, QListWidget, QStyle, QFileDialog  # Principais widgets
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QComboBox
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from .widgets.smallWidgets import inputValue, messageDialog, buttonMainMenu
from constants import ICON2_PATH, WINDOW_HEIGTH, WINDOW_WIDTH
from .Charts.generateCharts import MplCanvas
#from datetime import datetime
import sys

# Herda QMainWindow para ter acesso a alguns componentes da janela em si, como title e icon 
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.errorMessage = None # Gerencia a messagem de erro na leitura de dado, se ela deve ser exibida ou nao
        self.fileName = None # Gerencia o arquivo que será enviado para ordenar 
        self.algorithm = None # Gerencia o algorítmo escolhido para ordenação


        self.setWindowTitle("Algoritmos de Ordenação")
        self.setBaseSize(WINDOW_HEIGTH, WINDOW_WIDTH)
        self.setWindowIcon(QIcon(ICON2_PATH)) # Troca o icone da janela
        self.showMainMenu()  # Mostra a primeira janela


    # Renderiza o menu principal da aplicacao 
    def showMainMenu(self):
        CENTER = Qt.AlignmentFlag.AlignCenter # Cria um centralizacao 

        widget = QWidget() # Widget generico
        layout = QVBoxLayout() # Box vertical

        # Plota os gráficos usando os dados de ordenação
        button_view_graph = buttonMainMenu("Visualizar gráficos de desempenho")
        button_view_graph.clicked.connect(self.showCharts) # Adiciona funcao para esse botao
        
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

    def showCharts(self):
        FONT = QFont("Arial")
        FONT.setPixelSize(25)

        # widget e layout da tela
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Seletor de Algoritmo para escolher quem vai ser usado
        label_select = QLabel("Selecione o algoritmo:")
        label_select.setFont(FONT)
        self.combo_algorithms = QComboBox()
        self.combo_algorithms.setFont(FONT)
        self.combo_algorithms.addItems(["Bubble Sort", "Selection Sort" , "Insertion Sort" , "Shell Sort", "Quick Sort", "Merge Sort", "Heap Sort"])

        # Canvas do matplotlib
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.clear
        self.canvas.axes.set_title("Desempenho do Algoritmo", fontsize=16)
        self.canvas.axes.set_xlabel("Quantidade de Nomes (Em milhares)")
        self.canvas.axes.set_ylabel("Tempo(ms)")
        self.canvas.draw()

        # Botão para plotar os gráficos do algoritmo selecionado
        button_plot = QPushButton("Gerar gráfico")
        button_plot.setFont(FONT)
        button_plot.setFixedSize(200, 40)
        button_plot.clicked.connect(self.updateChart)
    
        # Botão para voltar pro menu principal
        button_back = QPushButton("Voltar")
        button_back.setFont(FONT)
        button_back.setFixedSize(150, 40)
        button_back.clicked.connect(self.showMainMenu)

        # Adiciona os botões e o gráfico no layout do widget
        layout.addWidget(label_select, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.combo_algorithms, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.canvas)
        layout.addWidget(button_plot, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button_back, alignment=Qt.AlignmentFlag.AlignCenter)

        widget.setLayout(layout)
        self.setCentralWidget(widget) # Renderiza na tela o widget criado

    def updateChart(self):
        algorithm = self.combo_algorithms.currentText() # Pega oque está selecionado no combo

        # Define as coordenadas de X que são sempre fixas
        x = [100, 250, 500]

        # Os valores de Y serão pegos dos dados gerados, os de agora são de exemplo
        # Altera o gráfico conforme o algorítmo selecionado
        if algorithm == "Bubble Sort":
            dados = self.canvas.getData("bubble_sort")
            y = [dados[100], dados[250], dados[500]]
            self.canvas.axes.clear()
            self.canvas.axes.set_ylabel("Tempo (s)")
        
        if algorithm ==  "Selection Sort":
            dados = self.canvas.getData("selection_sort")
            y = [dados[100], dados[250], dados[500]]
            self.canvas.axes.clear()
            self.canvas.axes.set_ylabel("Tempo (s)")

        if algorithm == "Insertion Sort":
            dados = self.canvas.getData("insertion_sort")
            self.canvas.axes.clear()
            y = [dados[100], dados[250], dados[500]]

        if algorithm ==  "Shell Sort":
            dados = self.canvas.getData("shell_sort")
            y = [dados[100], dados[250], dados[500]]
            self.canvas.axes.clear()
            self.canvas.axes.set_ylabel("Tempo (s)")

        if algorithm == "Quick Sort":
            dados = self.canvas.getData("quick_sort")
            y = [dados[100]*1000, dados[250]*1000, dados[500]*1000]
            self.canvas.axes.clear()
            self.canvas.axes.set_ylabel("Tempo (ms)")

        if algorithm == "Merge Sort":
            dados = self.canvas.getData("merge_sort")
            y = [dados[100]*1000, dados[250]*1000, dados[500]*1000]
            self.canvas.axes.clear()
            self.canvas.axes.set_ylabel("Tempo (ms)")
    
        if algorithm == "Heap Sort":
            dados = self.canvas.getData("heap_sort")
            y = [dados[100]*1000, dados[250]*1000, dados[500]*1000]
            self.canvas.axes.clear()
            self.canvas.axes.set_ylabel("Tempo (ms)")
            

        # Atualiza o canvas
        self.canvas.axes.plot(x, y, marker='o', label=algorithm)
        self.canvas.axes.set_title(f"Desempenho: {algorithm}", fontsize=16)
        self.canvas.axes.set_xlabel("Quantidade de Nomes (Em milhares)")
        self.canvas.axes.legend()
        self.canvas.draw()


    # Sai da aplicacao
    def exitAplication(self):
        sys.exit()
    