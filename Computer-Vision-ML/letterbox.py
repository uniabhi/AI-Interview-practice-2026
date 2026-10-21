import cv2
import numpy as np

def letterbox(image, target_size=(640, 640)):
    # image.shape में height पहले, width बाद में आती है।
    original_h, original_w = image.shape[:2]

    # इस function में target_size का क्रम width, height है।
    target_w, target_h = target_size

    scale = min(
        target_w / original_w,
        target_h / original_h
    )

    resized_w = round(original_w * scale)
    resized_h = round(original_h * scale)

    resized = cv2.resize(image, (resized_w, resized_h))

    # बची हुई जगह को दोनों तरफ बाँटो।
    remaining_w = target_w - resized_w
    remaining_h = target_h - resized_h

    left = remaining_w // 2
    right = remaining_w - left

    top = remaining_h // 2
    bottom = remaining_h - top

    padded = cv2.copyMakeBorder(
        resized,
        top,
        bottom,
        left,
        right,
        borderType=cv2.BORDER_CONSTANT,
        value=(114, 114, 114)
    )

    # Rounding के बाद इस्तेमाल हुए वास्तविक scale सुरक्षित रखो।
    scale_x = resized_w / original_w
    scale_y = resized_h / original_h

    metadata = {
        "scale_x": scale_x,
        "scale_y": scale_y,
        "left": left,
        "top": top,
        "original_w": original_w,
        "original_h": original_h
    }

    return padded, metadata

def map_boxes_back(boxes, metadata):
    # Copy बनाओ और decimal calculations की अनुमति दो।
    boxes = np.array(boxes, dtype=np.float64, copy=True)

    # पहले padding घटाओ, फिर scale से divide करो।
    boxes[:, [0, 2]] = (
        boxes[:, [0, 2]] - metadata["left"]
    ) / metadata["scale_x"]

    boxes[:, [1, 3]] = (
        boxes[:, [1, 3]] - metadata["top"]
    ) / metadata["scale_y"]

    # Box को original image की boundaries के अंदर रखो।
    boxes[:, [0, 2]] = np.clip(
        boxes[:, [0, 2]], 0, metadata["original_w"]
    )

    boxes[:, [1, 3]] = np.clip(
        boxes[:, [1, 3]], 0, metadata["original_h"]
    )

    return boxes


image = cv2.imread("Computer-Vision-ML/frame_0029.jpg")

if image is None:
    raise ValueError("Image नहीं मिली. File का path जाँचो.")

model_input, metadata = letterbox(image)

# उदाहरण के लिए मान रहे हैं कि model ने यह box दिया।
predicted_boxes = [
    [80, 200, 400, 360]
]

original_boxes = map_boxes_back(predicted_boxes, metadata)

print(original_boxes)