# MAC Changer

Simple MAC changer for Unix/Linux.

## The algorithm

The script uses the optparse module to get the interface and MAC address values from terminal, then with subprocess module it sets the new MAC address. At the end it checks if MAC was successfuly changed.

## Clone

> Clone this repo to your local machine using https://github.com/rsoares10/mac-changer.git

## Usage
```
mac-changer  [OPTION1] arg1 [OPTION2] arg2

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Interface to change its MAC address
  -m NEW_MAC, --mac=NEW_MAC
                        New MAC address
```

## Example

```
# Provide an interface and new MAC value
 ./mac-changer.py -i wlp2s0 -m 5c:c9:d3:c3:d9:41

# Output
Current MAC: 00:11:22:33:44:55
[+] Changing MAc address for wlp2s0 to 5c:c9:d3:c3:d9:41
[+] MAC address was successfuly changed to 5c:c9:d3:c3:d9:41
```

> _Note: It might be required root privileges for this script to work._

## Prerequisites
- Python 2.7

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Support
Reach out to me at one of the following places!
- Facebook at https://www.facebook.com/max.monteiro.520
- Gmail at rsoares.monteiro10@gmail.com