import concurrent.futures
import sensor_data_converter as sensor
from program import playground as pl
import start


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(start.start)
        #f2 = executor.submit(pl.print_pad_detected_value())
        f3 = executor.submit(sensor.run_sensor_data_converter)

        concurrent.futures.wait([f1, f3])
        #concurrent.futures.wait([f3])
