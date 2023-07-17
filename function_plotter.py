import sys
import matplotlib.pyplot as plt
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide2.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from sympy import symbols, lambdify
import numpy as np

class FunctionPlotter(QMainWindow):
    """
    A GUI application for plotting user-defined functions.
    """

    def __init__(self):
        """
        Initializes the FunctionPlotter class.
        """

        # Initialization method of the parent class
        super().__init__()

        self.setWindowTitle('Function Plotter')
        self.setMinimumWidth(1024)
        self.setMinimumHeight(720)

        # Create the UI elements
        self.function_label = QLabel('Function:')
        self.function_input = QLineEdit()
        self.min_label = QLabel('Min:')
        self.min_input = QLineEdit()
        self.max_label = QLabel('Max:')
        self.max_input = QLineEdit()
        self.plot_button = QPushButton('Plot')
        self.plot_button.clicked.connect(self.plot)

        self.figure = plt.Figure()
        self.canvas = FigureCanvas(self.figure)

        # Create the layout for the UI elements
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.function_label)
        input_layout.addWidget(self.function_input)
        input_layout.addWidget(self.min_label)
        input_layout.addWidget(self.min_input)
        input_layout.addWidget(self.max_label)
        input_layout.addWidget(self.max_input)
        input_layout.addWidget(self.plot_button)

        layout = QVBoxLayout()
        layout.addLayout(input_layout)
        layout.addWidget(self.canvas)

        # Create the central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def validate_inputs(self, function, min_value, max_value):
        """
        Validates the user inputs for function, min value, and max value.

        Args:
            function (str): The user-defined function.
            min_value (str): The minimum value for the x-axis range.
            max_value (str): The maximum value for the x-axis range.

        Returns:
            bool: True if the inputs are valid, False otherwise.
        """

        # Validate function
        if not function:
            return False

        try:
            # Create a symbolic variable
            x = symbols('x')
            expr = function.replace('^', '**')
            lambdify(x, expr)
        except (SyntaxError, NameError, TypeError):
            return False

        # Validate min and max values
        if not min_value or not max_value:
            return False
        try:
            float(min_value)
            float(max_value)
        except ValueError:
            return False
        if float(min_value) >= float(max_value):
            return False

        return True

    def plot(self):
        """
        Plots the user-defined function with the specified x-axis range.
        """

        function = self.function_input.text().strip()
        min_value = self.min_input.text().strip()
        max_value = self.max_input.text().strip()

        if not self.validate_inputs(function, min_value, max_value):
            QMessageBox.critical(self, 'Invalid Input', 'Please enter a valid input.')
            return

        # Create a symbolic variable
        x = symbols('x')
        expr = function.replace('^', '**')

        # Create a lambda function from the symbolic expression
        f = lambdify(x, expr)

        # Generate x and y values
        x_values = np.linspace(float(min_value), float(max_value), 100)
        y_values = np.array([f(x_val) for x_val in x_values])

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x_values, y_values)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Function Plot')
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    plotter = FunctionPlotter()
    plotter.show()
    sys.exit(app.exec_())
