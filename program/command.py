import logging
import config


class Command:
    def __init__(self, name, param):
        self.name = name
        self.__param = self.set_param(param)
        self.__exec_time = self.set_exec_time(name)

    def set_param(self, param):
        valid_param = [x[1] for x in config.CMDS if x[0] == self.name][0]
        if param in valid_param:
            return param
        else:
            logging.error(f"Invalid parameter ({param}) for command \"{self.name}\"!"
                          f" Valid parameters are: {valid_param} ")
            return None

    def get_param(self):
        return self.__param

    def get_exec_time(self):
        return self.__exec_time

    def set_exec_time(self, cmd_name):
        return [ x[2] for x in config.CMDS if x[0] == cmd_name][0]


# ------------------- TESTS ---------------------
"""
cmd = Command("back", 660)
print(f'cmd name: {cmd.name}, param: {cmd.get_param()},'
      f' exec time: {cmd.get_exec_time()}')
"""
