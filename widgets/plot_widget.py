from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import serpentTools
import os

# Функция для поиска файлов по расширению
def find_file_by_extension(folder_path, extension):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                return file_path
    return None

# Функция, определяющая, каким образом будет строиться график
def check_word_in_filename(file_path, search_word):
    file_name = os.path.basename(file_path)
    if search_word in file_name:
        return True
    else:
        return False

folder_path = "C:/Users/USER/PycharmProjects/chamber-shape/widgets"
extension = '.m'

class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        # x = [1, 2, 3, 4, 5, 6]
        # y = [10, 20, 30, 40, 50, 60]

        # Здесь осуществляется поиск файлов с расширением .m
        detFilePath = find_file_by_extension(folder_path, extension)

        # Если строим график детектора в пространстве
        if check_word_in_filename(detFilePath, "profile"):
            detFile = serpentTools.read(detFilePath)
            print(detFile.detectors)

            # fig = Figure()
            # ax = fig.add_subplot()
            # ax.plot(x, y, label='')

            spectrum = detFile.detectors['1SPOVERALL']
            EMidGrid = spectrum.grids['E'][:, 2]
            SpFlux = spectrum.tallies
            SpErr = spectrum.errors
            print(SpErr[:10])
            fig, Axes = plt.subplots()

            # Здесь настроить цвет и название
            Axes.errorbar(EMidGrid, SpFlux, SpErr * 3 * SpFlux, color='blue', marker=',',
                          label='Спектральная плотность потока')
            # Здесь настроить основные линии сетки
            Axes.grid(visible=True, which='major', axis='both', color='0.3', linestyle='-', linewidth=0.5)
            # Здесь настроить вспомогательные линии сетки
            Axes.grid(visible=True, which='minor', axis='x', color='0.3', linestyle='-', linewidth=0.5)
            # Здесь настроить пределы и подписи осей, логарифмические или нет
            Axes.set(xlabel='Энергия, МэВ', ylabel='ФV, $см^3/(см^2\u00B7с)$', xscale='log', yscale='log',
                     xlim=(1e-8, 20), ylim=(1e12, 1e15))
            # Здесь указать дополнительные точки на оси Х
            Axes.set_xticks((1e-7, 1e-5, 1e-3, 1e-1, 10), minor=True)
            # Размещаем легенду
            Axes.legend(loc='best')

        # Если строим график детектора значение от энергии
        if check_word_in_filename(detFilePath, "spectrum"):

            # Здесь указать имена детекторов в файле
            detNames = ['1SPOVERALL', '1SPWATER', '1SPFUEL']

            # Здесь указать подписи к графикам. Количество должно совпадать
            detLegend = ['Общий', 'Вода', 'Топливо']

            # Здесь указать цвета к графикам. Количество должно совпадать
            Colorr = ['k', 'blue', 'orange']

            N = len(detNames)
            detFile, EMidGrid, SpFlux, SpErr = [0], [0], [0], [0]
            if os.path.isfile(detFilePath):
                detFile = serpentTools.read(detFilePath, reader='det')

            for j in range(N):
                if j > 0:
                    EMidGrid.append(0)
                    SpFlux.append(0)
                    SpErr.append(0)
                spectrum = detFile.detectors[detNames[j]]
                EMidGrid[j] = spectrum.grids['E'][:, 2]
                SpFlux[j] = spectrum.tallies
                SpErr[j] = spectrum.errors
                # Переводим спектры в относительные единицы
                Num = len(EMidGrid[j])
                F = sum(SpFlux[j])
                SpFlux[j] = SpFlux[j] / F * Num

            fig, Axes = plt.subplots()

            for j in range(N):
                # Здесь настроить цвет и название
                Axes.errorbar(EMidGrid[j], SpFlux[j], SpErr[j] * 3 * SpFlux[j], color=Colorr[j], marker=',',
                              label=detLegend[j])

            # добавляем теоретический спектр Ферми
            # Ftheor = 1/EMidGrid[0]
            # Num = len(Ftheor)
            # Ft=sum(SpFlux[j])
            # SpFluxFermi = Ftheor/Ft
            # Axes.plot(EMidGrid[0], SpFluxFermi, color='0.5', marker=',',
            #                  label='Спектр Ферми')

            # Здесь настроить основные линии сетки
            Axes.grid(visible=True, which='major', axis='both', color='0.3', linestyle='-', linewidth=0.5)

            # Здесь настроить вспомогательные линии сетки
            Axes.grid(visible=True, which='minor', axis='both', color='0.7', linestyle='-', linewidth=0.5)

            # Здесь настроить пределы и подписи осей, логарифмические или нет
            Axes.set(xlabel='Энергия, МэВ', ylabel='ФV, отн. ед.', xscale='log', yscale='log',
                     xlim=(1e-8, 20), ylim=(2e-3, 2e1))

            # Здесь указать дополнительные точки на оси Х
            Axes.set_xticks((1e-7, 1e-5, 1e-3, 1e-1, 10), minor=True)

            # Размещаем легенду
            Axes.legend(loc='best')

        canvas = FigureCanvasQTAgg(fig)
        layout.addWidget(canvas)
