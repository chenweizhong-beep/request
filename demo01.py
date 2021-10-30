# ***
# @autor CWZ
# ***
import datetime
import os

if __name__ == '__main__':
    b = "logs"
    a = b + "_" + str(datetime.date.today()) + ".log"
    print(a)
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # BASE_PATH_1 = os.path.dirname(os.path.realpath(__file__))
    # ROOT_PATH = os.getcwd()
    print(BASE_PATH)

    c = os.path.join(BASE_PATH, "logs")
    print(c)
    if not os.path.exists(c):
        os.makedirs(c)
        print('创建文件夹成功')