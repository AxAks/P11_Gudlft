# P11_Gudlift
## Study project for testing

## Chapters

1. [Presentation](#presentation)
2. [Prerequisites (for developers)](#prerequisites)
3. [Installation](#installation)
4. [Execution](#execution)
5. [Testing](#testing)
***

# 1. Presentation <a name="presentation"></a>
This project is a fork of the original Gudlift application available
at : https://github.com/OpenClassrooms-Student-Center/Python_Testing

This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is
the keep things as light as possible, and use feedback from the users to iterate.
***

# 2. Prerequisites (for developers) <a name="prerequisites"></a>
This project uses the following technologies:

   - Python v3.9+

   - [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)
     This ensures you'll be able to install the correct packages without interfering with Python on your machine.
     Before you begin, please ensure you have this installed globally. 

   - [Flask](https://flask.palletsprojects.com/en/2.0.x/en/)
***

# 3. Installation <a name="installation"></a>
__Download the project:__    
_Via Git_      
$ git clone https://github.com/AxAks/P11_Gudlft.git    
    
_Via the Web_     
- Visit the page : https://github.com/AxAks/P11_Gudlft 
- Click on the button "Code"     
- Download the project     

__Linux / Mac__       
in the project directory in a shell:       
_create the virtual environment_       
$ python3.9 -m virtualenv 'venv_name'        
_activate the environment:_        
$ source 'venv_name'/bin/activate         
_install project requirements:_       
$ pip install -r requirements.txt         
  
__Windows__    
in the project directory in a shell:        
_create the virtual environment_      
$ virtualenv 'venv_name'      
_activate the environment:_     
$ C:\Users\'Username'\'venv_name'\Scripts\activate.bat       
_install project requirements:_            
$ pip install -r requirements.txt
***


#4. Execution <a name="execution"></a>    
_activate the environment:_       
$ source 'venv_name'/bin/activate    
    
_launch the app:_    
(terminal)    
- At the Project root level:     
('venv_name') $ export set FLASK_APP=server     
-> sets the environment variable    
('venv_name') $ python -m flask run    
-> run the program: then reachable at http://localhost:5000     
     
The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around    
having a DB until we actually need one. The main ones are:    
- the JSON DB file database.json     
    
# 5. Testing <a name="testing"></a>    
(virtual environment must be activated !)    
    
_Unit and integration Tests_    
The tests can be run with pytest    
The main testing environment (code and sample data) is located in the folder "tests"     
It contains:    
- The unit tests    
- The integration tests    
    
A "test_launcher" file is available to launch both series of tests at once  
using the following command:    
->   python -m pytest -v tests/tests_launcher.py    
or  
-> python -m pytest -v [testfile1_path] [testfile2_path] [...]  
    
or separately:  
->   python -m pytest -v tests/integration_tests/integration_tests.py   
->   python -m pytest -v tests/unit_tests/*     
(unit test are separated in different modules sorted by route)  
More info about pytest at :[pytest](https://docs.pytest.org/en/7.0.x/)  
    
    
We also like to show how well we're testing, so the project contains a module called:   
   [coverage](https://coverage.readthedocs.io/en/coverage-5.1/)    
Basic run oif tests with coverage rate, use the following command:   
coverage run -m pytest -v tests/tests_launcher.py (unit tests and integration tests at once)    
    
You can also generate a HTML report using the command:  
-> coverage html    
    
     
Performance test are run under the module locust ( integrated in the project with locustfile.py as config file)    
      [locust](http://docs.locust.io/en/stable/)    
    
Basic run of locust    
-> locust -f locustfile.py    
    
Basic run of locust from within the project with two threads    
This enables to save CPU usage if needed.    
Using two differents terminals:    
-> locust -f locustfile.py --master (to set the master thread)       
-> locust -f locustfile.py --worker (to set the workers)     
            
The performance tests are then reachable at : http://localhost:8089/       
(The app server must be launched)      
You can set the user's peak and the spawn rate you wish     
Enter the address of the app : http://localhost:5000    
And Launch    
-> the tests calls all routes and evaluates the performance.