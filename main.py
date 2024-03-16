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
        background-color: blue;
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
        background-color: white;
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

def add_note():
    note_name, ok = QInputDialog.getText(window,"Додати замітку","Назва замітки")
    if ok and note_name != "":
        notes[note_name] = {"текст": "", "теги": []}
        pole2.clear()
        pole1.clear()
        pole2.addItems(notes)

        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False)

def save_note():
    if pole2.selectedItems():
        key = pole2.selectedItems()[0].text()
        notes[key]["текст"] = pole1.toPlainText()
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False)
    else:
        print("Замітка для збереження не вибрана")

def show_note():
    key = pole2.selectedItems()[0].text() #вибирає ключ
    print(key)
    pole1.setText(notes[key]["текст"])
    pole3.clear()
    pole3.addItems(notes[key]["теги"])

def del_note():
    if pole2.selectedItems():
        key = pole2.selectedItems()[0].text()
        notes.pop(key)
        pole2.clear()
        pole3.clear()






window.setLayout(mainline)
window.show()

pole2.addItems(notes)

app.exec()