# Searching

## Case Sensitive Search

- /searchterm = Search in the file (Normal Mode)
	- n = next occurence in the file
	- N = previous occurence in the file 

## Case Insensitive Search

- Just add \c
Eg: /searchterm\c


### Search Backwards

- ?searchterm
	- n = previous occurence
	- N = next occurence



# Search and Replace

- :%s/replaceme/withme/g
	- g will replace all occurences without prompting
	- without g it will only replace the first occurence throughout the file on each line
- c prompts before changing every occurence

## Case Insensitive Search and Replace

- Just add \c 
- Eg: :%s/\creplaceme/withme/g
