import logging
import config


class Command:
    def __init__(self, name, param):
        self.name = name
        self.param = self.set_param(param, name)
        self.__exec_time = self.set_exec_time(name)
        logging.debug(f"[command | init] param: {self.param}, name: {self.name}")

    def set_param(self, param, name):
        if name == "cw" or name == "ccw":
            valid_param = [x[1] for x in config.CMDS if x[0] == self.name][0]
            if param in valid_param:
                self.param = param
                return param
            else:
                logging.error(f"Invalid parameter ({param}) for command \"{self.name}\"!"
                              f" Valid parameters are: {valid_param} ")
        elif name == "takeoff" or name == "land":
            # self.param = None
            return None
        else:
            self.param = param
            logging.debug(f"[command | set_param] param: {param}, name: {name}, "
                          f" get_param: {self.get_param()}")
            return param

    def get_param(self):
        return self.param

    def get_exec_time(self):
        return self.__exec_time

    def set_exec_time(self, cmd_name):
        return [x[2] for x in config.CMDS if x[0] == cmd_name][0]

    def to_string(self):
        if self.name == "takeoff" or self.name == "land":
            return self.name
        else:
            return self.name + " " + str(self.get_param())


# ------------------- TESTS ---------------------
"""
cmd_to = Command("takeoff", "")
cmd_land = Command("land", "")
print(cmd_to.to_string())
print(cmd_land.to_string())
"""

"""
#cmd = Command("back", 60)
cmd_f = Command("forward", 40)
#cmd_r = Command("right", 40)
#cmd_l = Command("left", 20)
cmd_cw = Command("cw", 90)
#print(f'cmd name: {cmd.name}, param: {cmd.get_param()},'
#      f' exec time: {cmd.get_exec_time()}')
#print(f'cmd as string: {cmd.to_string()}')
print(f'cmd as string: {cmd_f.to_string()}')
#print(f'cmd as string: {cmd_r.to_string()}')
#print(f'cmd as string: {cmd_l.to_string()}')
print(f'cmd as string: {cmd_cw.to_string()}')

"""
