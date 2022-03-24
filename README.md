# HappyPet AI
<div align="center">
  <img alt="header" width="75%" src="media/jetson-nano-dev-kit-agustus-2020-page_banner_epsindo_w2-1.jpg"/>
</div>

<div align="center">PetBowl AI Computer Vision  Nvidia Jetson Nano </div>

## Motivation

A few months ago my girlfriend adopted a cat named TOM. I currently have a remote job, I spend the day in an office in the apartment, sometimes the cat would come towards me and start meowing, well it was because his food bowl was empty.
I was also thinking about what project to do to obtain the Nvidia certification, two other worlds joined and it occurred to me to train a computer vision algorithm which would detect when Tom's bowl was empty, So he is a happy cat without hunger.

# Project Overview

This is a detection system which will be carried out in different phases, one of the first is the training of the computer vision model for the detection of the empty or full bowl. The hardware used is the Nvidia Jetson Nano 4GB, which is connected to an Ezviz Wireless Wifi 1080P IP Camera (RTSP Protocol) which is installed viewing the food bowl.

This project uses:

Hardware

<li>Laptop</li>
<li>Nvidia Jetson Nano 4GB</li>
<li>Logitech Web 720P or Ezviz C3A</li>
<li>Pet Bowl</li>
<li>Pet Food</li>


Software

<li>Windows</li>
<li>Ubuntu/JetPack 4.6</li>
<li>LabelImg for Windows</li>
<li>Anaconda for Windows</li>
<li>Jetson-inference library</li>


## First steps

In the first instance, the computer vision algorithm was trained to detect if the bowl is empty or full.
One of the first jobs I did was to collect the data, I took about 90 Photos of the empty bowl and another 90 with the full bowl.
The annotations of the images are made with the Anaconda + LabelImg tool using the Windows operating system

First Install Anaconda (Link) https://www.anaconda.com/products/individual#download

Second follow steps of Labelimg (Link ) https://github.com/tzutalin/labelImg

Once Anaconda is installed, run it and clone the LabelImg repository.
```bash
$ git clone https://github.com/tzutalin/labelImg
```
Once the repository is downloaded, run the Labelimg installation instructions
```bash
conda install pyqt=5
conda install -c anaconda lxml
pyrcc5 -o libs/resources.py resources.qrc
python labelImg.py
python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

Inside the labelImg folder, you must create the data set with the following folders Project name inside the following folder Annotations / ImageSets / JPEGImages subfolders.
Inside the JPEGImages layer you should save all the images you want to tag.
<img alt="header"  src="media/Captura .png"/>

