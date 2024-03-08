from PyQt5.QtWidgets import*
import json

try:
    with open("notes_data.json", "r", 
        encoding="utf-8") as file:
        notes = json.load(file)
except:
    notes = {}

app = QApplication([])
app.setStyleSheet("""
    QWidget {
        background-color: black ;
        color : #ffffff;
        font-size: 25px;
    }

    QPushButton {
        background-color: purple;
        color : #aaaaff;
        border-radius: 7px ;
        border-color: #3232ff;
        border-style: hidden;
        border-width: 5px;
        min-height: 20px;
        font-size: 25px;
        font-family: none;

    }
                  
    QPushButton:hover{
        background-color: red;
    }

    QLabel {
        background-color: #000000 ;
        color : #ffffff;
        font-size: 25px;
    }
    
    QTextEdit {  
        background-color: #1111111 ;
        color : #ffffff;
        font-size: 25px;
    }
    
    QListWidget {
        background-color: #111111 ;
        color : #ffffff;
        font-size: 25px;
    }
    
    QLineEdit {
        background-color: #000000 ;
        color : #ffffff;
        font-size: 25px;
    }
""")

window = QWidget()
window.resize(800, 500)
mainline = QHBoxLayout()

baton1 = QPushButton('створити замітку')
baton2 = QPushButton('видалити замітку')
baton3 = QPushButton('зберегти замітку')
baton4 = QPushButton('додати до замітки')
baton5 = QPushButton('відкріпити від замітки')
baton6 = QPushButton('Шукати замітки за тегом')
text1 = QLabel('список заміток')
text2 = QLabel('список тегів')
pole1 = QTextEdit()
pole2 = QListWidget() # список записів
pole3 = QListWidget() # список тегів
pole4 = QLineEdit()

linepole = QVBoxLayout()
linemenu = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()

mainline.addLayout(linepole)
mainline.addLayout(linemenu)
linepole.addWidget(pole1)
linemenu.addWidget(text1)
linemenu.addWidget(pole2)
line1.addWidget(baton1)
line1.addWidget(baton2)
linemenu.addLayout(line1)
linemenu.addWidget(baton3)
linemenu.addWidget(text2)
linemenu.addWidget(pole3)
linemenu.addWidget(pole4)
line2.addWidget(baton4)
line2.addWidget(baton5)
linemenu.addLayout(line2)
linemenu.addWidget(baton6)

window.setLayout(mainline)
window.show()

app.exec()
