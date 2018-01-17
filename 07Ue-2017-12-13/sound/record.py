"""Usage: record.py -t # [-h]
            -t #: Time in seconds to be recorded (default: 2)
              -h: Print this help message
     -o filename: Write output to filename.raw and filename.dat (default: record16)
  RESULT:
   Records t seconds from your default sound card.
   With a sample rate of 22050 Hz in format S16LE (16 bit int little endian)  
"""
import sys
import time
import getopt
import alsaaudio
import numpy as np
from math import *
from getopt import *
import matplotlib.pyplot as plt
#from scipy.io import wavfile as wav	

if __name__ == '__main__':
  opt=getopt(sys.argv[1:], "t:o:h")

  RATE = 22050
  card = 'default'
  out_filename='record16'
  tr=2.
  for o in opt[0]:
     if o[0]=='-t': tr=float(o[1])
     if o[0]=='-o': out_filename=o[1]
     if o[0]=='-h': print __doc__; sys.exit(0)


  inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, card)
  inp.setchannels(1)
  inp.setrate(RATE)
  inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
  inp.setperiodsize(160)


  iwav = ""

  t0 = time.time()
  while time.time()-t0<tr:
    l, data = inp.read()
    #print len(data)
    if l:
      iwav += data
    time.sleep(.00005)

  
  fiwav = open(out_filename+".raw", "w")
  fiwav.write(iwav)
  fiwav.close()

  rec_arr=[]

  fidat = open(out_filename+".dat", "w")
  for i in range(0, len(iwav) / 2):
    lb = ord(iwav[2*i])
    hb = ord(iwav[2*i+1])
    f = (hb << 8) | lb
    
    if hb > 127:
      f -= 65536
    rec_arr.append(f)
    print >> fidat, f
  
  fidat.close()


  Fs = 22050  # sampling rate
  Ts = 1.0/Fs
  t = np.arange(0,1,Ts) # time vector

  ff = 5;   # frequency of the signal
 

  n = len(rec_arr) # length of the signal
  k = np.arange(n)
  T = n/Fs
  frq = k/T # two sides frequency range
  frq = frq[range(n/2)] # one side frequency range

  #Y = np.fft.fft(y)/n # fft computing and normalization
  #Y = Y[range(n/2)]


  #plt.plot(rec_arr)
  #fidat = open(out_filename+".dat", "r")
  sp = np.fft.fft(rec_arr)/len(rec_arr)
  sp=sp[range(len(rec_arr)/2)]
  #plt.plot(np.abs(sp))
  
  fig, ax = plt.subplots(2, 1)
  ax[0].plot(rec_arr)
  ax[0].set_xlabel('Time')
  ax[0].set_ylabel('Amplitude')
  ax[1].plot(frq,abs(sp),'r') # plotting the spectrum
  ax[1].set_xlabel('Freq (Hz)')
  ax[1].set_ylabel('|Y(freq)|')
  plt.show()
"""
  rate, data = wav.read('record16.raw')
  fft_out = fft(data)
  #matplotlib inline
  plt.plot(data, np.abs(fft_out))
  plt.show() 
"""  








