# Forensics workshop by CSS 24th October 2019

## Purpose of this workshop
We all can agree that computer science is such a big and overwhelming field that it can sometimes be hard to find a field that you like to pursue your career with. The goal of this workshop is to expose students to something new that they usually do no come across during their years studying in Nottingham. This workshop aims to get your feet wet with some basic digital forensics and linux skills.

## Where are these challenges taken from?
They are taken from the [2018 picoCTF](https://2018game.picoctf.com). I highly suggest you to try the challenges even if you are not interested in computer security as I have personally learned a lot from these challenges, not just in digital forensics but also in fields such as general computing skills, web security and binary exploitation.

## Pre-requisites
For this workshop, we will be using [VirtualBox](https://www.virtualbox.org/) to run a guest [Kali Linux](https://www.kali.org/) virtual machine. However, VirtualBox requires a technology called VT-x for intel machines, or AMD-V for AMD machines. To check if your computer is compatible, refer below.

### Windows
1. Refer to this [link](https://www.shaileshjha.com/how-to-find-out-if-intel-vt-x-or-amd-v-virtualization-technology-is-supported-in-windows-10-windows-8-windows-vista-or-windows-7-machine/)
2. Note: VT-x or AMD-V may be disabled in the bios, check your CPU model online to see if it is VT-x enabled. If so, enable it in the bios.

### MacOS
1. Open a terminal
2. Type in this command: `sysctl -a | grep machdep.cpu.features | grep VMX`
3. If the output looks something like this, you can use VirtualBox:
```
machdep.cpu.features: FPU VME DE PSE TSC MSR PAE MCE CX8 APIC SEP MTRR PGE MCA CMOV PAT PSE36 CLFSH DS ACPI MMX FXSR SSE SSE2 SS HTT TM PBE SSE3 PCLMULQDQ DTES64 MON DSCPL VMX SMX EST TM2 SSSE3 FMA CX16 TPR PDCM SSE4.1 SSE4.2 x2APIC MOVBE POPCNT AES PCID XSAVE OSXSAVE SEGLIM64 TSCTMR AVX1.0 RDRAND F16C
```
4. If it is empty, you do not have VT-x enabled on your machine

### Linux
If you are already using a linux distribution, you can just use your current machine for this workshop.

## Installation

