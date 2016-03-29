import sched,time, datetime

timeout = 10
dt = 15

def setTimeout():
    global timeout, dt
    nu = datetime.datetime.today()
    timeout = (dt-nu.minute%dt)*60 - nu.second

def collect_data():
    global timeout
    setTimeout()
    now = datetime.datetime.today()
    print "current time = %s:%s:%s >> delay = %s" %(now.hour, now.minute, now.second, timeout)
    

s = sched.scheduler(time.time, time.sleep)
def schedule_data_acquisition(sc):
    collect_data()
    global timeout
    sc.enter(timeout,1, schedule_data_acquisition, (sc,))    # Re-do same action in timeout seconds.

collect_data()
s.enter(timeout, 1, schedule_data_acquisition, (s,))         
s.run()
