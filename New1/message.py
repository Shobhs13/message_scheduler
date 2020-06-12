from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from messagesch import newmessage

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(newmessage, 'interval', seconds=10)

sched.start()