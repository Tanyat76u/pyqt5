a = 2
b = 3
c = 4
def proverka(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        print("Это треугольник")
    else:
        print("Это не треугольник")


proverka(a, b, c)

#
# @QtCore.pyqtSlot()
# def first_side(self):
#     print(self.lineEdit.text())
#     x = self.lineEdit.text()
#     list1 = x.split()
#     print(list1)
#     a = int(list1[0])
#     b = int(list1[1])
#     c = int(list1[2])
#     self.proverka(a, b, c)