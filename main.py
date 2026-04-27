import sys
import random
import math

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QPainter, QColor, QCursor
from PySide6.QtCore import QTimer, Qt, QRectF, QPoint
from cell import Cell
from player import Player

WIDTH = 800
HEIGHT = 600
CELL_RADIUS = 5

class GameCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.menu = True
        self.radius = 12
        self.mouseX = WIDTH / 2
        self.mouseY = HEIGHT / 2
        self.targetX = 0
        self.targetY = 0
        self.player = Player(WIDTH / 2, 
                             HEIGHT / 2, 
                             self.radius, "#ff00ff")
        self.cells = [Cell(random.randint(0, WIDTH), 
                           random.randint(0, HEIGHT), 
                           CELL_RADIUS, "#00ff00") 
                      for i in range(100)]

        self.nameInput = QLineEdit(self)
        self.nameInput.setPlaceholderText("Name")
        self.nameInput.move(WIDTH // 2 - 75, HEIGHT // 2 - 75)
        self.playButton = QPushButton("Play", self)
        self.playButton.move(WIDTH // 2 - 75, HEIGHT // 2 - 75)
        self.playButton.clicked.connect(self.startGame)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateGame)
        self.timer.start(1)

    def startGame(self):
        self.menu = False
        self.nameInput.hide()
        self.playButton.hide()

    def updateGame(self):
        for cell in self.cells[:]:
            distance = math.sqrt((cell.x - self.player.x)**2 + (cell.y - self.player.y)**2)
            if distance < self.player.radius + CELL_RADIUS:
                self.cells.remove(cell)
                self.player.radius += 1
                self.player.speed -= 0.000025
                color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
                self.cells.append(Cell(random.randint(0, WIDTH), 
                                   random.randint(0, HEIGHT), 
                                   CELL_RADIUS, color))
        dx = self.mouseX - self.player.x
        dy = self.mouseY - self.player.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance > 1:
            self.player.x += (dx / distance) * self.player.speed
            self.player.y += (dy / distance) * self.player.speed
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), QColor("#ffffff"))
        self.player.draw(painter)
        for cell in self.cells:
            cell.draw(painter)
        if self.menu:
                    painter.fillRect(self.rect(), QColor(0, 0, 0, 150))

    def mouseMoveEvent(self, event):
        if not self.menu:
            self.mouseX = event.position().x()
            self.mouseY = event.position().y()

    # def drawMenu(self, painter):
    #     button = QPushButton()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agar.io - Python - Chaz Cook")
        self.setFixedSize(WIDTH, HEIGHT)

        self.game = GameCanvas()

        self.setCentralWidget(self.game)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
