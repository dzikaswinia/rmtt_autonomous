import concurrent.futures
import circus_mode_cv as cmc
import stream


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(cmc.start)
        f2 = executor.submit(stream.run_stream)

        concurrent.futures.wait([f1, f2])
