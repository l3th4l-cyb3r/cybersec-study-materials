# A Primer On Subnetting

Subnetting = splitting up a network into smaller, miniature networks within itself

is achieved by splitting up the number of hosts that can fit within the network, represented by a no. called subnet mask.

#### IP Address 
- 4 sections
- called octets

#### Subnet Mask
- represented as no. of 4 bytes (32 bits)
- ranging from 0 to 255 (0-255)

Subnets use IP Address in 3 different ways:
- Identifying network address
- Identifying host address
- Identifying default gateway

| **Type**        	| **Purpose**                                                                                                                                    	| **Explanation**                                                                                                                                                                                                                                      	| **Example**   	|
|-----------------	|------------------------------------------------------------------------------------------------------------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|---------------	|
| Network Address 	| This address identifies the start of the actual network and is used to identify a network's existence.                                         	| For example, a device with the IP address of 192.168.1.100 will be on the network identified by 192.168.1.0                                                                                                                                          	| 192.168.1.0   	|
| Host Address    	| An IP address here is used to identify a device on the subnet                                                                                  	| For example, a device will have the network address of 192.168.1.1                                                                                                                                                                                   	| 192.168.1.100 	|
| Default Gateway 	| The default gateway address is a special address assigned to a device on the network that is capable of sending information to another network 	| Any data that needs to go to a device that isn't on the same network (i.e. isn't on 192.168.1.0) will be sent to this device. These devices can use any host address but usually use either the first or last host address in a network (.1 or .254) 	| 192.168.1.254 	|

### Small Networks
- Eg: Home
- will be on 1 subnet
- there is an unlikely chance that 254 devices connected at a time

### Large Networks
- Eg: Businesses, Offices
- much more of devices

## Subnetting Benefits
- Efficiency
- Security
- Full Control

Eg: Typical Cafe on the street

Cafe will have 2 networks
- Employees, cash registers and other devices for the facility
- General Public to use as a hotspot

Subnetting allows us to seperate these 2 use cases from each other whilst having the befits of a connection to larger networks

