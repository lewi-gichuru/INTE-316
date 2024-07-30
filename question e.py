import numpy as np
import matplotlib.pyplot as plt

def analyze_signal_fft(f1, f2, sampling_rate, duration):
    # Generate the time vector
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    
    # Generate the signal s(t)
    s_t = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    
    # Compute the FFT
    N = len(s_t)
    fft_values = np.fft.fft(s_t)
    fft_frequencies = np.fft.fftfreq(N, 1 / sampling_rate)
    
    # Take the magnitude of the FFT values
    fft_magnitude = np.abs(fft_values)
    
    # Only take the positive frequencies
    pos_mask = fft_frequencies >= 0
    fft_frequencies = fft_frequencies[pos_mask]
    fft_magnitude = fft_magnitude[pos_mask]
    
    # Plot the signal
    plt.figure(figsize=(12, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(t, s_t)
    plt.title("Time Domain Signal")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    
    # Plot the FFT magnitude spectrum
    plt.subplot(2, 1, 2)
    plt.plot(fft_frequencies, fft_magnitude)
    plt.title("Frequency Domain Signal")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.grid()
    
    plt.tight_layout()
    plt.show()

# Parameters
f1 = 50  # Frequency 1 in Hz
f2 = 120  # Frequency 2 in Hz
sampling_rate = 1000  # Sampling rate in Hz
duration = 1  # Duration in seconds

# Analyze the signal
analyze_signal_fft(f1, f2, sampling_rate, duration)
