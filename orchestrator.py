import os
import time
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NEEDS_ACTION = os.path.join(BASE_DIR, "Needs_Action")
DONE = os.path.join(BASE_DIR, "Done")
PENDING_APPROVAL = os.path.join(BASE_DIR, "Pending_Approval")

os.makedirs(PENDING_APPROVAL, exist_ok=True)
os.makedirs(DONE, exist_ok=True)

def process_file(filepath):
    filename = os.path.basename(filepath)
    print(f"Processing: {filename}")
    
    # Check if approval needed
    if "payment" in filename.lower() or "send" in filename.lower():
        dest = os.path.join(PENDING_APPROVAL, filename)
        os.rename(filepath, dest)
        print(f"Needs approval: {filename}")
    else:
        # Create plan
        plan_path = os.path.join(BASE_DIR, "Plan.md")
        with open(plan_path, "a") as f:
            f.write(f"\n## Task: {filename}\n")
            f.write(f"- Status: Processing\n")
            f.write(f"- Time: {time.ctime()}\n")
        
        # Move to done
        dest = os.path.join(DONE, filename)
        os.rename(filepath, dest)
        print(f"Done: {filename}")

print("Orchestrator started!")
while True:
    for filename in os.listdir(NEEDS_ACTION):
        filepath = os.path.join(NEEDS_ACTION, filename)
        if os.path.isfile(filepath):
            process_file(filepath)
    time.sleep(10)