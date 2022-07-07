There have been many network designs over the years

"Topology" = Referring to design or look of network 

## Star Topology

- devices are individually connected via a central networking device such as switch or hub
- most popular because of its reliability and scalability
- any information sent to a device in this topology is sent via the central device to which it connects
- more cabling and purchase of equipments = more cost
- more scalable in nature
- very easy to add more devices as the demand for network increases
- the more network scales, the more maintenance is required to keep the network functional
- increased dependence on maintenance can also make troubleshooting much harder
- still prone to failure - albeit reduced
- if centralised hardware that connects devices fails, these devices will no longer be able to send or recieve data
- centralised hardware devices are often robust

![Star Topology](https://assets.tryhackme.com/additional/networking-fundamentals/intro-to-lan/star.png)


## Bus Toplogy

- relies upon a single connection which is known as backbone cable
- all data for each device travels along the same cable
- very quickly prine to becoming slow and bottlenecked if devices are simulataneously requesting data
- bottleneck also results in very difficult troubleshotting 
- quickly becomes difficult to identify which device is experiencing issues with data all travelling along the same route
- are one of the easier and more cost-efficient technologies to set up
- little redundancy in place of case of failures
- if cable were to break, devices can no longer recieve or transmit data along the bus

![Bus Topology](https://assets.tryhackme.com/additional/networking-fundamentals/intro-to-lan/bus.png)


## Ring Topology

- also known as token topology
- devices are connected direcly to each other to form a loop
- little cabling required
- less dependence on dedicated hardware 
- works by sending data across the loop until it reaches the destined device using other devices along the loop to forward the data
- a device will only send recieved data from another device if it doesn't have any to send itself
- if the device happens to have data to sendm it will send its own data first before sending data from another device
- only one direction for data to travel across 
- fairly easy to troubleshoot any faults that arise
- double-edged sword because it isn't an efficient way of data travelling across a network as it may have to visit multiple devices first before reaching the intended device
- less prone to bottlenecks
- large amounts are not travelling across the network at any 1 time
- if cable cuts or a device breaks, entire network breaking

![Ring Topology](https://assets.tryhackme.com/additional/networking-fundamentals/intro-to-lan/ring.png)

## What is a Switch?

- dedicated devices within a network that are designed to aggregate multiple other devices such as computers, printers or any other networking-capable device using ethernet- various devices plug into a switch's port
- usually found in larger networks such as businesses, schools or similar-sized networks where there are many devices to connect to the network
- can connect a large number of devices by having ports of 4,8,16,24,32 & 64 for devices to plug into
- much more efficient that their lesser counterpart (hubs/repeaters)
- keep track of what device is connected to which port
- when they recieve a packet, instead of repeating that packet to every port like a hub would do, just sends it to intended target, thus reducing network traffic
- both switches and routers can be connected to one another
- ability to do this increases the redundancy of a network by adding multiple paths for data to take
- if one path goes down, another can be used
- this may reduce overall performance of a network because packets have to take longer to travel, but no downtime

![Switch and Routers](https://assets.tryhackme.com/additional/networking-fundamentals/intro-to-lan/switches.png)
## What is a router?
 
- connects networks and pass data between them
- does this by using routing(hence name router)
- Routing is the label given to process of data travelling across networks
- involves creating a path between networks so this data can be successfully delivered- is useful when devices are connected by many paths

![Routing](https://assets.tryhackme.com/additional/networking-fundamentals/intro-to-networking/what-is-the-internet/routing2.png)

