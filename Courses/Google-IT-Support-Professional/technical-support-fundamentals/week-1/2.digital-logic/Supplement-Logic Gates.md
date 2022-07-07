# Supplemental Reading: Logic Gates

Imagination for how logic gates work: [[3. Binary#^a71a66|here]]
- Logic Gate = Used to conduct electricity based on a rule
- Work on 2 states: Positive Level(On) & 0 Level(Off)
- On --> Voltage -> Positive -> b/w 3.5 to 5 volts
- Off --> Voltage -> 0
- Compare the state of their inputs -> decide what output should be
- if rules correctly met: on/active
	- Electricity flowing through the gate 
- Electronic version of boolean logic
- Truth tables -> tell what output will be
	- depending on the inputs

## Types of Logic Gates
```ad-note
title: AND Logic Gate
collapse: close

- 2 inputs
- output is on
	- only if both inputs -> on
	- If one input off -> off

![General Idea for AND Logic Gate](https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/And.svg/400px-And.svg.png)

![AND Truth Table](AND-truth-table.png)
```
```ad-note
title: OR Logic Gate
collapse:close

- 2 inputs
- output is on
	- one of 2 inputs -> on
	- both input off -> off

![OR Logic Gate](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Or-gate-en.svg/400px-Or-gate-en.svg.png)

![OR Truth Table](OR-truth-table.png)
```
```ad-note
title: NOT Logic Gate
collapse:close

- 1 input
- output on -> input off
- output off -> input on
- Also known as "inverter"

![NOT Logic Gate](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Not-gate-en.svg/400px-Not-gate-en.svg.png)

![NOT Truth Table](NOT-truth-table.png)
```
```ad-note
title: XOR Logic Gate
collapse:close

XOR = exclusive or
- 2 inputs
- output = true
	- only if 2 inputs are different from each other
	- i.e: A not= B
- output = false
	- both inputs are same
	- i.e: A = B
![XOR Logic Gate](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Xor-gate-en.svg/440px-Xor-gate-en.svg.png)

![XOR Truth Table](XOR-truth-table.png)
```
```ad-note
title:NAND Logic Gate
collapse:close

NAND = not both (not and)

- 2 inputs
- output = true
	- either 1 should be off
- output = false
	- both on

![NAND Logic Gate](https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Logic-gate-nand-de.png/440px-Logic-gate-nand-de.png)

![NAND Truth Table](NAND-truth-table.png)
```
```ad-note
title: XNOR Logic Gate
collapse: close

XNOR = not exclusive or
- 2 inputs
- output = true
	- both inputs same
	- i.e: A=B
- Opposite of XOR

![XNOR Logic Gate](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Logic-gate-xnor-us.png/440px-Logic-gate-xnor-us.png)
![XNOR Truth Table](XNOR-truth-table.png)
```
