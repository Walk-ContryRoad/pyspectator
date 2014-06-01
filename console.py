import subprocess
import platform
from time import sleep

clear_command = "cls" if platform.system() == "Windows" else "clear"


def clear():
    subprocess.call(clear_command, shell=True)


def start(computer):
    print('Start monitoring system...')
    # Show system info for ~16 seconds
    for _ in range(16):
        clear()
        # Display general information about computer
        print('Hostname: ' + str(computer.hostname))
        print('OS: ' + str(computer.os))
        print('CPU name: ' + str(computer.processor.name))
        print('Amount of CPU cores: ' + str(computer.processor.count))
        print('Boot time: ' + str(computer.boot_time))
        print('Used CPU: ' + str(computer.processor.percent))
        cpu_temperature = 'unknown' if computer.processor.temperature is None else str(computer.processor.temperature)
        print('CPU temperature: ' + cpu_temperature)
        # Display memory info
        print('Nonvolatile memory: used {0} from {1}, {2}'.format(
            computer.nonvolatile_memory.available,
            computer.nonvolatile_memory.total,
            computer.nonvolatile_memory.percent
        ))
        print('Virtual memory: used {0} from {1}, {2}'.format(
            computer.virtual_memory.available,
            computer.virtual_memory.total,
            computer.virtual_memory.percent
        ))
        sleep(1)
    clear()
    print('Shutdown monitoring system...')