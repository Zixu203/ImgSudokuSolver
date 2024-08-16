import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
from PIL.PngImagePlugin import PngImageFile
import numpy as np

class SudokuCNN(nn.Module):
    def __init__(self):
        super(SudokuCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)
        
    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.max_pool2d(x, 2)
        x = torch.relu(self.conv2(x))
        x = torch.max_pool2d(x, 2)
        x = x.view(-1, 64 * 7 * 7)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

class Predictor():
    def __init__(self):
        self.model = SudokuCNN()
        self.model.load_state_dict(torch.load('sudoku_cnn.pth'))
        self.model.eval()

        self.transform = transforms.Compose([
            transforms.Grayscale(num_output_channels=1),
            transforms.Resize((28, 28)),
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,))
        ])

    def predict(self, imgPath: str) -> list[list]:
        return self.predictSudoku(imgPath)

    def preprocessImg(self, cell: Image.Image) -> torch.Tensor:
        cell = self.transform(cell)
        return cell.unsqueeze(0)  

    def splitImg(self, img: PngImageFile) -> list[Image.Image]:
        cellImgs = []
        cellSize = img.size[0] // 9  
        for i in range(0, 9):
            for j in range(0, 9):
                left = j * cellSize
                top = i * cellSize
                right = (j + 1) * cellSize
                bottom = (i + 1) * cellSize
                cell = img.crop((left, top, right, bottom))
                cellImgs.append(cell)
        return cellImgs

    def predictSudoku(self, imgPath: str) -> list[list]:
        img = Image.open(imgPath) 
        cells = self.splitImg(img)
        sudokuMat = np.zeros((9, 9), dtype=int)
        
        with torch.no_grad():
            for i in range(9):
                for j in range(9):
                    cell = cells[i * 9 + j]
                    cell = self.preprocessImg(cell)
                    output = self.model(cell)
                    _, predicted = torch.max(output.data, 1)
                    sudokuMat[i, j] = predicted.item()
        return sudokuMat


if __name__ == "__main__": 
    p = Predictor()
    s = p.predict("sudoku4.png")
    print(s)




