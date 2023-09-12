import socket
import logging

import config

root = logging.getLogger()
root.setLevel(logging.INFO)

""" Example decoded_data
mid:-1;x:-100;y:-100;z:-100;mpry:0,0,0;pitch:-1;roll:0;yaw:0;vgx:0;vgy:0;vgz:0;templ:62;temph:65;tof:10;h:0;bat:100;
baro:-16.41;time:0;agx:-23.00;agy:-3.00;agz:-999.00;
"""


def convert_to_matrix_row_format(item):
    # stripping from unnecessary symbols
    item = item[1:]  # remove byte symbol
    item = item[:-6]
    l = item.split(';')  # converts each parameter into separate list element
    result = ''
    for i in range(len(l)):
        val = l[i].split(':')
        result += val[1]
        if i < len(l) - 1:
            result += ':'
    return result


# ---------- detecting mission pads ---------------------------------------

def get_sensor_value(sensor_data_point, value_id):
    """
    Usage example: pad_id = get_sensor_value(data_point, "mid")
    :param sensor_data_point: string with whole sensor data (drone not controller)
    :param value_id: e.g. "mid" for mission pad id (see SDK documentation)
    :return: value for a given id (e.g. mid -> -1)
    """
    parts = sensor_data_point.split(";")
    for part in parts:
        if part.startswith(value_id + ":"):
            value = part.split(":")[1]
            return value


def run_sensor_data_converter():
    # setup
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 8890))

    while True:
        try:
            # print('trying to get sensor state')
            data, server = sock.recvfrom(1024)
            decoded_data = data.decode()
            #logging.info(f'[sensor data converter] sensor date: {decoded_data}')
            mid = get_sensor_value(decoded_data, "mid")
            print(mid)
            #x = get_sensor_value(decoded_data, "x")
            #print(f'x: {x}')
            #print(decoded_data)
            """
            logging.info(f'[sensor data converter] mission pad id: {mid},  '
                         f'config.PAD_DETECTED {config.PAD_DETECTED}')
                         
            """
            if mid != str(-1):
                config.PAD_DETECTED = True
                config.PAD = mid
            #config.CURRENT_X = x

        except Exception as err:
            print(err)
            sock.close()
            break


if __name__ == "__main__":
    run_sensor_data_converter()
    #str = "mid:20;x:-13;y:-100;z:-100;mpry:0,0,0;"
    #print(get_sensor_value(str, "x"))
