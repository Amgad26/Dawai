from PyQt6.QtWidgets import QWidget , QHBoxLayout
import GuiBuilder

class UserSelectScreen(QWidget):
    
    def __init__(self , main_window):
        
        super().__init__()
        self.main = main_window
        
        layout = QHBoxLayout()
        title = GuiBuilder.title("Dawai 💊")
        layout.addWidget(title)
        
        self.setLayout(layout)
        