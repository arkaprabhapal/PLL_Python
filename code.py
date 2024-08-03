import numpy as np 
import matplotlib.pyplot as plt 
# Define simulation parameters 
f_ref = 1e3  # Hz, reference frequency 
f_vco_min = 0.8e3  # Hz, minimum VCO frequency 
f_vco_max = 1.2e3  # Hz, maximum VCO frequency 
kp = 1  # proportional gain of phase detector 
ki = 0.1  # integral gain of phase detector 
f_sim = 10e3  # Hz, simulation frequency 
# Define time vector 
t = np.arange(0, 1, 1/f_sim) 
# Initialize error voltage and VCO frequency 
error_voltage = 0 
f_vco = f_vco_min
# Simulate PLL operation 
phase_ref = 2*np.pi*f_ref*t  # reference phase 
phase_vco = 2*np.pi*f_vco*t  # VCO phase 
# Lists to store signals 
vco_in = [] 
vco_out = [] 
error_out = [] 
for i in range(len(t)): 
# Phase error 
phase_error = phase_ref[i] - phase_vco[i] 
# Update error voltage (low-pass filter for noise reduction) 
error_voltage = error_voltage + ki * phase_error 
error_voltage = kp * phase_error + 0.9 * error_voltage  # with low-pass filtering 
# Update VCO frequency based on error voltage 
f_vco += error_voltage 
# Limit VCO frequency 
f_vco = max(f_vco_min, min(f_vco, f_vco_max)) 
# Update phase based on adjusted frequency 
phase_vco += 2*np.pi*f_vco*(t[++i] - t[i]) 
# Store signals 
vco_in.append(f_ref) 
vco_out.append(f_vco) 
error_out.append(error_voltage) 
# Plot results 
plt.figure(figsize=(10, 6)) 
plt.subplot(3, 1, 1) 
plt.plot(t, vco_in, label='Reference Frequency') 
plt.plot(t, vco_out, label='VCO Frequency') 
plt.xlabel('Time (s)') 
plt.ylabel('Frequency (kHz)') 
plt.legend() 
plt.subplot(3, 1, 2) 
plt.plot(t, error_out) 
plt.xlabel('Time (s)') 
plt.ylabel('Error Voltage') 
plt.subplot(3, 1, 3) 
plt.hist(error_out) 
plt.xlabel('Error Voltage') 
plt.ylabel('Frequency') 
plt.tight_layout() 
plt.show()
# Estimate locked and captured range 
locked_range = 2*np.pi / (kp*ki)  # rad/s 
captured_range = f_vco_max - f_vco_min  # Hz 
# Print results 
print("Locked Range:", locked_range/(2*np.pi), "Hz") 
print("Captured Range:", captured_range, "Hz")
