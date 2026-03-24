import os
import shutil
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PENDING_APPROVAL = os.path.join(BASE_DIR, "Pending_Approval")
APPROVED = os.path.join(BASE_DIR, "Approved")
REJECTED = os.path.join(BASE_DIR, "Rejected")

os.makedirs(PENDING_APPROVAL, exist_ok=True)
os.makedirs(APPROVED, exist_ok=True)
os.makedirs(REJECTED, exist_ok=True)

def process_approval_triggers():
    files = os.listdir(PENDING_APPROVAL)
    trigger_files = [f for f in files if f.upper().startswith("APPROVE") or f.upper().startswith("REJECT")]
    
    approve_trigger_found = any(f.upper().startswith("APPROVE") for f in trigger_files)
    reject_trigger_found = any(f.upper().startswith("REJECT") for f in trigger_files)
    
    if approve_trigger_found:
        print("APPROVED! Moving task to Approved folder...")
        for f in files:
            if not f.upper().startswith("APPROVE") and not f.upper().startswith("REJECT"):
                src = os.path.join(PENDING_APPROVAL, f)
                dst = os.path.join(APPROVED, f)
                shutil.move(src, dst)
        # Delete trigger file
        for f in trigger_files:
            os.remove(os.path.join(PENDING_APPROVAL, f))
        print("Task approved and moved!")
        
    elif reject_trigger_found:
        print("REJECTED! Moving task to Rejected folder...")
        for f in files:
            if not f.upper().startswith("APPROVE") and not f.upper().startswith("REJECT"):
                src = os.path.join(PENDING_APPROVAL, f)
                dst = os.path.join(REJECTED, f)
                shutil.move(src, dst)
        for f in trigger_files:
            os.remove(os.path.join(PENDING_APPROVAL, f))
        print("Task rejected and moved!")

print("Approval Watcher started!")
while True:
    process_approval_triggers()
    time.sleep(5)