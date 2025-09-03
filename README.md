# 🩺 ECG Signal Processing & PDF Report Generator (CLI-based Python Project)

## 📌 Project Overview

This is a command-line based Python project that reads an ECG signal from a `.csv` file, processes it to detect heartbeats (R-peaks), calculates key heart rate metrics, visualizes the signal, and automatically generates a clean PDF report containing the results and ECG plot.

It is designed to work **without any frontend**, and is perfect for biomedical analysis, educational demos, or back-end health tools.

---

## 🎯 Features

- ✅ Reads ECG waveform from `.csv`
- 🧼 Denoises signal using filtering
- ❤️ Detects R-peaks (heartbeats)
- 📈 Calculates metrics: BPM, R-R intervals, HRV
- 🖼 Saves ECG plot as `.png`
- 📄 Generates automatic `.pdf` report with stats + waveform

---

## 📂 Project Structure

ecg_analyzer/
│
├── data/
│ └── ecg_sample.csv # ECG input data (CSV format)
│
├── output/
│ ├── ecg_plot.png # ECG waveform with R-peaks
│ └── ecg_report.pdf # Final PDF report
│
├── main.py # Main execution script
├── ecg_reader.py # Loads and parses CSV ECG data
├── ecg_processor.py # Applies filters and detects R-peaks
├── ecg_metrics.py # Calculates BPM, HRV, R-R metrics
├── report_generator.py # Builds PDF report from data
├── utils.py # Helper for saving plots
├── requirements.txt # All required packages


---

## 🧠 How It Works

1. **Input:** Load ECG signal from CSV file
2. **Processing:** Filter the signal and detect R-peaks
3. **Analysis:** Compute heart rate and variability
4. **Plotting:** Save ECG waveform with peaks as `png`
5. **Reporting:** Create a final PDF report (`ecg_report.pdf`)

---

## 📦 Dependencies

Install required libraries in a virtual environment.

### `requirements.txt`

numpy
pandas
scipy
matplotlib
biosppy
fpdf
peakutils


---

## 🛠️ Setup Instructions (Run on Any System)

### 1. 📥 Clone or Copy the Project

```bash
git clone https://github.com/yourname/ecg_analyzer.git
cd ecg_analyzer


Or manually copy the folder.
🐍 Create a Virtual Environment

>>bash
python -m venv venv

Activate it:

Windows CMD: venv\Scripts\activate

PowerShell: .\venv\Scripts\Activate.ps1

Linux/macOS: source venv/bin/activate

📦 Install Dependencies

>>bash
pip install -r requirements.txt

🚀 Run the Project

>>bash
python main.py

You’ll see:

📈 output/ecg_plot.png — ECG waveform with R-peaks

📄 output/ecg_report.pdf — Auto-generated clinical-style report