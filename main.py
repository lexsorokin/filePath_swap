import os.path
import sys
from typing import List
import wmi
from PySide2.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow


# path = r'C:\Users\lexni\OneDrive\Desktop\TestTaskParovoz\project\scene\test_scene.ma'


def get_current_ma_file() -> str:
    """
    Функция ищет процесс с именем Notepad и возвращает командную строку,
    в которой есть путь к открытому файлу расширения .ma
    :return: путь к открытому файлу .ma
    """
    process_view = wmi.WMI()
    for process in process_view.Win32_Process():
        if process.Name == 'Notepad.exe':
            return str(process.CommandLine).split('" "')[1][:-1]


def analyze_ma_file_nodes() -> List:
    """
    Функция ищет файл ноды и проверяет пути на их наличие на компьютере
    :return: список ненайденных путей
    """
    ma_path = get_current_ma_file()
    path_do_not_exist = []

    with open(ma_path, 'r') as file:
        for line in file:
            if '.ftn' in line:
                file_path = line[:-2].split()[-1][1:-1]
                if not os.path.exists(file_path):
                    path_do_not_exist.append(file_path)

    return path_do_not_exist


class MainWindow(QMainWindow):
    def __init__(self, not_existing_paths, ma_file, parent=None):
        super(MainWindow, self).__init__(parent)

        self.not_existing_paths = not_existing_paths
        self.ma_file = ma_file
        self.old_path = None
        self.new_path = None
        self.ready_for_swap = False

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if len(self.not_existing_paths) == 0:
            self.ui.missing_path.setText('Все пути файл нод указаны верно!')
        else:
            self.ui.missing_path.setText("\n".join(self.not_existing_paths))
        self.ui.pushButton_preview_path.clicked.connect(self.preview_path_change)
        self.ui.pushButton_change_button.clicked.connect(self.change_path_in_ma_file)

    def preview_path_change(self):
        """
        Метод проверяет ввод пользователя на:
        1) Наличие старого пути в .ma файле;
        2) Наличие нового пути на компьютере;
        3) Наличие обратных слешей в пути, меняя их при True значении.
        Далее передает валидные данные в аттрибуты класса.
        Далее выводит новый путь пользователю для проверки.
        :return: None
        """
        old_path = self.ui.input_old_path.text()
        new_path = self.ui.input_new_path.text()

        self.old_path = old_path
        self.new_path = new_path

        if len(self.new_path) == 0 or len(self.old_path) == 0:
            self.ui.preview_new_path.setText('Вы не заполнили ключевую информацию...:(\n'
                                             'Убедитесь, что поля FIND и REPLACE заполнены :)')

        else:

            with open(self.ma_file, 'r') as file:
                data = file.read()

            if self.old_path not in data:
                self.ui.preview_new_path.setText("СТАРЫЙ путь не существует в файл нодах сцены...:(\n"
                                                 "Убедитесь, что старый путь введен верно и нажмите PREVIEW :)")

            elif not os.path.exists(self.new_path):
                self.ui.preview_new_path.setText('НОВЫЙ путь не существует...:(\n'
                                                 'Убедитесь, что новый путь введен верно и нажмите PREVIEW :)')
            else:
                self.ready_for_swap = True
                if '\\' in self.new_path:
                    self.new_path = self.new_path.replace('\\', '/')
                self.ui.preview_new_path.setText(self.new_path)

    def change_path_in_ma_file(self):
        """
        Метод меняет данные файл нода в .ma файле.
        :return: None
        """
        if not self.ready_for_swap:
            self.ui.preview_new_path.setText('Вы не заполнили ключевую информацию...:(\n'
                                             'Убедитесь, что поля FIND и REPLACE заполнены и нажмите PREVIEW :).')

        else:
            with open(self.ma_file, 'r') as file:
                old_data = file.read()

            new_data = old_data.replace(self.old_path, self.new_path)

            with open(self.ma_file, 'w') as file:
                file.write(new_data)

            self.ui.preview_new_path.setText(f'Путь успешно изменен на! :)')






if __name__ == '__main__':
    not_existing_paths = analyze_ma_file_nodes()
    app = QApplication()
    window = MainWindow(not_existing_paths=not_existing_paths,
                        ma_file=get_current_ma_file())
    window.show()
    sys.exit(app.exec_())

o = 'D:/project/textures/01.jpg'
n = r"C:\Users\lexni\OneDrive\Desktop\TestTaskParovoz\project\textures\file_01.jpg"
