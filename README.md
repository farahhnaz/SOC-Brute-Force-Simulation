# SOC Detection Lab: Brute-Force Simulation

## Project Overview

This project simulates SSH authentication activity for a cybersecurity detection lab. It generates synthetic Linux-style authentication logs to represent normal login activity and a simulated SSH brute-force attack.

## Objectives

- Generate 50 successful SSH login entries.
- Generate 10 consecutive failed SSH login entries.
- Use a single attacker IP address: `192.168.1.100`.
- Create a Linux-style `auth.log` file for future security monitoring and detection.

## Technologies Used

- Python 3
- Visual Studio Code
- Git and GitHub

## Project Files

| File | Description |
|---|---|
| `generate_logs.py` | Python script that generates the authentication logs. |
| `auth.log` | Generated synthetic SSH authentication log containing 60 entries. |

## How to Run

1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the integrated terminal.
4. Execute: py generate_logs.py
5. The script generates `auth.log` in the project directory.

## Verification

The generated log file contains:

- 60 total authentication entries.
- 50 successful SSH login entries.
- 10 consecutive failed SSH login entries.
- All 10 failed attempts originate from `192.168.1.100`.

## Security Note

All authentication events and IP addresses in this project are synthetic. No real systems were targeted, and no actual brute-force attack was performed.

## Purpose

The generated authentication logs will be used in the next stage of the SOC detection lab to test SSH brute-force detection using Wazuh.