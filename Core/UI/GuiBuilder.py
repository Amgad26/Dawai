from Style.Colors import Colors
from Style.FontSize import FontSize
from Style.FontWeight import FontWeight
from Style.Spacing import Spacing

from CardFrame import CardFrame
from PyQt6.QtWidgets import QLabel , QPushButton , QFrame , QHBoxLayout , QVBoxLayout , QCheckBox , QWidget , QSpinBox , QScrollArea
from PyQt6.QtCore import Qt

def build_avatar(title : str) -> QWidget:
    
    initials = [name[0] for name in title.split()]
    if len(initials) >= 2:
        
        initials = "".join(initials)[:2]
        
    else:
        
        initials = "".join(initials)
        
    av = QLabel(initials)
    av.setFixedSize(Spacing.AVATAR_LG , Spacing.AVATAR_LG)
    av.setAlignment(Qt.AlignmentFlag.AlignCenter)
    radius = Spacing.AVATAR_LG // 2
    av.setStyleSheet(f"""
        QLabel {{
            background-color: {Colors.AV_GREEN_BG};
            color: {Colors.AV_GREEN_TEXT};
            border-radius: {radius}px;
            font-weight: {FontWeight.BOLD};
            font-size: {FontSize.MEDIUM}px;
            border: none;
        }}
    """)
    return av

def build_chevron() -> QWidget:
    
    chevron = QLabel("›")
    chevron.setStyleSheet(f"""
        QLabel {{
            color: {Colors.TEXT3};
            font-size: {FontSize.XL}px;
            font-weight: {FontWeight.NORMAL};
            border: none;
        }}
    """)
    return chevron

def build_checkbox(checked = False , on_toggle = None) -> QWidget:
    
    box = QCheckBox()
    box.setChecked(checked)
    box.setCursor(Qt.CursorShape.PointingHandCursor)

    box.setStyleSheet(f"""
        QCheckBox::indicator {{
            width: 18px;
            height: 18px;
            border-radius: {Spacing.RADIUS_SM}px;
            border: 1px solid {Colors.BORDER};
            background-color: {Colors.BORDER_STRONG};
        }}

        QCheckBox::indicator:unchecked:hover {{
            border-color: {Colors.ACCENT};
        }}

        QCheckBox::indicator:checked {{
            background-color: {Colors.ACCENT};
            border: 1px solid {Colors.ACCENT};
        }}

        QCheckBox::indicator:checked:hover {{
            background-color: {Colors.ACCENT};
            border-color: {Colors.ACCENT};
        }}
    """)

    if on_toggle:
        
        box.toggled.connect(on_toggle)
        
    return box

def build_status_label(text: str , bg = None , fg = None) -> QWidget:
    
    bg = bg or Colors.AV_GREEN_BG
    fg = fg or Colors.AV_GREEN_TEXT
    lbl = QLabel(text)
    lbl.setStyleSheet(f"""
        QLabel {{
            background-color: {bg};
            color: {fg};
            border-radius: {Spacing.RADIUS_SM}px;
            padding: 2px 8px;
            font-size: {FontSize.SMALL}px;
            font-weight: {FontWeight.BOLD};
            border: none;
        }}
    """)
    return lbl

def build_spinbox(value = 0 , minimum = 0 , maximum = 99 , on_change = None) -> QWidget:
    
    spin = QSpinBox()
    spin.setRange(minimum , maximum)
    spin.setValue(value)
    spin.setFixedWidth(80)

    spin.setStyleSheet(f"""
        QSpinBox {{
            background-color: {Colors.SURFACE};
            color: {Colors.TEXT};
            border: 1px solid {Colors.BORDER};
            border-radius: {Spacing.RADIUS_SM}px;
            padding: 2px 4px;
            font-size: {FontSize.BODY}px;
        }}

        QSpinBox::up-button, QSpinBox::down-button {{
            width: 16px;
            border: none;
            background-color: {Colors.SURFACE2};
        }}

        QSpinBox::up-button:hover, QSpinBox::down-button:hover {{
            background-color: {Colors.BORDER};
        }}
    """)

    if on_change:
        
        spin.valueChanged.connect(on_change)

    return spin

def make_card(
    name: str,
    subtitle_text: str,
    *,
    leading: QWidget,
    trailing: QWidget,
    clickable: bool = False,
) -> CardFrame:
    card = CardFrame(clickable = clickable)

    row = QHBoxLayout(card)
    row.setContentsMargins(
        Spacing.CARD_PADDING_H, Spacing.CARD_PADDING_V,
        Spacing.CARD_PADDING_H, Spacing.CARD_PADDING_V
    )
    row.setSpacing(Spacing.SECTION_GAP)

    info = QVBoxLayout()
    info.setSpacing(2)

    name_label = title(name , BOLD = False)
    name_label.setStyleSheet(name_label.styleSheet() + "border: none;")

    sub_label = subtitle(subtitle_text)
    sub_label.setStyleSheet(sub_label.styleSheet() + "border: none;")

    info.addWidget(name_label)
    info.addWidget(sub_label)

    row.addWidget(leading)
    row.addLayout(info)
    row.addStretch()
    row.addWidget(trailing)

    return card

def build_card_list(cards: list[QWidget]) -> QScrollArea:
    
    container = QWidget()
    layout = QVBoxLayout(container)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(Spacing.SECTION_GAP)

    for card in cards:
        
        layout.addWidget(card)
        
    layout.addStretch()  # pushes cards to top instead of spreading them out

    scroll = QScrollArea()
    scroll.setWidget(container)
    scroll.setWidgetResizable(True)  # important — lets container resize with the scroll area
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    scroll.setStyleSheet(f"""
        QScrollArea {{
            border: none;
            background-color: transparent;
        }}
        QScrollBar:vertical {{
            width: 8px;
            background: transparent;
        }}
        QScrollBar::handle:vertical {{
            background: {Colors.BORDER};
            border-radius: 4px;
            min-height: 20px;
        }}
        QScrollBar::handle:vertical:hover {{
            background: {Colors.BORDER_STRONG};
        }}
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0px;
        }}
    """)
    return scroll

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
