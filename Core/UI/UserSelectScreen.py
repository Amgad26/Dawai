from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
import GuiBuilder

class UserSelectScreen(QWidget):

    def __init__(self, main_window):
        
        super().__init__()
        self.main = main_window

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        header_panel = QWidget()
        header_panel_layout = QHBoxLayout(header_panel)

        labels_panel = QWidget()
        labels_panel_layout = QVBoxLayout(labels_panel)
        title = GuiBuilder.title("Dawai 💊")
        subtitle = GuiBuilder.subtitle("Who's managing medicines?")
        labels_panel_layout.addWidget(title)
        labels_panel_layout.addWidget(subtitle)

        setting_button = GuiBuilder.icon_button("⚙️")

        header_panel_layout.addWidget(labels_panel)
        header_panel_layout.addStretch()
        header_panel_layout.addWidget(setting_button)

        main_layout.addWidget(header_panel)
        main_layout.addWidget(GuiBuilder.separator("horizontal"))
        
        middle_panel = QWidget()
        middle_panel_layout = QVBoxLayout(middle_panel)
        
        section_name = GuiBuilder.section_name("USERS")
        middle_panel_layout.addWidget(section_name)
        
        card = GuiBuilder.make_card("Amgad" , "6 meds" , "AM")
        middle_panel_layout.addWidget(card)
        
        middle_panel_layout.addStretch() 
        
        main_layout.addWidget(middle_panel)