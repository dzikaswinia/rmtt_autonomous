import concurrent.futures
import sensor_data_converter as sensor
import start


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(start.start)
        f3 = executor.submit(sensor.run_sensor_data_converter)

        concurrent.futures.wait([f1, f3])
