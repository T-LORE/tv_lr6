import math
import sys
import re
from mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QListWidgetItem, QFileDialog, QTableWidgetItem, QTableWidget, QHeaderView, QSizePolicy
from PySide6.QtCore import Slot, Signal, Qt
from PySide6.QtGui import QIcon, QPixmap
from qpixmapCreator import mathTex_to_QPixmap, mathTex_to_QPixmap_system
from workingWithRowData import getVariationRow, getFrequencyRow, RowType, getX, getD, getSigma, getS, split
import numpy as np
import pyqtgraph as pg

from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np

import graphingFunctions as graph
from graphingFunctions import roundValue


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mode = 1
        
        self.currentArray = []
        self.currentIntervals = []
        
        #Включить/выключить динамическую генерацию эмпмрических функций
        self.generateDynamicEmpirical = True
        
        #Как записывается формула: r"$Твоя формула$"
        #Формула среднего выборочного
        x = mathTex_to_QPixmap(r"$\overline{X_{в}} = \frac{1}{n} \sum_{i=1}^{n} x_{i} * m_{i}$", 16)
        self.ui.formulaX.setPixmap(x)
        self.ui.formulaX_2.setPixmap(x)
        self.ui.formulaX_3.setPixmap(x)
        #Формула выборочной дисперсии
        d = mathTex_to_QPixmap(r"$D_{в} = X^{2} - (\overline{X_{в}})^{2}$", 16)
        self.ui.formulaD.setPixmap(d)
        self.ui.formulaD_2.setPixmap(d)
        self.ui.formulaD_3.setPixmap(d)
        #Формула выборочного среднего квадратического отклонения
        sigma = mathTex_to_QPixmap(r"$\sigma_{в} = \sqrt{D_{в}}$", 16)
        self.ui.formulaSigma.setPixmap(sigma)
        self.ui.formulaSigma_2.setPixmap(sigma)
        self.ui.formulaSigma_3.setPixmap(sigma)
        
        #Формула A* (x выборочное)
        aStar = mathTex_to_QPixmap(r"$a^{*} = \frac{1}{n} \sum_{i=1}^{n} x_{i} * m_{i}$", 16)
        self.ui.formulaA_2.setPixmap(aStar)
        self.ui.formulaA_2.setPixmap(aStar)
        self.ui.formulaA_2.setPixmap(aStar)
        
        #Формула сигма* (обычная сигма)
        sigmaStar = mathTex_to_QPixmap(r"$\sigma^{*} = \sqrt{D_{в}}$", 16)
        self.ui.sigmaStar_2.setPixmap(sigmaStar)
        
        # #поменять высоту ячеек в таблице
        # self.ui.rowsTable.verticalHeader().setDefaultSectionSize(40)
        
        
        #Прописанные коннекты
        #Задание 1 массив чисел
        self.ui.secondTask.clicked.connect(lambda x: (self.setCurrentMode(1)))
        self.ui.openFileBtn_2.clicked.connect(self.openFileBtnClicked_2)
        self.ui.frequencyHistogramBtn_2.clicked.connect(self.frequencyHistogram2)
        self.ui.relativeFrequencyHistogramBtn_2.clicked.connect(self.relativeFrequencyHistogram2)
       
        
        #Задание 1 интервалы
        self.ui.thirdTask.clicked.connect(lambda x: (self.setCurrentMode(2)))
        self.ui.openFileBtn_3.clicked.connect(self.openFileBtnClicked_3)
        self.ui.frequencyHistogramBtn_3.clicked.connect(self.frequencyHistogram2)
        self.ui.relativeFrequencyHistogramBtn_3.clicked.connect(self.relativeFrequencyHistogram2)
        self.ui.empiricalIntervalFunctionBtn_3.clicked.connect(lambda x: (graph.drawEmpiricalGraph(self.empiricalIntervalFunction, xLabel="x", yLabel="F*(x)", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)))
        self.ui.empiricalGroupFunctionBtn_3.clicked.connect(lambda x: (graph.drawEmpiricalGraph(self.empiricalGroupFunction, xLabel="x", yLabel="F*(x)", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)))
        self.ui.frequencyPolygonBtn_3.clicked.connect(self.frequencyPolygon2)
        self.ui.relativeFrequencyPolygonBtn_3.clicked.connect(self.relativeFrequencyPolygon2)
        
        #------------------------------------------------------
        #Тест вставки эмпирической функции
        # testEmpirical = {
        #     'start': [4.25, 4.45, 4.55, 4.65, 4.85], 
        #     'end': [4.45, 4.55, 4.65, 4.85, 4.949999999999999], 
        #     'y': [0.27, 0.49, 0.72, 0.82, 1]}
        
        # #Создать строчку Latex из библиотеки matplotLib, в которой будет система эмпирическоф функции по шаблону: F(x) = {[start[i], end[i]]: y[i]}
        # latexStr = r"$F(x)= \begin{cases} "
        # for i in range(len(testEmpirical['start'])):
        #     latexStr += str(testEmpirical['y'][i])
        #     latexStr += r" & \text{при } x \in [" + str(testEmpirical['start'][i]) + r", " + str(testEmpirical['end'][i]) + r"]"
        #     if i != len(testEmpirical['start']) - 1:
        #         latexStr += r" \\ "
        # latexStr += r" \end{cases}$"
        
        # pixmap = mathTex_to_QPixmap_system(latexStr, 20)
        # self.ui.empiricalLatex_1.setPixmap(pixmap)
        
        #------------------------------------------------------
        self.setCurrentMode(1)
        
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
            self.ui.fileBuffer_2.setText(np.array2string(self.currentArray, formatter={'float_kind':lambda x: "%.1f" % x}).replace('[','').replace(']', ''))                      
                        
            #Получить кол-во интервалов от пользователя
            try:
                self.intervalCount = int(self.ui.userIntervalCount.text())
            except ValueError:
                print("Неверно введено кол-во интервалов")
                return
            
            try:
                # self.intervalRow = {
                # 'start' : [],
                # 'end' : [],
                # 'frequency' : []
                # }
                self.intervalRow = split(self.currentArray, self.intervalCount)
            except ValueError as e:
                print(e)
                return
            print("intervalRow: ", self.intervalRow)      
            #Вывести интервальный ряд
            self.showIntervalRow(self.ui.intervalRow2)
            
            #Вывести группированный ряд
            self.showGroupRow(self.ui.groupRow2)
            
            #Создать массив группированного ряда  
            array = np.repeat(self.groupRow['numbers'], self.groupRow['numerators'])
            
            #Вывести D выборочное
            self.ui.lineD_2.setText(str(roundValue(getD(array))))
            #Вывести x выборочное
            self.ui.lineX_2.setText(str(roundValue(getX(array))))
            #Вывести сигма выборочной
            self.ui.lineSigma_2.setText(str(roundValue(getSigma(array))))
            #Вывести результат aStar для нормального закона распределения
            self.aStar = roundValue(getX(array))
            self.ui.lineAStar.setText(str(self.aStar))
            
            #Вывести результат sigmaStar для нормального закона распределения
            self.sigmaStar = roundValue(getSigma(array))
            self.ui.lineSigmaStar.setText(str(self.sigmaStar))
            
            
            
    @Slot()    
    def openFileBtnClicked_3(self):
        #Выбор файла с помощью диалогового окна QfileDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Текстовый файл (*.txt)")
        if fileName:
            #Открытие файла
            file = open(fileName, 'r')
            
            #Чтение интервалов и их n из файла
            self.intervalRow = np.genfromtxt(fileName, delimiter=',', names=True)
            
            #Закрытие файла
            file.close()
            
            #Вывести интервальный ряд
            self.showIntervalRow(self.ui.intervalRow3)
            
            #Вывести группированный ряд
            self.showGroupRow(self.ui.groupRow3)
            
            #Вывод сообщения в консоль
            print("Файл успешно открыт")
            
                                  
            

            #Создать массив группированного ряда  
            array = np.repeat(self.groupRow['numbers'], self.groupRow['numerators'])
            
            #Вывести D выборочное
            self.ui.lineD_3.setText(str(roundValue(getD(array))))
            #Вывести x выборочное
            self.ui.lineX_3.setText(str(roundValue(getX(array))))
            #Вывести сигма выборочной
            self.ui.lineSigma_3.setText(str(roundValue(getSigma(array))))
            #Вывести результат S
            self.ui.lineS_3.setText(str(roundValue(getS(array))))
            #Посчитать эмпирическую функцию
            self.empiricalIntervalFunction = self.empiricalIntervalFunction2()
            #Вывести эмпирическую функцию
            if self.generateDynamicEmpirical:
                self.setEmpirical(self.ui.empiricalIntervalLatex_3, self.empiricalIntervalFunction)
            #Посчитать эмипирическую функцию для группированного ряда
            self.empiricalGroupFunction = self.empiricalGroupFunction2()
            #Вывести эмпирическую функцию для группированного ряда
            if self.generateDynamicEmpirical:
                self.setEmpirical(self.ui.empiricalGroupLatex_3, self.empiricalGroupFunction)
            
    
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
            
        self.ui.rowsTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            
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
        
        #Округление
        x = [roundValue(i) for i in x]
        y = [roundValue(i) for i in y]
        
        #Построение графика
        graph.drawPolygonGraph(x, y, xLabel="Число", yLabel="Относительная частота", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)
        
        #Вывод сообщения в консоль
        print("График частотной полигональной линии успешно построен")
    
    @Slot()
    def generateEmpiricalFunction(self):
        relativefrequencyRow = getFrequencyRow(self.currentArray, RowType.RELATIVE_FREQUENCY)
        
        x = relativefrequencyRow['numbers']
        np.append(x, 999)
        empiricalFunction = {
            'start': [],
            'end': [],
            'y': []
        }
        for i in range(len(x)-1):
            empiricalFunction['start'].append(roundValue(x[i])) 
            empiricalFunction['end'].append(roundValue(x[i+1]))
            empiricalFunction['y'].append(roundValue(sum(relativefrequencyRow['numerators'][:i+1])/relativefrequencyRow['denominator']))
        
        allX = [value for value in empiricalFunction["start"]] + [value for value in empiricalFunction["end"]] 
        xMinDiff = graph.minDiffInList(allX)
        lastx = empiricalFunction['end'][-1] 
        empiricalFunction['start'].append(roundValue(lastx))
        empiricalFunction['end'].append(roundValue(lastx+xMinDiff)) 
        empiricalFunction['y'].append(1)
        
        return empiricalFunction
        #Построение разорванного графика
        
    
    @Slot()
    def showIntervalRow(self, table: QTableWidget):
        #Очистка таблицы
        table.clearContents()
        
        #Добавить столбцы в таблицу
        table.setColumnCount(len(self.intervalRow['start']))
        
        #Заполнить первую строку таблицы - интервалы [x1,x2]
        for i in range (len(self.intervalRow['start'])):
            string = "[" + str(self.intervalRow['start'][i]) + "," + str(self.intervalRow['end'][i]) + "]"
            newItem = QTableWidgetItem(string)
            table.setItem(0, i, newItem)
        #Заполнить вторую строку таблицы - частоты интервалов
        for i in range (len(self.intervalRow['start'])):
            newItem = QTableWidgetItem(str(self.intervalRow['frequency'][i]))
            table.setItem(1, i, newItem)
            
        #Заполнить третью строку таблицы - относительные частоты в виде натуральной дроби
        for i in range(len(self.intervalRow['start'])):
            numerator = self.intervalRow['frequency'][i]
            denominator = sum(self.intervalRow['frequency'])
            naturalFraction = mathTex_to_QPixmap(r"$\frac{" + str(numerator) + "}{" + str(denominator) + "}$", 15)
            newItem = QTableWidgetItem("")
            newItem.setData(Qt.DecorationRole, naturalFraction)
            table.setItem(2, i, newItem)
        
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        print("Интервальный ряд частот и относительных частот успешно построен")
        
    @Slot()
    def showGroupRow(self,table):
        #Очистка таблицы
        table.clearContents()
       
        #Добавить столбцы в таблицу
        table.setColumnCount(len(self.intervalRow['start']))
        #Увеличить размер ячеек
        for i in range(len(self.intervalRow['start'])):
            table.setColumnWidth(i, 100)
        
        self.groupRow = {
            'numbers': [],
            'numerators': [],
            'denominator': sum(self.intervalRow['frequency'])
        }
        
        for i in range(len(self.intervalRow['start'])):
            self.groupRow['numbers'].append((self.intervalRow['start'][i] + self.intervalRow['end'][i]) / 2)
            self.groupRow['numerators'].append(self.intervalRow['frequency'][i])
            
        
        #Заполнить первую строку таблицы - интервалы [x1,x2]
        for i in range(len(self.groupRow['numbers'])):
            string = str(self.groupRow['numbers'][i])  
            newItem = QTableWidgetItem(string)
            table.setItem(0, i, newItem)
        #Заполнить вторую строку таблицы - частоты интервалов
        for i in range (len(self.groupRow['numbers'])):
            newItem = QTableWidgetItem(str(self.groupRow['numerators'][i]))
            table.setItem(1, i, newItem)
            
        #Заполнить третью строку таблицы - относительные частоты в виде натуральной дроби
        for i in range(len(self.groupRow['numbers'])):
            numerator = self.groupRow['numerators'][i]
            denominator = self.groupRow['denominator']
            naturalFraction = mathTex_to_QPixmap(r"$\frac{" + str(numerator) + "}{" + str(denominator) + "}$", 15)
            newItem = QTableWidgetItem("")
            newItem.setData(Qt.DecorationRole, naturalFraction)
            table.setItem(2, i, newItem)
           
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        print("Группированный ряд частот и относительных частот успешно построен")
            
    @Slot()
    def frequencyHistogram2(self):
        # Данные для гистограммы хранятся в словаре frequencyHistogram
        frequencyHistogram = {
            'start': [],
            'end': [],
            'frequency': []
        }
        
        for i in range(len(self.intervalRow['start'])):
            frequencyHistogram['start'].append(roundValue(self.intervalRow['start'][i]))
            frequencyHistogram['end'].append(roundValue(self.intervalRow['end'][i]))
            intervalLen = self.intervalRow['end'][i]-self.intervalRow['start'][i]
            frequencyHistogram['frequency'].append(roundValue(self.intervalRow['frequency'][i]/intervalLen))
        
        
        graph.drawHistogramGraph(frequencyHistogram, xLabel="x", yLabel="Относительная частота", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)

        
        print("frequencyHistogram: ", frequencyHistogram)  
    
    @Slot()
    def relativeFrequencyHistogram2(self):
        # Данные для гистограммы хранятся в словаре relativeIntervalRow
        relativeIntervalRow = {
            'start': [],
            'end': [],
            'relativeFrequency': []
        }
        
        for i in range(len(self.intervalRow['start'])):
            relativeIntervalRow['start'].append(roundValue(self.intervalRow['start'][i]))
            relativeIntervalRow['end'].append(roundValue(self.intervalRow['end'][i]))
            
            intervalLen = self.intervalRow['end'][i] - self.intervalRow['start'][i]
            frequencySum = sum(self.intervalRow['frequency'])
            relativeFreaquency = self.intervalRow['frequency'][i] / frequencySum
            relativeIntervalRow['relativeFrequency'].append(roundValue(relativeFreaquency / intervalLen))
        
        graph.drawHistogramGraph(relativeIntervalRow, xLabel="x", yLabel="Относительная частота", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)
        
        
        print("relativeFrequencyHistogram2: ", relativeIntervalRow)
    
    @Slot()
    def empiricalIntervalFunction2(self):
        # Делал опираясь на это https://vk.com/im?sel=c68&z=photo246012063_457245640%2Fmail903103
        # Данные для гистограммы хранятся в словаре intervalEmpirical
        intervalEmpirical = {
            'start': [],
            'end': [],
            'y': []
        }
        
        for i in range(1, len(self.intervalRow['start'])):
            intervalEmpirical['start'].append(roundValue(self.intervalRow['start'][i]))
            intervalEmpirical['end'].append(roundValue(self.intervalRow['end'][i]))
            intervalEmpirical['y'].append(roundValue(sum(self.intervalRow['frequency'][:i]) / sum(self.intervalRow['frequency'])))
        
        # Добавить последнюю точку равную 1
        allX = [value for value in intervalEmpirical["start"]] + [value for value in intervalEmpirical["end"]] 
        xMinDiff = graph.minDiffInList(allX)
        lastx = intervalEmpirical['end'][-1] 
        intervalEmpirical['start'].append(roundValue(lastx))
        intervalEmpirical['end'].append(roundValue(lastx+xMinDiff)) 
        intervalEmpirical['y'].append(1)
        

        
        print("intervalEmpirical: ", intervalEmpirical)
        return intervalEmpirical
        
    
    @Slot()
    def empiricalGroupFunction2(self):
        # Данные для эмпирической функции хранятся в словаре groupEmpirical
        x = self.groupRow['numbers']
        np.append(x, 999)
        groupEmpirical = {
            'start': [],
            'end': [],
            'y': []
        }
        for i in range(len(x)-1):
            groupEmpirical['start'].append(roundValue(x[i])) 
            groupEmpirical['end'].append(roundValue(x[i+1]))
            groupEmpirical['y'].append(roundValue(sum(self.groupRow['numerators'][:i+1])/self.groupRow['denominator']))
        
        # Добавить последнюю точку равную 1
        allX = [value for value in groupEmpirical["start"]] + [value for value in groupEmpirical["end"]] 
        xMinDiff = graph.minDiffInList(allX)
        lastx = groupEmpirical['end'][-1] 
        groupEmpirical['start'].append(roundValue(lastx))
        groupEmpirical['end'].append(roundValue(lastx+xMinDiff)) 
        groupEmpirical['y'].append(1)
            
        print("groupEmpirical: ", groupEmpirical)
        return groupEmpirical
            
        

    
    @Slot()
    def frequencyPolygon2(self):
        # Данные для гистограммы хранятся в словаре frequencyPolygon
        
        frequencyPolygon = {
            'x': [],
            'y': []
        }
        
        for i in range(len(self.groupRow['numbers'])):
            frequencyPolygon['x'].append(self.groupRow['numbers'][i])
            frequencyPolygon['y'].append(self.groupRow['numerators'][i])
        
        graph.drawPolygonGraph(frequencyPolygon['x'], frequencyPolygon['y'], xLabel="Число", yLabel="Частота", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)

        
        print("frequencyPolygon2: ", frequencyPolygon)
        
    
    @Slot()
    def relativeFrequencyPolygon2(self):
        # Данные для гистограммы хранятся в словаре relativeFrequencyPolygon
        relativeFrequencyPolygon = {
            'x': [],
            'y': []
        }
        
        for i in range(len(self.groupRow['numbers'])):
            relativeFrequencyPolygon['x'].append(roundValue(self.groupRow['numbers'][i]))
            relativeFrequencyPolygon['y'].append(roundValue(self.groupRow['numerators'][i] / self.groupRow['denominator']))
            
            
        graph.drawPolygonGraph(relativeFrequencyPolygon['x'], relativeFrequencyPolygon['y'], xLabel="Число", yLabel="Относительная частота", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)

            
        print("relativeFrequencyPolygon2: ", relativeFrequencyPolygon)
        
    @Slot()
    def setEmpirical(self, widget, empiricalFunction):
        #Создать строчку Latex из библиотеки matplotLib, в которой будет система эмпирическоф функции по шаблону: F(x) = {[start[i], end[i]]: y[i]}
        latexStr = r"$F(x)= \begin{cases} "
        for i in range(len(empiricalFunction['start'])):
            latexStr += str(empiricalFunction['y'][i])
            latexStr += r" & \text{при } x \in [" + str(empiricalFunction['start'][i]) + r", " + str(empiricalFunction['end'][i]) + r"]"
            if i != len(empiricalFunction['start']) - 1:
                latexStr += r" \\ "
        latexStr += r" \end{cases}$"
        
       
        pixmap = mathTex_to_QPixmap_system(latexStr, 50)             

        #Без этого после сворачивания окна qPixMap поломает пропорции окна, а так просто картинку обрежет
        widget.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        
        #Ставим qPixMap'у размер его label'а
        widget.setPixmap(pixmap.scaled(widget.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        #widget.setPixmap(pixmap) 
        
    @Slot()
    def fillTableWithArray(self,tableWidget : QTableWidget, array, row):
        
        if tableWidget.rowCount() < row + 1:
            tableWidget.setRowCount(row + 1)
        if tableWidget.columnCount() < len(array):
            tableWidget.setColumnCount(len(array))
           
        if type(array[0]) == QPixmap:
            for i in range(len(array)):
                newItem = QTableWidgetItem("")
                newItem.setData(Qt.DecorationRole, array[i])
                tableWidget.setItem(2, i, newItem)
        else:
             for i in range(len(array)):
                tableWidget.setItem(row, i, QTableWidgetItem(str(array[i])))
            
        
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow() 
    window.show()
    sys.exit(app.exec())
    


