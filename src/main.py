#-*- coding:utf-8 -*-
import sys

from URMessageChannel import TimerEvtHandle, logconfig, init_base
import wpe    #User module, such as "hello" module

###############################################################################
#Predefined event loop class，add custom operation in timerHandle method
###############################################################################
class startWork(TimerEvtHandle):
    def __init__(self, sec):	#Trigger timer after "sec" seconds
        self.base = init_base()
        TimerEvtHandle.__init__(self, self.base, sec)
	
    def timerHandle(self, evt, userdata):
        #add custom operation before "self.startTimer", such as "hello.print_hello()"
        wpe.Sent_toServer()
        self.startTimer()

#################################################################################
#need implements start_app() by yourself，add custom operation in function body，
#if you want to use timer event and loop your operation, you must extends 
#"TimerEvtHandle" to implement your event loop.
#################################################################################
def start_app():
    pass

def usage():
    print 'add help info'
    sys.exit(255)
	
def main(argv=sys.argv):
    import getopt

    short_args="h:"
    long_args=[
        "help",
    ]
    arguments = argv[1:]
    try:
        opts, args = getopt.getopt(arguments, short_args, long_args)
    except:
        usage()

    for option, value in opts:
        if option in ('-h', '--help'):
            usage()
    logconfig('info')	#set log level，such as"info"
    #instantiates a startWork object and start event loop or invoke start_app() directly
    work = startWork(60)
    work.start()
		
if __name__=='__main__':
    main()
