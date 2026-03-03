# Detecting diseases > 2022-11-12 10:18am
https://universe.roboflow.com/artificial-intelligence-82oex/detecting-diseases

Provided by a Roboflow user
License: CC BY 4.0

Beans, Strawberry and Tomato diseases - v1 2022-09-01
==============================

This dataset was exported via roboflow.com on Sep 2, 2022 

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 5494 images.
Diseases are annotated in YOLO v7 PyTorch format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)

No image augmentation techniques were applied.

Classes:
	Strawberry
		'Angular Leafspot'
		'Anthracnose Fruit Rot'
		'Blossom Blight'
		'Gray Mold'
		'Leaf Spot'
		'Powdery Mildew Fruit'
		'Powdery Mildew Leaf'
	Tomato
		'disease'
		'leaf mold'
		'spider mites'
	Bean
		'ALS'
		'Bean Rust'

