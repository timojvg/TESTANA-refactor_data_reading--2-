import numpy as np
import scipy as sp
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
import statsmodels

from read_data.read_acc_data import get_acceleration_data

plt.ion()


def butter_lowpass_filter(data, cutoff, fs, order=5):
    def butter_lowpass():
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        return b, a

    b, a = butter_lowpass()
    y = filtfilt(b, a, data)
    return y


def filter_all_data(data, cutoff=200, fs=12500, order=5):
    for key in data.keys():
        for j in range(1, data[key].shape[1]):
            data[key].loc[:, list(data[key])[j]] = butter_lowpass_filter(data[key].loc[:, list(data[key])[j]],
                                                                         cutoff, fs, order)
    return data


def perform_fourier_transform(t, y):
    t, y = np.array(t), np.array(y)
    A_fft = np.abs(sp.fft.fft(y))
    f_fft = sp.fft.fftfreq(len(A_fft), d=(t[1] - t[0]))
    return f_fft, A_fft

def autocovariance(lists):


if __name__ == "__main__":
    cutoff = 200
    acc_dict = filter_all_data(get_acceleration_data("../Dataset"), cutoff=cutoff)

    segment_start = 10000
    segment_end = 20000
    acc_segment_dict = {}
    for index in acc_dict:
        acc_segment_dict[index] = acc_dict[index].iloc[segment_start:segment_end]


    # f_fft, A_fft = perform_fourier_transform(acc_dict["0"]["t"][100000:200000], acc_dict["0"]["U8_z"][100000:200000])
    #
    # fig, axs = plt.subplots(1, 2)
    # axs[0].plot(f_fft, A_fft)
    # axs[0].set_xlim(0, cutoff)
    # axs[1].plot(acc_dict["0"]["t"][0:10000], acc_dict["0"]["U8_z"][0:10000])
    plt.show()
