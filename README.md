Technical Report Summary
Title:
Enhanced Canny Edge Detection and Vanishing Point Estimation for Intelligent Vehicles

Authors:
Rohit Raj Uppala, Murali Krishna Kaye, Mehrdad Zadeh

1. Objective
The project aims to overcome the limitations of traditional Canny edge detection in intelligent vehicles by introducing enhancements that improve edge accuracy, robustness in noisy environments, and enable reliable vanishing point estimation for camera calibration.

2. Key Innovations
Quaternion-Based Filtering: Preserves color details in edge detection.

Adaptive Thresholding: Automatically determines thresholds using gradient histograms.

Gravitational Field Intensity (GFI): Models pixel interaction like mass to detect subtle edges.

Scale Multiplication: Enhances edge consistency across resolutions.

Vanishing Point Detection: Employs DBSCAN and RANSAC to identify and refine perspective lines.

Homogeneous Transformation Estimation: Computes camera intrinsic and extrinsic matrices for calibration.

3. System Pipeline Overview
Image Preprocessing: Uses Non-Local Means filtering for denoising with minimal detail loss.

Gradient Estimation: Applies GFI for noise-resilient edge gradient calculation.

Enhanced Canny Pipeline: Incorporates adaptive thresholds, non-max suppression, and hysteresis.

Multiscale Fusion: Combines results across multiple Gaussian scales for structural integrity.

Line Detection & Vanishing Point Estimation: Uses Hough Transform + clustering to extract vanishing points.

Camera Calibration: Derives intrinsic and extrinsic parameters from vanishing points.

4. Results & Evaluation
Best Filtering Technique: Non-Local Means (highest PSNR: 27.01, best Canny Overlap: 0.988).

Edge Clarity: Enhanced over traditional Canny due to adaptive thresholding and GFI.

Vanishing Point Accuracy: Improved using DBSCAN + RANSAC to eliminate noise and outliers.

Visualization: Edge maps and vanishing clusters validated with OpenCV overlays.

5. Applications
Lane detection, obstacle localization, and road geometry analysis.

Real-time camera calibration in autonomous vehicles.

Foundations for 3D reconstruction and navigation tasks.

6. Future Scope
Integration with deep learning (e.g., HED, CNNs).

Real-time video frame consistency and embedded GPU acceleration.

Multi-camera support and extended datasets for highway, urban, and rural environments.

