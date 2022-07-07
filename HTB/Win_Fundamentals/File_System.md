# File System

### 5 types of Windows File Systems:
- FAT12
- FAT16
- FAT32
- NTFS
- exFAT

FAT12 and FAT16 - no longer used on modern Windows Operating Systems

## FAT32 = (File Allocation Table)
- widely used across many types of storage devices such as USB memory sticks and SD cards
- format hard drives
- 32 means FAT32 uses 32 bits of data for identifying data clusters on a storage device

### Pros of FAT32:
- Device Compatibility - can be used on computers, digital cameras, gaming consoles, smartphones, tablets, etc.
- OS Cross-Compatibility - works on all Windows OSes from Windows 95, also supported by MacOS and Linux

### Cons of FAT32:
- can only be used with files that are less than 4GB
- No built-in data protection or file compression features
- Must use third-party tools for file encryption


## NTFS = (New Technology File System)
- default Windows File System since WIndows NT 3.1

### Pros of NTFS
- better support for metadata 
- better performance due to improved data structuring
- reliable and can restore the consistency of the file system in the event of a system failure or power loss
- provides security by allowing us to set granular permissions on both files and folders
- supports very large-sized partitions
- journaling built-in, meaning that file modifications (addition, modification, deletion) are logged

### Cons of NTFS
- most mobile devices do not support NTFS natively
- older media devices such as TVs and digital cameras do not offer support for NTFS storage devices


## Permissions

Full Control - allows reading, writing, changing, deleting of files/folders

Modify - allows reading, writing and deletion of files/folders

List Folder Contents - allows for viewing and listing folders and subfolders as well as executing files. Only folders inherit this permission

Read and Execute - Allows for viewing and listing files and subfolders as well as executing files. Both files and folders inherit this permission

Write - Allows for adding files to folders and subfolders and writing to a file

Read - Allows for viewing and listing of files and subfolders and viewing a file's contents

Traverse Folder -  Allows or denies the ability to move through folders to reach other files and folders. For example, a user may not have permission to list the directory contents or view files in the documents or web apps directory in this example c:\users\d4rk\documents\webapps\backups\backup_02042020.zip but with Traverse Folder permissions applied, they can access the backup archive.

Files/Folders - inherit the NTFS permissions of their Parent Folder for ease of administration, so administrators do not need to explicitly set permissions for each file and folder, as this would be extremely time-consuming.

If permissions do need to be set explicitly, an administrator can disable permissions inheritance for the necessary files and folders and then set the permissions directly on each.

## Integrity Control Access Control List (icacls)

NTFS permissions on files and folders in Windows can be managed using the File Explorer GUI under the security tab. Apart from the GUI, we can also achieve a fine level of granularity over NTFS file permissions in Windows from the command line using the icacls utility.

list out NTFS permissions on a specific directory by running either `icacls` from within the working directory or `icacls C:\Windows` against a directory not currently in.

### Basic Access Permissions
- F: Full Access
- D: Delete Access
- N: No Access
- M: Modify Access
- RX: Read and Execute Access
- R: Read-Only Access
- W: Write-Only Access

### Possible Inheritance Settings
- (CI): Container Inherit
- (OI): Object Inherit
- (IO): Inherit Only
- (NP): Do not propogate inherit
- (I): Permission inherited from parent container

full listing of icacls command-line arguments and detailed permissions settings: https://ss64.com/nt/icacls.html

## CheatSheet:
| **Command** | **Description** |
| --------------|-------------------|
| `xfreerdp /v:<target IP address> /u:htb-student /p:<password>` | RDP to lab target |
| `Get-WmiObject -Class win32_OperatingSystem` | Get information about the operating system |
| `dir c:\ /a` | View all files and directories in the c:\ root directory |
| `tree <directory>` | Graphically displaying the directory structure of a path |
| `tree c:\ /f \| more` | Walk through results of the `tree` command page by page |
| `icacls <directory>` | View the permissions set on a directory |
| `icacls c:\users /grant joe:f` | Grant a user full permissions to a directory |
| `icacls c:\users /remove joe` | Remove a users' permissions on a directory |
| `Get-Service` | `PowerShell` cmdlet to view running services |
| `help <command>` | Display the help menu for a specific command |
| `get-alias` | List `PowerShell` aliases |
| `New-Alias -Name "Show-Files" Get-ChildItem` | Create a new `PowerShell` alias |
| `Get-Module \| select Name,ExportedCommands \| fl` | View imported `PowerShell` modules and their associated commands |
| `Get-ExecutionPolicy -List` | View the `PowerShell` execution policy |
| `Set-ExecutionPolicy Bypass -Scope Process` | Set the `PowerShell` execution policy to bypass for the current session |
| `wmic os list brief` | Get information about the operating system with `wmic` |
| `Invoke-WmiMethod` | Call methods of `WMI` objects |
| `whoami /user` | View the current users' SID |
| `reg query <key>` | View information about a registry key |
| `Get-MpComputerStatus` | Check which `Defender` protection settings are enabled |
| `sconfig` | Load Server Configuration menu in Windows Server Core |

