from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import pyqtSignal , Qt
from Style.Colors import Colors
from Style.Spacing import Spacing

class CardFrame(QFrame):
    """
    Base card. Clickable only if `clickable=True`.
    Emits `clicked` signal when clicked (only if clickable).
    """
    clicked = pyqtSignal()

    def __init__(self , clickable: bool = False , parent = None):
        
        super().__init__(parent)
        self.clickable = clickable
        self._base_style()
        
        if clickable:
            
            self.setCursor(Qt.CursorShape.PointingHandCursor)

    def _base_style(self):
        
        hover_rule = f"""
            QFrame:hover {{
                border-color: {Colors.ACCENT};
            }}
        """ if self.clickable else ""

        self.setStyleSheet(f"""
            QFrame {{
                background-color: {Colors.SURFACE};
                border: 1px solid {Colors.BORDER};
                border-radius: {Spacing.RADIUS_LG}px;
            }}
            {hover_rule}
        """)

    def mousePressEvent(self, event):
        
        if self.clickable and event.button() == Qt.MouseButton.LeftButton:
            
            self.clicked.emit()
            
        super().mousePressEvent(event)