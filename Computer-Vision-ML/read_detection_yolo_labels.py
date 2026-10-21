from pathlib import Path

def read_yolo_labels(label_path: str) -> list[dict]:
    labels = []

    with Path(label_path).open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            fields = line.strip().split()

            if not fields:  # empty line skip
                continue

            # Detection format में ठीक 5 fields होने चाहिए
            if len(fields) != 5:
                raise ValueError(
                    f"Line {line_number}: expected 5 fields "
                    f"(class_id cx cy width height), got {len(fields)}"
                )

            try:
                class_id = int(fields[0])
                cx, cy, width, height = map(float, fields[1:])
            except ValueError as error:
                raise ValueError(
                    f"Line {line_number}: class ID integer और coordinates numbers होने चाहिए"
                ) from error

            if not all(0 <= value <= 1 for value in [cx, cy, width, height]):
                raise ValueError(
                    f"Line {line_number}: coordinates 0 से 1 के बीच होने चाहिए"
                )

            labels.append({
                "class_id": class_id,
                "cx": cx,
                "cy": cy,
                "width": width,
                "height": height,
            })

    return labels

result = read_yolo_labels("Computer-Vision-ML/frame_0000.txt")
print(result)