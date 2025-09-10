#!/usr/bin/env python3

import os

def clear_cache():
    os.system("sync")
    os.system("echo 3 | sudo tee /proc/sys/vm/drop_caches")
    os.system('notify-send "Limpeza de RAM" "✅ Cache liberado!"')

if __name__ == "__main__":
    clear_cache()
