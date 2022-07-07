# VimDiff
- Can be assumed an extension of vim
- built into the vim program
- enables us to compare 2 files side by side

## How to use this
- Through Linux/Unix CLI

- Open Files = vimdiff <file 1><file 2>

## Colors
- It's helpful to us by showing us where the differences lie by difference color codes

- Purple = differing line
- Red = differing characters in the differing line
- Blue = new block
	- Appears when there is a certain thing in file 1 but not in file 2
- Teal = missing block
	- in file 2 there would be teal where in file 1 there would be blue if file 1 had additional lines

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- Ctrl + ww switches between windows

- ]c = next diff
- [c = previous diff

#### We can use diffput or diffget to put that change into the other file or get the change from the other file

- dp = diffput (push/put changes)
	- it will change the opposite file from where the cursor lies
- do = diffget
	- it will get the changes from the file where our cursor is not
- :diffupdate - Rescan the files for any changes
