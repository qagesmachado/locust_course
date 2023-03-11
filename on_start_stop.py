from locust import HttpUser, task, between, User

# locust -f on_start_stop.py -u 1 -r 1 -t 15s --headless --logfile logfiles/mylog.log --only-summary --loglevel DEBUG

class MyUser(User):
    wait_time = between(1,2) # min and max random wait in seconds

    # Deleting @task this method will be execute once in the begining
    # This def will be repeat by the number of users, 2 user then 2 logins 
    def on_start(self):
        print('I am loggin into URL') # print to simulate request

    @task  # what will be execute
    def doing_work(self):
        print('I am doing my work') # print to simulate request

    # Deleting @task this method will be execute once in the ending
    # This def will be repeat by the number of users, 2 user then 2 logout
    def on_stop(self):
        print('I am logout') # print to simulate request

