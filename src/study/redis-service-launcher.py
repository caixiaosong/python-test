# coding=utf-8
import subprocess


def startRedisServiceByCallFull():
    ''' 通过全路径启动redisServie,测试通过,call是阻塞调用不推荐'''

    redis_service_cmd_full_path = "D:/redis-3.21/redis-server.exe D:/redis-3.21/redis.windows-service.conf"
    child = subprocess.call(redis_service_cmd_full_path)
    print("线程恢复阻塞的时候，我被调用！")


def startRedisServiceByPopen():
    '''想要通过设置cwd调用的,必须设置shell=True才能实现调用.正确的启动程序'''

    cwd = "D:/redis-3.21/"
    redis_service_cmd = "redis-server.exe redis.windows-service.conf"
    # shell=True调用了shell启动。如果是调用exe文件则不用使用shell=True
    # 使用shell是存在风险的。因为直接调用了shell所以如果传入的命令是用户输入，
    # 那么这些输入在没有校验的情况下可能是致命的。所以命令不应该接收用户输入。
    child = subprocess.Popen(redis_service_cmd, cwd=cwd, shell=True)


if __name__ == "__main__":
    # TestPopen()
    # startRedisServiceByCallFull()
    startRedisServiceByPopen()
    print("这个窗口一闪而过,应该是redis service 已经启动过了,服务一次只能启动一个")
    print("在这里启动的程序,不能关闭这个脚本,如果脚本关闭了,这个进程的子进程也会关闭,所以全部都会关闭")
