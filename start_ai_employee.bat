@echo off
cd "C:\Users\JUNCTION\Documents\personal ai employee"
start "Watcher" python watcher.py
start "Orchestrator" python orchestrator.py
echo AI Employee Started!