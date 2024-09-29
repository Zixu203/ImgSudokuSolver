# Sudoku Solver and Dataset Generator

This repository contains a Python project that includes a Sudoku puzzle solver, a dataset generator for training purposes, and additional modules for solving and predicting Sudoku grids. The project is designed to automate the process of solving Sudoku puzzles and generating a dataset by capturing images from a [web-based Sudoku game](https://www.websudoku.com).

You can watch the demo video [here](https://youtu.be/I7lTdXfyhiI)

## Project Structure

- `main.py`: Contains the `ImgSudokuSolver` class, which automates the solving of Sudoku puzzles by capturing the puzzle from the screen, predicting the numbers, solving the puzzle, and filling in the solution on the webpage.
  
- `genDataset.py`: Contains the `DatasetGenerator` class, which is used to generate a dataset of Sudoku puzzles by capturing the puzzle grid from the screen, splitting it into cells, and recognizing the numbers using OCR.

- `solver.py`: Contains the `Solver` class, which implements a depth-first search algorithm to solve the Sudoku puzzles. This class is used by the `ImgSudokuSolver` in `main.py` to solve the captured puzzle.

- `predictor.py`: Contains the `Predictor` class, which uses a Convolutional Neural Network (CNN) to predict the digits in each cell of the Sudoku puzzle. This class is also used by the `ImgSudokuSolver` in `main.py` for recognizing the puzzle numbers.

- `train.ipynb`: Jupyter notebook that is likely used for training the CNN model (`SudokuCNN`) to recognize Sudoku digits.

## Installation

### Prerequisites

- Python 3.10.11
- Required Python libraries:
  - `torch`
  - `torchvision`
  - `pyautogui`
  - `keyboard`
  - `PIL`
  - `opencv-python`
  - `numpy`
  - `pytesseract`
  - `tqdm`

### Installation Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/Zixu203/ImgSudokuSolver.git
    cd sudoku-solver
    ```

2. Install the required Python libraries:
    ```sh
    pip install -r requirements.txt
    ```

3. Make sure you have Tesseract OCR installed and properly configured. You can download it from [here](https://github.com/tesseract-ocr/tesseract).

4. Download the pre-trained model ([`sudoku_cnn.pth`](https://reurl.cc/0dpvgl)) and place it in the same directory as `predictor.py`.

5. (Optional) Download the dataset [here](https://reurl.cc/g62Gkb) and train your own model.

## Usage

### Sudoku Solver

To use the Sudoku solver:

1. Open the Sudoku website on your screen.
2. Run the `main.py` script:
    ```sh
    python main.py
    ```

### Dataset Generator

To generate a dataset of Sudoku puzzles:

1. Open the Sudoku website on your screen.
2. Run the `genDataset.py` script:
    ```sh
    python genDataset.py
    ```
3. The script will automatically capture the puzzle grid, recognize the digits, and save them in the `train` directory organized by digit.

### Sudoku Solver Module

The `solver.py` script can be run independently to test the Sudoku solving algorithm:

```sh
python solver.py
```

Sudoku Predictor Module
The predictor.py script can be run independently to test the digit recognition:

```sh
python predictor.py
```

Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions and improvements.
