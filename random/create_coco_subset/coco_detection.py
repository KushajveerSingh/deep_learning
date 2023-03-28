import os
import json
from pathlib import Path
from shutil import copy

# Change the three variables below. Rest no changes need to be made to the
# script

# ORIG_DIR should follow the following directory structure
# |-- annotations
#     |-- captions_train2017.json
#     |-- captions_val2017.json
# |-- train2017
#     Images
# |-- val2017
#     Images

# SAVE_DIR will produce the same directory structure as above

ORIG_DIR = Path('/home/kushaj/Desktop/Data/coco')
SAVE_DIR = Path('../../datasets/coco_detection_2d')
CLASSES = [
    'person',
    'car',
    'bus',
    'truck',
    'traffic light',
]


def handle_categories():
    with open('categories.json') as f:
        cats = json.load(f)
    out = []
    id_count = 1
    orig_ids = []

    for cat in cats["categories"]:
        if cat["name"] in CLASSES:
            orig_ids.append(cat["id"])
            cat["id"] = id_count
            out.append(cat)
            id_count += 1

    orig_ids = sorted(orig_ids)
    ids = {}
    for i, o_id in enumerate(orig_ids):
        ids[o_id] = i
    return out, ids


def parse_annotation_file(path):
    with open(path) as f:
        src = json.load(f)
    out = {}
    out["info"] = src["info"]
    out["licenses"] = src["licenses"]

    # Get the valid image ids for the given classes
    image_ids = set()
    for annot in src["annotations"]:
        if annot["category_id"] in orig_ids:
            image_ids.add(annot["image_id"])

    images = []
    for image in src["images"]:
        if image["id"] in image_ids:
            images.append(image)
    out["images"] = images

    annotations = []
    for annot in src["annotations"]:
        if annot["image_id"] in image_ids and annot["category_id"] in orig_ids:
            annot["category_id"] = orig_ids[annot["category_id"]]
            annotations.append(annot)
    out["annotations"] = annotations

    out["categories"] = categories

    return out


def get_annotation_files():
    # Make necessary folders in destination
    os.makedirs(SAVE_DIR, exist_ok=True)
    os.makedirs(SAVE_DIR/'annotations', exist_ok=True)

    # Train file
    train_annot = parse_annotation_file(ORIG_DIR/'annotations/instances_train2017.json')
    with open(SAVE_DIR/'annotations/instances_train2017.json', 'w') as f:
        json.dump(train_annot, f)

    # Valid file
    val_annot = parse_annotation_file(ORIG_DIR/'annotations/instances_val2017.json')
    with open(SAVE_DIR/'annotations/instances_val2017.json', 'w') as f:
        json.dump(val_annot, f)


def copy_image_files():
    with open(SAVE_DIR/'annotations/instances_train2017.json') as f:
        train_annot = json.load(f)
    with open(SAVE_DIR/'annotations/instances_val2017.json') as f:
        valid_annot = json.load(f)
    os.makedirs(SAVE_DIR/'train2017', exist_ok=True)
    os.makedirs(SAVE_DIR/'val2017', exist_ok=True)

    for image in train_annot["images"]:
        src = ORIG_DIR/'train2017'/image["file_name"]
        dest = SAVE_DIR/'train2017'/image["file_name"]
        copy(src, dest)

    for image in valid_annot["images"]:
        src = ORIG_DIR/'val2017'/image["file_name"]
        dest = SAVE_DIR/'val2017'/image["file_name"]
        copy(src, dest)

if __name__ == "__main__":
    categories, orig_ids = handle_categories()
    # get_annotation_files()
    copy_image_files()