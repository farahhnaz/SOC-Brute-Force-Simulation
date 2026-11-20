
from datetime import datetime, timedelta
from pathlib import Path

# ==========================================
# SOC DETECTION LAB - BRUTE FORCE SIMULATION
# ==========================================

# Configuration
HOSTNAME = "ubuntu-server"
NORMAL_IP = "192.168.1.20"
ATTACKER_IP = "192.168.1.100"

SUCCESSFUL_ATTEMPTS = 50
FAILED_ATTEMPTS = 10

# Save auth.log in the same folder as this script
LOG_FILE = Path(__file__).resolve().parent / "auth.log"

# Starting timestamp
start_time = datetime.now() - timedelta(minutes=59)

log_entries = []

# ==========================================
# PART 1: GENERATE 50 SUCCESSFUL LOGINS
# ==========================================

for i in range(SUCCESSFUL_ATTEMPTS):

    timestamp = start_time + timedelta(minutes=i)

    formatted_time = (
        f"{timestamp.strftime('%b')} "
        f"{timestamp.day:2d} "
        f"{timestamp.strftime('%H:%M:%S')}"
    )

    process_id = 1200 + i
    port = 51000 + i

    log_line = (
        f"{formatted_time} {HOSTNAME} "
        f"sshd[{process_id}]: Accepted password "
        f"for ubuntu from {NORMAL_IP} port {port} ssh2"
    )

    log_entries.append(log_line)


# ==========================================
# PART 2: GENERATE 10 CONSECUTIVE FAILURES
# ==========================================

for i in range(FAILED_ATTEMPTS):

    timestamp = start_time + timedelta(
        minutes=SUCCESSFUL_ATTEMPTS,
        seconds=i * 8
    )

    formatted_time = (
        f"{timestamp.strftime('%b')} "
        f"{timestamp.day:2d} "
        f"{timestamp.strftime('%H:%M:%S')}"
    )

    process_id = 1300 + i
    port = 52000 + i

    log_line = (
        f"{formatted_time} {HOSTNAME} "
        f"sshd[{process_id}]: Failed password "
        f"for ubuntu from {ATTACKER_IP} port {port} ssh2"
    )

    log_entries.append(log_line)


# ==========================================
# PART 3: WRITE LOGS TO auth.log
# ==========================================

LOG_FILE.write_text(
    "\n".join(log_entries) + "\n",
    encoding="utf-8"
)


# ==========================================
# PART 4: VERIFY GENERATED LOGS
# ==========================================

successful_logs = [
    line for line in log_entries
    if "Accepted password" in line
]

failed_logs = [
    line for line in log_entries
    if "Failed password" in line
]

assert len(log_entries) >= 60
assert len(successful_logs) == 50
assert len(failed_logs) == 10

# Verify the final 10 lines are consecutive failures
assert all(
    "Failed password" in line and ATTACKER_IP in line
    for line in log_entries[-10:]
)

print("Log generation completed successfully!")
print(f"Total log entries: {len(log_entries)}")
print(f"Successful logins: {len(successful_logs)}")
print(f"Failed logins: {len(failed_logs)}")
print(f"Attacker IP: {ATTACKER_IP}")
print(f"Output file: {LOG_FILE}")
