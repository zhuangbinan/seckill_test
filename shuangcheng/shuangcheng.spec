# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['shuangcheng.py'],
    pathex=['D:\\dev\\anaconda3\\envs\\pkg_env\\Lib\\site-packages\\paddleocr','D:\\dev\\anaconda3\\envs\\pkg_env\\Lib\\site-packages\\paddle\\libs',],
    binaries=[('D:\\dev\\anaconda3\\envs\\pkg_env\\Lib\\site-packages\\paddle\\libs', '.')],
    datas=[('D:\\dev\\anaconda3\\envs\\pkg_env\\Lib\\site-packages\\paddleocr', '.')],
    hiddenimports=['scipy.special._cdflib'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='TKinter_Test',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
