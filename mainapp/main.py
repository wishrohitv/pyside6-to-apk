import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QGridLayout, QLineEdit

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.grid = QGridLayout()
        self.text_input = QLineEdit()
        self.grid.addWidget(self.text_input, 0, 0, 1, 4)  # Add the text input to the grid

        buttons = ["-", "+", "*", "/","c","=",1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        for i, button in enumerate(buttons):
            row, col = divmod(i, 4)
            self.button_ = QPushButton(str(button))
            self.button_.clicked.connect(self.button_number)
            self.grid.addWidget(self.button_, row + 1, col)  # Add buttons to the grid

        self.setLayout(self.grid)  # Set the grid layout as the main layout

    def button_number(self):
        s = self.sender()
        button_output = s.text()
        textfield_text = self.text_input
        t_ = textfield_text.text()

        match button_output:
            case "=":
                try:
                    self.text_input.setText(str(eval(t_)))
                except:
                    self.text_input.setText("error")

            case "c":
                self.text_input.setText("")

            case _:
                t_ += button_output
                self.text_input.setText(t_)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    #window.resize(320, 400)
    window.show()
    sys.exit(app.exec())
