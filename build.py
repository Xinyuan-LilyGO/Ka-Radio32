
import os
import sys

# http://icecast.omroep.nl//3fm-sb-mp3
# export ESPTOOLS=/mnt/d/esp/esp-idf-3v3/esp-idf-v3.3/components/esptool_py/esptool/

PORT = '/dev/ttyS32'
ESPTOOLS = '/mnt/d/esp/esp-idf-3v3/esp-idf-v3.3/components/esptool_py/esptool/esptool.py'

def write_nvs():
    os.chdir("boards")
    os.system("pwd")
    os.system(" ./nvs_partition_generator.sh " + sys.argv[1])
    filename = str(sys.argv[1])
    try:
        pos = filename.index('.csv')
    except:
        print('error to format,is not csv file')
        print("format: python ./build.py xxxx.csv")
        os.chdir("../")
        pass
    else:
        os.system("python " +  ESPTOOLS + " -p "+  PORT+ " write_flash 0x3a2000 build/"+ filename[:pos]  +".bin")
        os.chdir("../")


def flash():
    os.system("make -j && make flash ESPPORT=" + PORT)

def monitor():
    os.system("make monitor ESPPORT=" + PORT)


if __name__ == "__main__":
    flash()
    if len(sys.argv) == 2:
        write_nvs()
    monitor()


