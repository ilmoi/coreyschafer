# we're going to be using cron table or "crontab" for short

# see running jobs
crontab -l

# edit jobs
crontab -e

 """
 * first star = minute (0-59)
 * = hour (0-23)
 * = day of month (1-31)
 * = month (1-12)
 * = day of week (0-6) (on some systems 7 is also a sunday)

so ***** means run a job every minute every hour every day every month every week
a lot of jobs!!

30 5 * * * = will run the command on 5:30 every day

0 0 * * 1 = will run at midnight on every monday

0 0 1,15 * * = will run at midnight on the 1st and 15th of every month
* * 1,15 * * = this would be wrong, this would run the command every minute on the 1st and 15th of the month

*/10 * * * * = will run every 10min (so with /10 we're specifying an interval)
0 0 */3 * * = midnight every 3 days

0 0-5 * * * = every hour between 0 and 5am daily

*/30 9-17 * * 1-5

this helps -> https://crontab.guru/#0_*/4_*_*_*

 """

crontab -u callum -e #allows us to edit another user's crontab

crontab -r #empties your crontab file

"""
Some questions I have:
1. Does this thing boot automatically with restarts?
2. Does it run even when the selected user logged off?

"""
