# The DHCP Protocol

**DHCP** = **D**ynamic **H**ost **C**onfiguration **P**rotocol

IP Address assign ways:
- Manually (entering them physically on a device)
- Automatically, Most commonly (DHCP)

When device connects to network:
- if it has not already been manually assigned an IP Address 
- sends out a request (**DHCP Discover**)
- to see if any DHCP servers are on the network
- DHCP server then replies back with an IP Address the device could use (**DHCP Offer**)
- device then sends reply confirming it wants the offered IP Address (**DHCP Request**)
- lastly, DHCP Server sends a reply acknowledging this has been completed
- device can start using IP Address (**DHCP ACK**)

## DHCP Demonstration
![DHCP](https://assets.tryhackme.com/additional/networking-fundamentals/intro-to-networking/what-is-a-network/DHCP.png)



