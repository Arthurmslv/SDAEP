from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt


class MaisDetalhesUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mais detalhes")
        self.setFixedSize(500, 400)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 15, 20, 15)

        titulo = QLabel("Mais detalhes")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        main_layout.addWidget(titulo)

        labels_texto = [
            "ID: -",
            "DESCRIÇÃO: -",
            "LOCAL: -",
            "OBSERVAÇÕES: -",
            "DATA DE CADASTRO: -",
            "QUEM ENCONTROU: -",
            "ONDE ESTAVA: -",
            "",
            "STATUS: -",
            "DATA DA DEVOLUÇÃO: -",
            "RECEBIDO POR: -"
        ]

        for texto in labels_texto:
            label = QLabel(texto)
            label.setStyleSheet("font-size: 14px;")
            main_layout.addWidget(label)

        main_layout.addStretch()

        bottom_layout = QHBoxLayout()
        btn_fechar = QPushButton("Fechar")
        btn_fechar.setFixedWidth(100)
        btn_fechar.clicked.connect(self.close)

        bottom_layout.addWidget(btn_fechar, alignment=Qt.AlignLeft)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)