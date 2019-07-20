# coding=utf-8
import subprocess


def TestPopen():
    '''直接调用dir命令 shell = True是必须的'''
    import subprocess
    p = subprocess.Popen("dir", shell=True)


def startRedisServiceByCallFull():
    ''' 通过全路径启动redisServie,测试通过'''

    redis_service_cmd_full_path = "D:/redis-3.21/redis-server.exe D:/redis-3.21/redis.windows-service.conf"
    child = subprocess.call(redis_service_cmd_full_path)
    print("startRedisServiceByCallFull successfully !")


def startRedisServiceByPopen():
    '''想要通过设置cwd调用的,必须设置shell=True才能实现调用.正确的启动程序'''

    cwd = "D:/redis-3.21/"
    redis_service_cmd = "redis-server.exe redis.windows-service.conf"
    child = subprocess.Popen(redis_service_cmd, cwd=cwd, shell=True)
    print("已经启动redis service")


if __name__ == "__main__":
    # TestPopen()
    # startRedisServiceByCallFull()
    startRedisServiceByPopen()
    print("这个窗口一闪而过,应该是redis service 已经启动过了,服务一次只能启动一个")
    print("在这里启动的程序,不能关闭这个脚本,如果脚本关闭了,这个进程的子进程也会关闭,所以全部都会关闭")
