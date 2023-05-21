from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np

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


def drawPolygonGraph(x, y, xLabel="", yLabel="", color="black", width=2, dashColor="black", dashAlpha=0.5, dashWidth=0.7, fullscreenStart=True, tickFontSize=11):
    #Построение графика в отдельном окне
        rc = {"xtick.direction" : "inout", "ytick.direction" : "inout",
            "xtick.major.size" : 5, "ytick.major.size" : 5,}
        #with - это не цикл, а что-то типа try except 
        with plt.rc_context(rc):
            fig, ax = plt.subplots()

            #Реальные значения x и y
            xUnscaled = [i for i in x]
            yUnscaled = [i for i in y]
            #Изменённые значения для разрыва
            xScaled = []
            yScaled = []           

            #Находим мин разницу м/у элементами
            allX = x        
            xMinDiff = minDiffInList(allX)
            print(f"Min x diff = { xMinDiff }")
        
            allY = y        
            yMinDiff = minDiffInList(allY)
            print(f"Min y diff = { yMinDiff }")
        
            #Находим смещение для всех X
            xFirst = min(allX)
            xDeltaForScaling = xFirst - xMinDiff        
            
            xUseScaling = xDeltaForScaling > 0.5 * xMinDiff
            
            #Находим смещение для всех Y
            yFirst = min(allY)
            yDeltaForScaling = yFirst - 2*yMinDiff 
            
            yUseScaling = yDeltaForScaling > 0.5 * yMinDiff

            xScaled = xUnscaled[:]
            if xUseScaling:
                xScaled = [i - xDeltaForScaling for i in xScaled]
                
            yScaled = yUnscaled[:]
            if yUseScaling:
                yScaled = [i - yDeltaForScaling for i in yScaled]

            #Пунктирные линии к точкам
            drawLinesToPoints(ax, xScaled, yScaled, dashColor, dashAlpha, dashWidth, style="--", orientation="both", zorder=5)
            
            #Рисуем сам график
            ax.plot(xScaled, yScaled, color=color, linewidth=width, zorder=6)

            #Убрать границы и добавить стрелочки на осях
            removeBordersAndAddArrows(ax)
        
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
        
        #Названия осей
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        
        #Отображаем только известные значения
        xScaledUniqTicks = list(dict.fromkeys([0] + xScaled))
        xUnscaledUniqTicks = list(dict.fromkeys([0] + xUnscaled))
        ax.set_xticks(xScaledUniqTicks, xUnscaledUniqTicks, fontsize=tickFontSize, minor=False)
        
        yScaledUniqTicks = list(dict.fromkeys([0] + yScaled))
        yUnscaledUniqTicks = list(dict.fromkeys([0] + yUnscaled))
        ax.set_yticks(yScaledUniqTicks, yUnscaledUniqTicks, fontsize=tickFontSize, minor=False)
          
        #Окно на весь экран
        if fullscreenStart:
            figManager = plt.get_current_fig_manager() 
            figManager.window.showMaximized()
          
        #Вывести окно с графиком
        plt.show()
    
def minDiffInList(lst):
    sorted_lst = sorted(set(lst))
    return min(n2 - n1 for n1, n2 in zip(sorted_lst, sorted_lst[1:]))
        
def drawEmpiricalGraph(empiricalFunction, xLabel="", yLabel="", color="black", width=2, dashColor="black", dashAlpha=0.5, dashWidth=0.7, fullscreenStart=True, tickFontSize=11):       
    rc = {"xtick.direction" : "inout", "ytick.direction" : "inout",
            "xtick.major.size" : 5, "ytick.major.size" : 5,}
    #with - это не цикл, а что-то типа try except 
    with plt.rc_context(rc):
        fig, ax = plt.subplots()
        
        #Получаем названия ключей
        startKey, endKey, yKey = empiricalFunction.keys()
        
        #Реальные значения x и y
        xUnscaled = []
        yUnscaled = []
        #Изменённые значения для разрыва
        xScaled = []
        yScaled = []
        
        #Находим мин разницу м/у элементами
        allX = [value for value in empiricalFunction[startKey]] + [value for value in empiricalFunction[endKey]]        
        xMinDiff = minDiffInList(allX)
        print(f"Min diff = { xMinDiff }")
    
        #Находим смещение для всех X
        xFirst = min(allX)
        xDeltaForScaling = xFirst - xMinDiff        
        
        useScaling = xDeltaForScaling > 0.5 * xMinDiff
        
        #Рисуем основные стрелочки
        for i in range(len(empiricalFunction[yKey])):
            #Точки для отрисовки линии
            xx = [empiricalFunction[startKey][i], empiricalFunction[endKey][i]]
            yy = [empiricalFunction[yKey][i]] * len(xx)
                  
            #Записываем изначальные значения для названий на осях
            xUnscaled += xx
            yUnscaled += yy
                      
            #Смещаем значения
            if useScaling:
                xx = [i - xDeltaForScaling for i in xx]
            
            #Записываем изменённые значения на которых будут находится названия
            xScaled += xx
            yScaled += yy
            
            #Рисуем линию
            ax.plot(xx, yy, color=color, linewidth=width, zorder=6)
            
            #Добавляем стрелочку
            ax.plot(xx[0], yy[0], marker="<", color=color, linewidth=width, zorder=6)
            

        #Пунктирные линии к точкам
        #Список обрезан, т.к. последняя стрелка идет из бесконечности
        drawLinesToPoints(ax, xScaled[:-1], yScaled[:-1], dashColor, dashAlpha, dashWidth, style="--", orientation="both", zorder=5)

        #Убрать границы и добавить стрелочки на осях
        removeBordersAndAddArrows(ax)
        
        #Добавить разрыв оси 
        if useScaling:
            firstScaledX = min(xScaled)
            #Белый фон для разрыва
            ax.plot(firstScaledX / 2, 0, ls="", marker="s", markersize=25, color="white", clip_on=False, zorder=3)
            #Символ разрыва
            plt.text(firstScaledX / 2, 0, "∿", size=20, horizontalalignment='center', verticalalignment='center', zorder=4)
    
    #Названия осей
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    
    #Отображаем только известные значения
    #Список обрезан, т.к. последняя стрелка идет из бесконечности
    xScaledUniqTicks = list(dict.fromkeys([0] + xScaled[:-1]))
    xUnscaledUniqTicks = list(dict.fromkeys([0] + xUnscaled[:-1]))
    ax.set_xticks(xScaledUniqTicks, xUnscaledUniqTicks, fontsize=tickFontSize, minor=False)
    
    yScaledUniqTicks = list(dict.fromkeys([0] + yScaled))
    yUnscaledUniqTicks = list(dict.fromkeys([0] + yUnscaled))
    ax.set_yticks(yScaledUniqTicks, yUnscaledUniqTicks, fontsize=tickFontSize, minor=False)
    
    #Не продлевать ось X дальше графика
    ax.margins(x=0.0)
    
    #Окно на весь экран
    if fullscreenStart:
        figManager = plt.get_current_fig_manager() 
        figManager.window.showMaximized()
    
    plt.show()
    
def drawHistogramGraph(histogramFunction, xLabel="", yLabel="", color="black", width=2, dashColor="black", dashAlpha=0.5, dashWidth=0.7, fullscreenStart=True, tickFontSize=11):       
    rc = {"xtick.direction" : "inout", "ytick.direction" : "inout",
            "xtick.major.size" : 5, "ytick.major.size" : 5,}
    #with - это не цикл, а что-то типа try except 
    with plt.rc_context(rc):
        fig, ax = plt.subplots()
        
        #Получаем названия ключей
        startKey, endKey, yKey = histogramFunction.keys()
        
        #Реальные значения x и y
        xUnscaled = []
        yUnscaled = []
        #Изменённые значения для разрыва
        xScaled = []
        yScaled = []
        
        #Находим мин разницу м/у элементами
        allX = [value for value in histogramFunction[startKey]] + [value for value in histogramFunction[endKey]]        
        xMinDiff = minDiffInList(allX)
        print(f"Min x diff = { xMinDiff }")
    
        allY = [value for value in histogramFunction[yKey]]        
        yMinDiff = minDiffInList(allY)
        print(f"Min y diff = { yMinDiff }")
    
        #Находим смещение для всех X
        xFirst = min(allX)
        xDeltaForScaling = xFirst - xMinDiff        
        
        xUseScaling = xDeltaForScaling > 0.5 * xMinDiff
        
        #Находим смещение для всех Y
        yFirst = min(allY)
        yDeltaForScaling = yFirst - 2*yMinDiff 
        
        yUseScaling = yDeltaForScaling > 0.5 * yMinDiff 
        
        #Рисуем линии
        for i in range(len(histogramFunction[yKey])):
            #Точки для отрисовки линии
            xx = [histogramFunction[startKey][i], histogramFunction[endKey][i]]
            yy = [histogramFunction[yKey][i]] * len(xx)
                  
            #Записываем изначальные значения для названий на осях
            xUnscaled += xx
            yUnscaled += yy
                      
            #Смещаем значения
            if xUseScaling:
                xx = [i - xDeltaForScaling for i in xx]
            if yUseScaling:
                yy = [i - yDeltaForScaling for i in yy]
            
            #Записываем изменённые значения на которых будут находится названия
            xScaled += xx
            yScaled += yy
            
            #Рисуем линию
            ax.plot(xx, yy, color=color, linewidth=width, zorder=6)
            
        #Сплошные линии для стобиков
        drawLinesToPoints(ax, xScaled, yScaled, color, 1, width, style="solid", orientation="vertical", zorder=5)

        #Пунктирные линии к точкам
        drawLinesToPoints(ax, xScaled, yScaled, dashColor, dashAlpha, dashWidth, style="--", orientation="horizontal", zorder=5)

        #Убрать границы и добавить стрелочки на осях
        removeBordersAndAddArrows(ax)
        
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
    
    #Названия осей
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    
    #Отображаем только известные значения
    xScaledUniqTicks = list(dict.fromkeys([0] + xScaled))
    xUnscaledUniqTicks = list(dict.fromkeys([0] + xUnscaled))
    ax.set_xticks(xScaledUniqTicks, xUnscaledUniqTicks, fontsize=tickFontSize, minor=False)
    
    yScaledUniqTicks = list(dict.fromkeys([0] + yScaled))
    yUnscaledUniqTicks = list(dict.fromkeys([0] + yUnscaled))
    ax.set_yticks(yScaledUniqTicks, yUnscaledUniqTicks, fontsize=tickFontSize, minor=False)
    
    
    #Окно на весь экран
    if fullscreenStart:
        figManager = plt.get_current_fig_manager() 
        figManager.window.showMaximized()
    
    plt.show()