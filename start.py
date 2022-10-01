
try:
    import sys
    import webview
    import importlib
    import io,urllib.request
    from zipfile import ZipFile
    from importlib import util
    import requests
    import os
    import time
    import base64
    import json
    import configparser
    import pyautogui
    import win32api
    import logging
    import shutil
    import base64
    from PIL import Image
    import io
    import numpy as np
    import win32gui
    import win32ui
    import win32con
    import ctypes
    import clipboard



except:
    print('import error')
# from urllib.request import urlretrieve
try:
    import subprocess
except:
    print('import error1')
try:
#pyupdater
    from pyupdater.client import Client
    from urllib.request import Request
except:
    print('import error2')



if len(sys.argv) > 1:
    spec = util.spec_from_file_location('', os.getcwd()+'/apps/'+sys.argv[1]+'/'+sys.argv[1]+'.py')
    module = util.module_from_spec(spec)

    sys.path.append(os.getcwd()+'\\apps\\'+sys.argv[1])
    os.chdir(r"apps/"+sys.argv[1])
    # sys.path.append(os.getcwd()+'\\apps\\'+sys.argv[1]+'\\eggman')
    # sys.path.append('apps/'+sys.argv[1])
    spec.loader.exec_module(module)
else:
   
    spec = util.spec_from_file_location('', os.getcwd()+'/apps/hub/hub.py')
    module = util.module_from_spec(spec)
    sys.path.append(os.getcwd()+'\\apps\\hub')
    # sys.path.append('apps/hub')
    spec.loader.exec_module(module)



    
