from PySide6.QtGui import QColor 
# from PySide6.QtCore import Qt

class Player():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 0.5
        
    def draw(self, painter):
        painter.setBrush(QColor(self.color))
        # painter.setPen(Qt.NoPen)
        painter.drawEllipse(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

