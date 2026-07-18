from abc import ABC, abstractmethod
#SRP
class Report:
    def __new__(self, content):
        return self.content

class ReportBuilder():
    def build():
        return Report("report builder")

class ReportSaver():
    def save():
        return Report("report saver")

class ReportEmailer():
    def send():
        return Report("send email")

#OCP
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):

class SquareShape(Shape):

    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return side **2

class RectangleShape(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return length * width
