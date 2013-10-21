TARGET = template

.PHONY: all
all: $(TARGET).bin

$(TARGET).bin: $(TARGET).exe
	@ cp $< tmp.exe
	>/dev/null dosbox -c "mount c ." -c "c:" -c "tools\exe2bin tmp.exe tmp.bin >exe2bin.log" -c "exit"
	@ python scripts/fix_case.py
	@ cat exe2bin.log
	@ rm -f tmp.exe *.log
	@ mv tmp.bin $@ 2>/dev/null

$(TARGET).exe: $(TARGET).obj
	@ cp $< tmp.obj
	>/dev/null dosbox -c "mount c ." -c "c:" -c "tools\tlink tmp.obj, tmp.exe >tlink.log" -c "exit"
	@ python scripts/fix_case.py
	@ cat tlink.log
	@ rm -f tmp.obj *.log
	@ mv tmp.exe $@ 2>/dev/null
	@ perl -pi -e 's/\r\n|\n|\r/\n/g' tmp.map
	@ mv tmp.map $(TARGET).map


$(TARGET).obj: $(TARGET).asm
	@ cp $< tmp.asm
	>/dev/null dosbox -c "mount c ." -c "c:" -c "tools\tasm tmp.asm, tmp.obj >tasm.log" -c "exit"
	@ python scripts/fix_case.py
	@ cat tasm.log
	@ rm -f tmp.asm *.log
	@ mv tmp.obj $@ 2>/dev/null

.PHONY: clean
clean:
	rm -f *.bin *.exe *.map *.obj
