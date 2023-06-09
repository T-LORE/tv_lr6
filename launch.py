import math
import sys
import re
from mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QListWidgetItem, QFileDialog, QTableWidgetItem, QTableWidget, QHeaderView, QSizePolicy
from PySide6.QtCore import Slot, Signal, Qt
from PySide6.QtGui import QIcon, QPixmap
from qpixmapCreator import mathTex_to_QPixmap, mathTex_to_QPixmap_system
from workingWithRowData import *
import numpy as np
import pyqtgraph as pg

from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats    

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
        """
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
        """
        
        lambdaPixmap = mathTex_to_QPixmap(r"$\lambda^{*} = \frac{1}{n} \sum_{i = 0}^{n}x_{i}=$", 16)
        self.ui.formulaLambda.setPixmap(lambdaPixmap)
        
        xObservedPixmap = mathTex_to_QPixmap(r"$\chi^{2}_{набл} = \frac{1}{n} \sum_{i = 0}^{n} \frac{(m_{i}-np_{i})^{2}}{np_{i}}=$", 16)
        self.ui.formulaXObserved.setPixmap(xObservedPixmap)
        
        xCriticalPixmap = mathTex_to_QPixmap(r"$\chi^{2}_{кр} = (k, \alpha)=$", 16)
        self.ui.formulaXCritical.setPixmap(xCriticalPixmap)
        
        pPixmap = mathTex_to_QPixmap(r"$P_{i} = P(X=x_{i}) = \frac{\lambda^{x_{i}} \cdot e^{-\lambda}}{x_{i}!}$", 16)
        self.ui.pFormula.setPixmap(pPixmap)
        
        kPixmap = mathTex_to_QPixmap(r"$k = s - 2 =$", 16)
        self.ui.formulaK.setPixmap(kPixmap)
        
        # Прописанные коннекты
        # Задание 1
        self.ui.firstTaskBtn.clicked.connect(lambda x: (self.setCurrentMode(0)))
        self.ui.openFileBtn_1.clicked.connect(self.openFileBtnClicked_1)
        self.ui.distributionDensityBtn.clicked.connect(self.relativeFrequencyHistogram2)
        """
        self.ui.frequencyHistogramBtn_2.clicked.connect(self.frequencyHistogram2)
        
        """
        
        #Задание 2
        self.ui.openFileBtn_2.clicked.connect(self.openFileBtnClicked_2)
        self.ui.secondTaskBtn.clicked.connect(lambda x: (self.setCurrentMode(1)))
        self.ui.relativeFrequenciesPolygonBtn.clicked.connect(self.generateRelativeFrequencyPolygon)
        
        # self.ui.openFileBtn_3.clicked.connect(self.openFileBtnClicked_3)
        # self.ui.frequencyHistogramBtn_3.clicked.connect(self.frequencyHistogram2)
        # self.ui.relativeFrequencyHistogramBtn_3.clicked.connect(self.relativeFrequencyHistogram2)
        # self.ui.empiricalIntervalFunctionBtn_3.clicked.connect(lambda x: (graph.renderEmpiricalGraph(self.empiricalIntervalFunction, xLabel="x", yLabel="F*(x)", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)))
        # self.ui.empiricalGroupFunctionBtn_3.clicked.connect(lambda x: (graph.renderEmpiricalGraph(self.empiricalGroupFunction, xLabel="x", yLabel="F*(x)", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)))
        # self.ui.frequencyPolygonBtn_3.clicked.connect(self.frequencyPolygon2)
        # self.ui.relativeFrequencyPolygonBtn_3.clicked.connect(self.relativeFrequencyPolygon2)
        
        #Открытие на полный экран
        self.showMaximized()
        
        self.prepareForFirstTask()
        self.setCurrentMode(0)
         
    @Slot()
    def setCurrentMode(self, newMode: str):
        self.mode = newMode
        if self.mode == 0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        elif self.mode == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        # elif self.mode == 2:
            # self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
            
        print(f"Changed mode to { newMode }")
      
    @Slot()    
    def openFileBtnClicked_2(self):
        #Выбор файла с помощью диалогового окна QfileDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Текстовый файл (*.txt)")
        if fileName:
           #Открытие файла
            file = open(fileName, 'r')
            
            #Чтение интервалов и их n из файла
            self.puasonRow = np.genfromtxt(fileName, delimiter=',', names=True)
           
            #Записать содержимое файла
            self.ui.fileBuffer_2.setText(file.read())
           
            #Закрытие файла
            file.close()
                        
            #Вывод сообщения в консоль
            print("Файл успешно открыт")
            
            latexStrs = { "xi" : r"$x_{i}$",  
                         "ni" : r"$n_{i}$", 
                         "mi" : r"$m_{i}$", 
                         "pi" : r"$p_{i}$",
                         "n*pi" : r"$n \cdot p_{i}$", 
                         "(ni - npi)**2" : r"$(n_{i} - np_{i})^{2}$", 
                         "(ni - npi)**2 / npi" : r"$\frac{(n_{i} - np_{i})^{2}}{np_{i}}$"}
            
            #Заполнить таблицу групп. ряда
            #Очистить перед заполнением
            self.clearTable(self.ui.rowsTable_2_1)
            #Заполнить
            pix1 = mathTex_to_QPixmap(latexStrs["xi"], 16)
            self.fillTableWithArray(self.ui.rowsTable_2_1, [pix1] + [ i for i in self.puasonRow["x"] ], 0)
            pix2 = mathTex_to_QPixmap(latexStrs["ni"], 16)
            self.fillTableWithArray(self.ui.rowsTable_2_1, [pix2] + [ i for i in self.puasonRow["m"] ], 1)
           
            #Вычислить и записать лямбду
            self.lambd = getLamda(self.puasonRow)
            self.ui.lineLambda.setText(str(roundValue(self.lambd)))
            
            #Добавить в формулу конкретное значение лямбды 
            pPixmap = mathTex_to_QPixmap(r"$P_{i} = P(X=x_{i}) = \frac{\lambda^{x_{i}} \cdot e^{-\lambda}}{x_{i}!} =" + r"\frac{" + str(roundValue(self.lambd)) + r"^{x_{i}} \cdot e^{-" + str(roundValue(self.lambd)) + r"}}{x_{i}!}$", 16)
            self.ui.pFormula.setPixmap(pPixmap)
            
            #Вычислить значения для известного групп. ряда
            n = sum(self.puasonRow["m"])
            pi = [getTheoreticalProbability(self.lambd, i ) for i in self.puasonRow["x"]]
            npi = [n * i for i in pi]
            complex1 = [ (pair[0] - n * pair[1])**2 for pair in zip(self.puasonRow["m"], pi) ]
            complex2 = [ pair[0] / (n * pair[1]) for pair in zip(complex1, pi)]
            
            tableData = { "xi" : self.puasonRow["x"], "mi" : self.puasonRow["m"],  "pi" : pi, "n*pi" : npi, "(ni - npi)**2" : complex1, "(ni - npi)**2 / npi" : complex2}
            
            #Заполнить таблицу с вычисленными данными
            #Очистить перед заполнением
            self.clearTable(self.ui.rowsTable_2_2)
            #Заполнить            
            rowToFill = int(0)
            for key, array in tableData.items():
                headerPixmap = mathTex_to_QPixmap(latexStrs[key], 16)
                self.fillTableWithArray(self.ui.rowsTable_2_2, [headerPixmap] + [ graph.roundValue(i) for i in array], rowToFill, stretchVertical=False)
                rowToFill += 1
            
            #Вычислить и записать лямбду
            self.k = len(self.puasonRow["m"]) - 2
            self.ui.lineK.setText(str(self.k))
        
            #Вычислить и записать X ожидаемое
            xObserved = sum(gethi2ObservedArray(self.puasonRow["m"], pi))
            self.ui.lineXObserved.setText(str(roundValue(xObserved)))
            
            #Записать X критическое
            xCritical = libGethi2CriticalArray(self.k, float(self.ui.lineAlpha.text()))
            self.ui.lineXCritical.setText(str(roundValue(xCritical)))
            
            #Записать результат сравнения
            if xCritical > xObserved:
                comparasionPixmap = mathTex_to_QPixmap(r"$\chi_{кр}^{2} > \chi_{набл}^{2} \Rightarrow $", 16)
                outputStr = "Гипотеза согласуется с экспериментальными данными"
            else:
                comparasionPixmap = mathTex_to_QPixmap(r"$\chi_{кр}^{2} < \chi_{набл}^{2} \Rightarrow $", 16)
                outputStr = "Гипотеза не согласуется с экспериментальными данными"
            self.ui.formulaXComparasion.setPixmap(comparasionPixmap)
            self.ui.lineCompare_2.setText(outputStr)
            
                    
    @Slot()    
    def openFileBtnClicked_1(self):
        #Выбор файла с помощью диалогового окна QfileDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Текстовый файл (*.txt)")
        if fileName:
            self.clearTable(self.ui.rowsTable_1_1)
            # self.ui.tableResults_5.clear()
            # self.prepareForFirstTask()
            #Открытие файла
            #Выбор ряда (дискретный или интервальынй)
            if (self.ui.listRowType_5.currentRow() == 0):
                #Дискретный                
                file = open(fileName, 'r')
                #Чтение массива целых чисел из файла
                array = np.loadtxt(file)
                #Закрытие файлаn
                file.close()
                
                #Вывод массива чисел в виджет через запятую
                self.ui.fileBuffer_3.setText(np.array2string(array, formatter={'float_kind':lambda x: "%.1f" % x}).replace('[','').replace(']', '').replace('\n', ''))                      
                #Получить кол-во интервалов от пользователя
                try:
                    self.intervalCount = int(self.ui.lineIntervalCount.text())
                except ValueError:
                    print("Неверно введено кол-во интервалов")
                    return
                
                self.intervalRow = split(array, self.intervalCount)
                print("intervalRow: ", self.intervalRow)
                
            elif (self.ui.listRowType_5.currentRow() == 1):
                #Интервальный
                file = open(fileName, 'r')
                self.intervalRow = np.genfromtxt(fileName, delimiter=',', names=True)
                #вывести содержимое файла 
                self.ui.fileBuffer_3.setText(file.read())
                #Округлить интервалы
                self.intervalRow["start"] = [roundValue(i) for i in self.intervalRow["start"]]
                self.intervalRow["end"] = [roundValue(i) for i in self.intervalRow["end"]]
                self.groupRow = {
                'numbers': [],
                'numerators': [],
                'denominator': sum(self.intervalRow['frequency'])
                }
            
                for i in range(len(self.intervalRow['start'])):
                    self.groupRow['numbers'].append((self.intervalRow['start'][i] + self.intervalRow['end'][i]) / 2)
                    self.groupRow['numerators'].append(self.intervalRow['frequency'][i])
                    
                #Создать массив группированного ряда  
                array = np.repeat(self.groupRow['numbers'], self.groupRow['numerators'])
             
            #Массив заполнения таблицы:
            tableContent = []
                   
            #X выборочное
            x = roundValue(getX(array))
            tableContent.append(x)
            
            # D выборочное
            d = roundValue(getD(array))
            tableContent.append(d)
            
            # Сигма выборочная
            sigma = roundValue(getSigma(array))
            tableContent.append(sigma)
            
            # aStar
            aStar = roundValue(getX(array))
            tableContent.append(aStar)
            
            # sigmaStar
            sigmaStar = roundValue(getSigma(array))
            tableContent.append(sigmaStar)
            
            # теоретические вероятности
            pi = getPi(aStar, sigmaStar, self.intervalRow)
            
            
            #Уровень значимости
            a = float(self.ui.lineAlpha_5.text())
            #Число степеней свободы
            k  = len(self.intervalRow['start'])-3
            tableContent.append(k)
            
            #Хи квадрат наблюдаемое
            hi2Observed = roundValue(sum(gethi2ObservedArray(self.intervalRow['frequency'], pi)))
            tableContent.append(hi2Observed)
            
            #Хи квадрат критическое
            hi2Critical = roundValue(libGethi2CriticalArray(k, a))
            tableContent.append(hi2Critical)

            #Вывод результатов в таблицу
            self.fillTableWithArray(self.ui.tableResults_5, tableContent, 2, ignoreVertical = True)
            
            #Записать результат сравнения
            if hi2Critical > hi2Observed:
                comparasionPixmap = mathTex_to_QPixmap(r"$\chi_{кр}^{2} > \chi_{набл}^{2} \Rightarrow $", 16)
                outputStr = "Гипотеза согласуется с экспериментальными данными"
            else:
                comparasionPixmap = mathTex_to_QPixmap(r"$\chi_{кр}^{2} < \chi_{набл}^{2} \Rightarrow $", 16)
                outputStr = "Гипотеза не согласуется с экспериментальными данными"
                
            intervalsStr = [f"[{intr[0]},{intr[1]}]" for intr in zip(self.intervalRow["start"], self.intervalRow["end"])]
            ni = self.intervalRow["frequency"][:]
            #naturalFraction = mathTex_to_QPixmap(r"$\frac{" + str(numerator) + "}{" + str(denominator) + "}$", 15)
            sumFreq = sum(self.intervalRow["frequency"])
            wi = [mathTex_to_QPixmap(r"$\frac{" + str(i) + "}{" + str(sumFreq) + "}$", 15) for i in self.intervalRow["frequency"]]
            
            tableData = {
                "[x(i), x(i+1)]": intervalsStr,
                "n(i)": ni,
                "w(i)": wi,
                "p(i)": pi
            }
            
            latexHeaderData = {
                "[x(i), x(i+1)]": r"$[x_{i}, x_{i+1}]$",
                "n(i)": r"$n_{i}$",
                "w(i)": r"$w_{i}$",
                "p(i)": r"$p_{i}$"
            }
            rowIndex = int(0)
            for key, value in tableData.items():
                headerPixmap = mathTex_to_QPixmap(latexHeaderData[key], 20) 
                toFIll = [headerPixmap] + [i for i in value]
                self.fillTableWithArray(self.ui.rowsTable_1_1, toFIll, rowIndex, stretchVertical = False)
                rowIndex += 1
            #Вывести результат сравнения
            self.ui.formulaXComparasion_1.setPixmap(comparasionPixmap)
            self.ui.lineCompare_1.setText(outputStr)
            
            # Плотность нормального закона распределения через лямбда функцию испльзуя библиотеку scipy
            self.densityFuncPtr = lambda x: stats.norm.pdf(x, aStar, sigmaStar)
                
            # Вывести формулу плотности нормального закона распределения в latex формате с подставленными значениями aStar и sigmaStar
            self.setLatexForNormalDensity(self.ui.densityFunction, aStar, sigmaStar) 
    @Slot()
    def prepareForFirstTask(self):
        #Массив заполнения таблицы:
        tableHeaders = []
        tableFormulas = []
        
        formulaFontSize = 22
        headersFontSize = 20

        #X выборочное
        x = mathTex_to_QPixmap(r"$x_{в}$", headersFontSize)
        formulaX = mathTex_to_QPixmap(r"$\frac{1}{n} \sum_{i=1}^{n} x_{i} * m_{i}$", formulaFontSize)
        tableHeaders.append(x)
        tableFormulas.append(formulaX)

        # D выборочное     
        d = mathTex_to_QPixmap(r"$D_{в}$", headersFontSize)
        formulaD = mathTex_to_QPixmap(r"$X^{2} - (\overline{X_{в}})^{2}$", formulaFontSize)
        tableHeaders.append(d)
        tableFormulas.append(formulaD)
        
        #Сигма выборочное
        sigma = mathTex_to_QPixmap(r"$\sigma_{в}$", headersFontSize)
        formulaSigma = mathTex_to_QPixmap(r"$\sqrt{D_{в}}$", formulaFontSize)
        tableHeaders.append(sigma)
        tableFormulas.append(formulaSigma)
        
        #A* 
        aStar = mathTex_to_QPixmap(r"$a^{*}$", headersFontSize)
        formulaAStar = mathTex_to_QPixmap(r"$\frac{1}{n} \sum_{i=1}^{n} x_{i} * m_{i}$", formulaFontSize)
        tableHeaders.append(aStar)
        tableFormulas.append(formulaAStar)
        
        #сигма*
        sigmaStar = mathTex_to_QPixmap(r"$\sigma^{*}$", headersFontSize)
        formulaSigmaStar = mathTex_to_QPixmap(r"$\sqrt{D_{в}}$", formulaFontSize)
        tableHeaders.append(sigmaStar)
        tableFormulas.append(formulaSigmaStar)
        
        #Степени свободы k
        k = mathTex_to_QPixmap(r"$k$", headersFontSize)
        formulaK = mathTex_to_QPixmap(r"$m - r - 1$", formulaFontSize)
        tableHeaders.append(k)
        tableFormulas.append(formulaK)
        
        #Хи квадрат наблюдаемое
        hi2Observed = mathTex_to_QPixmap(r"$\chi^{2}_{набл}$", headersFontSize)
        formulaHi2Observed = mathTex_to_QPixmap(r"$\sum_{i=1}^{m} \frac{(m_{i} - np_{i})^{2}}{np_{i}}$", formulaFontSize-1)
        tableHeaders.append(hi2Observed)
        tableFormulas.append(formulaHi2Observed)
        
        #Хи квадрат критическое
        hi2Critical = mathTex_to_QPixmap(r"$\chi^{2}_{кр}$", headersFontSize)
        formulaHi2Critical = mathTex_to_QPixmap(r"$Табличное$", formulaFontSize)
        tableHeaders.append(hi2Critical)
        tableFormulas.append(formulaHi2Critical)
        
        #Вывод в таблицу
        self.fillTableWithArray(self.ui.tableResults_5, tableHeaders, 0, ignoreVertical = True)
        self.fillTableWithArray(self.ui.tableResults_5, tableFormulas, 1, ignoreVertical = True)
        
        
        #Ресайз таблицы
        self.ui.tableResults_5.verticalHeader().setSectionResizeMode(self.ui.tableResults_5.rowCount()-1, QHeaderView.ResizeToContents)
        self.ui.tableResults_5.verticalHeader().setSectionResizeMode(self.ui.tableResults_5.rowCount(), QHeaderView.Stretch)
        


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
        graph.renderPolygonGraph(x, y, xLabel="Число", yLabel="Частота", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)

                          
        #Вывод сообщения в консоль
        print("График частотного полигональной линии успешно построен")        
        
    @Slot()
    def generateRelativeFrequencyPolygon(self):
        #Получение данных из таблицы
        relativeFrequencyRow = getFrequencyRow(self.currentArray, RowType.RELATIVE_FREQUENCY)
        
        #Рассчёт данных для графика
        x = self.puasonRow["x"]
        y = self.puasonRow["m"] / sum(self.puasonRow["m"])
        
        #Округление
        x = [roundValue(i) for i in x]
        y = [roundValue(i) for i in y]
        
        #Построение графика
        graph.renderComplexPolygon(x, y, lambda xi: getTheoreticalProbability(self.lambd, xi), xLabel="Число", yLabel="Относительная частота", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)
        # graph.renderPolygonGraph(x, y, xLabel="Число", yLabel="Относительная частота", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)
        
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
        
        
        graph.renderComplexHistogram(frequencyHistogram, densityFunc=self.densityFuncPtr, xLabel="x", yLabel="Относительная частота", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)

        
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
        
        graph.renderComplexHistogram(relativeIntervalRow, densityFunc=self.densityFuncPtr, xLabel="x", yLabel="Относительная частота", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)
        
        
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
        
        graph.renderPolygonGraph(frequencyPolygon['x'], frequencyPolygon['y'], xLabel="Число", yLabel="Частота", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)

        
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
            
            
        graph.renderPolygonGraph(relativeFrequencyPolygon['x'], relativeFrequencyPolygon['y'], xLabel="Число", yLabel="Относительная частота", color="black", width=1.5, dashColor="black", dashAlpha=0.5, dashWidth=0.7)

            
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
        
    def clearTable(self,tableWidget : QTableWidget):
        tableWidget.clear()
        tableWidget.setRowCount(0)
        tableWidget.setColumnCount(0)
        
    @Slot()
    def fillTableWithArray(self,tableWidget : QTableWidget, array, row, stretchVertical = True, stretchHorizontal = True, ignoreVertical = False):
        
        if tableWidget.rowCount() < row + 1:
            tableWidget.setRowCount(row + 1)
        if tableWidget.columnCount() < len(array):
            tableWidget.setColumnCount(len(array))
          
        overrideHeight = {}  
        
        for i, elem in enumerate(array):
            if type(elem) == QPixmap:
                newItem = QTableWidgetItem("")
                newItem.setData(Qt.DecorationRole, elem)
                tableWidget.setItem(row, i, newItem)
                overrideHeight[i] = elem.height()
            else:
                tableWidget.setItem(row, i, QTableWidgetItem(str(elem)))
                
        if stretchHorizontal:
            horizontalMode = QHeaderView.ResizeMode.Stretch
        else:
            horizontalMode = QHeaderView.ResizeMode.ResizeToContents
                
        tableWidget.horizontalHeader().setSectionResizeMode(horizontalMode)
        
        if stretchVertical:
            verticalMode = QHeaderView.ResizeMode.Stretch
        else:
            verticalMode = QHeaderView.ResizeMode.ResizeToContents
        
        if not ignoreVertical:
            tableWidget.verticalHeader().setSectionResizeMode(verticalMode)
        
        

        
    @Slot()
    def setLatexForNormalDensity(self, widget, aStar, sigmaStar):
        
        #Ощая формула
        normalFormula = r"$f(x)= \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-a)^2}{2\sigma^2}} = "
        
        
        firstFraction = r"\frac{1}{" + str(sigmaStar) + r"\sqrt{2\pi}}"
        
        exponentDegree = r"{-\frac{(x-" + str(aStar) + r")^2}{2 * " + str(sigmaStar) + r"^2}}"
        
        exponent = r"e^{" + exponentDegree + r"}"
        
        densityFormula = r"$f(x)= " + firstFraction + exponent + r"$"
        
        normalFormula += firstFraction
        normalFormula += exponent
        normalFormula+=r"$"
        
        
        pixmap = mathTex_to_QPixmap_system(normalFormula, 50)
        widget.setPixmap(pixmap.scaled(widget.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        
        
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow() 
    window.show()
    sys.exit(app.exec())
    


