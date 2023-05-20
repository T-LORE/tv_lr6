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
    
    

def drawDashLines(ax, x, y, dashColor, dashAlpha, dashWidth, zorder=3):
    #zip(x, y) - cписок всех точек графика      
    points = [i for i in zip(x, y)]
            
    #Dictionary горизонтальных линий
    horizontalLines = {}
    for point in points:
        horizontalLines[point[1]] = []
    for point in points:
        horizontalLines[point[1]].append(point[0])
        
    #Dictionary вертикальных линий
    vertiaclLines = {}
    for point in points:
        vertiaclLines[point[0]] = []
    for point in points:
        vertiaclLines[point[0]].append(point[1])
                            
    #Рисуем горизонтальные линии
    for lineY in horizontalLines:
        horizontalLines[lineY].sort()
        biggestX = horizontalLines[lineY][-1]
        xx = [0, biggestX]
        yy = [lineY] * 2
        ax.plot(xx, yy, '--', color=dashColor, alpha=dashAlpha, linewidth=dashWidth, zorder=zorder)
    
    #Рисуем вертикальные линии
    for lineX in vertiaclLines:
        vertiaclLines[lineX].sort()
        biggestY = vertiaclLines[lineX][-1]
        xx = [lineX] * 2
        yy = [0, biggestY]
        ax.plot(xx, yy, '--', color=dashColor, alpha=dashAlpha, linewidth=dashWidth, zorder=zorder)

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
            print(f"Min diff = { xMinDiff }")
        
            #Находим смещение для всех X
            xFirst = x[0]
            xDeltaForScaling = xFirst - xMinDiff  

            useScaling = xDeltaForScaling > 0.1

            xScaled = [i for i in xUnscaled]
            if useScaling:
                xScaled = [i - xDeltaForScaling for i in xScaled]
            yScaled = yUnscaled

            #Пунктирные линии к точкам
            drawDashLines(ax, xScaled, yScaled, dashColor, dashAlpha, dashWidth, zorder=5)
            
            #Рисуем сам график
            ax.plot(xScaled, yScaled, color=color, linewidth=width, zorder=6)

            #Убрать границы и добавить стрелочки на осях
            removeBordersAndAddArrows(ax)
        
            #Добавить разрыв оси 
            if useScaling:
                #Белый фон для разрыва
                ax.plot(xScaled[0] / 2, 0, ls="", marker="s", markersize=25, color="white", clip_on=False, zorder=3)
                #Символ разрыва
                plt.text(xScaled[0] / 2, 0, "∿", size=20, horizontalalignment='center', verticalalignment='center', zorder=4)
        
        #Названия осей
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        
        #Отображаем только известные значения
        ax.set_xticks([0] + xScaled, [0] + xUnscaled, fontsize=tickFontSize, minor=False)
        ax.set_yticks([0] + yScaled, [0] + yUnscaled, fontsize=tickFontSize, minor=False)
          
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
        
        #Реальные значения x и y
        xUnscaled = []
        yUnscaled = []
        #Изменённые значения для разрыва
        xScaled = []
        yScaled = []
        
        #Находим мин разницу м/у элементами
        allX = [value for value in empiricalFunction["start"]] + [value for value in empiricalFunction["end"]]        
        xMinDiff = minDiffInList(allX)
        print(f"Min diff = { xMinDiff }")
    
        #Находим смещение для всех X
        xFirst = empiricalFunction["start"][0]
        xDeltaForScaling = xFirst - xMinDiff        
        
        useScaling = xDeltaForScaling > 0.1
        
        #Рисуем основные стрелочки
        for i in range(len(empiricalFunction["y"])):
            #Точки для отрисовки линии
            xx = [empiricalFunction['start'][i], empiricalFunction['end'][i]]
            yy = [empiricalFunction['y'][i]] * len(xx)
                  
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
        drawDashLines(ax, xScaled[:-1], yScaled[:-1], dashColor, dashAlpha, dashWidth, zorder=5)

        #Убрать границы и добавить стрелочки на осях
        removeBordersAndAddArrows(ax)
        
        #Добавить разрыв оси 
        if useScaling:
            #Белый фон для разрыва
            ax.plot(xScaled[0] / 2, 0, ls="", marker="s", markersize=25, color="white", clip_on=False, zorder=3)
            #Символ разрыва
            plt.text(xScaled[0] / 2, 0, "∿", size=20, horizontalalignment='center', verticalalignment='center', zorder=4)
    
    #Названия осей
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    
    #Отображаем только известные значения
    #Список обрезан, т.к. последняя стрелка идет из бесконечности
    ax.set_xticks([0] + xScaled[:-1], [0] + xUnscaled[:-1], fontsize=tickFontSize, minor=False)
    ax.set_yticks([0] + yScaled, [0] + yUnscaled, fontsize=tickFontSize, minor=False)
    
    #Не продлевать ось X дальше графика
    ax.margins(x=0.0)
    
    #Окно на весь экран
    if fullscreenStart:
        figManager = plt.get_current_fig_manager() 
        figManager.window.showMaximized()
    
    plt.show()