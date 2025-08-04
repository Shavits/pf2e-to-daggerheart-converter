from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pf2e-daggerheart converter")
        self.layout = QVBoxLayout()

        self.input_label = QLabel("Enter stats pf2e:")
        self.layout.addWidget(self.input_label)

        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)

        self.recommend_button = QPushButton("Generate Recommendation")
        self.recommend_button.clicked.connect(self.get_recommendations)
        self.layout.addWidget(self.recommend_button)

        self.output_label = QLabel("Recommended Daggerheart stats")
        self.layout.addWidget(self.output_label)

        self.setLayout(self.layout)

    def get_recommendations(self):
        input_value = self.input_field.text()
        # Logic to calculate recommendations based on input_value
        recommended_value = "Recommended value based on " + input_value  # Placeholder logic
        self.output_label.setText(recommended_value)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()