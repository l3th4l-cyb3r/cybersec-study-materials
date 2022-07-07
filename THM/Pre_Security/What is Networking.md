# What is Networking?
First Iteration of the Internet - **ARPANET** project in late 1960s
funded by United States Defence Department 
first documented network in action

**W**orld **W**ide **W**eb (**WWW**) - 1989 - Tim Berners-Lee
first time internet used as a repository for storing and sharing information

![](https://assets.tryhackme.com/additional/networking-fundamentals/intro-to-networking/what-is-the-internet/internet2.png)


Internet - Made up of many small networks joined together
Small Networks = Private Networks
Networks connecting Private Networks are called Public Networks/**Internet**

Network - 2 types
- Private Network
- Public Network

**NOTE**: Devices use a set of labels to identify themselves on the network

## Identifying devices on a network
To communicate and maintain order, devices must be both identifying and identifiable on a network

devices have 2 means of identification, just like us humans

Humans - 
1. Name
2. FIngerprints
 
1 can be changed

Devices
1. IP Address
2. Media Access Control (MAC) Address -  SImilar to serial number

here too, 1 can be changed

### IP Addresses
IP Address -  **I**nternet **P**rotocol

- used as a way of identifying a host on a network for a period of time
- same IP Address then can be associated with another device without IP Address changing

![IP Address](https://assets.tryhackme.com/additional/networking-fundamentals/intro-to-networking/what-is-a-network/octets.png)

- Set of numbers
- devided into 4 octets
- nuber is calculated through a technique known as IP Addressing & Subnetting
- change from device to device
- cannot be active simultaneously more than once within the same network
- follow a set of standards known as **protocols**
- devices can be both on a private and public network
- public address - used to identify devices on the internet
- private address - used to identify a device amongst other devices 

##### Protocols
- backbone of networking 
- force many devices to communicate in the same language 

**NOTE**: 50 billion devices will be connected to the internet by the end of 2021
- it's becoming increasingly harder to get a ip address
- IPv4 - 2^32 IP Addresses (4.29 Billion)
- therefore, 4.29 billion < 50 billion

IPv6 - new iteration
- supports 2^128 IP Addresses (340 trillion)
- more efficient due to new methodologies


### MAC Addresses
- devices on a network will all have a physical network interface
	- microchip board found in device's motherboard
- assigned a unique address at the factory it was built at
- 12 character hexadecimal number
	- split in 2s
	- seperated by a colon
		- colons - seperators
- first 6 characters represent the company that made the network interface
- last 6 - unique number

![](https://assets.tryhackme.com/additional/networking-fundamentals/intro-to-networking/what-is-a-network/mac_address.png)

**Interesting thing**: can be faked or spoofed

**Spoofing** occurs when a networked device pretends to identify as another using its MAC Address
- often break poorly implemented security designs

**Example**: A firewall is configured to allow any communication going to and from the MAC address of the **administrator**. If a device were to pretend or "spoof" this MAC address, the firewall would now think that it is receiving communication from the **administrator** when it isn't.