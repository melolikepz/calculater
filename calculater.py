import sys
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton,QGridLayout, QVBoxLayout, QApplication

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        return "Error"
    return a / b

class CalculatorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.operand = None
        self.current_operator = None
        self.init_ui()

    def init_ui(self):
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(35)

        grid = QGridLayout()

        labels = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 0, 0), ('Del', 0, 1)
        ]

        for (text, row, col) in labels:
            button = QPushButton(text)
            button.clicked.connect(self.create_button_handler(text))
            grid.addWidget(button, row, col)

        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(grid)

        self.setLayout(layout)
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 300)

    def create_button_handler(self, text):

        def handler():
            self.on_button_clicked(text)
        return handler

    def on_button_clicked(self, char: str):
        if char.isdigit() or char == '.':
            self.display.setText(self.display.text() + char)
        elif char in ['+', '-', '*', '/']:
            self.operand = float(self.display.text()) if self.display.text() else 0
            self.current_operator = char
            self.display.clear()
        elif char == '=':
            if self.operand is not None and self.current_operator is not None:
                try:
                    num2 = float(self.display.text()) if self.display.text() else 0
                    if self.current_operator == '+':
                        result = add(self.operand, num2)
                    elif self.current_operator == '-':
                        result = subtract(self.operand, num2)
                    elif self.current_operator == '*':
                        result = multiply(self.operand, num2)
                    elif self.current_operator == '/':
                        result = divide(self.operand, num2)
                    else:
                        result = "Error"
                    self.display.setText(str(result))
                except ValueError:
                    self.display.setText("Error")
                finally:
                    self.operand = None
                    self.current_operator = None
        elif char == 'C':
            self.display.clear()
            self.operand = None
            self.current_operator = None
        elif char == 'Del':
            self.display.setText(self.display.text()[:-1])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorUI()
    calculator.show()
    sys.exit(app.exec())
