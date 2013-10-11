; vim: set ts=4 sw=4 sts=4 noet:
; asmsyntax=nasm

ram_size equ 0x800
rom_size equ 0x8000

start:
		mov ax, 0
		mov ds, ax
		mov ss, ax
		mov sp, ram_size

loop1:
		nop
		jmp	loop1

		times rom_size-0x10-($-$$) db 0
		jmp ((0x100000-rom_size)>>4):0
