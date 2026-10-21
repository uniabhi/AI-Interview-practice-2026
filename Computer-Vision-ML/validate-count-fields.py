from pathlib import Path


def validate_pose_line(line: str, num_keypoints: int) -> None:
    # Line को spaces के आधार पर values की list में बदलता है
    fields = line.strip().split()

    # 5 bounding-box fields + हर keypoint के लिए x, y, visibility
    expected_fields = 5 + (num_keypoints * 3)

    # Values की संख्या सही नहीं है तो clear error दें
    if len(fields) != expected_fields:
        raise ValueError(
            f"Expected {expected_fields} fields for {num_keypoints} keypoints, "
            f"but got {len(fields)}"
        )


# YOLO pose label file का path
label_file = Path("Computer-Vision-ML/frame_0003.txt")

# आपके label file में 30 keypoints हैं
num_keypoints = 30

# File की पहली line पढ़ें
with label_file.open("r", encoding="utf-8") as file:
    first_line = file.readline()

# Field count validate करें
validate_pose_line(first_line, num_keypoints)

# यदि error नहीं आया, तो label सही है
total_fields = len(first_line.strip().split())

print("YOLO Pose label is valid.")
print(f"Expected fields: {5 + (num_keypoints * 3)}")
print(f"Actual fields: {total_fields}")
print(f"Keypoints: {num_keypoints}")