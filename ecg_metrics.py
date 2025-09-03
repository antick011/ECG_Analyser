import numpy as np

def calculate_metrics(rpeaks, fs, heart_rate):
    rr_intervals = np.diff(rpeaks) / fs  # in seconds
    bpm = np.mean(heart_rate)
    return {
        "avg_bpm": bpm,
        "min_rr": np.min(rr_intervals),
        "max_rr": np.max(rr_intervals),
        "rr_std": np.std(rr_intervals)
    }
