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
        
        section_name_label = GuiBuilder.section_name("USERS")
        
        card1 = GuiBuilder.make_card("A" , "2 medicines" ,
                                    leading = GuiBuilder.build_avatar("A") ,
                                    trailing = GuiBuilder.build_chevron() ,
                                    clickable = True)
        
        card2 = GuiBuilder.make_card("Hassan Yehia Hassan" , "100 medicines" ,
                            leading = GuiBuilder.build_avatar("Hassan Yehia Hassan") ,
                            trailing = GuiBuilder.build_chevron() ,
                            clickable = True)
        
        card3 = GuiBuilder.make_card("Vitamin D 1000IU" , "12.50 EGP · tablet · round" ,
                    leading = GuiBuilder.build_avatar("💊") ,
                    trailing = GuiBuilder.icon_button("✏️") ,
                    clickable = False)
        
        card4 = GuiBuilder.make_card("Vitamin D 1000IU" , "12.50 EGP · tablet · round" ,
            leading = GuiBuilder.build_avatar("💊") ,
            trailing = GuiBuilder.build_checkbox() ,
            clickable = False)
        
        card5 = GuiBuilder.make_card("Vitamin D 1000IU" , "12.50 EGP · tablet · round" ,
            leading = GuiBuilder.build_avatar("💊") ,
            trailing = GuiBuilder.build_status_label("25.00 EGP") ,
            clickable = False)
        
        card6 = GuiBuilder.make_card("Vitamin D 1000IU" , "12.50 EGP · tablet · round" ,
            leading = GuiBuilder.build_avatar("💊") ,
            trailing = GuiBuilder.build_spinbox() ,
            clickable = False)
        
        cards = [card1, card2, card3, card4, card5 , card6 , card1 , card1 , card1 , card1 , card1 , card1 , card1]
        scroll_area = GuiBuilder.build_card_list(cards)
    
        middle_panel_layout.addWidget(section_name_label)
        middle_panel_layout.addWidget(scroll_area)
        middle_panel_layout.addStretch() 
        
        main_layout.addWidget(middle_panel)