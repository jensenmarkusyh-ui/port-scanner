#!/usr/bin/env python3
import socket
import sys

def ask_int(prompt, default=None):
    try:
        s = input(prompt).strip()
        if s == "" and default is not None:
            return default
        return int(s)
    except ValueError:
        print("Invalid number. Exiting.")
        sys.exit(1)

print("Very basic port scanner (only use on hosts you are allowed to test).")

target = input("Enter hostname or IP: ").strip()
if not target:
    print("No host provided. Exiting.")
    sys.exit(1)

# Try resolve hostname early so we fail fast on bad names
try:
    host_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Could not resolve hostname. Check the address and try again.")
    sys.exit(1)

start = ask_int("Start port")
end = ask_int("End port")

timeout = 0.4
print(f"\nScanning {target} ({host_ip}) from {start} to {end} with timeout {timeout}s\n")

for port in range(start, end + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        result = s.connect_ex((host_ip, port))
        if result == 0:
            # try read banner (may be empty)
            banner = ""
            try:
                banner = s.recv(1024).decode(errors="ignore").strip()
            except Exception:
                banner = ""
            if banner:
                print(f"Port {port} — OPEN {banner.splitlines}")
            else:
                print(f"Port {port} — OPEN")
        else:
            print(f"Port {port} — CLOSED")
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        break
    except Exception as e:
        print(f"Port {port} — ERROR ({e})")
    finally:
        s.close()

print("\nDone.")
