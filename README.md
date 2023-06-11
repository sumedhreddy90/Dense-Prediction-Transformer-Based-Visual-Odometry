# Visual-Transformers-Mono-Odometry
In this project, we aim to develop a transformer-based model architecture for visual
odometry(VO) that can accurately estimate the position and orientation of a robot using
images as input. To achieve this, we will first collect the dataset and preprocess the
image sequences and then implement and train the proposed model architecture.
The performance of the model will be evaluated and based on the setbacks of the
pre-trained model, we will fine-tune it in other scenes. This deep-learning approach
to visual odometry improves the accuracy and reliability of the systems across
various applications.

## Team Members
1. Hritvik Choudhari
2. Sumedh Reddy Koppula
3. Ashutosh Reddy Atimyala
4. Mohammed Maaruf Vazifdar
5. Venkata Sairam Polina

## Approach
In our research, we aim to address the challenge of scale recovery in monocular systems. To do so, we will leverage the depth map estimated by a deep learning technique, specifically a transformer-based network.

<p align="center">
<img src="https://github.com/Hritvik-Choudhari0411/visual-transformers-mono-odometry/blob/main/Final%20project%20results/dpt-vo.png" width="800" height="400"/>
</p>

## Architecture
#### Part 1 - Dense Prediction
- Embedded Phase: We begin by extracting non-overlapping patches from the input image utilizing a ResNeXT101 feature extractor to generate tokens.
- Processing Tokens for feeding into Transformers: These tokens are enhanced with positional and readout embeddings and routed through several transformer stages. 
- Reassemble Phase: Tokens from several stages are reassembled into an image-like representation at many resolutions and merged using fusion modules, which build a fine-grained prediction gradually. 
- Fusing Feature Maps: The feature maps are upsampled using residual convolutional units in the fusion blocks. Our architecture leverages fine tuned modified version of hybrid Dense Prediction Transformer (DPT) model on KITTI odometry dataset.

#### Part 2 - Visual Odometry using scale estimation
- Feature detection and matching: Used Accelerated Segment Test (FAST) corner detection algorithm for feature detection.Used iterative Lucas-Kanade method for feature Matching.
- Scale: We estimated the relative scale in MVO by using the depth from module 1 and aligning it with the triangulated depth to generate the scale, which is obtained by a RANSAC regressor with a depth ratio vector as input.

ViT-DPT architecture
<p align="center">
<img src="https://github.com/Hritvik-Choudhari0411/visual-transformers-mono-odometry/blob/main/Final%20project%20results/architecture.png" width="800" height="300"/>
</p>

VO result plot
<p align="center">
<img src="https://github.com/Hritvik-Choudhari0411/visual-transformers-mono-odometry/blob/main/Final%20project%20results/plot_02.png" width="500" height="400"/>
</p>

## Results
Overall, our visual odometry model achieved good accuracy on the KITTI dataset, with low errors on all evaluation metrics. This demonstrates the effectiveness of our approach and the importance of accurate depth maps for visual odometry estimation.

- Depth estimation using DPT
<p align="center">
<img src="https://github.com/Hritvik-Choudhari0411/visual-transformers-mono-odometry/blob/main/Final%20project%20results/520.png" width="600" height="200"/>
</p>
<p align="center">
<img src="https://github.com/Hritvik-Choudhari0411/visual-transformers-mono-odometry/blob/main/Final%20project%20results/521.png" width="600" height="200"/>
</p>

- Visual Odometry metrices obtained
<p align="center">
<img src="https://github.com/Hritvik-Choudhari0411/visual-transformers-mono-odometry/blob/main/Final%20project%20results/table22.png" width="500" height="400"/>
</p>

<p align="center">
<img src="https://github.com/Hritvik-Choudhari0411/visual-transformers-mono-odometry/blob/main/Final%20project%20results/trans_err_02_page-0001.jpg" width="500" height="400"/>
</p>
<p align="center">
<img src="https://github.com/Hritvik-Choudhari0411/visual-transformers-mono-odometry/blob/main/Final%20project%20results/rot_err_02_page-0001.jpg" width="500" height="400"/>
</p>
