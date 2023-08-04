def convert_to_matrix_row_format(data):
    # stripping from unnecessary symbols
    data = data[1:-3]  # remove byte symbol
    l = data.split(';')  # converts each parameter into separate list element
    result = ''
    for i in range(len(l)):
        val = l[i].split(':')
        print(val[1])
        result += val[1]
        if i < len(l) - 1:
            result += ':'
    return result

example = "b'mid:-1;x:-100;y:-100;z:-100;mpry:0,0,0;pitch:-1;roll:0;yaw:0;vgx:0;vgy:0;vgz:0;templ:66;temph:69;tof:10;h:0;bat:58;baro:101.66;time:0;agx:-32.00;agy:-10.00;agz:-998.00;\r\n"
print(convert_to_matrix_row_format(example))


"""
# stripping from unnecessary symbols
t1 = example[1:] # remove byte symbol
t1 = t1[:-3]
print(t1)
l = t1.split(';') # converts each parameter into separate list element
print(l)
temp = ''
for i in range(len(l)):
    val = l[i].split(':')
    print(val[1])
    temp += val[1]
    if i < len(l) - 1:
        temp += ':'
"""


