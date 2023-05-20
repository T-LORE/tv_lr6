import math
import sys
import re
from mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QListWidgetItem, QFileDialog, QTableWidgetItem
from PySide6.QtCore import Slot, Signal, Qt
from PySide6.QtGui import QIcon
from qpixmapCreator import mathTex_to_QPixmap
from workingWithRowData import getVariationRow, getFrequencyRow, RowType, getX, getD, getSigma, getS, split
import numpy as np
import pyqtgraph as pg


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mode = 0
        self.currentArray = []
        self.currentIntervals = []
        
        #Как записывается формула: r"$Твоя формула$"
        qpixmap = mathTex_to_QPixmap(r"$P_{n} (m) = C^{m}_{n}*p^{m}*q^{n-m} $", 20)
        #Формула среднего выборочного
        x = mathTex_to_QPixmap(r"$\overline{X_{в}} = \frac{1}{n} \sum_{i=1}^{n} x_{i} * m_{i}$", 20)
        self.ui.formulaX.setPixmap(x)
        #Формула выборочной дисперсии
        d = mathTex_to_QPixmap(r"$D_{в} = X^{2} - (\overline{X_{в}})^{2}$", 20)
        self.ui.formulaD.setPixmap(d)
        #Формула выборочного среднего квадратического отклонения
        sigma = mathTex_to_QPixmap(r"$\sigma_{в} = \sqrt{D_{в}}$", 20)
        self.ui.formulaSigma.setPixmap(sigma)
        #Формула выборочного среднего квадратического отклонения
        s = mathTex_to_QPixmap(r"$S_{в} = \sqrt{D_{в}}$", 20)
        self.ui.formulaS.setText("S = что это такое?")
        
        #поменять высоту ячеек в таблице
        self.ui.rowsTable.verticalHeader().setDefaultSectionSize(40)
        
        #Прописанные коннекты
        self.ui.openFileBtn.clicked.connect(self.openFileBtnClicked_1)
        self.ui.openFileBtn_2.clicked.connect(self.openFileBtnClicked_2)
        self.ui.openFileBtn_3.clicked.connect(self.openFileBtnClicked_3)
        self.ui.frequencyPolygonBtn.clicked.connect(self.generateFrequencyPolygon)
        self.ui.relativeFrequencyPolygonBtn.clicked.connect(self.generateRelativeFrequencyPolygon)
        self.ui.empiricalFunctionBtn.clicked.connect(self.generateEmpiricalFunction)
        self.ui.firstTask.clicked.connect(lambda x: (self.setCurrentMode(0)))
        self.ui.secondTask.clicked.connect(lambda x: (self.setCurrentMode(1)))
        self.ui.thirdTask.clicked.connect(lambda x: (self.setCurrentMode(2)))
        
        self.setCurrentMode(0)
        
    @Slot()
    def setCurrentMode(self, newMode: str):
        self.mode = newMode
        if self.mode == 0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        elif self.mode == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        elif self.mode == 2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
            
        print(f"Changed mode to { newMode }")
        
    
    @Slot()    
    def openFileBtnClicked_1(self):
        #Выбор файла с помощью диалогового окна QfileDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Текстовый файл (*.txt)")
        if fileName:
            #Открытие файла
            file = open(fileName, 'r')
            
            #Чтение массива целых чисел из файла
            self.currentArray = np.loadtxt(file, dtype=int)
           
            #Закрытие файла
            file.close()
            
            #Вывод массива чисел в виджет через запятую
            self.ui.fileBuffer.setText(np.array2string(self.currentArray, formatter={'float_kind':lambda x: "%.1f" % x}).replace('[','').replace(']', ''))
            
            #Вывод сообщения в консоль
            print("Файл успешно открыт")
            
            #Очистить таблицу
            self.ui.rowsTable.clear()
            #Вывести вариационный ряд
            self.showVariationRow()
            #Вывести статистический ряд частот
            self.showFrequencyRows()
            #Вывести D выборочное
            self.showD()
            #Вывести x выборочное
            self.showX()
            #Вывести сигма выборочное
            self.showSigma()
            #Вывести результат S
            self.showS()            
    
    @Slot()    
    def openFileBtnClicked_2(self):
        #Выбор файла с помощью диалогового окна QfileDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Текстовый файл (*.txt)")
        if fileName:
            #Открытие файла
            file = open(fileName, 'r')
            
            #Чтение массива целых чисел из файла
            self.currentArray = np.loadtxt(file)
            
            #Закрытие файла
            file.close()
            
            #Вывод массива чисел в виджет через запятую
            self.ui.fileBuffer.setText(np.array2string(self.currentArray, formatter={'float_kind':lambda x: "%.1f" % x}).replace('[','').replace(']', ''))                      
                        
            #Получить кол-во интервалов от пользователя
            self.intervalCount = int(self.ui.userIntervalCount.text())
                          
            #Вывести интервальный ряд
            self.showIntervalRow()
            
            #Вывести группированный ряд
            self.showGroupRow()
            
            #Построить полигон вероятностей
            
            #Найти эмпирическую функцию
            
            #Построить график эмпирической функции
            
            #Вывести D выборочное
            self.showD()
            #Вывести x выборочное
            self.showX()
            #Вывести сигма выборочной
            self.showSigma()
            #Вывести результат S
            self.showS()
            
    @Slot()    
    def openFileBtnClicked_3(self):
        #Выбор файла с помощью диалогового окна QfileDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Текстовый файл (*.txt)")
        if fileName:
            #Открытие файла
            file = open(fileName, 'r')
            
            #Чтение интервалов и их n из файла
            self.currentIntervals = np.loadtxt(file)
            
            #Закрытие файла
            file.close()
            
            #Вывод интервала чисел в виджет через запятую
            
            #Получить интервалы от пользователя
            
            #Вывод сообщения в консоль
            print("Файл успешно открыт")
            
            #Очистить таблицу интервального ряда
            
            #Посчитать n для каждого интервала
                
            #Заполняем таблицу интервального ряда
            
            #Очистить таблицу группированного ряда
            
            #Находим центры интервалов
            
            #Заполняем таблицу группированого ряда
            
            #Построить полигон вероятностей
            
            #Найти эмпирическую функцию
            #Построить график эмпирической функции
            
             
            
            
            #Вывести вариационный ряд
            self.showVariationRow()
            #Вывести статистический ряд частот
            self.showFrequencyRows()
            #Вывести D выборочное
            self.showD()
            #Вывести x выборочное
            self.showX()
            #Вывести сигма выборочной
            self.showSigma()
            #Вывести результат S
            self.showS()
            
    
    @Slot()
    def showVariationRow(self):
        self.variationRow = getVariationRow(self.currentArray)
       
        #Вывод вариационного ряда
        self.ui.variationRowLine.setText(np.array2string(self.variationRow, formatter={'float_kind':lambda x: "%.1f" % x}).replace('[','').replace(']', ''))
        print("Вариационный ряд успешно выведен")
           
    @Slot()
    def showFrequencyRows(self):
        frequencyRow = getFrequencyRow(self.currentArray, RowType.FREQUENCY)
        relativeFrequencyRow = getFrequencyRow(self.currentArray, RowType.RELATIVE_FREQUENCY)
        
        self.ui.rowsTable.setColumnCount(len(frequencyRow['numbers']))
        
        #Вывод чисел
        for i in range(len(frequencyRow['numbers'])):
            self.ui.rowsTable.setItem(0, i, QTableWidgetItem(str(frequencyRow['numbers'][i])))
        print("Числа успешно выведены")
        
        
        #Вывод статистического ряда частот
        for i in range(len(frequencyRow['frequencies'])):
            self.ui.rowsTable.setItem(1, i, QTableWidgetItem(str(frequencyRow['frequencies'][i])))
        print("Статистический ряд частот успешно выведен")
        
        #Вывод статистического ряда относительных частот в виде натуральной дроби
        for i in range(len(relativeFrequencyRow['numerators'])):
            numerator = relativeFrequencyRow['numerators'][i]
            denominator = relativeFrequencyRow['denominator']
            naturalFraction = mathTex_to_QPixmap(r"$\frac{" + str(numerator) + "}{" + str(denominator) + "}$", 15)
            newItem = QTableWidgetItem("")
            newItem.setData(Qt.DecorationRole, naturalFraction)
            self.ui.rowsTable.setItem(2, i, newItem)
        print("Статистический ряд относительных частот успешно выведен")
    
    @Slot()
    def generateFrequencyPolygon(self):
        #Получение данных из таблицы
        frequencyRow = getFrequencyRow(self.currentArray, RowType.FREQUENCY)
        
        #Построение графика в отдельном окне
        #Получение данных для графика
        x = frequencyRow['numbers']
        y = frequencyRow['frequencies']
        #Построение графика. Не выделять точки построения, задать цвет линии и точек
        penLines = pg.mkPen(color=(0, 0, 0), width=2)
        
        #График с выколотыми точками
        # pg.plot(x, 
        #         y, 
        #         title='Плигон частот', 
        #         pen=penLines, 
        #         symbol='o', 
        #         symbolPen=penDots,    #Цвет обводки точек
        #         symbolBrush='w',      #Цвет заливки точек
        #         symbolSize=10, 
        #         background='w', 
        #         foreground='k', 
        #         antialias=True,
        #         fillLevel=0,
        #         fillOutline=True)
        
        pg.plot(x, 
                y, 
                title='Плигон частот', 
                pen=penLines, 
                background='w', 
                foreground='k', 
                antialias=True,
                fillLevel=0,
                fillOutline=True,
                labels={'left': 'Частота', 'bottom': 'Число'})
        
        
        
        #Вывод сообщения в консоль
        print("График частотного полигональной линии успешно построен")
        
        
        
    @Slot()
    def generateRelativeFrequencyPolygon(self):
        #Получение данных из таблицы
        relativeFrequencyRow = getFrequencyRow(self.currentArray, RowType.RELATIVE_FREQUENCY)
        
        pg.plot(relativeFrequencyRow['numbers'],
                relativeFrequencyRow['numerators']/relativeFrequencyRow['denominator'],
                title='Плигон относительных частот', 
                pen=pg.mkPen(color=(0, 0, 0), width=2), 
                background='w', 
                foreground='#000000', 
                antialias=True,
                fillLevel=0,
                fillOutline=True,
                labels={'left': '<span style="color: #000">Частота</span>', 'bottom': '<span style="color: #000">Число</span>'},
                color = '#000000')
        
        
        #Вывод сообщения в консоль
        print("График частотной полигональной линии успешно построен")
    
    @Slot()
    def generateEmpiricalFunction(self):
        print("График эмпирической функции успешно построен")
        #Создать график эмпирической функции
        #Получение данных из таблицы
        relativefrequencyRow = getFrequencyRow(self.currentArray, RowType.RELATIVE_FREQUENCY)
        
        #Построение графика в отдельном окне
        #Получение данных для графика
        x = relativefrequencyRow['numbers']
        np.append(x, 999)
        empiricalFunction = {
            'start': [],
            'end': [],
            'y': []
        }
        for i in range(len(x)-1):
            empiricalFunction['start'].append(x[i]) 
            empiricalFunction['end'].append(x[i+1])
            empiricalFunction['y'].append(sum(relativefrequencyRow['numerators'][:i+1])/relativefrequencyRow['denominator'])
        #Построение разорванного графика.

        self.plotWidget = pg.plot(title = 'asdasd', background = 'w', foreground = 'k')
       
        for i in range(len(empiricalFunction['y'])):
            self.plotWidget.plot([empiricalFunction['start'][i]],[empiricalFunction['y'][i]],pen=pg.mkPen(color=(0, 0, 0), width=2), symbol='o', symbolPen=pg.mkPen(color=(0, 0, 0), width=2), symbolBrush='w', symbolSize=10, antialias=True)
            self.plotWidget.plot([empiricalFunction['start'][i], empiricalFunction['end'][i]], [empiricalFunction['y'][i], empiricalFunction['y'][i]], pen=pg.mkPen(color=(0, 0, 0), width=2))
        
        
        
    @Slot()
    def showD(self):
        self.ui.lineD.setText(str(getD(self.currentArray)))
    
    @Slot()
    def showX(self):
        self.ui.lineX.setText(str(getX(self.currentArray)))
    
    @Slot()
    def showSigma(self):
        self.ui.lineSigma.setText(str(getSigma(self.currentArray)))
    
    @Slot()
    def showS(self):
        self.ui.lineS.setText(str(getS(self.currentArray)))
    
    @Slot()
    def showIntervalRow(self):
        #Очистка таблицы
        self.ui.intervalRow2.clear()
        
        
        
        #Получить интервалы
        try:
            self.intervalRow = split(self.currentArray, self.intervalCount)
        except ValueError as e:
            print(e)
            return
        else: 
            #
            print(self.intervalRow)
            #Добавить столбцы в таблицу
            self.ui.intervalRow2.setColumnCount(len(self.intervalRow['start']))
            #Заполнить первую строку таблицы - интервалы [x1,x2]
            for i in range (len(self.intervalRow['start'])):
                string = "[" + str(self.intervalRow['start'][i]) + "," + str(self.intervalRow['end'][i]) + "]"
                newItem = QTableWidgetItem(string)
                self.ui.intervalRow2.setItem(0, i, newItem)
            #Заполнить вторую строку таблицы - частоты интервалов
            for i in range (len(self.intervalRow['start'])):
                newItem = QTableWidgetItem(str(self.intervalRow['frequency'][i]))
                self.ui.intervalRow2.setItem(1, i, newItem)
                
            #Заполнить третью строку таблицы - относительные частоты в виде натуральной дроби
            for i in range(len(self.intervalRow['start'])):
                numerator = self.intervalRow['frequency'][i]
                denominator = len(self.currentArray)
                naturalFraction = mathTex_to_QPixmap(r"$\frac{" + str(numerator) + "}{" + str(denominator) + "}$", 15)
                newItem = QTableWidgetItem("")
                newItem.setData(Qt.DecorationRole, naturalFraction)
                self.ui.intervalRow2.setItem(2, i, newItem)
            print("Интервал частот успешно выведен")
        
    @Slot()
    def showGroupRow(self):
         #Очистка таблицы
        self.ui.groupRow2.clear()
        
        #Получить интервалы
        try:
            self.intervalRow = split(self.currentArray, self.intervalCount)
        except ValueError as e:
            print(e)
            return
        else:
            #Добавить столбцы в таблицу
            self.ui.groupRow2.setColumnCount(len(self.intervalRow['start']))
            #Увеличить размер ячеек
            for i in range(len(self.intervalRow['start'])):
                self.ui.groupRow2.setColumnWidth(i, 100)
            #Заполнить первую строку таблицы - интервалы [x1,x2]
            for i in range (len(self.intervalRow['start'])):
                string = "[" + str(self.intervalRow['start'][i]) + "," + str(self.intervalRow['end'][i]) + "]"
                newItem = QTableWidgetItem(string)
                self.ui.groupRow2.setItem(0, i, newItem)
            #Заполнить вторую строку таблицы - частоты интервалов
            for i in range (len(self.intervalRow['start'])):
                newItem = QTableWidgetItem(str(self.intervalRow['frequency'][i]))
                self.ui.groupRow2.setItem(1, i, newItem)
                
            #Заполнить третью строку таблицы - относительные частоты в виде натуральной дроби
            for i in range(len(self.intervalRow['start'])):
                numerator = self.intervalRow['frequency'][i]
                denominator = len(self.currentArray)
                naturalFraction = mathTex_to_QPixmap(r"$\frac{" + str(numerator) + "}{" + str(denominator) + "}$", 15)
                newItem = QTableWidgetItem("")
                newItem.setData(Qt.DecorationRole, naturalFraction)
                self.ui.groupRow2.setItem(2, i, newItem)
            print("Интервал частот успешно выведен")
        
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow() 
    window.show()
    sys.exit(app.exec())
    


