import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, freqz

#Funkcja służąca wczytaniu danych z pliku ekg1.txt oraz ich wyswietlenia
def wczytaj_ekg1():
    data = np.loadtxt("ekg1.txt")
    N=data.shape[0]
    fs = 1000
    T=np.arange(N)/fs
    channel = 0
    plt.figure(figsize=(10,4))
    plt.plot(T,data[:,channel])
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("EKG1")
    plt.grid(True)
    plt.show()

#Funkcja służąca wczytaniu danych z pliku ekg100.txt oraz ich wyswietlenia
def wczytaj_ekg100():
    data = np.loadtxt("ekg100.txt")
    N=data.shape[0]
    fs = 360
    T=np.arange(N)/fs
    channel = 0
    plt.figure(figsize=(10,4))
    plt.plot(T, data)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("EKG100")
    plt.grid(True)
    plt.show()

#Funkcja służąca wczytaniu danych z pliku ekg_noise.txt oraz ich wyswietlenia
def wczytaj_ekg_noise():
    data = np.loadtxt("ekg_noise.txt")

    t = data[:, 0]
    signal = data[:, 1]

    plt.figure(figsize=(10,4))
    plt.plot(t, signal)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("EKG noise")
    plt.grid(True)
    plt.show()

def zadanie2():
    fs = 1000
    f = 50
    N = 65536
    t = np.arange(N)/fs
    signal = np.sin(2*np.pi*f*t)
    signal = np.fft.fft(signal)
    signal_mag = np.abs(signal)
    freq = np.fft.fftfreq(N, 1/fs)
    plt.figure(figsize=(10,4))
    plt.plot(freq[:N//2], signal_mag[:N//2])
    plt.xlabel("Frequency (Hz)")
    plt.title("Transformata Fouriera sinusoidy 50Hz")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True)
    plt.show()


    signal = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 60 * t)
    signal = np.fft.fft(signal)
    signal_mag = np.abs(signal)
    freq = np.fft.fftfreq(N, 1 / fs)
    plt.figure(figsize=(10, 4))
    plt.plot(freq[:N // 2], signal_mag[:N // 2])
    plt.xlabel("Frequency (Hz)")
    plt.title("Transformata Fouriera sumy sinusoid 50Hz i 60Hz")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True)
    plt.show()

    N = 1024
    t = np.arange(N) / fs
    signal = np.sin(2 * np.pi * f * t)
    signal = np.fft.fft(signal)
    signal_mag = np.abs(signal)
    freq = np.fft.fftfreq(N, 1 / fs)
    plt.figure(figsize=(10, 4))
    plt.plot(freq[:N // 2], signal_mag[:N // 2])
    plt.xlabel("Frequency (Hz)")
    plt.title("Transformata Fouriera sinusoidy 50Hz o dlugosci 1024")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True)
    plt.show()

    N = 65536
    fs = 200
    t = np.arange(N) / fs
    signal = np.sin(2 * np.pi * f * t)
    signal = np.fft.fft(signal)
    signal_mag = np.abs(signal)
    freq = np.fft.fftfreq(N, 1 / fs)
    plt.figure(figsize=(10, 4))
    plt.plot(freq[:N // 2], signal_mag[:N // 2])
    plt.xlabel("Frequency (Hz)")
    plt.title("Transformata Fouriera sinusoidy 50Hz o czestotliwosci probkowania 200Hz")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True)
    plt.show()

    fs = 1000
    f = 50
    N = 65536
    t = np.arange(N) / fs
    signal = np.sin(2 * np.pi * f * t)
    signal_fft = np.fft.fft(signal)
    signal_rec = np.fft.ifft(signal_fft)
    plt.figure(figsize=(10, 4))
    plt.plot(t[:1000], signal[:1000], label="oryginalny")
    plt.plot(t[:1000], signal_rec[:1000], '--', label="po IFFT")
    plt.legend()
    plt.title("Porównanie sygnału oryginalnego i po IFFT")
    plt.grid(True)
    plt.show()


def zadanie3():
    data = np.loadtxt("ekg100.txt")
    fs = 360
    N = len(data)
    t = np.arange(N) / fs
    plt.figure(figsize=(10, 4))
    plt.plot(t, data)
    plt.title("Sygnał EKG (czas)")
    plt.xlabel("Czas (s)")
    plt.ylabel("Amplituda")
    plt.grid(True)
    plt.show()
    fft_data = np.fft.fft(data)
    fft_mag = np.abs(fft_data)
    freq = np.fft.fftfreq(N, 1 / fs)
    half = N // 2
    plt.figure(figsize=(10, 4))
    plt.plot(freq[:half], fft_mag[:half])
    plt.title("Widmo amplitudowe EKG")
    plt.xlabel("Częstotliwość (Hz)")
    plt.ylabel("Amplituda")
    plt.grid(True)
    plt.show()
    rec_signal = np.fft.ifft(fft_data)
    rec_signal = np.real(rec_signal)
    plt.figure(figsize=(10, 4))
    plt.plot(t, data, label="oryginalny")
    plt.plot(t, rec_signal, '--', label="po IFFT")
    plt.legend()
    plt.title("Porównanie sygnałów")
    plt.grid(True)
    plt.show()
    diff = data - rec_signal
    plt.figure(figsize=(10, 4))
    plt.plot(t, diff)
    plt.title("Różnica sygnałów")
    plt.xlabel("Czas (s)")
    plt.ylabel("Błąd")
    plt.grid(True)
    plt.show()
    print("Maksymalny błąd:", np.max(np.abs(diff)))

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, freqz

def zadanie4():
    data = np.loadtxt("ekg_noise.txt")
    t = data[:, 0]
    signal = data[:, 1]

    fs = 360
    N = len(signal)

    plt.figure(figsize=(10, 4))
    plt.plot(t, signal)
    plt.title("Sygnał EKG z zakłóceniami (czas)")
    plt.xlabel("Czas (s)")
    plt.ylabel("Amplituda")
    plt.grid(True)
    plt.show()

    fft_data = np.fft.fft(signal)
    fft_mag = np.abs(fft_data) / N
    freq = np.fft.fftfreq(N, d=1/fs)
    half = N // 2

    plt.figure(figsize=(10, 4))
    plt.plot(freq[:half], 2 * fft_mag[:half])
    plt.title("Widmo amplitudowe sygnału EKG (z zakłóceniami)")
    plt.xlabel("Częstotliwość (Hz)")
    plt.ylabel("Amplituda")
    plt.grid(True)
    plt.show()

    fc_lp = 60
    wn_lp = fc_lp / (fs / 2)
    b_lp, a_lp = butter(4, wn_lp, btype='low')
    filtered_lp = filtfilt(b_lp, a_lp, signal)

    w, h = freqz(b_lp, a_lp, worN=8000)
    freqs = w * fs / (2 * np.pi)

    plt.figure(figsize=(10, 4))
    plt.plot(freqs, np.abs(h))
    plt.title("Charakterystyka filtra dolnoprzepustowego (60 Hz)")
    plt.xlabel("Częstotliwość (Hz)")
    plt.ylabel("Wzmocnienie")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(t, signal, label="przed filtracją", alpha=0.5)
    plt.plot(t, filtered_lp, label="po LPF", linewidth=2)
    plt.legend()
    plt.title("Sygnał po filtracji dolnoprzepustowej")
    plt.xlabel("Czas (s)")
    plt.ylabel("Amplituda")
    plt.grid(True)
    plt.show()

    fc_hp = 5
    wn_hp = fc_hp / (fs / 2)
    b_hp, a_hp = butter(4, wn_hp, btype='high')
    filtered = filtfilt(b_hp, a_hp, filtered_lp)

    w, h = freqz(b_hp, a_hp, worN=8000)
    freqs = w * fs / (2 * np.pi)

    plt.figure(figsize=(10, 4))
    plt.plot(freqs, np.abs(h))
    plt.title("Charakterystyka filtra górnoprzepustowego (5 Hz)")
    plt.xlabel("Częstotliwość (Hz)")
    plt.ylabel("Wzmocnienie")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(t, filtered_lp, label="po LPF", alpha=0.5)
    plt.plot(t, filtered, label="po HPF", linewidth=2)
    plt.legend()
    plt.title("Sygnał po filtracji pasmowej (5–60 Hz)")
    plt.xlabel("Czas (s)")
    plt.ylabel("Amplituda")
    plt.grid(True)
    plt.show()

    fft_filt = np.fft.fft(filtered)
    fft_filt_mag = np.abs(fft_filt) / N

    plt.figure(figsize=(10, 4))
    plt.plot(freq[:half], 2 * fft_filt_mag[:half])
    plt.title("Widmo po filtracji pasmowej")
    plt.xlabel("Częstotliwość (Hz)")
    plt.ylabel("Amplituda")
    plt.grid(True)
    plt.show()

    diff = signal - filtered

    plt.figure(figsize=(10, 4))
    plt.plot(t, diff)
    plt.title("Różnica sygnałów")
    plt.xlabel("Czas (s)")
    plt.ylabel("Amplituda")
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    print("Prosze podac numer zadania:")
    x = input()
    if x == "1":
        wczytaj_ekg1()
        wczytaj_ekg100()
        wczytaj_ekg_noise()
    if x == "2":
        zadanie2()
    if x == "3":
        zadanie3()
    if x == "4":
        zadanie4()


