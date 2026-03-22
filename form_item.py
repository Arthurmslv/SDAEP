from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from form_ui import Ui_Form


class FormularioItem(QWidget):

    dados_salvos = pyqtSignal(dict)

    def __init__(self, dados=None):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.grupoDevolucao.hide()
        self.ui.checkboxDevolvido.stateChanged.connect(self.toggle_devolucao)

        self.ui.botaoSalvar.clicked.connect(self.salvar)
        self.ui.botaoVoltar.clicked.connect(self.close)

        self.dados = dados

        if dados:
            self.ui.descricao.setText(dados["descricao"])
            if dados["status"] == "DEVOLVIDO":
                self.ui.checkboxDevolvido.setChecked(True)

    def toggle_devolucao(self):
        if self.ui.checkboxDevolvido.isChecked():
            self.ui.grupoDevolucao.show()
        else:
            self.ui.grupoDevolucao.hide()

    def salvar(self):
        status = "DEVOLVIDO" if self.ui.checkboxDevolvido.isChecked() else "NÃO DEVOLVIDO"

        dados = {
            "descricao": self.ui.descricao.text(),
            "status": status
        }

        self.dados_salvos.emit(dados)
        self.close()