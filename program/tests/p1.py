import time

import test_global as tg

PAD_DETECTED = False

if __name__ == "__main__":
    count = 0
    while not PAD_DETECTED:
        print(f"[p1] no pad detected {count}")
        print(f"[p1] \tPAD_DETECTED: {PAD_DETECTED}")
        time.sleep(1)
        count += 1

    print(f"[p1] Pad detected!")
    print(f"[p1] \tPAD_DETECTED: {PAD_DETECTED}")