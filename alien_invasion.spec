# -*- mode: python -*-

block_cipher = None

data_files = [
				('game_data/*.txt', 'game_data'),
				('game_sounds/*.mp3', 'game_sounds'),
				('game_sounds/*.wav', 'game_sounds'),
				('images/*.png', 'images'),
				('images/*.bmp', 'images')
				
				
			]

a = Analysis(['alien_invasion.py'],
             pathex=['Z:\\NewProjects\\python_training\\AlienInvasion'],
             binaries=[],
             datas=data_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='alien_invasion',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='alien_invasion')
