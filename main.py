import sys
import time
from datetime import datetime

for number in range(1, int(sys.argv[1]) + 1):
    time.sleep(1)
    print(datetime.now())
