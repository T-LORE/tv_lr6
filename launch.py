import math
import sys
import re
from mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QListWidgetItem, QFileDialog, QTableWidgetItem
from PySide6.QtCore import Slot, Signal, Qt
from PySide6.QtGui import QIcon
from qpixmapCreator import mathTex_to_QPixmap
from workingWithRowData import getVariationRow, getFrequencyRow, RowType, getX, getD, getSigma, getS
import numpy as np
import pyqtgraph as pg

from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np

import graphingFunctions as graph


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
            self.currentArray = np.loadtxt(file)
           
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
            
            #Разделить массив на интервалы
            print(np.array_split(self.currentArray, 3))
            
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
        
        #Получение данных для графика
        x = frequencyRow['numbers']
        y = frequencyRow['frequencies']
        
        #Построение графика
        graph.drawPolygonGraph(x, y, xLabel="Число", yLabel="Частота", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)

                          
        #Вывод сообщения в консоль
        print("График частотного полигональной линии успешно построен")
        
        
        
    @Slot()
    def generateRelativeFrequencyPolygon(self):
        #Получение данных из таблицы
        relativeFrequencyRow = getFrequencyRow(self.currentArray, RowType.RELATIVE_FREQUENCY)
        
        #Рассчёт данных для графика
        x = relativeFrequencyRow['numbers']
        y = relativeFrequencyRow['numerators']/relativeFrequencyRow['denominator']
        
        #Построение графика
        graph.drawPolygonGraph(x, y, xLabel="Число", yLabel="Относительная частота", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)
        
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
            
        #Построение разорванного графика
        graph.drawEmpiricalGraph(empiricalFunction, xLabel="X axis", yLabel="Y axis", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)
             
        
        
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
                

 
        
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow() 
    window.show()
    sys.exit(app.exec())
    


