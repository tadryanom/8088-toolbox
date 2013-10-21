import os
import shutil
import subprocess
import urllib
import zipfile

# exe2bin
print 'downloading exe2bin ...'
urllib.urlretrieve('http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/exe2bin/exe2b15x.zip', 'exe2b15x.zip')

with zipfile.ZipFile('exe2b15x.zip', 'r') as myzip:
	mydata = myzip.read('bin/exe2bin.com')
with open('../tools/exe2bin.com', 'wb') as myfile:
	myfile.write(mydata)

os.remove('exe2b15x.zip')

# tasm
print 'downloading tasm ...'
urllib.urlretrieve('http://www.phatcode.net/res/280/files/tasm5.zip', 'tasm5.zip')

with zipfile.ZipFile('tasm5.zip', 'r') as myzip:
	myzip.extract('DISK1/UNPAK.EXE', 'tmp')
	myzip.extract('DISK1/CMDLINE.PAK', 'tmp')
	myzip.extract('DISK3/CMD16.PAK', 'tmp')

subprocess.call('dosbox -c "mount c ./tmp" -c "c:" -c "disk1\\unpak x disk1\\cmdline.pak" -c "disk1\unpak x disk3\\cmd16.pak" -c "exit"', shell=True)

shutil.copyfile('tmp/TASM.EXE', '../tools/tasm.exe')
shutil.copyfile('tmp/TLINK.EXE', '../tools/tlink.exe')
shutil.copyfile('tmp/DPMI16BI.OVL', '../tools/dpmi16bi.ovl')
shutil.copyfile('tmp/RTM.EXE', '../tools/rtm.exe')

shutil.rmtree('tmp/')

os.remove('tasm5.zip')