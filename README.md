# Locust Course Readme

The main goal of this repository is to show what I learn during the course https://www.udemy.com/course/performance-testing-using-locust/learn/lecture/20253594#overview,

## Installation

You need to install python and locust library

You must go on the python website and download it.

Confirm installation:
```bash
python --version
```

Install locust
```bash
pip install locust
```

## Command line
locust -f <file_name>.py
At web page search for localhost:8089

You can define host by command line:
```bash
locust -f <file_name>.py --host="<host_name>"
```

If you have more than 1 Class you can choose which one you want to run
```bash
locust -f <file_name>.py <class_name>
```

Execution in headless  mode
```bash
locust -f <file_name>.py -u <users> -r <user_rate> -t <time><ms,s,min,h> --headless --logfile logfiles/<log_file_name>.log --loglevel DEBUG
```

https://docs.locust.io/en/stable/config-options.html#

--headless

-u, --users

-r, --hatch-rate

-t, --run-time

--logfile

--only-summary : Disable periodic printing of request stats during headless run

## Locust Documentation
https://docs.locust.io/en/stable/index.html

## License

[MIT](https://choosealicense.com/licenses/mit/)