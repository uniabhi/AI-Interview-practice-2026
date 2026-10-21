from pathlib import Path


def write_yolo_labels(labels_path: str, labels: list[dict]) -> None:
    # File path को Path object में बदलता है
    path = Path(labels_path)

    # अगर labels folder नहीं है, तो उसे बना देगा
    path.parent.mkdir(parents=True, exist_ok=True)

    # "w" mode: नई file बनाएगा; पुरानी file हो तो overwrite करेगा
    with path.open("w", encoding="utf-8") as file:
        # हर dictionary/object के लिए एक YOLO label line लिखेगा
        for label in labels:
            file.write(
                f'{label["class_id"]} '
                f'{label["cx"]:.6f} '
                f'{label["cy"]:.6f} '
                f'{label["width"]:.6f} '
                f'{label["height"]:.6f}\n'
            )


# यह वह data है जो YOLO .txt file में लिखा जाएगा
labels = [
    {
        "class_id": 0,  # जैसे: 0 = fire
        "cx": 0.50,     # bounding box center x
        "cy": 0.40,     # bounding box center y
        "width": 0.30,  # bounding box width
        "height": 0.20, # bounding box height
    },
    {
        "class_id": 1,  # जैसे: 1 = smoke
        "cx": 0.25,
        "cy": 0.60,
        "width": 0.10,
        "height": 0.15,
    },
]


# यह file create होगी
output_path = "Computer-Vision-ML/labels/fire_01.txt"

# YOLO labels file में लिखो
write_yolo_labels(output_path, labels)

# Terminal में confirmation और file content दिखाओ
print(f"YOLO label file created successfully: {output_path}")
print("\nFile content:")

print(Path(output_path).read_text(encoding="utf-8"))