from biosppy.signals import ecg

def process_ecg(signal, fs=360):
    result = ecg.ecg(signal=signal, sampling_rate=fs, show=False)
    return result['filtered'], result['rpeaks'], result['heart_rate']
