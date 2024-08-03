# PLL_Python
The PLL block models a Phase Lock Loop (PLL) closed-loop control system, which tracks the 
frequency and phase of a sinusoidal signal by using an internal frequency oscillator. The control 
system adjusts the internal oscillator frequency to keep the phase difference to 0. 
The figure shows the internal diagram of the PLL.
![image](https://github.com/user-attachments/assets/03887d3a-f638-4ae2-a932-1f857e8e56f6)

Locked Range: The locked range of a PLL circuit refers to the range of input frequencies over 
which the PLL can maintain phase lock with the reference signal. It is typically specified as a 
frequency range centered around the PLL's free-running frequency. The locked range depends 
on the loop filter design, phase detector characteristics, and VCO tuning range. 

Capture Range: The capture range of a PLL circuit refers to the range of input frequencies over 
which the PLL can acquire phase lock with the reference signal from an unlocked state. It is 
typically larger than the locked range and is determined by the PLL's loop dynamics and phase 
detector sensitivity. The capture range is important for ensuring that the PLL can quickly lock 
onto the input signal when initially powered on or when the input frequency changes abruptly.

![image](https://github.com/user-attachments/assets/ac3dfd40-a1d6-4d2f-9ae2-c16de4854415)
![image](https://github.com/user-attachments/assets/bf346c72-b581-46ca-9f0c-400e7121ef24)

