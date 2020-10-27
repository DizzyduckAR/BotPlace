# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
added_files = [
    ( 'resources', 'resources' ),
    ( 'venv\Lib\site-packages/adbutils', 'adbutils' ),
    ( 'venv\Lib\site-packages\gcloud-0.17.0-py3.6.egg-info', 'gcloud-0.17.0-py3.6.egg-info' )
    
]

a = Analysis(['F:\\New Botit\\Botit PyUpdater\\main.py'],
             pathex=['F:\\New Botit\\Botit PyUpdater', 'F:\\New Botit\\Botit PyUpdater'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=['f:\\new botit\\botit pyupdater\\venv\\lib\\site-packages\\pyupdater\\hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='win',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          icon='resources/base/Gui/Icon.ico',
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='win')
