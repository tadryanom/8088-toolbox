8088 Toolbox
============

Introduction
------------

Despite being the CPU of origin IBM PC, Intel 8088 can be used in other ways.

The problem is, however, many software tools surround Intel 8088 are DOS software. 
DOS software is annoying on any modern OS including Linux, Mac OS X and Windows.

This project tries to solve this problem by providing ready-to-use project templates.
The project templates use Make as build system.
The project templates try to hide the ugliness of DOS from the user,
through the use of [DOSBox](http://www.dosbox.com/).

Assembler
---------

[NASM](http://nasm.us/) is an excellent choice.
It can generate binary ROM image directly.

TASM (Turbo Assembler, DOS) seems to have more mind share in academic world. 

Disassembler
------------

[NDISASM](http://www.nasm.us/doc/nasmdoca.html) should be good enough for our purpose.

Emulator
--------

[EMU8086](http://www.emu8086.com/) (Windows) is the best 8086/8088 emulator known so far.
Non-Windows OS can run it through [Wine](http://www.winehq.org/).

Linker
------

TLINK (Turbo Linker, DOS) is currently used, when a linker is needed.

Text Editor
-----------

[Geany](http://www.geany.org/) (Linux, Windows),
[Sublime Text](http://www.sublimetext.com/) and
[TextMate](http://macromates.com/) (Mac) are excellent choices.
