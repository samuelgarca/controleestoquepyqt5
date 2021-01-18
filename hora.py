from PyQt5.QtCore import QDateTime, Qt


data = QDateTime.currentDateTime()


print(data.toString(Qt.ISODate))