import json
import os
from gfw.config import DATA_DIR

def load_data(filePath):
    file_path = os.path.join(DATA_DIR, filePath)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # 인코딩을 명시적으로 지정
            data = json.load(file)  # 파일 객체를 인자로 전달
            frames = data.get("FRAMES", {})
            frame_info = data.get("FRAME_INFO", {})
            frames = {
                key: [tuple(frame) for frame in value] for key, value in frames.items()
            }
            frame_info = {
                key: tuple(info) for key, info in frame_info.items()
            }
            return frames, frame_info
    except FileNotFoundError:
        print(f"Error: {file_path} 파일을 찾을 수 없습니다.")
        return None, None
    except json.JSONDecodeError as e:
        print(f"Error: JSON 파일 형식이 잘못되었습니다. {e}")
        return None, None