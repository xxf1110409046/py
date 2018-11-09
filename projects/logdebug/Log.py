#coding = utf-8
import os
import logbook
from logbook import Logger,StreamHandler,FileHandler,TimedRotatingFileHandler
from logbook.more import ColorizedStderrHandler


#定义日志格式
def log_type(record,handler):
    log = "[{date}][{level}][{filename}][{func_name}][{lineno}]{msg}".format(
        date=record.time,  # 日志时间
        level=record.level_name,  # 日志等级
        filename=os.path.split(record.filename)[-1],  # 文件名
        func_name=record.func_name,  # 函数名
        lineno=record.lineno,  # 行号
        msg=record.message  # 日志内容
    )


log_dir = os.getcwd()
print('123')
if os.path.exists(log_dir):
    print('文件存在')
else:
    print('文件不存在')
# print(path)


#日志打印到屏幕
log_led = ColorizedStderrHandler(bubble=True) #获取打印在屏幕上的句柄
log_led.formatter = log_type #log打印的格式设置

# 日志打印到文件
log_file = TimedRotatingFileHandler(os.path.join(log_dir,'%s.log' % 'log'),date_format='%Y-%m-%d',bubble=True,encoding='utf-8')
log_file.formatter = log_type

#脚本日志
run_log = Logger("script_log")
def init_logger():
    logbook.set_datetime_format("local")
    run_log.handlers = []
    run_log.handlers.append(log_file)
    run_log.handlers.append(log_led)

logger = init_logger()

