<div align = "center">

![Binary1.png](Thesis%20Resources%2FImagesTemp%2FBinary1.png)

</div>


# Project Title

An Effective Method for the Recognition and Verification of 
Bangladeshi Vehicle Digital Number Plates.

---

## Table of Contents

1. [Description](#description)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Execution Step by Step](#execution-step-by-step)
6. [Folder Structure](#folder-structure)



---

## Description

This project is an image processing pipeline that performs various operations on input images. It includes steps for image rotation, feature extraction, and character segmentation. The pipeline aims to enhance and analyze images, making it suitable for tasks such as text recognition, image enhancement, and more. With a clear folder structure and usage instructions, it offers a convenient way to process images for various applications.

---

## Prerequisites

Project Folder should have this basic needs to execute 
- Python
- OpenCV
- NumPy
- scikit-image

---

## Installation

First Open a Python Project in Pycharm. Then install this package one by one. Wait for some time until all package are
installed successfully.
```bash
pip install opencv-python
pip install numpy
pip install scikit-image  
```

---

## Usage

Explain how to use your code step by step. Include code examples and provide clear instructions for running the code. You can use markdown code blocks for code snippets:

```python
# Step 1: Rotation
python Step_1_Rotation.py

# Step 2: Extraction
python Step_2_Extraction.py

# Step 3: Character Segmentation
python Step_3_Character Segmentation.py
```


## Execution Step by Step

#### Step - 1 : Select/Paste Your Number-Plate Image in "Input Image" Folder

![Image2.png](Input%20Image%2FImage2.png)

#### Step - 2 : Open and Run "Step_1_Rotation.py"
- [Optional] If you added new image in "Input Image" Folder. Then Change it location in "Step_1_Rotation.py"
```python
# Change File Location Here
filename = './Input Image/Image2.png'
```

#### Step - 3 : "Step_1_Rotation.py" will all rotation process and save those images in "Step_1_Rotation_Result" Folder
  - Checkout the folder to see the results after doing rotation process

![tillFinal.png](Thesis%20Resources%2FTilt%20Correction%2FtillFinal.png)


#### Step - 4 : Open and Run "Step_2_Extraction.py"

- All extraction process executes and save those images in "Step_2_Extraction_Result" Folder
- Checkout the folder to see the results after doing extraction process


![extraction.png](Thesis%20Resources%2FExtraction%2Fextraction.png)



#### Step - 5 : Open and Run "Step_3_Character Segmentation.py"

- All segmentation process executes and save those images in "Step_3_CharacterSegmentation_Result" Folder
- Checkout the folder to see the results after doing segmentation process

![CSbasic - Copy.png](Thesis%20Resources%2FSegmentaion%20of%20Character%2FCSbasic%20-%20Copy.png)
![CSbasic.png](Thesis%20Resources%2FSegmentaion%20of%20Character%2FCSbasic.png)
---


## Folder Structure


- `Input Image/`: Folder containing input images.
- `Step_1_Rotation_Result/`: Folder for saving intermediate images in Step 3.
- `Step_2_Extraction_Result/`: Folder for saving intermediate images in Step 4.
- `Step_3_CharacterSegmentation_Result/`: Folder for saving intermediate images in Step 5.

---

