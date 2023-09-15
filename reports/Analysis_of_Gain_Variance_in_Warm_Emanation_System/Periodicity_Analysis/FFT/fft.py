    """
    # Plot the Periodicity Determination Raw Data
    plt.figure('FFT Periodicity Determination Run {}'.format(runNum))
    plt.plot(
        timeInHours, 
        np.abs(peaksFFT_Y[:halfPeaksFFT])/halfPeaksFFT
    )
    plt.xlabel('Period ($hours$)')
    plt.title('FFT Periodicity Determination Run {}'.format(runNum))
    plt.grid()

    # Reconstructed Signal 
    peaksFFT_ReconstructedSignal = np.fft.ifft(peaksFFT_Y)

    # Plot the Inverse FFT of the Raw Data
    plt.figure('Inverse Fourier Transform of Raw Data Peaks Run {}'.format(runNum))
    plt.plot(
        peaksFFT_XValue, 
        peaksFFT_ReconstructedSignal
    )
    plt.xlabel('Time')
    plt.ylabel('Signal')
    plt.title('Inverse Fourier Transform of Raw Data Peaks Run {}'.format(runNum))
    plt.grid()
    
    # Plot the FFT of the Raw Data
    plt.figure("Fast Fourier Transform Run {}".format(runNum))
    plt.title("Fast Fourier Transform Run {}".format(runNum))
    plt.plot(
        peaksFFTFrequencies,
        np.abs(peaksFFT_Y)
    )
    plt.xlabel("Frequency ($Hz$)")
    plt.ylabel("FFT Amplitude")
    plt.grid()
    """
    
        """
    # Plot the FFT of the Smoothed Data
    plt.figure("Fast Fourier Transform after Savitzky-Golay Filter Run {}".format(runNum))
    plt.title("Fast Fourier Transform after Savitzky-Golay Filter Run {}".format(runNum))
    plt.plot(
        peaksFFTFrequencies,
        peaksFFT_YSavGol
    )
    plt.xlabel("Frequency ($Hz$)")
    plt.ylabel("FFT Amplitude")
    plt.grid()
    """
    
        """
    halfPeaksFFT = numPeaksFFT//2
    peaksFFTSampleRate = 1.0 / (peaksFFT_XValue[1] - peaksFFT_XValue[0])
    peaksFFTFrequencies = np.fft.fftfreq(numPeaksFFT, d=1.0 / peaksFFTSampleRate)
    peaksFFTPeriod = 1 / peaksFFTFrequencies
    peaksFFTPeriodHours = peaksFFTPeriod / 3600
    oneSidedFrequency = peaksFFTFrequencies[:halfPeaksFFT]
    timeInHours = 1/oneSidedFrequency / (60*60)
    """
    
        """
    # The following code will perform the Fast Fourier Transform on the Y values
    peaksFFT_Y = fft(peaksFFT_YValue)
    peaksFFT_YSavGol = fft(peaksData_YSavGol)
    """
