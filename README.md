# Wake-on-LAN-Python
Hey everyone. I created a working Wake On Lan script via Python, using MagicPacket. The script will ask the user input of first a MAC Address. There are safeguards in place which forces the user to input a valid MAC Address. Currently, you can only seperate the MAC Address hexadecimal characters by a dash (-) or a colon (:), and not a dot (.). After a valid MAC Address is inputted, the script will ask the user to input a Private IP Address. Once again, there are safeguards in place to assess whether the inputted IP Address is valid and not a Public IP Address. Afterwards, if everything is inputted correctly, it will send a Magic Packet and should wake up the targetted machine!

Everything is open source and you're more than welcome to code it so that it will permenantly do one MAC Address and IP Address only.

## Prerequisites
```bash
pip install wakeonlan
pip install termcolor
```

## Troubleshooting
*Important to note:*
Wake on LAN may not work with Fast Startup enabled. Make sure to disable it. *(sometimes it worked on my computer when enabled, but I found it works 100% of the time when it's off)*

***How to Manually Disable Fast Startup:***

1) Navigate to the Control Panel and select ‘Power Options.’
2) Choose ‘Choose what the power buttons do.’
3) Click on ‘Change settings that are currently unavailable.’
4) Under ‘Shutdown settings,’ uncheck the ‘Turn on fast startup’ box.

<hr>

When you shut down your computer, it matters if it is shutting down in **S3 (sleep mode), S4 (hibernate) or S5 (soft power off mode)**.
**According to Microsoft, WoL only works with S3 or S4. It does not work with fast startup or soft shut off (S5).**

1) Did you enable Wake on LAN in BIOS? Double check to make sure that `Resume by PCI/E or WakeOnLAN is enabled`
2) In Device Manager, under Network adapters, select your network device.
3) Click Properties -->  Advanced --> Under the Property section, select `Wake on Magic Packet` and select Enable in the value box. You should also enable `Wake on magic packet when system is in the S0ix power state`
4) Open the Power Management tab
5) Enable `Allow this device to wake the computer` and `Only allow a magic packet` to wake the computer.

## Sources
https://stackoverflow.com/questions/7629643/how-do-i-validate-the-format-of-a-mac-address  
https://pypi.org/project/wakeonlan/  
https://serverfault.com/questions/1018470/wol-and-wow-does-not-work-after-a-certain-time  
https://www.lifewire.com/wake-on-lan-4149800

##### Created by Yash Batish (LeakyEarth2000)
