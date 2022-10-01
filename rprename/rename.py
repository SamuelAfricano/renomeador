import time
from  pathlib import Path

from PyQt5.QtCore import QObject, pyqtSignal

class Renamer(QObject):
    progressed = pyqtSignal(int)
    renamerFile = pyqtSignal(Path)
    finished = pyqtSignal()

    def __init__(self, files, prefix):
        super().__init__()
        self._files = files
        self._prefix = prefix

    def renameFiles(self):
        for fileNumber, file in enumerate(self._files, 1):
            newFile = file.parent.joinpath(
                f"{self._prefix}{str(fileNumber)}{file.suffix}"
            )
            file.rename(newFile)
            time.sleep(1)
            self.progressed.emit(fileNumber)
            self.renamerFile.emit(newFile)
        self.progressed.emit(0) # Resetar a barra de progresso
        self.finished.emit()