# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 15:10:44 2024
@author: 梓旭
"""

import pyautogui, keyboard
from PIL import ImageGrab, Image
import cv2
import os
from pathlib import Path
import time
import pytesseract
from tqdm import tqdm

ITERATION = 100

class DatasetGenerator():

    # Website: https://www.websudoku.com

    def __init__(self):
        print("Please make sure you put the sudoku website on main screen")
        time.sleep(3)
        # self.getPosition()

        self.nextLevel()
        for i in tqdm(range(0, ITERATION)):
            self.getFullPic()
            cells = self.splitImg()
            for cell in cells:
                text = self.recogCell(cell)
                if text==0: continue
                targetDir = Path(f".\\a\\{text}")
                targetDir.mkdir(parents=True, exist_ok=True)
                maxVal = -1 if len(list(targetDir.glob("*.png")))==0 else max([int(x.stem) for x in targetDir.glob("*.png")])
                maxVal+=1
                p = str(targetDir/str(maxVal))+".png"
                cv2.imwrite(p, cell)
            self.nextLevel()
            
    # ! Infinity Loop
    def getPosition(self) -> None:
        while True:
            if keyboard.read_key() == "a": print(pyautogui.position())

    def selectScreenShotRange(self, box: list[int], sec: float) -> None:
        pyautogui.moveTo(box[0], box[1], duration=sec/2)
        pyautogui.dragTo(box[2], box[3], duration=sec/2, button="left")

    def nextLevel(self) -> None:
        p1 = [1703, 1103] # select level btn
        p2 = [1569, 1025] # confirm btn
        p3 = [874, 620] # Blank
        pyautogui.leftClick(p1[0], p1[1], duration=0.5)
        time.sleep(1)
        pyautogui.leftClick(p2[0], p2[1], duration=0.5)
        pyautogui.leftClick(p3[0], p3[1], duration=0.5)
        time.sleep(1)

    def getFullPic(self) -> None:
        box = [1272, 542, 1791, 1056] # [x1, y1, x2, y2]
        time.sleep(0.5)
        keyboard.press_and_release("win+shift+s")
        time.sleep(0.5)
        self.selectScreenShotRange(box, 1)
        clipboard = ImageGrab.grabclipboard()
        clipboard.save("current.png", format='png')
    
    def splitImg(self) -> list[Image.Image]:
        img = cv2.imread('current.png')
        cells = []
        side = img.shape[0] // 9
        for row in range(9):
            for col in range(9):
                x1, y1 = col * side, row * side
                x2, y2 = (col + 1) * side, (row + 1) * side
                cell = img[y1:y2, x1:x2]
                cells.append(cell)
        return cells

    def recogCell(self, img: Image.Image) -> str:
        text = pytesseract.image_to_string(img, config=("--psm 10")).strip("\n")
        try: text = 0 if str(text) not in "123456789" else int(text)
        except: text = 0
        return text

if __name__ == "__main__": 
    os.chdir(Path(__file__).absolute().parent)
    DatasetGenerator()


