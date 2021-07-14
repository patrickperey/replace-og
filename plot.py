#!/usr/bin/python3
import subprocess
import shlex
import os
def launch(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if str(output.decode()).find('Started copy to') == 0:
            os.system("find /path/to/plots -name 'plot-k32*' ! -newermt '2021-06-29 10:00:00' -delete -quit")
        if output != '':
            print(output.decode())
    rc = process.poll()
    return rc

launch("./build/chia_plot -n <numberofplots> -r <nrthreads> -t /temp/1 -2 /temp/2 -d /path/to/plots/ -c <yourpoolkey>  -f <yourfarmerkey>")
