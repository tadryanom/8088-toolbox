; vim: set ts=4 sw=4 sts=4 noet:
; asmsyntax=masm

stack_seg segment at 0
top_of_stack equ 800h
stack_seg ends

data_seg segment at 0
data_seg ends

dummy_code segment at 0f800h
dumst label far
dummy_code ends

code_seg segment public 'code'
		assume cs:code_seg
start:
		mov ax, data_seg
		mov ds, ax
		assume ds:data_seg
		mov ax, stack_seg
		mov ss, ax
		assume ss:stack_seg
		mov sp, top_of_stack

loop1:
		nop
		jmp loop1

		org 7ff0h
		jmp dumst
code_seg ends
		end start
