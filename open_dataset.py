import datasets
import os
from PIL import Image, ImageDraw

import random


random.seed(6)

dataset_root = "[PATH]"
dataset_name = "AIHub-MSG-OCR-valid"

dataset_path = os.path.join(dataset_root, dataset_name)
dataset = datasets.Dataset.load_from_disk(dataset_path)
dataset_length = len(dataset)
while True:
    sample = dataset[random.randint(0, dataset_length - 1)]

    img_path = os.path.join(*[dataset_path, "images", sample["image_path"]])
    img = Image.open(img_path)
    width = img.width
    height = img.height
    bboxes = sample["bbox"]
    for bbox in bboxes:
        text = bbox["text"]
        coords = bbox["coords"]
        x1, y1, x2, y2 = coords
        x1 *= width
        y1 *= height
        x2 *= width
        y2 *= height

        draw = ImageDraw.Draw(img)
        draw.rectangle((x1, y1, x2, y2), outline=(0, 255, 0), width=2)
    
    img.save("./sample.jpg")
    import pdb; pdb.set_trace()
