import subprocess
import sys

INVENTORY = "inventory.ini"

def run_playbook(playbook, extra_vars=None):
    cmd = ["ansible-playbook", "-i", INVENTORY, playbook]
    if extra_vars:
        cmd.extend(["--extra-vars", extra_vars])

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("❌ Playbook execution failed")
        sys.exit(1)

def menu():
    print("""
🔹 Linux Level-1 Monitoring Automation
1. Disk Usage Check
2. CPU Utilization Check
3. Memory Utilization Check
4. Connectivity Check
5. Restart Qualys Service
6. Exit
""")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        mount = input("Enter mount point (e.g /): ")
        run_playbook("playbooks/disk_check.yml", f"mount_point={mount}")

    elif choice == "2":
        run_playbook("playbooks/cpu_check.yml")

    elif choice == "3":
        run_playbook("playbooks/memory_check.yml")

    elif choice == "4":
        run_playbook("playbooks/connectivity_check.yml")

    elif choice == "5":
        run_playbook("playbooks/qualys_restart.yml")

    elif choice == "6":
        print("Exiting...")
        sys.exit(0)

    else:
        print("Invalid choice")
