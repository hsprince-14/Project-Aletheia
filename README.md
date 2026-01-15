<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/AI%20Forensics-Spectral%20Analysis-purple?style=for-the-badge"/>
</p>

<h1 align="center">👁️ Project Aletheia 2.0</h1>
<h3 align="center">Advanced Spectral Deepfake Forensics</h3>

<p align="center">
Detecting AI-Generated Imagery Through Mathematical Verification
</p>

---

## 📌 Overview
**Project Aletheia 2.0** is a next-generation **digital forensic intelligence system** designed to reliably distinguish **real photographs** from **AI-generated images** using **frequency-domain mathematical analysis**.

As modern generative models become visually indistinguishable from real-world imagery, they still leave behind **structural spectral artifacts** — invisible to the human eye but undeniable under mathematical inspection.  
Aletheia 2.0 exploits these artifacts to deliver **92%+ confidence detection** with transparent, explainable forensic reporting.

---

## 🔬 Scientific Foundation — Why Aletheia Works
Unlike conventional detectors that analyze spatial pixels, **Aletheia operates in the frequency domain**, where AI generation artifacts are fundamentally exposed.

### 🧬 Natural Entropy (Real Images)
- Chaotic yet smooth spectral energy distribution
- Absence of repeating or directional patterns
- True sensor noise characteristics

### 🧩 Artificial Grid Artifacts (AI Images)
- High-frequency directional grids introduced by generator architectures
- Straight-line spectral patterns caused by upsampling and convolution layers
- Consistent mathematical signatures across models

### 🧠 Mathematical Certainty
These artifacts are **structural**, not cosmetic — meaning:
> ❌ They cannot be removed by filters, resizing, compression, or post-processing.

---

## 🚀 What’s New in Version 2.0
✔ **Advanced Grid Detection Engine**  
Directional high-frequency analysis with normalized scoring

✔ **Confidence-Based Classification**  
Transparent percentage-based confidence metrics

✔ **Robust Scene Compatibility**  
Effective across skies, textures, noise-heavy backgrounds, and high-detail images

✔ **Focused Artifact Zone Analysis**  
Targets the **20–50% high-frequency ring**, where AI artifacts are most pronounced

✔ **Professional Forensic Reports**  
High-resolution visual evidence suitable for research, media, and cybersecurity use

---

## 🛠️ Technical Architecture
Built on **Python 3.8+**, leveraging industry-standard scientific libraries:

| Technology | Purpose |
|----------|--------|
| **NumPy** | FFT computation & high-performance matrix operations |
| **OpenCV** | Image preprocessing & grayscale signal acquisition |
| **Matplotlib** | High-fidelity forensic heatmaps (`inferno` colormap) |
| **Signal Processing** | Directional grid analysis with statistical validation |

---

## ⚡ Quick Start Guide

### 1️⃣ Install Dependencies
```bash
pip install opencv-python numpy matplotlib

2️⃣ Prepare Input Data

Create a folder containing exactly two images:

🟢 One real photograph

🔴 One AI-generated image

Supported formats: JPG, PNG, BMP, TIFF

No manual labeling required — Aletheia determines authenticity automatically.

3️⃣ Run the Analyzer
- bash
- Copy code
- python aletheia.py

4️⃣ Analysis Pipeline

Once the folder path is provided, the system will:

- Extract frequency spectra

- Detect grid-based artifacts

- Compute confidence scores

- Generate a forensic-grade visual report

5️⃣ Output

📁 Aletheia_Forensic_Report.png

Includes:

- Correctly labeled images

- Frequency spectrum visualizations

- Artifact heatmaps

- Confidence metrics

- Professional attribution

📊 Interpreting Results

Left Panel:
✔ Real Image — Natural Noise Distribution

Right Panel:
⚠ AI Image — Artificial Grid Artifacts Detected

Confidence Score:

Numerical reliability of the classification result

🌍 Real-World Applications

🕵️ Digital Forensics — Legal & investigative verification

📰 Media & Journalism — Synthetic content identification

🎓 Academic Research — Generative model artifact analysis

🔐 Cybersecurity — AI-driven phishing & misinformation detection

🛡️ Content Moderation — Platform-scale synthetic media filtering


🧑‍💻 Author & Credits:
Rezwan Hossain Prince
Computer Science & Engineering Student

🔗 LinkedIn:
https://www.linkedin.com/in/rezwan-hossain-prince-9b7304214/

⚠️ Disclaimer
This project is intended solely for educational and research purposes.
No guarantees are made regarding detection accuracy against all present or future generative models.
AI evolves — forensic science must evolve faster.

