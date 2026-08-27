Network Traffic Guard and Automated Cut-Off
A Python-based security automation tool for Windows that continuously monitors network interface activity using psutil and automatically isolates the host system from the network upon detecting abnormal data exfiltration or suspicious traffic spikes.

Key Features
Real-time Traffic Monitoring: Tracks network interface bytes sent and received using system-level metrics.

Automated Threat Mitigation: Temporarily disables network access via the Windows netsh utility when threshold limits are breached.

Proactive Security Enforcement: Evaluates post-isolation traffic trends to issue emergency system restarts if threats persist.

Privilege Validation: Built-in administrator privilege check IsUserAnAdmin to ensure administrative system interaction.

Tech Stack and Requirements
Language: Python 3.x

Core Libraries: psutil, subprocess, ctypes, os, time

OS Support: Windows requires Administrator permissions to control network interface states

Configuration and Usage
Prerequisites
Ensure you have the psutil library installed:
pip install psutil

Execution
Run the script inside an Administrator-elevated command prompt or terminal:
python traffic_monitor.py

Parameters
Adjust configuration variables directly in traffic_monitor.py according to your environment:

TRAFFIC_THRESHOLD: Maximum byte limit allowed per interval default: 100 MB.

CHECK_INTERVAL: Monitoring frequency in seconds default: 10s.

ADAPTER_NAME: Exact name of the network interface to control default: "Wi-Fi".

Use Case Alignment
This tool addresses host-level automated response mechanisms in Cloud Security and DevSecOps pipelines, mirroring basic local Data Loss Prevention DLP behavior.
