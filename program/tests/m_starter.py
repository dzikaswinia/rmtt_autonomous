import multiprocessing
import time
import concurrent.futures
import test_global as tg
import p2

def counting():
    for i in range(20):
        print(i)
        print(f'[f1] pad detected: {tg.PAD_DETECTED}')
        time.sleep(3)

def dummy_sensor():

    land = False
    for i in range(10):
        sensor_data = input("is there a pad?")
        if sensor_data == str(1):
            tg.PAD_DETECTED = True
        print(f'[f2] pad detected: {tg.PAD_DETECTED}')

def start_p2():
    p2.main()


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(counting)
        f2 = executor.submit(dummy_sensor)
        f3 = executor.submit(start_p2)

        concurrent.futures.wait([f1, f2, f3])



    """
    p2 = multiprocessing.Process(target=dummy_sensor())
    p1 = multiprocessing.Process(target=counting(2))

    p2.start()
    p1.start()

    p1.join()
    p2.join()
    """


