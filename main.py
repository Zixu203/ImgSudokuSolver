# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:41:04 2024
@author: 梓旭
"""

from predictor import Predictor
from solver import Solver
import pyautogui
import time
from tqdm import tqdm
import keyboard
from PIL import ImageGrab

ITERATION = 10

class ImgSudokuSolver():
    def __init__(self):
        self.predictor = Predictor()
        self.solver = Solver()

    def solve(self):
        print("Please make sure you put the sudoku website on main screen")
        time.sleep(3)

        self.randomPickLevel()
        for i in tqdm(range(0, ITERATION)):
            self.getFullPic()
            questionMat = self.predictor.predict("current.png")
            ansMat = self.solver.solve(questionMat)
            if len(ansMat)!=1:
                print("Failed to found answer, next puzzle")
                self.randomPickLevel()
                continue
            self.fillAns(ansMat[0])
            self.nextLevel()

    def selectScreenShotRange(self, box: list[int], sec: float) -> None:
        pyautogui.moveTo(box[0], box[1], duration=sec/2)
        pyautogui.dragTo(box[2], box[3], duration=sec/2, button="left")
    
    def getFullPic(self) -> None:
        box = [1272, 542, 1791, 1056] # [x1, y1, x2, y2]
        time.sleep(0.5)
        keyboard.press_and_release("win+shift+s")
        time.sleep(0.5)
        self.selectScreenShotRange(box, 1)
        clipboard = ImageGrab.grabclipboard()
        clipboard.save("current.png", format='png')

    def randomPickLevel(self) -> None:
        p1 = [1703, 1103] # select level btn
        p2 = [1569, 1025] # confirm btn
        p3 = [874, 620] # Blank
        pyautogui.leftClick(p1[0], p1[1], duration=0.5)
        time.sleep(2)
        pyautogui.leftClick(p2[0], p2[1], duration=0.5)
        pyautogui.leftClick(p3[0], p3[1], duration=0.5)
        time.sleep(1)
    
    def nextLevel(self) -> None:
        p1 = [1518, 905]    # Confirm Btn for next levhel
        p2 = [874, 620] # Blank
        time.sleep(0.5)
        pyautogui.leftClick(p1[0], p1[1], duration=0.5)
        time.sleep(2)
        pyautogui.leftClick(p2[0], p2[1], duration=0.5)
        

    def fillAns(self, ansMat: list[list]) -> None:
        box = [1299, 575]
        pyautogui.leftClick(box[0], box[1])
        for i in range(0, 9):
            for j in range(0, 9):
                keyboard.press_and_release(str(ansMat[i][j]))
                time.sleep(0.01)
                keyboard.press_and_release("right")
                time.sleep(0.01)
            if i!=8: keyboard.press_and_release("down")

        keyboard.press_and_release("enter")

if __name__ == "__main__": 
    s = ImgSudokuSolver()
    s.solve()


