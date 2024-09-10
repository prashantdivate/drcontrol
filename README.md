# drcontrol
Direction Controller for 8 channel USB relay Board-FT245RL for Linux environment

1. Get the connected device name using below command
``` $ sudo python3 -m pylibftdi.examples.list_devices ```
and update it for bb variable 

2. Run the command to start
```$ ./drcontrol.py```
