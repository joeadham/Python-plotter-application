# Python-plotter-application
A python application that plots user defined functions over a specified range.

![Python 3.7](https://img.shields.io/badge/Python-3.7-blue.svg)


## Technologies Used

The web application is built using the following technologies:

- PySide2
- Matplotlib
- pytest

## Features

- Accept user defined functions, minimum and maximum x values
- Plots the function across the specified range

## Installation

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the requirements from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    python function_plotter.py
    ```
5. To test the application's functions run the `test_function_plotter.py` file

## How to Use

1. Run the application using the above instructions.
2. Input a valid function e.g: `5*x^3 + 2*x`
3. Input valid minimum and maximum ranges, minimum should always be less than maximum
4. Press the plot button

## Screenshots

### Valid functions:
![1](https://github.com/joeadham/Python-plotter-application/assets/81246343/a1458edc-3eaf-4b38-a6eb-bdd4ae7fe5c1)
![2](https://github.com/joeadham/Python-plotter-application/assets/81246343/a576cb54-db92-4258-b36f-7feb178e60fb)
![3](https://github.com/joeadham/Python-plotter-application/assets/81246343/6192efe5-9c68-47d0-8373-6554663c64fe)

### Invalid functions:
![5](https://github.com/joeadham/Python-plotter-application/assets/81246343/f33340ec-0e1c-4ab0-9453-3d381a6933df)
![4](https://github.com/joeadham/Python-plotter-application/assets/81246343/5f2129f7-96be-4c72-9062-640d8b39b2fb)


