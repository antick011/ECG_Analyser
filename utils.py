import matplotlib.pyplot as plt

def save_ecg_plot(signal, rpeaks, path="output/ecg_plot.png"):
    plt.figure(figsize=(10, 3))
    plt.plot(signal, label="ECG Signal", color='black')
    plt.scatter(rpeaks, signal[rpeaks], color='red', label='R-peaks')
    plt.title("ECG with R-Peaks")
    plt.legend()
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
