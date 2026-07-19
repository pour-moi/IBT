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

#Singleton

class AppSettings:
    _instance = None
    def __new__(cls):
        _currency = "ETB"
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"
        return cls._instance

as1 = AppSettings()
as2 = AppSettings()
print(as1.currency)
