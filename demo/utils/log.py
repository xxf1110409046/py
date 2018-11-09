import os
import logbook
from logbook.more import ColorizedStderrHandler


#判断根目录下是否有Log文件
path = os.path.join('log')
#根据路径获取文件Boolean值
boolean = os.path.exists(path)
#判断文件是否存在，不存在，生成该文件
if not boolean:
    os.mkdir('log')
else:
    print('已经存在log文件')
#print(path)
#print(boolean)

#通过logbook实例化操作句柄，get_logger
def get_logger(name='接口',level=''):
    #设置时间格式
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False,level=level).push_thread()
    logbook.TimedRotatingFileHandler(os.path.join(path,'%s.log' % name),
                                     date_format='%Y-%m-%d-%H',bubble=True,encoding='utf-8').push_thread()
    #print('join_path =' + os.path.join(path,'%s.log' % name))
    return logbook.Logger(name)
LOG = get_logger(name='接口',level='INFO')
#LOG.info('成功返回结果')

