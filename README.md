# Hydra-RTSP-Brute-Force-Script
Brute-force RTSP camera login credentials using Hydra with auto IP rotation.


##Python script to brute-force RTSP credentials on networked IP cameras using Hydra, with automatic IP rotation to help evade lockouts.

##how it works:
The script launches Hydra with the given username and password lists to target the RTSP service.
After every 2 failed attempts, the script switches the IP address of the attacking machine from a predefined list to avoid being blocked.

##Notes:
Must be on the same network as the target device.
Only works if IPs in the rotation list are valid and available.
Requires Hydra installed and accessible via command line.
IP switching assumes Linux and ifconfig availability.

##Disclamer
This code was created for educational and research purposes only.
