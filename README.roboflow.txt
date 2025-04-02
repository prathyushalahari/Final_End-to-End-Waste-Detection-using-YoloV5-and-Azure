
images - v20 2023-06-06 5:41pm
==============================

This dataset was exported via roboflow.com on June 7, 2023 at 4:09 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 6046 images.
Idk are annotated in YOLO v5 PyTorch format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise, upside-down
* Randomly crop between 0 and 39 percent of the image
* Random rotation of between -45 and +45 degrees
* Random shear of between -45° to +45° horizontally and -45° to +45° vertically
* Random brigthness adjustment of between -37 and +37 percent
* Random exposure adjustment of between -22 and +22 percent
* Random Gaussian blur of between 0 and 7 pixels
* Salt and pepper noise was applied to 25 percent of pixels


