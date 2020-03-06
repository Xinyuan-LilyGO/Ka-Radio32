
import os
import sys

# http://icecast.omroep.nl//3fm-sb-mp3
# export ESPTOOLS=/mnt/d/esp/esp-idf-3v3/esp-idf-v3.3/components/esptool_py/esptool/
PORT = '/dev/ttyS42'
ESPTOOLS = '/mnt/d/esp/esp-idf-3v3/esp-idf-v3.3/components/esptool_py/esptool/esptool.py'
if len(sys.argv) == 1:
    os.system("make -j && make flash monitor ESPPORT=" + PORT)
elif sys.argv[1] == 'erase':
    os.system("python "+ ESPTOOLS + " -p "+  PORT+ " erase_flash ")
# print(sys.argv.count)
elif sys.argv[1] == 'gen':
    # os.system("cd boards")
    os.chdir("boards")
    os.system("pwd")
    os.system(" ./nvs_partition_generator.sh " + sys.argv[2])
    # os.system("python " +  ESPTOOLS + " -p "+  PORT+ " write_flash 0x3a2000 build/ttgot14v1.2.bin")
    os.system("python " +  ESPTOOLS + " -p "+  PORT+ " write_flash 0x3a2000 build/ttgotm.bin")
    os.system("")