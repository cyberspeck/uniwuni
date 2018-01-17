"""Usage: play.py -t # [-h]
            -s sin|ramp|noise play either a sinus or a ramp or noise
            -t # Time in seconds to be played (default: 5)
            -f # Frequency in Hz (default: 440)
            -d # Frequency range for ramp (default: 8000)
            -a # Amplitude (default: 30000)
            -h: Print this help message
  RESULT:
   Play a sound t seconds at your default sound card.
   With a sample rate of 22050 Hz in format S16LE (16 bit int little endian)  
"""
import sys
import time
import getopt
import alsaaudio
import numpy as np
import matplotlib.pyplot as plt
#from scipy.io import wavfile as wav
#from scipy.fftpack import fft
from math import *
from getopt import *
from random import *


def make_ramp(f0=30.,df=2000., ampl=100000., rate=22050,length=5):
  a = 2. * pi * f0/rate              
  n = int(rate * length)
  df_step = df / rate
  wav=''
  for i in range(0, n):
    f = int(ampl*sin((a+(i*df_step/rate))*i))
    wav += chr(f & 0x00FF) + chr((f & 0xFF00) >> 8)
  return wav
# -------------------------------------
def make_sin(f0=100.,ampl=500000.,rate=22050,length=5.):
  a = 2. * pi * f0/rate             
  n = int(rate * length)
  wav=''
  for i in range(0, n):
    f = int(ampl*sin(a*i))
    wav += chr(f & 0x00FF) + chr((f & 0xFF00) >> 8)
  return wav
# ------------------------------------------
def make_noise(ampl=30000,rate=22050,length=5.):

  n = int(rate * length)
  df_step = df / rate
  wav=''
  for i in range(0, n):
    f = int((np.random.rand()*2-1)*ampl)
    wav += chr(f & 0x00FF) + chr((f & 0xFF00) >> 8)
  return wav
# ------------------------------------------
def make_Rechteck(ampl=30000,rate=22050,length=5.):
  print ("Rechteck")
  liste=[]
  N=[]
  f=int(0)
  n = int(rate * length)
  #for i in range(n):
   # N.append(i)		
  #N=np.arrange(n)
  wav=''
  for i in range(0, n):
    if i%10 < 5:
      f=1500
    else:
      f=-1500
    wav += chr(f & 0x00FF) + chr((f & 0xFF00) >> 8)
    liste.append(f)
  #plt.plot(N, liste)
  #plt.show()
  return wav
# -------------------------------------
def make_Dreieck(f0=1000.,ampl=1000,rate=22050,length=5.):
  print('Dreieck')
  liste=[]
  N=[]            
  n = int(rate * length)
  for i in range(n):
    N.append(i)
  wav=''
  delta_t=200
  for i in range(0, n):
    if i%delta_t < (delta_t/2):
      f = int((i%(delta_t/2))*ampl)
    else:
      f=int(((delta_t/2)-i%(delta_t/2))*ampl)
    print f
    liste.append(f)
    wav += chr(f & 0x00FF) + chr((f & 0xFF00) >> 8)
  plt.plot(N, liste)
  plt.show()
  return wav
# ------------------------------------------

if __name__ == '__main__':
  opt=getopt(sys.argv[1:], "s:f:d:t:a:h")

  rate = 22050
  crd = 'default'
  sound= 'sin'
  freq=440.
  df=8000.
  tr=5.
  ampl=30000
  for o in opt[0]:
     if o[0]=='-t': tr=float(o[1])
     if o[0]=='-s': sound=o[1]
     if o[0]=='-f': freq=float(o[1])
     if o[0]=='-d': df=float(o[1])
     if o[0]=='-a': ampl=float(o[1])
     if o[0]=='-h': print __doc__; sys.exit(0)

  type_d={"sin": {"func": make_sin, "args":{"f0":freq,"ampl":ampl,"rate":22050,"length":tr}},
         "ramp": {"func": make_ramp,"args":{"f0":freq,"df":df,"ampl":ampl,"rate":22050,"length":tr}},
         "noise": {"func": make_noise,"args":{"ampl":ampl,"rate":22050,"length":tr}},
         "Rechteck": {"func": make_Rechteck,"args":{"ampl":ampl,"rate":22050,"length":tr}},
		 "Dreieck": {"func": make_Dreieck,"args":{"ampl":ampl,"rate":22050,"length":tr}}	 }
  wave=type_d[sound]["func"](**type_d[sound]["args"])

  # Open the device in playback mode. 
  out = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, card=crd)
  # Set attributes: Mono, 44100 Hz, 16 bit little endian frames
  out.setchannels(1)
  out.setrate(rate)
  out.setformat(alsaaudio.PCM_FORMAT_S16_LE)
  out.setperiodsize(160)

  i = 0
  l= len(wave)
  while i < l:
       i+=2*out.write(wave[i:i+320])



"""
  for i in range(n/4, n/2):
    f = int(ampl*sin(150*i))
    wav += chr(f & 0x00FF) + chr((f & 0xFF00) >> 8)
  for i in range(n/2, 3*n/4):
    f = int(10000+ampl*sin(150*i))
    wav += chr(f & 0x00FF) + chr((f & 0xFF00) >> 8)
  for i in range(3*n/4, n):
    f = int(ampl*sin(150*i))
    wav += chr(f & 0x00FF) + chr((f & 0xFF00) >> 8)
"""
"""
    for j in range(1,7,2):

      f=f+int(ampl*sin(j*100*i)/j)
      #print i, j, f, sin(j*1000*i)
    #f = int((ampl*sin(150*i)
    #print ('Gesamt' ,f, j)
    liste.append(f)
"""



