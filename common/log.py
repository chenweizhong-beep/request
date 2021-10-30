# ***
# @autor CWZ
# ***
import datetime
import logging
import os

from day04_reqursts.common.config import cf


class Log:
    # 生成的格式化器
    formatter = logging.Formatter("%(asctime)s|%(levelname)-6s|%(filename)s:%(lineno)-3s|%(message)s", "%Y-%m-%d-%H:%M")
    # 获取项目的根路径
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print(BASE_PATH)

    def __init__(self, name="logs"):
        '''
        初始化日志生成器
        '''
        self.log_name = name
        # 拼接路径
        a = os.path.join(self.BASE_PATH, 'logs')
        # 判断是否存在当前目录
        if not os.path.exists(a):
            # 不存在路径，创建该路径
            os.makedirs(a)
            print(f"创建{a}路径成功")
        else:
            print(f"该路径已存在")

        # 生成记录器，名字为"logs",其实是用logger调用，这里估计是给配置文件用的
        self.logger = logging.getLogger(name)
        # 默认等级都是最低级别的DEBUG，因为记录器的默认等级优先级高于处理器的
        self.logger.setLevel(logging.DEBUG)

    def set_stream(self):
        """
        初始化流处理器
        """
        # 生成处理器流处理器
        console_handle = logging.StreamHandler()
        # 默认等级为DEBUG
        console_handle.setLevel(logging.DEBUG)
        # 处理器添加格式，这里都添加同一个
        console_handle.setFormatter(self.formatter)
        # 记录器添加处理器，就拥有了屏幕输出的和文件输出的日志了
        self.logger.addHandler(console_handle)

    def set_file(self):
        """
        初始化文件处理器
        """
        # 生成日期：创造Log_2020-12-03.log文件
        a = self.log_name + "_" + str(datetime.date.today()) + ".log"
        # b是最终的文件路径，在根路径的logs文件夹下
        b = os.path.join(self.BASE_PATH, "logs", a)
        # 通过配置文件，获取log是w模式还是a的追加模式
        file_mode = cf.get_value("logs", "file_mode")
        # 文件处理器，文件名为demo.logs
        file_handle = logging.FileHandler(filename=b, mode=file_mode)
        # # 默认等级为INFO
        file_handle.setLevel(logging.INFO)
        # # 处理器添加格式，这里都添加同一个
        file_handle.setFormatter(self.formatter)
        # # 记录器添加处理器，就拥有了屏幕输出的和文件输出的日志了
        self.logger.addHandler(file_handle)

    def get_log(self):
        self.set_stream()
        self.set_file()
        return self.logger
'''
单例模式
'''
log = Log().get_log()
if __name__ == '__main__':
    log.info("111")
    log.error("222")
    log.warning("333")
    log.debug("444")

