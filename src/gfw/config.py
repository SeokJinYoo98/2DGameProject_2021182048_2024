import os

# 프로젝트 루트 경로
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# assets 경로 설정
DATA_DIR = os.path.join(BASE_DIR, 'data')
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
SPRITES_DIR = os.path.join(ASSETS_DIR, 'sprites')
SOUNDS_DIR = os.path.join(ASSETS_DIR, 'sound')
FONT_DIR = os.path.join(ASSETS_DIR, 'font')
