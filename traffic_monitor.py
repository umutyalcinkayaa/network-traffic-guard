import ctypes
import os
import subprocess
import time
import psutil

TRAFFIC_THRESHOLD = 100 * 1024 * 1024
CHECK_INTERVAL = 10
WAIT_BEFORE_REBOOT = 1800
ADAPTER_NAME = "Wi-Fi"


def get_total_traffic():
    counters = psutil.net_io_counters(pernic=True)
    wifi_counters = counters.get(ADAPTER_NAME)
    if wifi_counters:
        return wifi_counters.bytes_sent + wifi_counters.bytes_recv
    else:
        print("No adapter found!")
        return 0


def disable_internet():
    subprocess.call(
        f'netsh interface set interface name="{ADAPTER_NAME}" admin=disabled',
        shell=True,
    )
    print("Internet access is lost")


def enable_internet():
    subprocess.call(
        f'netsh interface set interface name="{ADAPTER_NAME}" admin=enabled',
        shell=True,
    )
    print("Internet access is enabled")


def reboot_system():
    print(
        "Computer will be restarted for security reasons, please do not intervene!"
    )
    os.system("shutdown /r /t 0")


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


# Ana Çalıştırma Bloğu
if __name__ == "__main__":
    if not is_admin():
        print("Access authorization could not be obtained!")
        exit()

    print("Network is being monitored")

    base_traffic = get_total_traffic()

    while True:
        time.sleep(CHECK_INTERVAL)
        current_traffic = get_total_traffic()
        diff = current_traffic - base_traffic

        print(
            f"Increased network traffic, please do not visit suspicious sites!: {diff / (1024 * 1024):.2f} MB"
        )

        if diff > TRAFFIC_THRESHOLD:
            print(
                "Suspicious network access detected. Internet access is lost, access will remain disabled until network access returns to normal"
            )
            disable_internet()

            print("Waiting for 30 minutes")
            time.sleep(WAIT_BEFORE_REBOOT)

            after_wait = get_total_traffic()
            new_diff = after_wait - current_traffic

            if new_diff > TRAFFIC_THRESHOLD:
                reboot_system()
            else:
                print(
                    "Network access is back to normal, internet access is enabled. Have fun!"
                )
                enable_internet()
                base_traffic = get_total_traffic()