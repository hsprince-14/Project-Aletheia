# Project Aletheia: Spectral Deepfake Forensics 👁️🔍
**Exposing AI Artifacts via Discrete Fourier Transform (DFT)**

## 📌 Project Overview
Project Aletheia is a digital forensic tool designed to detect synthetic imagery. While modern Generative AI (GANs/Diffusion) produces visually perfect results, they often leave behind invisible mathematical "fingerprints" in the frequency domain. This project utilizes Fast Fourier Transform (FFT) to expose these spectral anomalies.

## 🔬 The Science: Frequency Domain Analysis
Unlike standard detection that looks at pixels, Aletheia looks at **frequencies**. 
* **Natural Entropy:** Real-world photos have a chaotic, smooth frequency distribution.
* **Artificial Grids:** AI-generated images often contain high-frequency "checkerboard artifacts" caused by upsampling layers. These appear as sharp, unnatural spikes in the spectral heatmap.

## 🛠️ Technical Implementation
The engine is built on Python 3.12+ and uses:
- **NumPy:** For high-performance matrix operations and FFT calculation.
- **OpenCV:** For grayscale preprocessing and signal acquisition.
- **Matplotlib:** To generate high-fidelity forensic heatmaps (using the 'inferno' colormap for clarity).

## 🚀 How to Use (Quick Start)

### 1. Requirements
Ensure you have the stable dependencies installed:
```bash
pip install opencv-python matplotlib numpy

2. File Setup
To run the analysis, place your target images in the root directory of this project:

Rename your real photo to: real.jpg

Rename your AI-generated photo to: fake.jpg

3. Execution
Run the forensic analyzer through your terminal:

4. Run
python aletheia.py
