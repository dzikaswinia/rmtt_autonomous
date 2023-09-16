import concurrent.futures
import sensor_data_converter as sensor
import circus_mode_2pads


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(circus_mode_2pads.test)
        f2 = executor.submit(sensor.run_sensor_data_converter)

        concurrent.futures.wait([f1, f2])
