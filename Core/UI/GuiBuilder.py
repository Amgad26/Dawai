from Style.Colors import Colors
from Style.FontSize import FontSize
from Style.FontWeight import FontWeight
from Style.Spacing import Spacing

from PyQt6.QtWidgets import QLabel

def title(text):
    
    label = QLabel(text)
    label.setStyleSheet(f"""
            font-size: {FontSize.XXL}px;
            font-weight: {FontWeight.BOLD};
        """)
    return label
    