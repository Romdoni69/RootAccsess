import os
import time as t
import sys

os.system('clear')
t.sleep(0.1)
logo= '''
\033[92m
          +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMMm\033[0m:\033[92mNMMMMMMN\033[0m:\033[92mmMMd`
      hMMMMMMMMMMMMMMMMMMh
  \033[92m..  yyyyyyyyyyyyyyyyyyyy  ..
\033[92m.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.
\033[92m:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs'''


print (logo)
os.system('pkg install wget openssl-tool proot -y')
os.system('hash -r')
os.system('wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh')
os.system('bash kali.sh')
os.system('mv start-kali.sh root')
os.system('mv root ../usr/bin')
os.system('mv kali-fs ../usr/bin')
os.system('mv kali-binds ../usr/bin')
os.system('rm kali.sh')
t.sleep(1)
print ('''type root to use''')
t.sleep(1)
raw_input('Press Enter To Exit !!')
os.sys.exit()
