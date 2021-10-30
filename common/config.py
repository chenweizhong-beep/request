# ***
# @autor CWZ
# ***
import configparser
import os


class ConfigIn:
    # 获取当前项目的绝对路径
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # print(BASE_PATH)
    # 拼接配置文件对的路径
    CONFIG_INI_PATH = os.path.join(BASE_PATH, 'config.ini')

    # print(CONFIG_INI_PATH)

    def __init__(self, file_name=CONFIG_INI_PATH):
        # 默认配置文件的路径是CONFIG_INI_PATH
        self.config_file_name = file_name
        # 初始化实例
        self.cf = configparser.ConfigParser()
        # 读取配置文件
        self.cf.read(self.config_file_name)

    def get_value(self, section, option):
        '''
        获取配置文件中的值方法
        :param section:
        :param option:
        :return:
        '''
        value = self.cf.get(section=section, option=option)
        return value

    def set_value(self, section, option, value):
        '''
        修改配置文件中的值的方法
        :param section:
        :param option:
        :param value:
        :return:
        '''
        self.cf.set(section=section, option=option, value=value)
        with open(self.config_file_name, 'w') as f:
            self.cf.write(f)


# 配置单例模式
cf = ConfigIn()
if __name__ == '__main__':
    cf.set_value('logs', 'file_name', 'r')
    print(cf.get_value('logs', 'file_name'))
