Microsoft owns over 70% of the global market share on desktop operating systems with Windows.

If software can be written for an operating system then a virus can be written for an operating system.

Virus = Software written with malicious intent and can be written for any OS.

infamous **EternalBlue** vulnerability - still haunts unpatched Windows Systems running SMBv1 and often paves the way for ransomeware to shut down organizations.

SMB (Server Message Block Protocol):
- used in Windows to connect shared resources like files and printers.
- used in large, medium and small enterprise environments

NTFS Permissions and share permission not same
- often apply to same shared resource

### Share Permissions

Full Control - Users are permitted to perform all actions given by Change and Read permissions as well as change permissions for NTFS files and subfolders

Change - Users are permitted to read, edit, delete and add files and subfolders

Read - Users are allowed to view file & subfolder contents


### NTFS Basic Permissions

Full Control  - Users are permitted to add, edit, move, delete files & folders as well as change NTFS permissions that apply to all allowed folders

Modify - Users are permitted or denied permissions to view and modify files and folders. This includes adding or deleting files

Read & Execute - Users are permitted or denied permissions to read the contents of files and execute programs

List Folder Contents - Users are permitted or denied permissions to view a listing of files and subfolders

Read - 	Users are permitted or denied permissions to read the contents of files

Write - Users are permitted or denied permissions to write changes to a file and add new files to a folder

Special Permissions - A variety of advanced permissions options


## NTFS Special Permissions 

Traverse Folder / Execute File - Users are permitted or denied permissions to access a subfolder within a directory structure even if the user is denied access to contents at the parent folder level. Users may also permitted or denied permissions to execute programs

List Folder / Read Data  - Users are permitted or denied permissions to view files and folders contained in the parent folder. Users can also be permitted to open and view files

Read Attributes - Users are permitted or denied permissions to view basic attributes of a file or folder. Examples of basic attributes: system, archive, read-only, and hidden

Read Extended Attributes - Users are permitted or denied permissions to view extended attributes of a file or folder. Attributes differ depending on the program

Create Files / Write Data - Users are permitted or denied permissions to create files within a folder and make changes to a file

Create Folders / Append Data - Users are permitted or denied permissions to create subfolders within a folder. Data can be added to files but pre-existing content cannot be overwritten

Write Attributes - Users are permitted or denied to change file attributes. This permission does not grant access to creating files or folders

Write Extended Attributes - Users are permitted or denied permissions to change extended attributes on a file or folder. Attributes differ depending on the program

Delete Subfolders and Files - Users are permitted or denied permissions to delete subfolders and files. Parent folders will not be deleted

Delete - Users are permitted or denied permissions to delete parent folders, subfolders and files.

Read Permissions - Users are permitted or denied permissions to read permissions of a folder

Change Permissions - Users are permitted or denied permissions to change permissions of a file or folder

Take Ownership - Users are permitted or denied permission to take ownership of a file or folder. The owner of a file has full permissions to change any permissions

**NOTES**: 
- Possible to disable inheritance to set custom permissions on parent and subfolders
- Share perms apply when the folder is being accessed through SMB, typically from a different system over the network
