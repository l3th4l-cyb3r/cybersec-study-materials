# The Windows Operating System

## Beginnings
- First Introduced in Nov.20, 1985
- First version of Windows was a graphical Operating system shell for MS-DOS
- Later versions of Windows Desktop introduced
	- File Manager
	- Program Manager
	- Print Manager

## Windows 95
- first full integration of Windows and DOS 
- offered built-in internet support for 1st time
- debuted Internet Explorer Web Browser

Since initial version, over a dozen version of Windows released
- Windows XP
- Windows Vista
- Windows 7
- Windows 8
- Windows 10
- Windows 11 etc.

Overtime, Microsoft has offered various edition of each Windows Desktop released catering to everyone from casual consumers to enterprise customers

## Windows Server
- 1st release = 1993
- with released of Windows NT 3.1 Advanced Server
- Windows NT saw several updates over the years
	- adding in technologies such as Internet Information Services (IIS)
	- various networking protocols
	- Administrative Wizards to facilitate admin tasks and much more

## Windows 2000
- Active Directory
	- Originally intended to help sysadmins set up file sharing, data encryption, 		VPNs, etc.
	- also included Microsoft Management Console (MMC)
	- supported dynamic disk volumes

## Windows Server 2003
- server roles
- built-in firewall
- Volume Shadow Copy Service

## Windows Server 2008
- failover clustering
- Hyper-V Virtualization Software
- Server Core
- Event Viewer
- Majot Enhancements to Active Directory

## Windows Server 2019
- Support for Kubernetes
- Linux Containers
- more advanced security features

As new versions of Windows are introduced, older versions are deprecated and no longer receive Microsoft updates (unless a long-term support contract is purchased in some cases).

Windows Server 2008 and 2012 
- reached end of life for security updates on January 14,2020

Currently, only server 2012 R2 and later are in support

However, Microsoft has released out-of-band patches for earlier versions of Windows in the past few years due to the discovery of the critical SMBv1 vulnerability (EternalBlue).

Many versions of Windows are now deemed legacy and are no longer supported

Organizations often find themselves running various older operating systems to support critical applications or due to operational or budgetary concerns.

An assessor needs to understand the differences between versions and the various misconfigurations and vulnerabilities inherent to each.

## Windows OSes and their Versions

|OS Names
|-----------
|Windows NT 4
|-----------
|Windows 2000
|-----------
|Windows XP
|-----------
|Windows Server 2003, 2003 R2
|-----------
|Windows Vista, Server 2008
|-----------
|Windows 7, Server 2008 R2
|-----------
|Windows 8, Server 2012
|-----------
|Windows 8.1, Server 2012 R2
|-----------
|Windows 10, Server 2016, Server 2019
|-----------

We can use the Get-WmiObject cmdlet to find information about the operating system. This cmdlet can be used to get instances of WMI classes or information about available WMI classes. There are a variety of ways to find the version and build number of our system. We can easily obtain this information using the win32_OperatingSystem class, which shows that we are on a Windows 10 host, build number 18362.   

Some other useful classes that can be used with Get-WmiObject are Win32_Process to get a process listing, Win32_Service to get a listing of services Win32_Bios to get BIOS information. We can use the ComputerName parameter to get information about remote computers. GetWmiObject can be used to start and stop services on local and remote computers, and more. Further information about the cmdlet can be found here and here.

Obtain **Version** and **BuildNumber**

Get-WmiObject -Class win32_OperatingSystem | select Version,BuildNumber

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


