import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QTextEdit
from PyQt5.QtGui import QFont
from modules.module1_introduction_to_finops import module1
from modules.module2_language_of_finops_and_cloud import module2
from modules.module3_finops_lifecycle import module3

class FinOpsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FinOps Learning App")
        self.setGeometry(100, 100, 800, 600)
        
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Add a title label
        title_label = QLabel("FinOps Learning App")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Add buttons for each module
        btn_module1 = QPushButton("Module 1: Introduction to FinOps")
        btn_module1.clicked.connect(self.show_module1)
        layout.addWidget(btn_module1)

        btn_module2 = QPushButton("Module 2: Language of FinOps and Cloud")
        btn_module2.clicked.connect(self.show_module2)
        layout.addWidget(btn_module2)

        btn_module3 = QPushButton("Module 3: FinOps Lifecycle")
        btn_module3.clicked.connect(self.show_module3)
        layout.addWidget(btn_module3)

        btn_module4 = QPushButton("Module 4: Allocation")
        btn_module4.clicked.connect(self.show_module4)
        layout.addWidget(btn_module4)

        btn_module5 = QPushButton("Module 5: Tags, Labels, and Accounts")
        btn_module5.clicked.connect(self.show_module5)
        layout.addWidget(btn_module5)

        btn_module6 = QPushButton("Module 6: Optimise Phase")
        btn_module6.clicked.connect(self.show_module6)
        layout.addWidget(btn_module6)

        btn_module7 = QPushButton("Module 7: Automating Cost Management")
        btn_module7.clicked.connect(self.show_module7)
        layout.addWidget(btn_module7)

        btn_module8 = QPushButton("Module 8: FinOps for the Container World")
        btn_module8.clicked.connect(self.show_module8)
        layout.addWidget(btn_module8)

        btn_module9 = QPushButton("Module 9: Managing to Unit Economics: FinOps Nirvana")
        btn_module9.clicked.connect(self.show_module9)
        layout.addWidget(btn_module9)

        # Apply styling to buttons
        for btn in [btn_module1, btn_module2, btn_module3, btn_module4, btn_module5, btn_module6, btn_module7, btn_module8, btn_module9]:
            btn.setStyleSheet("font-size: 18px; padding: 10px;")

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_module1(self):
        content = module1.get_content()
        self.show_module_content("Module 1: Introduction to FinOps", content)

    def show_module2(self):
        content = module2.get_content()
        self.show_module_content("Module 2: Language of FinOps and Cloud", content)

    def show_module3(self):
        content = module3.get_content()
        self.show_module_content("Module 3: FinOps Lifecycle", content)

    def show_module4(self):
        self.show_module_content("Module 4: Allocation", "Allocation is crucial for understanding and managing cloud costs. It helps in attributing costs to the right teams and projects, ensuring accountability and transparency.")

    def show_module5(self):
        self.show_module_content("Module 5: Tags, Labels, and Accounts", "Starting early with tagging helps in organizing and managing cloud resources effectively.")

    def show_module6(self):
        self.show_module_content("Module 6: Optimise Phase", "Adjusting cloud usage and spending to meet organizational goals is a key aspect of the optimize phase.")

    def show_module7(self):
        self.show_module_content("Module 7: Automating Cost Management", "The goal of automation in cost management is to reduce manual effort, increase efficiency, and ensure consistent application of cost-saving measures.")

    def show_module8(self):
        self.show_module_content("Module 8: FinOps for the Container World", "The move to container orchestration involves using tools like Kubernetes to manage containerized applications. This shift brings new challenges and opportunities for FinOps.")

    def show_module9(self):
        self.show_module_content("Module 9: Managing to Unit Economics: FinOps Nirvana", "Metrics are essential for understanding unit economics. They provide the data needed to make informed decisions about cloud spending and efficiency.")

    def show_module_content(self, title, content):
        self.setWindowTitle(title)
        layout = QVBoxLayout()

        label = QLabel(title)
        label.setFont(QFont("Arial", 20, QFont.Bold))
        layout.addWidget(label)

        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setText(content)
        layout.addWidget(text_edit)

        back_button = QPushButton("Back")
        back_button.clicked.connect(self.initUI)
        back_button.setStyleSheet("font-size: 16px; padding: 8px;")
        layout.addWidget(back_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FinOpsApp()
    window.show()
    sys.exit(app.exec_())