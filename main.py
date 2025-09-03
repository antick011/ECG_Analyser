from ecg_reader import load_ecg_csv
from ecg_processor import process_ecg
from ecg_metrics import calculate_metrics
from utils import save_ecg_plot
from report_generator import generate_report

# Step 1: Load ECG signal
signal = load_ecg_csv("data/ecg_sample.csv")

# Step 2: Filter and detect peaks
filtered, rpeaks, heart_rate = process_ecg(signal)

# Step 3: Save plot
save_ecg_plot(filtered, rpeaks)

# Step 4: Calculate metrics
metrics = calculate_metrics(rpeaks, fs=360, heart_rate=heart_rate)

# Step 5: Generate PDF report
generate_report(metrics, image_path="output/ecg_plot.png")

print("✅ ECG report generated at output/ecg_report.pdf")
