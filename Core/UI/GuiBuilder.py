from Style.Colors import Colors
from Style.FontSize import FontSize
from Style.FontWeight import FontWeight
from Style.Spacing import Spacing

from PyQt6.QtWidgets import QLabel , QPushButton , QFrame , QHBoxLayout , QVBoxLayout
from PyQt6.QtCore import Qt

def title(text , BOLD = True):

    label = QLabel(text)
    label.setStyleSheet(f"""
            font-size: {FontSize.XXL}px;
            font-weight: {FontWeight.BOLD if BOLD else FontWeight.SEMIBOLD};
            color: {Colors.TEXT};
        """)
    return label

def subtitle(text):
    
    label = QLabel(text)
    label.setStyleSheet(f"""          
            font-size: {FontSize.BODY}px;
            font-weight: {FontWeight.MEDIUM};
            color: {Colors.TEXT3};
        """)
    return label

def section_name(text):
    
    label = QLabel(text)
    label.setStyleSheet(f"""          
            font-size: {FontSize.XS}px;
            font-weight: {FontWeight.SEMIBOLD};
            color: {Colors.TEXT3};
        """)
    return label

def icon_button(icon_text_or_path):
    
    button = QPushButton(icon_text_or_path)
    
    # Calculate half of the button size for a perfect circle radius
    circle_radius = Spacing.ICON_BTN // 2  # 34 // 2 = 17
    
    button.setStyleSheet(f"""
        QPushButton {{
            /* Fixed square dimensions */
            min-width: {Spacing.ICON_BTN}px;
            max-width: {Spacing.ICON_BTN}px;
            min-height: {Spacing.ICON_BTN}px;
            max-height: {Spacing.ICON_BTN}px;
            
            /* Border and Corner Styles */
            border-radius: {circle_radius}px;
            border: 1px solid {Colors.BORDER};
            
            /* Background and Typography */
            background-color: {Colors.SURFACE2};
            font-size: {FontSize.LARGE}px;
            color: {Colors.TEXT};
        }}
        
        /* Smooth hover state for interactive feedback */
        QPushButton:hover {{
            background-color: {Colors.BORDER};
            border-color: {Colors.BORDER_STRONG};
        }}
        
        /* Pressed / Active state */
        QPushButton:pressed {{
            background-color: {Colors.BORDER_STRONG};
        }}
    """)
    return button

def separator(orientation = "horizontal"):
    line = QFrame()
    
    if orientation == "horizontal":
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet(f"""
            QFrame {{
                background-color: {Colors.BORDER};
                max-height: 1px;
                margin: {Spacing.SECTION_GAP}px 0px;
            }}
        """)
    else:  # Vertical separator
        line.setFrameShape(QFrame.Shape.VLine)
        line.setStyleSheet(f"""
            QFrame {{
                background-color: {Colors.BORDER};
                max-width: 1px;
                margin: 0px {Spacing.SECTION_GAP}px;
            }}
        """)
        
    line.setFrameShadow(QFrame.Shadow.Plain)
    return line

def make_card(name , subtitle_text , initials):
    card = QFrame()
    card.setStyleSheet(f"""
        QFrame {{
            background-color: {Colors.SURFACE};
            border: 1px solid {Colors.BORDER};
            border-radius: {Spacing.RADIUS_LG}px;
        }}
        QFrame:hover {{
            border-color: {Colors.ACCENT};
        }}
    """)
    
    # Horizontal layout with tokenized interior padding
    row = QHBoxLayout(card)
    row.setContentsMargins(
        Spacing.CARD_PADDING_H, 
        Spacing.CARD_PADDING_V, 
        Spacing.CARD_PADDING_H, 
        Spacing.CARD_PADDING_V
    )
    row.setSpacing(Spacing.SECTION_GAP)

    # Circular Avatar Setup
    av = QLabel(initials)
    av.setFixedSize(Spacing.AVATAR_LG, Spacing.AVATAR_LG)
    av.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    # Calculate radius dynamically (44 // 2 = 22)
    av_radius = Spacing.AVATAR_LG // 2
    
    av.setStyleSheet(f"""
        QLabel {{
            background-color: {Colors.AV_GREEN_BG};
            color: {Colors.AV_GREEN_TEXT};
            border-radius: {av_radius}px;
            font-weight: {FontWeight.BOLD};
            font-size: {FontSize.MEDIUM}px;
            border: none; /* Prevents inheriting the parent QFrame's border */
        }}
    """)

    # Information Stack (using your existing title and subtitle functions)
    info = QVBoxLayout()
    info.setSpacing(2) # Minor gap between name and subtitle
    
    name_label = title(name , BOLD = False)
    name_label.setStyleSheet(name_label.styleSheet() + "border: none;") # strip QFrame border inheritance
    
    sub_label = subtitle(subtitle_text)
    sub_label.setStyleSheet(sub_label.styleSheet() + "border: none;")
    
    info.addWidget(name_label)
    info.addWidget(sub_label)

    # Chevron Arrow Indicator on the right side
    chevron = QLabel("›")
    chevron.setStyleSheet(f"""
        QLabel {{
            color: {Colors.TEXT3};
            font-size: {FontSize.XL}px;
            font-weight: {FontWeight.NORMAL};
            border: none;
        }}
    """)

    # Assemble the layout rows
    row.addWidget(av)
    row.addLayout(info)
    row.addStretch()
    row.addWidget(chevron)

    return card
