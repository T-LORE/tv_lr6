from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np
import math

def roundValue(num, digits=2):
    if num == 0: return 0
    
    absNum = abs(num - int(num))
    if absNum == 0: return num
    
    scale = int(-math.floor(math.log10(absNum))) + digits - 1
    if scale < digits: scale = digits
    return round(num, scale)

def removeBordersAndAddArrows(ax):    
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (1), ls="", marker="^", ms=10, color="k",
            transform=ax.get_xaxis_transform(), clip_on=False)
     
def showGraphWindow(fullscreenStart = True):
    #Окно на весь экран
    if fullscreenStart:
        figManager = plt.get_current_fig_manager() 
        figManager.window.showMaximized()
        
    #Вывести окно с графиком
    plt.show()
    
def setupCoordinateSystem(x, y, xLabel = "", yLabel = ""):
    rc = {"xtick.direction" : "inout", "ytick.direction" : "inout",
            "xtick.major.size" : 5, "ytick.major.size" : 5,}
    #with - это не цикл, а что-то типа try except 
    with plt.rc_context(rc):
        fig, ax = plt.subplots()
        
        #Убрать границы и добавить стрелочки на осях
        removeBordersAndAddArrows(ax)
        
        #Реальные значения x и y
        xUnscaled = x[:]
        yUnscaled = y[:]
        xUnscaled.sort()
        yUnscaled.sort()
        xUnscaled = list(dict.fromkeys(xUnscaled))
        yUnscaled = list(dict.fromkeys(yUnscaled))
                  

        #Находим мин разницу м/у элементами
        allX = x        
        xMinDiff = minDiffInList(allX)
        print(f"Min x diff = { xMinDiff }")
    
        allY = y        
        yMinDiff = minDiffInList(allY)
        print(f"Min y diff = { yMinDiff }")
        
        #Находим смещение для всех X
        xFirst = min(allX)
        xDeltaForScaling = xFirst - 2*xMinDiff        
        
        xUseScaling = xDeltaForScaling > 0.5 * xMinDiff
        if not xUseScaling:
            xDeltaForScaling = 0
        
        #Находим смещение для всех Y
        yFirst = min(allY)
        yDeltaForScaling = yFirst - 4*yMinDiff 
        
        yUseScaling = yDeltaForScaling > 0.5 * yMinDiff
        if not yUseScaling:
            yDeltaForScaling = 0
        
        #Изменённые значения для разрыва
        xScaled = [ i - xDeltaForScaling for i in xUnscaled ]
        yScaled = [ i - yDeltaForScaling for i in yUnscaled ] 
        
        #Добавить разрыв оси X
        if xUseScaling:
            firstScaledX = min(xScaled)
            #Белый фон для разрыва
            ax.plot(firstScaledX / 2, 0, ls="", marker="s", markersize=25, color="white", clip_on=False, zorder=3)
            #Символ разрыва
            plt.text(firstScaledX / 2, 0, "∿", size=20, horizontalalignment='center', verticalalignment='center', zorder=4)
            
        #Добавить разрыв оси Y
        if yUseScaling:
            firstScaledY = min(yScaled)
            #Белый фон для разрыва
            ax.plot(0, firstScaledY / 2, ls="", marker="s", markersize=25, color="white", clip_on=False, zorder=3)
            #Символ разрыва
            plt.text(0, firstScaledY / 2, "∿", rotation=90, size=20, horizontalalignment='center', verticalalignment='center', zorder=4)
        
    print(xDeltaForScaling)
    print(yDeltaForScaling)
        
    #Названия осей
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    
        
    return { "subPlot" : ax, "xScaling" : xDeltaForScaling, "yScaling" : yDeltaForScaling }    

def setTicks(ax, x, xDelta, y, yDelta, tickFontSize=11):
    #Отображаем только известные значения
    xUniq = list(dict.fromkeys(x))
    xUniqScaled = [ i - xDelta for i in xUniq]
    ax.set_xticks(xUniqScaled, [ roundValue(i) for i in xUniq ], fontsize=tickFontSize, minor=False)
    
    yUniq = list(dict.fromkeys(y))
    yUniqSclaed = [ i - yDelta for i in yUniq]
    ax.set_yticks(yUniqSclaed, [ roundValue(i) for i in yUniq ], fontsize=tickFontSize, minor=False)

def drawLinesToPoints(ax, x, y, color, alpha, width, style="-", orientation="both", zorder=3):
    points = [i for i in zip(x, y)]
          
    if orientation == "both" or orientation == "horizontal":
        #Dictionary горизонтальных линий
        horizontalLines = {}
        for point in points:
            horizontalLines[point[1]] = []
        for point in points:
            horizontalLines[point[1]].append(point[0])
            
        #Рисуем горизонтальные линии
        for lineY in horizontalLines:
            horizontalLines[lineY].sort()
            biggestX = horizontalLines[lineY][-1]
            xx = [0, biggestX]
            yy = [lineY] * 2
            ax.plot(xx, yy, linestyle=style, color=color, alpha=alpha, linewidth=width, zorder=zorder)
      
    if orientation == "both" or orientation == "vertical":  
        #Dictionary вертикальных линий
        vertiaclLines = {}
        for point in points:
            vertiaclLines[point[0]] = []
        for point in points:
            vertiaclLines[point[0]].append(point[1])                  
        
        #Рисуем вертикальные линии
        for lineX in vertiaclLines:
            vertiaclLines[lineX].sort()
            biggestY = vertiaclLines[lineX][-1]
            xx = [lineX] * 2
            yy = [0, biggestY]
            ax.plot(xx, yy, linestyle=style, color=color, alpha=alpha, linewidth=width, zorder=zorder)

def drawPolygonGraph(x, y, subPlot, color="black", width=2, dashColor="black", dashAlpha=0.5, dashWidth=0.7):
    #Построение графика в отдельном окне
    #Пунктирные линии к точкам
    ax = subPlot
    
    drawLinesToPoints(ax, x, y, dashColor, dashAlpha, dashWidth, style="--", orientation="both", zorder=5)
    
    #Рисуем сам график
    ax.plot(x, y, color=color, linewidth=width, zorder=6)

def minDiffInList(lst):
    sorted_lst = sorted(set(lst))
    if len(sorted_lst) < 2:
        return sorted_lst[0]
    return min(n2 - n1 for n1, n2 in zip(sorted_lst, sorted_lst[1:]))   
 
def drawEmpiricalGraph(empiricalFunction, subPlot, color="black", width=2, dashColor="black", dashAlpha=0.5, dashWidth=0.7):       
    
    ax = subPlot
    
    #Получаем названия ключей
    startKey, endKey, yKey = empiricalFunction.keys()
    
    allX = []        
    allY = []
    
    #Рисуем основные стрелочки
    for i in range(len(empiricalFunction[yKey])):
        #Точки для отрисовки линии
        xx = [empiricalFunction[startKey][i], empiricalFunction[endKey][i]]
        yy = [empiricalFunction[yKey][i]] * len(xx)
                
        #Записываем изначальные значения для названий на осях
        allX += xx
        allY += yy
                            
        #Рисуем линию
        ax.plot(xx, yy, color=color, linewidth=width, zorder=6)
        
        #Добавляем стрелочку
        ax.plot(xx[0], yy[0], marker="<", color=color, linewidth=width, zorder=6)
        

    #Пунктирные линии к точкам
    #Список обрезан, т.к. последняя стрелка идет из бесконечности
    drawLinesToPoints(ax, allX[:-1], allY[:-1], dashColor, dashAlpha, dashWidth, style="--", orientation="both", zorder=5)
       
def drawHistogramGraph(histogramFunction, subPlot, color="black", width=2, dashColor="black", dashAlpha=0.5, dashWidth=0.7):       
    
    ax = subPlot
    
    #Получаем названия ключей
    startKey, endKey, yKey = histogramFunction.keys()   
    
    allX = []
    allY = []
     
    #Рисуем линии
    for i in range(len(histogramFunction[yKey])):
        #Точки для отрисовки линии
        xx = [histogramFunction[startKey][i], histogramFunction[endKey][i]]
        yy = [histogramFunction[yKey][i]] * len(xx)
             
        #Записываем значения 
        allX += xx
        allY += yy
                        
        #Рисуем линию
        ax.plot(xx, yy, color=color, linewidth=width, zorder=6)
        
        
    #Сплошные линии для стобиков
    drawLinesToPoints(ax, allX, allY, color, 1, width, style="solid", orientation="vertical", zorder=5)

    #Пунктирные линии к точкам
    drawLinesToPoints(ax, allX, allY, dashColor, dashAlpha, dashWidth, style="--", orientation="horizontal", zorder=5)
    
def renderPolygonGraph(x, y, xLabel="", yLabel="", color="black", width=2, dashColor="black", dashAlpha=0.5, dashWidth=0.7, fullscreenStart=True, tickFontSize=11):
    plotInfo = setupCoordinateSystem(x, y, xLabel=xLabel, yLabel=yLabel)
    subPlot = plotInfo["subPlot"]
    xDelta = plotInfo["xScaling"]
    yDelta = plotInfo["yScaling"]
    
    xScaled = [ i - xDelta for i in x ]
    yScaled = [ i - yDelta for i in y ]
    
    drawPolygonGraph(xScaled, yScaled, subPlot, color=color, width=width, dashColor=dashColor, dashAlpha=dashAlpha, dashWidth=dashWidth)
    
    setTicks(subPlot, x, xDelta, y, yDelta, tickFontSize=tickFontSize)
    
    showGraphWindow(fullscreenStart)
    
def renderEmpiricalGraph(empiricalFunction, xLabel="", yLabel="", color="black", width=2, dashColor="black", dashAlpha=0.5, dashWidth=0.7, fullscreenStart=True, tickFontSize=11):
    #Получаем названия ключей
    startKey, endKey, yKey = empiricalFunction.keys()  
    
    allX = empiricalFunction[startKey] + empiricalFunction[endKey]
    allY = empiricalFunction[yKey]
    
    plotInfo = setupCoordinateSystem(allX, allY, xLabel=xLabel, yLabel=yLabel)
    subPlot = plotInfo["subPlot"]
    xDelta = plotInfo["xScaling"]
    yDelta = plotInfo["yScaling"]
    
    #Масштабируем
    empiricalFunction[startKey] = [ i - xDelta for i in empiricalFunction[startKey]]
    empiricalFunction[endKey] = [ i - xDelta for i in empiricalFunction[endKey]]
    empiricalFunction[yKey] = [ i - yDelta for i in empiricalFunction[yKey]]
    
    #Рисуем
    drawEmpiricalGraph(empiricalFunction, subPlot, color=color, width=width, dashColor=dashColor, dashAlpha=dashAlpha, dashWidth=dashWidth)
    
    setTicks(subPlot, allX, xDelta, allY, yDelta, tickFontSize=tickFontSize)
    
    showGraphWindow(fullscreenStart)
    
def renderComplexHistogram(histogramFunction, densityFunc, xLabel="", yLabel="", color="black", width=2, dashColor="black", dashAlpha=0.5, dashWidth=0.7, fullscreenStart=True, tickFontSize=11):
    #Получаем названия ключей
    startKey, endKey, yKey = histogramFunction.keys()
    
    #Средняя линия
    meanX = [sum(pair) / 2 for pair in zip(histogramFunction[startKey], histogramFunction[endKey])]
    meanY = histogramFunction[yKey][:]   
    
    #X и Y для определения масштаба
    allX = histogramFunction[startKey] + histogramFunction[endKey] + meanX
    allY = histogramFunction[yKey] + meanY
    
    #Получаем масштаб и систему координат
    plotInfo = setupCoordinateSystem(allX, allY, xLabel=xLabel, yLabel=yLabel)
    subPlot = plotInfo["subPlot"]
    xDelta = plotInfo["xScaling"]
    yDelta = plotInfo["yScaling"]
        
    #Масштабируем
    histogramFunction[startKey] = [ i - xDelta for i in histogramFunction[startKey]]
    histogramFunction[endKey] = [ i - xDelta for i in histogramFunction[endKey]]
    histogramFunction[yKey] = [ i - yDelta for i in histogramFunction[yKey]]
    
    #Рисуем
    drawHistogramGraph(histogramFunction, subPlot=subPlot, color=color, width=width, dashColor=dashColor, dashAlpha=dashAlpha, dashWidth=dashWidth)
    
    #Масштабируем
    meanX = [ i - xDelta for i in meanX ]
    meanY = [ i - yDelta for i in meanY ]
    
    #Рисуем
    subPlot.plot(meanX, meanY, color="red", linewidth=width, zorder=6)
    #Пунктирные линии к точкам
    drawLinesToPoints(subPlot, meanX, meanY, dashColor, dashAlpha, dashWidth, style="--", orientation="both", zorder=5)
    
    #Получаем точки для распределения
    densityX = np.linspace(min(allX), max(allX), int(max(allX) / (minDiffInList(allX) / 20)))
    densityY = [ densityFunc(i) for i in densityX ]
    
    #Масштабируем
    densityX = [ i - xDelta for i in densityX ]
    densityY = [ i - yDelta for i in densityY ]
    
    #Рисуем
    subPlot.plot(densityX, densityY, color="blue", linewidth=width, zorder=6)
    
    #Отмечаем точки
    setTicks(subPlot, allX, xDelta, allY, yDelta, tickFontSize=tickFontSize)
    
    showGraphWindow(fullscreenStart)

def renderComplexPolygon(x, y, densityFunc, xLabel="", yLabel="", color="black", width=2, dashColor="black", dashAlpha=0.5, dashWidth=0.7, fullscreenStart=True, tickFontSize=11):
    #Получаем масштаб и систему координат
    plotInfo = setupCoordinateSystem(x, y, xLabel=xLabel, yLabel=yLabel)
    subPlot = plotInfo["subPlot"]
    xDelta = plotInfo["xScaling"]
    yDelta = plotInfo["yScaling"]
    
    #Строим сам полигон с учетом масштаба
    xScaled = [ i - xDelta for i in x ]
    yScaled = [ i - yDelta for i in y ]
    drawPolygonGraph(xScaled, yScaled, subPlot, color=color, width=width, dashColor=dashColor, dashAlpha=dashAlpha, dashWidth=dashWidth)
    
    #Получаем точки для распределения
    densityX = np.linspace(min(x), max(x), int(max(x) / (minDiffInList(x) / 20)))
    densityY = [ densityFunc(i) for i in densityX ]
    
    #Масштабируем
    densityX = [ i - xDelta for i in densityX ]
    densityY = [ i - yDelta for i in densityY ]
    
    #Рисуем
    subPlot.plot(densityX, densityY, color="blue", linewidth=width, zorder=6)
    
    setTicks(subPlot, x, xDelta, y, yDelta, tickFontSize=tickFontSize)
    
    showGraphWindow(fullscreenStart)