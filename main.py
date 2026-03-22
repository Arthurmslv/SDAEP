import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem
from main_ui import Ui_MainWindow
from form_item import FormularioItem
from details_ui import MaisDetalhesUI


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botaoAdcItem.clicked.connect(self.abrir_formulario)

        self.adicionar_item_exemplo()

    def adicionar_item_exemplo(self):
        self.ui.tableWidget.setRowCount(1)
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem("Carteira preta"))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("18/03/2026"))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(""))
        self.ui.tableWidget.setItem(0, 3, QTableWidgetItem("NÃO DEVOLVIDO"))

        botao_abrir = QPushButton("Abrir")
        botao_abrir.clicked.connect(self.abrir_detalhes)
        self.ui.tableWidget.setCellWidget(0, 2, botao_abrir)

        botao = QPushButton("Alterar")
        botao.clicked.connect(lambda: self.editar_item(0))
        self.ui.tableWidget.setCellWidget(0, 4, botao)

    def abrir_detalhes(self):
        self.details = MaisDetalhesUI()
        self.details.show()

    def abrir_formulario(self):
        self.form = FormularioItem()
        self.form.dados_salvos.connect(self.adicionar_item)
        self.form.show()

    def adicionar_item(self, dados):
        linha = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(linha)

        self.ui.tableWidget.setItem(linha, 0, QTableWidgetItem(dados["descricao"]))
        self.ui.tableWidget.setItem(linha, 1, QTableWidgetItem(""))
        self.ui.tableWidget.setItem(linha, 2, QTableWidgetItem(""))
        self.ui.tableWidget.setItem(linha, 3, QTableWidgetItem(dados["status"]))

        botao_abrir = QPushButton("Abrir")
        botao_abrir.clicked.connect(self.abrir_detalhes)
        self.ui.tableWidget.setCellWidget(linha, 2, botao_abrir)

        botao = QPushButton("Alterar")
        botao.clicked.connect(lambda: self.editar_item(linha))
        self.ui.tableWidget.setCellWidget(linha, 4, botao)

    def editar_item(self, linha):
        descricao = self.ui.tableWidget.item(linha, 0).text()
        status = self.ui.tableWidget.item(linha, 3).text()

        dados = {
            "descricao": descricao,
            "status": status
        }

        self.form = FormularioItem(dados)
        self.form.dados_salvos.connect(lambda novos_dados: self.atualizar_item(linha, novos_dados))
        self.form.show()

    def atualizar_item(self, linha, dados):
        self.ui.tableWidget.setItem(linha, 0, QTableWidgetItem(dados["descricao"]))
        self.ui.tableWidget.setItem(linha, 3, QTableWidgetItem(dados["status"]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())