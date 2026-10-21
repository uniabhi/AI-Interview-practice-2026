import cv2
from pathlib import Path

def sample_every_nth_frame(
        video_path: str,
        output_folder: str,
        n: int = 300
) -> None:
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        raise FileNotFoundError(f"Video open नहीं हुई: {video_path}")

    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    frame_number = 0
    saved_count = 0

    try:
        while True:
            success, frame = video.read()

            if not success:
                break
            if frame_number % n ==0:
                frame_file = output_path/ f"frame_{frame_number:06d}.jpg"

                cv2.imwrite(str(frame_file), frame)
                saved_count+= 1

            frame_number+= 1

    finally:
        video.release()

    print(f"Total frames read: {frame_number}")
    print(f"frames saved: {saved_count}")

sample_every_nth_frame(
    video_path= "Computer-Vision-ML/clip_091 - Trim.mp4",
    output_folder= "Computer-Vision-ML/sampled_frames",
    n = 10
)

