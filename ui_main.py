from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from Stats.statConverter import ConvertStatToRange, GetAdversaryRanges, convertLevelToTier
from Stats.dhStat import Adversary_Type

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

        #Estimation
        self.estimation_button = QPushButton("Generate Estimation")
        self.estimation_button.clicked.connect(self.get_estimation)
        self.layout.addWidget(self.estimation_button)

        self.output_label = QLabel("PF2E estimations")
        self.layout.addWidget(self.output_label)

        self.estimationsLayout = QVBoxLayout()
        self.layout.addLayout(self.estimationsLayout)


        #Daggerheart Recommendation
        self.adversary_type = QComboBox()
        self.adversary_type.addItem("Bruiser")
        self.adversary_type.addItem("Horde")
        self.adversary_type.addItem("Leader")
        #self.adversary_type.addItem("Minion")
        self.adversary_type.addItem("Ranged")
        self.adversary_type.addItem("Skulk")
        self.adversary_type.addItem("Solo")
        self.adversary_type.addItem("Standard")
        self.adversary_type.addItem("Support")
        self.adversary_type.currentTextChanged.connect(self.on_dropdown_change)
        self.layout.addWidget(self.adversary_type)

        self.reccomendations_layout = QVBoxLayout()
        self.layout.addLayout(self.reccomendations_layout)







        self.setLayout(self.layout)

    def get_estimation(self):
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

    def on_dropdown_change(self, value):
        self.clear_layout(self.reccomendations_layout)
        adversary_type = Adversary_Type(value)
        tier = convertLevelToTier(int(self.level_input.text()))
        ranges = GetAdversaryRanges(tier, adversary_type)
        #print(ranges)
        difficulity = QLabel(f"Difficulty: {ranges["Difficulty"]}")
        m_thresh = QLabel(f"Major Threshold: {ranges["Major Threshold"]}")
        s_thresh = QLabel(f"Severe Threshold: {ranges["Severe Threshold"]}")
        hp = QLabel(f"HP: {ranges["HP"]}")
        strs = QLabel(f"Stress: {ranges["Stress"]}")
        att_bon = QLabel(f"ATK: {ranges["ATK"]}")
        dmg_avg = QLabel(f"Damage Average: {ranges["Damage Average"]}")
        self.reccomendations_layout.addWidget(difficulity)
        self.reccomendations_layout.addWidget(m_thresh)
        self.reccomendations_layout.addWidget(s_thresh)
        self.reccomendations_layout.addWidget(hp)
        self.reccomendations_layout.addWidget(strs)
        self.reccomendations_layout.addWidget(att_bon)
        self.reccomendations_layout.addWidget(dmg_avg)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        
        
        



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()