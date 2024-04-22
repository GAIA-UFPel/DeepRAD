import shutil
import os
import glob
import random
import sys

def split_yolov8_dataset(dataset_path, output_path, train_size, val_size):
    # Create the output directories
    os.makedirs(os.path.join(output_path, "train"), exist_ok=True)
    os.makedirs(os.path.join(output_path, "val"), exist_ok=True)
    os.makedirs(os.path.join(output_path, "test"), exist_ok=True)

    # Get the list of files
    image_files = glob.glob(os.path.join(dataset_path, "*.jpg"))
    image_files.extend(glob.glob(os.path.join(dataset_path, "*.jpeg")))
    image_files.extend(glob.glob(os.path.join(dataset_path, "*.png")))

    # Shuffle the files
    random.shuffle(image_files)

    # Split the files
    train_files = image_files[:int(train_size * len(image_files))]
    val_files = image_files[int(train_size * len(image_files)):int((train_size + val_size) * len(image_files))]
    test_files = image_files[int((train_size + val_size) * len(image_files)):]

    # Move the files
    for image_file in train_files:
        identifier = os.path.basename(image_file).split(".")[0]
        all_files = glob.glob(os.path.join(dataset_path, identifier + "*"))
        for file in all_files:
            shutil.copy(file, os.path.join(output_path, "train", os.path.basename(file)))

    for image_file in val_files:
        identifier = os.path.basename(image_file).split(".")[0]
        all_files = glob.glob(os.path.join(dataset_path, identifier + "*"))
        for file in all_files:
            shutil.copy(file, os.path.join(output_path, "val", os.path.basename(file)))

    for image_file in test_files:
        identifier = os.path.basename(image_file).split(".")[0]
        all_files = glob.glob(os.path.join(dataset_path, identifier + "*"))
        for file in all_files:
            shutil.copy(file, os.path.join(output_path, "test", os.path.basename(file)))

def split_coco_dataset(dataset_path, output_path, train_size, val_size):
    pass

if __name__ == "__main__":
    dataset_path = sys.argv[1]
    output_path = sys.argv[2]
    train_size = float(sys.argv[3])
    val_size = float(sys.argv[4])
    
    split_yolov8_dataset(dataset_path, output_path, train_size, val_size)