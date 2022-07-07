# Operating System Structure

Root Directory:
- <drive_letter>:\ (commonly C drive)
- also known as the boot partition
- where operating system is installed

Other physical and virtual drives are assigned other letters

Directory Structure of boot partition:

Perflogs = Can hold Windows performance logs but is empty by default.

Program Files = On 32-bit systems, all 16-bit and 32-bit programs are installed here. On 64-bit systems, only 64-bit programs are installed here.

Program Files (x86) = 32-bit and 16-bit programs are installed here on 64-bit editions of Windows.

ProgramData = This is a hidden folder that contains data that is essential for certain installed programs to run. This data is accessible by the program no matter what user is running it.

Users = This folder contains user profiles for each user that logs onto the system and contains the two folders Public and Default.

Default = This is the default user profile template for all created users. Whenever a new user is added to the system, their profile is based on the Default profile.

Public = This folder is intended for computer users to share files and is accessible to all users by default. This folder is shared over the network by default but requires a valid network account to access.

AppData = Per user application data and settings are stored in a hidden user subfolder (i.e., cliff.moore\AppData). Each of these folders contains three subfolders. The Roaming folder contains machine-independent data that should follow the user's profile, such as custom dictionaries. The Local folder is specific to the computer itself and is never synchronized across the network. LocalLow is similar to the Local folder, but it has a lower data integrity level. Therefore it can be used, for example, by a web browser set to protected or safe mode.

Windows  = The majority of the files required for the Windows operating system are contained here.

System, System32, SysWOW64 = Contains all DLLs required for the core features of Windows and the Windows API. The operating system searches these folders any time a program asks to load a DLL without specifying an absolute path.

WinSxS = The Windows Component Store contains a copy of all Windows components, updates, and service packs.


## Exploring Directories using Command Line
- explore file system using `dir` command
- if graphical displaying the directory structure of a path or a disk is required, use `tree` utility    

`tree c:\ /f | more` = can be used to walk through all the files in the C drive, one screen at a time. This command can be modified to be run against any directory.

# CheatSheet

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

