import pytest
from PySide2.QtTest import QTest
from PySide2.QtCore import Qt
from function_plotter import FunctionPlotter
from PySide2.QtWidgets import QMessageBox


@pytest.fixture
def function_plotter(qtbot):
    """
    Pytest fixture that creates an instance of FunctionPlotter and adds it to the Qt event loop.

    Args:
        qtbot (pytestqt.plugin.QtBot): Pytest-Qt fixture for interacting with Qt application.

    Returns:
        FunctionPlotter: An instance of FunctionPlotter.
    """
    plotter = FunctionPlotter()
    qtbot.addWidget(plotter)
    return plotter


def test_valid_input(function_plotter, qtbot):
    """
    Test case to verify the behavior of plotting with valid user input.

    Args:
        function_plotter (FunctionPlotter): An instance of FunctionPlotter.
        qtbot (pytestqt.plugin.QtBot): Pytest-Qt fixture for interacting with Qt application.
    """
    # Simulate user input
    function_input = function_plotter.function_input
    min_input = function_plotter.min_input
    max_input = function_plotter.max_input
    plot_button = function_plotter.plot_button

    qtbot.keyClicks(function_input, "x^2")
    qtbot.keyClicks(min_input, "-10")
    qtbot.keyClicks(max_input, "10")

    # Simulate button click
    qtbot.mouseClick(plot_button, Qt.LeftButton)

    # Assert that the plot was generated
    assert function_plotter.figure.axes[0].lines[0].get_xdata().size == 100
    assert function_plotter.figure.axes[0].lines[0].get_ydata().size == 100


def test_invalid_input():
    """
    Test case to verify the behavior of input validation with invalid input.

    Returns:
        bool: True if the input validation fails, False otherwise.
    """
    assert FunctionPlotter.validate_inputs(
        self=FunctionPlotter(), function="asjoa", min_value="ajnska", max_value=10) is False


def test_missing_function_input():
    """
    Test case to verify the behavior of input validation with a missing function input.

    Returns:
        bool: True if the input validation fails, False otherwise.
    """
    assert FunctionPlotter.validate_inputs(
        self=FunctionPlotter(), function="", min_value="0", max_value=10) is False


def test_missing_min_value_input():
    """
    Test case to verify the behavior of input validation with a missing min value input.

    Returns:
        bool: True if the input validation fails, False otherwise.
    """
    assert FunctionPlotter.validate_inputs(
        self=FunctionPlotter(), function="x", min_value="", max_value=10) is False


def test_missing_max_value_input():
    """
    Test case to verify the behavior of input validation with a missing max value input.

    Returns:
        bool: True if the input validation fails, False otherwise.
    """
    assert FunctionPlotter.validate_inputs(
        self=FunctionPlotter(), function="x", min_value="1", max_value="") is False


def test_non_numeric_min_value_input():
    """
    Test case to verify the behavior of input validation with a non-numeric min value input.

    Returns:
        bool: True if the input validation fails, False otherwise.
    """
    assert FunctionPlotter.validate_inputs(self=FunctionPlotter(), function="x", min_value="hh", max_value=10) is False


def test_non_numeric_max_value_input(function_plotter, qtbot):
    """
    Test case to verify the behavior of input validation with a non-numeric max value input.

    Returns:
        bool: True if the input validation fails, False otherwise.
    """
    assert FunctionPlotter.validate_inputs(
        self=FunctionPlotter(), function="x", min_value="0", max_value="ansj") is False


def test_min_value_greater_than_max_value_input(function_plotter, qtbot):
    """
    Test case to verify the behavior of input validation with min value greater than max value.

    Returns:
        bool: True if the input validation fails, False otherwise.
    """
    assert FunctionPlotter.validate_inputs(
        self=FunctionPlotter(), function="x", min_value="100", max_value=10) is False


if __name__ == "__main__":
    pytest.main(['-x', __file__])
