import cv2
import os
import glob

def extraer_fotogramas(video_path, output_folder, cada_n_frames=8):
    if not os.path.exists(video_path):
        return

    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps == 0:
        cap.release()
        return

    frame_num = 0
    foto_num = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_num % cada_n_frames == 0:
            filename = os.path.join(output_folder, f"foto_{foto_num:04d}.jpg")
            cv2.imwrite(filename, frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
            foto_num += 1

        frame_num += 1

    cap.release()

video_folder = "video"

if not os.path.exists(video_folder):
    exit()

mp4_files = glob.glob(os.path.join(video_folder, "*.mp4")) + glob.glob(os.path.join(video_folder, "*.MP4"))

if not mp4_files:
    exit()

video_path = mp4_files[0]
output_folder = "fotos"

extraer_fotogramas(video_path, output_folder, cada_n_frames=8)