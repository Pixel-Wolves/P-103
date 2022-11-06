import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "INGRESA LA RUTA DE LA CARPETA DESCARGAS (UTILIZA " / ") en VSC"
# to_dir = "INGRESA LA RUTA DE LA CARPETA DESTINO(UTILIZA " / ") en VSC"

from_dir = "D:\\rpoot\\Downloads"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt','.zip'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'],
    "Text_Files": ['.txt']
}

# Clase event handler 

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):

        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name=os.path.basename(event.src_path)
                print("File Created:"+file_name)

    def on_modified(self, event):

        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name=os.path.basename(event.src_path)
                print("File Modified:"+file_name)

    def on_moved(self, event):

        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name=os.path.basename(event.src_path)
                print("File Moved:"+file_name)

    def on_deleted(self, event):

        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name=os.path.basename(event.src_path)
                print("File Deleted:"+file_name)

# Inicia la clase event handler
event_handler = FileEventHandler()


# Inicia Observer
observer = Observer()

# Programa Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Inicia Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("Executing...")
except KeyboardInterrupt:
    print("Stop")
    observer.stop()