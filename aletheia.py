import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# ============================================================
# Project Aletheia
# Creator: Rezwan Hossain Prince
# License: Education & Research Usage Only
# ============================================================

def analyze_frequency_spectrum(image_path):
    """Load image and compute frequency spectrum"""
    print(f"[*] Analyzing Forensic Layer → {image_path}")

    img = cv2.imread(image_path, 0)
    if img is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)

    return img, magnitude_spectrum


def compute_grid_artifact_score(magnitude_spectrum):
    """
    Advanced grid artifact detection:
    1. Focuses on high-frequency regions where artifacts are most visible
    2. Uses directional analysis to detect grid patterns
    3. Normalizes scores for consistent comparison
    """
    rows, cols = magnitude_spectrum.shape
    crow, ccol = rows // 2, cols // 2

    # Create mask for high-frequency ring (20-50% from center)
    Y, X = np.ogrid[:rows, :cols]
    dist_from_center = np.sqrt((X - ccol) ** 2 + (Y - crow) ** 2)
    mask = np.logical_and(dist_from_center >= 0.2 * min(rows, cols),
                          dist_from_center <= 0.5 * min(rows, cols))

    # Extract high-frequency region
    high_freq = magnitude_spectrum * mask

    # Directional analysis for grid detection
    horizontal_score = 0
    vertical_score = 0

    # Analyze horizontal lines (vertical artifacts)
    for i in range(rows):
        if np.std(high_freq[i, :]) > np.mean(high_freq[i, :]) * 0.3:
            horizontal_score += 1

    # Analyze vertical lines (horizontal artifacts)
    for j in range(cols):
        if np.std(high_freq[:, j]) > np.mean(high_freq[:, j]) * 0.3:
            vertical_score += 1

    # Normalize score by image size
    total_pixels = rows * cols
    return (horizontal_score + vertical_score) / total_pixels * 1000


def generate_forensic_report(folder_path):
    print("\n🧠 Project Aletheia Initialized")
    print("🔬 Creator: Rezwan Hossain Prince\n")

    valid_ext = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")
    images = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(valid_ext)
    ]

    if len(images) != 2:
        raise ValueError("Folder must contain EXACTLY 2 images (1 real, 1 AI).")

    # Process both images and compute scores
    results = []
    for img_path in images:
        img, spec = analyze_frequency_spectrum(img_path)
        score = compute_grid_artifact_score(spec)
        results.append({
            "path": img_path,
            "image": img,
            "spectrum": spec,
            "score": score
        })
        print(f"  → {os.path.basename(img_path)}: Grid Score = {score:.2f}")

    # Sort by grid artifact score (higher = AI)
    results.sort(key=lambda x: x["score"], reverse=True)
    ai_result = results[0]
    real_result = results[1]

    # Verify detection confidence
    confidence = (ai_result["score"] - real_result["score"]) / ai_result["score"] * 100
    print(f"\n🔍 Detection Confidence: {confidence:.1f}%")
    print(f"  → AI Image: {os.path.basename(ai_result['path'])} (Score: {ai_result['score']:.2f})")
    print(f"  → Real Image: {os.path.basename(real_result['path'])} (Score: {real_result['score']:.2f})")

    output_path = os.path.join(folder_path, "Aletheia_Forensic_Report.png")

    # ============================
    # HIGH-RES FORENSIC FIGURE
    # ============================
    plt.style.use("default")
    fig, axs = plt.subplots(2, 2, figsize=(14, 14), dpi=300)

    # --- INPUT IMAGES ---
    axs[0, 0].imshow(real_result["image"], cmap="gray")
    axs[0, 0].set_title(
        "Input A: Organic Source (Real)",
        fontsize=14,
        color="green",
        pad=12
    )
    axs[0, 0].axis("off")

    axs[0, 1].imshow(ai_result["image"], cmap="gray")
    axs[0, 1].set_title(
        "Input B: Synthetic Source (AI)",
        fontsize=14,
        color="red",
        pad=12
    )
    axs[0, 1].axis("off")

    # --- FREQUENCY SPECTRUM ---
    axs[1, 0].imshow(real_result["spectrum"], cmap="inferno")
    axs[1, 0].set_title(
        "Spectral Analysis: Natural Noise Distribution",
        fontsize=12
    )
    axs[1, 0].axis("off")

    axs[1, 1].imshow(ai_result["spectrum"], cmap="inferno")
    axs[1, 1].set_title(
        "Spectral Analysis: Artificial Grid Artifacts detected",
        fontsize=12
    )
    axs[1, 1].axis("off")

    # --- FOOTER / ATTRIBUTION ---
    fig.text(
        0.5, 0.035,
        "Project Aletheia | Creator: Rezwan Hossain Prince | Education & Research Use Only",
        ha="center",
        fontsize=10
    )

    plt.tight_layout(rect=[0, 0.06, 1, 1])
    plt.savefig(output_path, dpi=300)
    plt.show()

    print(f"\n✅ Forensic Report Generated Successfully:")
    print(f"📁 {output_path}")
    print(f"  → Real Image: {os.path.basename(real_result['path'])}")
    print(f"  → AI Image: {os.path.basename(ai_result['path'])}")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    folder_path = input(
        "📂 Enter folder path containing 2 images (🧍 Real + 🤖 AI): "
    ).strip().strip('"')

    if not os.path.isdir(folder_path):
        print("❌ Error: Provided path is not a valid folder.")
    else:
        generate_forensic_report(folder_path)
