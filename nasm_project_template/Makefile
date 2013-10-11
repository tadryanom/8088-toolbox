TARGET=template

.PHONY: all
all: $(TARGET).bin

$(TARGET).bin: $(TARGET).asm
	nasm -o $@ -f bin -l $(TARGET).lst $<

.PHONY: clean
clean:
	-rm -f *.bin *.lst
