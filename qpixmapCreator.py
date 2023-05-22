import sys
import matplotlib as mpl
import matplotlib.figure as mplfigure
import matplotlib.mathtext as mathtext
from matplotlib.backends.backend_agg import FigureCanvasAgg
from PySide6 import QtGui, QtCore

def mathTex_to_QPixmap(mathTex, fs):

    # #Ебанина со стаковерфлоу
    # mpl.rcParams.update(mpl.rcParamsDefault)
    # mpl.rcParams['text.usetex'] = True
    # mpl.rcParams['text.latex.preamble'] = r''
    # mpl.rcParams['text.usetex'] = False
    # mpl.rcParams.update(mpl.rcParamsDefault)


    #---- set up a mpl figure instance ----

    fig = mplfigure.Figure()
    fig.patch.set_facecolor('none')
    fig.set_canvas(FigureCanvasAgg(fig))
    renderer = fig.canvas.get_renderer()

    #---- plot the mathTex expression ----

    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.patch.set_facecolor('none')
    t = ax.text(0, 0, mathTex, ha='left', va='bottom', fontsize=fs, color='white')

    #---- fit figure size to text artist ----

    fwidth, fheight = fig.get_size_inches()
    fig_bbox = fig.get_window_extent(renderer)

    text_bbox = t.get_window_extent(renderer)

    tight_fwidth = text_bbox.width * fwidth / fig_bbox.width
    tight_fheight = text_bbox.height * fheight / fig_bbox.height

    fig.set_size_inches(tight_fwidth, tight_fheight)

    #---- convert mpl figure to QPixmap ----

    buf, size = fig.canvas.print_to_buffer()
    qimage = QtGui.QImage.rgbSwapped(QtGui.QImage(buf, size[0], size[1],
                                                  QtGui.QImage.Format_ARGB32))
    qpixmap = QtGui.QPixmap(qimage)

    return qpixmap

def mathTex_to_QPixmap_system(mathTex, fs):

    # #Ебанина со стаковерфлоу
    # mpl.rcParams.update(mpl.rcParamsDefault)
    # mpl.rcParams['text.usetex'] = True
    mpl.rcParams['text.latex.preamble'] = r'\usepackage{{amsmath}} \usepackage[english,main=russian]{babel} \usepackage[T2A]{fontenc}'
    mpl.rcParams['text.usetex'] = True


    #---- set up a mpl figure instance ----

    fig = mplfigure.Figure()
    fig.patch.set_facecolor('none')
    fig.set_canvas(FigureCanvasAgg(fig))
    renderer = fig.canvas.get_renderer()

    #---- plot the mathTex expression ----

    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.patch.set_facecolor('none')
    t = ax.text(0, 0, mathTex, ha='left', va='bottom', fontsize=fs, color='white')

    #---- fit figure size to text artist ----

    fwidth, fheight = fig.get_size_inches()
    fig_bbox = fig.get_window_extent(renderer)

    text_bbox = t.get_window_extent(renderer)

    tight_fwidth = text_bbox.width * fwidth / fig_bbox.width
    tight_fheight = text_bbox.height * fheight / fig_bbox.height

    fig.set_size_inches(tight_fwidth, tight_fheight)

    #---- convert mpl figure to QPixmap ----

    buf, size = fig.canvas.print_to_buffer()
    qimage = QtGui.QImage.rgbSwapped(QtGui.QImage(buf, size[0], size[1],
                                                  QtGui.QImage.Format_ARGB32))
    qpixmap = QtGui.QPixmap(qimage)

    mpl.rcParams['text.latex.preamble'] = r''
    mpl.rcParams['text.usetex'] = False
    return qpixmap