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

def drawDashLines(ax, x, y, dashColor, dashAlpha, dashWidth):
    #zip(x, y) - cписок всех точек графика
            
    #Dictionary горизонтальных линий
    horizontalLines = {}
    for point in zip(x, y):
        horizontalLines[point[1]] = []
    for point in zip(x, y):
        horizontalLines[point[1]].append(point[0])
        
    #Dictionary вертикальных линий
    vertiaclLines = {}
    for point in zip(x, y):
        vertiaclLines[point[0]] = []
    for point in zip(x, y):
        vertiaclLines[point[0]].append(point[1])
                            
    #Рисуем горизонтальные линии
    for lineY in horizontalLines:
        horizontalLines[lineY].sort()
        biggestX = horizontalLines[lineY][-1]
        xx = [0, biggestX]
        yy = [lineY] * 2
        ax.plot(xx, yy, '--', color=dashColor, alpha=dashAlpha, linewidth=dashWidth)
    
    #Рисуем вертикальные линии
    for lineX in vertiaclLines:
        vertiaclLines[lineX].sort()
        biggestY = vertiaclLines[lineX][-1]
        xx = [lineX] * 2
        yy = [0, biggestY]
        ax.plot(xx, yy, '--', color=dashColor, alpha=dashAlpha, linewidth=dashWidth)

def drawPolygonGraph(x, y, xLabel="", yLabel="", color="black", width=2, dashColor="black", dashAlpha=0.5, dashWidth=0.7, fullscreenStart=True):
    #Построение графика в отдельном окне
        rc = {"xtick.direction" : "inout", "ytick.direction" : "inout",
            "xtick.major.size" : 5, "ytick.major.size" : 5,}
        #with - это не цикл, а что-то типа try except 
        with plt.rc_context(rc):
            fig, ax = plt.subplots()

            #Пунктирные линии с точком
            drawDashLines(ax, x, y, dashColor, dashAlpha, dashWidth)
            
            #Рисуем сам график
            ax.plot(x, y, color=color, linewidth=width)

            #Убрать границы и добавить стрелочки на осях
            removeBordersAndAddArrows(ax)
        
        #Названия осей
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        
        #Отображаем только известные значения
        ax.set_xticks(x, x, minor=False)
        ax.set_yticks(y, y, minor=False)
          
        #Окно на весь экран
        if fullscreenStart:
            figManager = plt.get_current_fig_manager() 
            figManager.window.showMaximized()
          
        #Вывести окно с графиком
        plt.show()
        
def drawEmpiricalGraph(empiricalFunction, xLabel="", yLabel="", color="black", width=2, dashColor="black", dashAlpha=0.5, dashWidth=0.7, fullscreenStart=True):   
    rc = {"xtick.direction" : "inout", "ytick.direction" : "inout",
            "xtick.major.size" : 5, "ytick.major.size" : 5,}
    with plt.rc_context(rc):
        fig, ax = plt.subplots()
        
        x = []
        y = []
        
        #Рисуем основные стрелочки
        for i in range(len(empiricalFunction["y"])):
            #Рисуем линию
            xx = [empiricalFunction['start'][i], empiricalFunction['end'][i]]
            yy = [empiricalFunction['y'][i]] * len(xx)
            ax.plot(xx, yy, color=color, linewidth=width)
            
            x = x + xx
            y = y + yy
            
            #Добавляем стрелочку
            ax.plot(xx[0], yy[0], marker="<", color=color, linewidth=width)

        #Пунктирные линии с точком
        drawDashLines(ax, x, y, dashColor, dashAlpha, dashWidth)

        #Убрать границы и добавить стрелочки на осях
        removeBordersAndAddArrows(ax)
    
    #Названия осей
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    
    #Отображаем только известные значения
    ax.set_xticks(x, x, minor=False)
    ax.set_yticks(y, y, minor=False)
    
    #Окно на весь экран
    if fullscreenStart:
        figManager = plt.get_current_fig_manager() 
        figManager.window.showMaximized()
    
    plt.show()