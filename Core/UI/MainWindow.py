from PyQt6.QtWidgets import QApplication , QMainWindow , QStackedWidget
from UserSelectScreen import UserSelectScreen

class MainWindow(QMainWindow):

    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Dawai — دوائي")
        self.setMinimumSize(400, 650)

        # The stack — holds all screens
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Create all screens once, pass reference to main window
        self.user_select_screen = UserSelectScreen(main_window = self)
        # self.add_user_screen    = AddUserScreen(main_window=self)

        # Add them to the stack in order
        self.stack.addWidget(self.user_select_screen)  # index 0
        # self.stack.addWidget(self.add_user_screen)     # index 1

        # Start on user select
        self.show_user_select()

    def show_user_select(self):
        self.stack.setCurrentIndex(0)

    def show_add_user(self):
        self.stack.setCurrentIndex(1)

if __name__ == "__main__":
    
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()