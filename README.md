8088 Toolbox
============

Introduction
------------

Despite being the CPU of origin IBM PC, Intel 8088 can be used in other ways.

The problem is, however, many software tools surround Intel 8088 are DOS software. 
DOS software is annoying on any modern OS including Windows NT.

This project tries to solve this problem by providing ready-to-use project templates.
The project templates use Make as build system.
The project templates try to hide the ugliness of DOS from the user,
through the use of [DOSBox](http://www.dosbox.com/).

Assembler
---------

[NASM](http://nasm.us/) is an excellent choice.
It runs everywhere.
It can generate binary ROM image directly.

TASM (Turbo Assembler) seems to have more mind share in academic world. 
We run it through DOSBox(http://www.dosbox.com/).

Disassembler
------------

[NDISASM](http://www.nasm.us/doc/nasmdoca.html) should be good enough for our purpose.
It runs everywhere.

Emulator
--------

[EMU8086](http://www.emu8086.com/) is the best 8086/8088 emulator known so far.
It is Windows software.
Non-Windows OS can run it through
[Wine](http://appdb.winehq.org/objectManager.php?sClass=application&iId=7143).

Linker
------

TLINK (Turbo Linker) is currently used, when a linker is needed.
We run it through [DOSBox](http://www.dosbox.com/).

Text Editor
-----------

Both [Sublime Text](http://www.sublimetext.com/) (Cross Platform) and
[TextMate](http://macromates.com/) (Mac) are excellent choices.
[Gedit](http://projects.gnome.org/gedit/index.html) is also acceptable.