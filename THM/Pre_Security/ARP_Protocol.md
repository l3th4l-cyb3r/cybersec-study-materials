## The ARP Protcol

ARP Protocol = **A**ddress **R**esolution **P**rotocol

- Technology that is responsible for allowing devices to identify themselves on a network
- Allows a device to associate its MAC Addresses with an IP Address on the network
- Each device on a network will keep a log of the MAC Addresses associated with other devices 

When devices wish to communicate with each other, they will send a broadcast to the entire network searching for the specific device. Devices can use the ARP Protocol to find the MAC Addresses (ie: Physical Identifier) of a device for communication


## How does ARP work?

Each device within a network has a ledger to store information on = Cache
In context of ARP Protocol, this cache stores the identifiers of other devices on the network

IN order to map these 2 identifiers together (**IP** Address and **MAC** Address), ARP Protocol sends 2 types of messages:
- ARP Request
- ARP Reply

### When ARP Request sent:
- message is broadcaster to every other device found on a network by device
- asking whether or not the device's MAC Address matches the requested IP Address
- If device does have requested IP Address, then:

### ARP Reply Sent:
- returned to initial device to acknowledge this
- initial device will now remember this and store it within its Cache **(ARP Entry)**

### Process Diagram:
![ARP Process](https://tryhackme-images.s3.amazonaws.com/user-uploads/5de96d9ca744773ea7ef8c00/room-content/b27c024d90342c60dd5cb35765e7ed7b.png)


