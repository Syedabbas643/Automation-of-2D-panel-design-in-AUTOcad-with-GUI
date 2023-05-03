import sys
import os
from cx_Freeze import setup,Executable

files= ['png.png','myicon.ico','INDOOR/','OUTDOOR/']

target = Executable(
    script= 'tkmain.py',
    base= 'Win32GUI',
    icon='myicon.ico'
)

setup(
    name='My GUI project',
    version= '1.1',
    options = {'build_exe':{'include_files': files}},
    executables = [target]
)