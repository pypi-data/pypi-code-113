import os
import re
import time
import traceback
import difflib
import numpy as np
import pandas as pd
import tkinter as tk
import sys
from tkinter import ttk
from ast import literal_eval
from skimage.color import label2rgb, gray2rgb
from skimage.measure import regionprops
from skimage import img_as_float
from natsort import natsorted
from pyqtgraph.Qt import QtGui
from PyQt5.QtWidgets import (
    QApplication, QPushButton, QHBoxLayout, QLabel, QSizePolicy
)
from PyQt5.QtCore import (
    Qt
)

from . import apps, myutils

class RichTextPushButton(QPushButton):
    def __init__(self, parent=None, text=None):
        if parent is not None:
            super().__init__(parent)
        else:
            super().__init__()
        self.__lbl = QLabel(self)
        if text is not None:
            self.__lbl.setText(text)
        self.__lyt = QHBoxLayout()
        self.__lyt.setContentsMargins(5, 0, 0, 0)
        self.__lyt.setSpacing(0)
        self.setLayout(self.__lyt)
        self.__lbl.setAttribute(Qt.WA_TranslucentBackground)
        self.__lbl.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.__lbl.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding,
        )
        self.__lbl.setTextFormat(Qt.RichText)
        self.__lyt.addWidget(self.__lbl)
        return

    def setText(self, text):
        self.__lbl.setText(text)
        self.updateGeometry()
        return

    def sizeHint(self):
        s = QPushButton.sizeHint(self)
        w = self.__lbl.sizeHint()
        s.setWidth(w.width()+10)
        s.setHeight(w.height()+8)
        return s

def folder_dialog(toplevel=False, **options):
    #Prompt the user to select the image file
    if toplevel:
        root = tk.Toplevel()
    else:
        root = tk.Tk()
        root.withdraw()
    path = tk.filedialog.Directory(**options).show()
    root.destroy()
    return path

class select_channel_name:
    def __init__(self, which_channel=None, allow_abort=True):
        self.is_first_call = True
        self.which_channel = which_channel
        self.last_sel_channel = self._load_last_selection()
        self.was_aborted = False
        self.allow_abort = allow_abort

    def get_available_channels(
            self, filenames, images_path, useExt='.tif'
        ):
        # First check if metadata.csv already has the channel names
        metadata_csv_path = None
        for file in myutils.listdir(images_path):
            if file.endswith('metadata.csv'):
                metadata_csv_path = os.path.join(images_path, file)
                break

        chNames_found = False
        if metadata_csv_path is not None:
            df = pd.read_csv(metadata_csv_path)
            if 'Description' in df.columns:
                channelNamesMask = df.Description.str.contains(r'channel_\d+_name')
                channelNames = df[channelNamesMask]['values'].to_list()
                if channelNames:
                    channel_names = channelNames.copy()
                    basename = None
                    for chName in channelNames:
                        chSaved = []
                        for file in filenames:
                            _, ext = os.path.splitext(file)
                            pattern = f'{chName}{ext}'
                            if file.endswith(pattern):
                                chSaved.append(True)
                                m = tuple(re.finditer(pattern, file))[-1]
                                chName_idx = m.start()
                                basename = file[:chName_idx]
                        if not any(chSaved):
                            channel_names.remove(chName)

                    if basename is not None:
                        self.basenameNotFound = False
                        self.basename = basename
                        return channel_names, False

        # Find basename as intersection of filenames
        channel_names = []
        self.basenameNotFound = False
        isBasenamePresent = myutils.checkDataIntegrity(filenames, images_path)
        basename = filenames[0]
        for file in filenames:
            # Determine the basename based on intersection of all .tif
            _, ext = os.path.splitext(file)
            if useExt is None:
                sm = difflib.SequenceMatcher(None, file, basename)
                i, j, k = sm.find_longest_match(0, len(file),
                                                0, len(basename))
                basename = file[i:i+k]
            elif ext == useExt:
                sm = difflib.SequenceMatcher(None, file, basename)
                i, j, k = sm.find_longest_match(0, len(file),
                                                0, len(basename))
                basename = file[i:i+k]
        self.basename = basename
        basenameNotFound = [False]
        for file in filenames:
            filename, ext = os.path.splitext(file)
            if useExt is None:
                channel_name = filename.split(basename)[-1]
                channel_names.append(channel_name)
                if channel_name == filename:
                    # Warn that an intersection could not be found
                    basenameNotFound.append(True)
            elif ext == useExt:
                channel_name = filename.split(basename)[-1]
                channel_names.append(channel_name)
                if channel_name == filename:
                    # Warn that an intersection could not be found
                    basenameNotFound.append(True)
        if any(basenameNotFound):
            self.basenameNotFound = True
            filenameNOext, _ = os.path.splitext(basename)
            self.basename = f'{filenameNOext}_'
        if self.which_channel is not None:
            # Search for "phase" and put that channel first on the list
            if self.which_channel == 'segm':
                is_phase_contr_li = [c.lower().find('phase')!=-1
                                     for c in channel_names]
                if any(is_phase_contr_li):
                    idx = is_phase_contr_li.index(True)
                    channel_names[0], channel_names[idx] = (
                                      channel_names[idx], channel_names[0])
        return channel_names, any(basenameNotFound)

    def _load_last_selection(self):
        last_sel_channel = None
        ch = self.which_channel
        if self.which_channel is not None:
            _path = os.path.dirname(os.path.realpath(__file__))
            temp_path = os.path.join(_path, 'temp')
            txt_path = os.path.join(temp_path, f'{ch}_last_sel.txt')
            if os.path.exists(txt_path):
                with open(txt_path) as txt:
                    last_sel_channel = txt.read()
        return last_sel_channel

    def _save_last_selection(self, selection):
        ch = self.which_channel
        if self.which_channel is not None:
            _path = os.path.dirname(os.path.realpath(__file__))
            temp_path = os.path.join(_path, 'temp')
            if not os.path.exists(temp_path):
                os.mkdir(temp_path)
            txt_path = os.path.join(temp_path, f'{ch}_last_sel.txt')
            with open(txt_path, 'w') as txt:
                txt.write(selection)

    def QtPrompt(self, parent, channel_names, informativeText='',
                 CbLabel='Select channel name:  '):
        font = QtGui.QFont()
        font.setPointSize(10)
        win = apps.QDialogCombobox(
                              'Select channel name',
                              channel_names,
                              informativeText,
                              CbLabel=CbLabel,
                              parent=parent,
                              defaultChannelName=self.last_sel_channel)
        win.setFont(font)
        win.exec_()
        if win.cancel:
            self.was_aborted = True
        self.channel_name = win.selectedItemText
        self._save_last_selection(self.channel_name)
        self.is_first_call = False

    def setUserChannelName(self):
        if self.basenameNotFound:
            reverse_ch_name = self.channel_name[::-1]
            idx = reverse_ch_name.find('_')
            if idx != -1:
                self.user_ch_name = self.channel_name[-idx:]
            else:
                self.user_ch_name = self.channel_name[-4:]
        else:
            self.user_ch_name = self.channel_name


    def prompt(self, channel_names, message=None, toplevel=False):
        if toplevel:
            root = tk.Toplevel()
        else:
            root = tk.Tk()
        root.lift()
        # root.attributes("-topmost", True)
        root.title('Select channel name')
        root.geometry("+800+400")
        row = 0
        if message is not None:
            tk.Label(root,
                     text=message,
                     font=(None, 11)).grid(row=row, column=0,
                                           columnspan= 2, pady=(10,0),
                                                          padx=10)
            row += 1

        tk.Label(root,
                 text='Select channel name to analyse:'
                 ).grid(row=row, column=0, pady=(10,0), padx=10)

        ch_name_var = tk.StringVar()
        w = max([len(s) for s in channel_names])+4
        ch_name_combob = ttk.Combobox(root, width=w, justify='center',
                                      textvariable=ch_name_var)
        ch_name_combob.option_add('*TCombobox*Listbox.Justify', 'center')
        ch_name_combob['values'] = channel_names
        ch_name_combob.grid(column=1, row=row, padx=10, pady=(10,0))
        if self.last_sel_channel is not None:
            if self.last_sel_channel in channel_names:
                ch_name_combob.current(channel_names.index(self.last_sel_channel))
            else:
                ch_name_combob.current(0)
        else:
            ch_name_combob.current(0)

        ch_name_var.trace_add("write", self._test)

        row += 1
        tk.Button(root, text='Ok', width=20,
                        command=self._tk_close).grid(row=row, column=0,
                                                  columnspan=2,
                                                  pady=10, padx=10)



        root.protocol("WM_DELETE_WINDOW", self._tk_abort)
        self.ch_name_var = ch_name_var
        self.root = root

        root.mainloop()

    def _tk_close(self):
        self.was_aborted = False
        self.channel_name = self.ch_name_var.get()
        self.root.quit()
        self.root.destroy()


    def _tk_abort(self):
        self.was_aborted = True
        self.root.quit()
        self.root.destroy()
        if self.allow_abort:
            exit('Execution aborted by the user')

    def _test(self, name=None, index=None, mode=None):
        pass

    def _abort(self):
        self.was_aborted = True
        if self.allow_abort:
            exit('Execution aborted by the user')

def askyesno(title='tk', message='Yes or no?', toplevel=False):
    if toplevel:
        root = tk.Toplevel()
    else:
        root = tk.Tk()
        root.withdraw()
    yes = tk.messagebox.askyesno(title, message, master=root)
    if not toplevel:
        root.quit()
        root.destroy()
    return yes
