from PySide6.QtGui import QColor 
# from PySide6.QtCore import Qt

class Cell():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, painter):
        painter.setBrush(QColor(self.color))
        # painter.setPen(Qt.NoPen)
        painter.drawEllipse(self.x, self.y, self.radius * 2, self.radius * 2)
