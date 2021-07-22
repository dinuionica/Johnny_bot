
#!/bin/bash

sudo apt install python3 &&
sudo apt install g++ &&
sudo apt install vscode && 
sudo apt install discord && 
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor &&
echo "All apps are installed!"