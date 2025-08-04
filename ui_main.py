from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton
from Stats.statConverter import ConvertStatToRange

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pf2e-daggerheart converter")
        self.layout = QVBoxLayout()

        self.pf2eStatHeader = QLabel("Enter stats pf2e:")
        self.layout.addWidget(self.pf2eStatHeader)
        
        #LEVEL
        level_layout = QHBoxLayout()
        level_label = QLabel("Level:")
        self.level_input = QLineEdit()
        self.level_input.setPlaceholderText("Enter level")

        level_layout.addWidget(level_label)
        level_layout.addWidget(self.level_input)

        self.layout.addLayout(level_layout)

        #AC
        armor_layout = QHBoxLayout()
        armor_label = QLabel("Armor Class:")
        self.armor_input = QLineEdit()
        self.armor_input.setPlaceholderText("Enter Armor Class")

        armor_layout.addWidget(armor_label)
        armor_layout.addWidget(self.armor_input)

        self.layout.addLayout(armor_layout)

        #HP
        hp_layout = QHBoxLayout()
        hp_label = QLabel("Hit Points:")
        self.hp_input = QLineEdit()
        self.hp_input.setPlaceholderText("Enter Hit Points")

        hp_layout.addWidget(hp_label)
        hp_layout.addWidget(self.hp_input)

        self.layout.addLayout(hp_layout)

        #ATTACK BONUS
        att_bon_layout = QHBoxLayout()
        att_bon_label = QLabel("Attack Bonus:")
        self.att_bon_input = QLineEdit()
        self.att_bon_input.setPlaceholderText("Enter Attack Bonus")

        att_bon_layout.addWidget(att_bon_label)
        att_bon_layout.addWidget(self.att_bon_input)

        self.layout.addLayout(att_bon_layout)


        self.recommend_button = QPushButton("Generate Recommendation")
        self.recommend_button.clicked.connect(self.get_recommendations)
        self.layout.addWidget(self.recommend_button)

        self.output_label = QLabel("PF2E estimations")
        self.layout.addWidget(self.output_label)

        self.estimationsLayout = QVBoxLayout()
        self.layout.addLayout(self.estimationsLayout)

        self.setLayout(self.layout)

    def get_recommendations(self):
        level = self.level_input.text()
        print(f"recommending for level - {level}")
        #AC
        ac_estimated_value = ConvertStatToRange(level, int(self.armor_input.text()), "armor_class")
        ac_estimation = QLabel(f"Armor Class: {ac_estimated_value}")
        self.estimationsLayout.addWidget(ac_estimation)
        #HP
        hp_estimated_value = ConvertStatToRange(level, int(self.hp_input.text()), "hit_points")
        hp_estimation = QLabel(f"Hit Points: {hp_estimated_value}")
        self.estimationsLayout.addWidget(hp_estimation)
        #ATTACK BONUS
        att_bon_estimated_value = ConvertStatToRange(level, int(self.att_bon_input.text()), "strike_attack_bonus")
        att_bon_estimation = QLabel(f"Strike Bonus: {att_bon_estimated_value}")
        self.estimationsLayout.addWidget(att_bon_estimation)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()