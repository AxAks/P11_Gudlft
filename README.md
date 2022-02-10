# P11_Gudlift
## Study project for testing

## Chapters

1. [Presentation](#presentation)
2. [Prerequisites (for developers)](#prerequisites)
3. [Installation](#installation)
4. [Execution](#execution)
5. [Usage](#usage)
6. [Generation of a code review report (for developers)](#generation_of_a_code_review_report)
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
- At the Project root level: 
('venv_name') $ export set FLASK_APP=server 
-> sets the environment variable
('venv_name') $ python -m flask run
-> run the program



Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set
      the file to be <code>server.py</code>.
      Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

    You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>
      python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

Current Setup

   The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around
   having a DB until we actually need one. The main ones are:

    competitions.json - list of competitions
    clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will
      accept for login.

Testing

      You are free to use whatever testing framework you like-the main thing is that you can show what tests you are using.

      We also like to show how well we're testing, so there's a module called
   [coverage](https://coverage.readthedocs.io/en/coverage-5.1/) you should add to your project.
   coverage run -m pytest -v tests/tests_launcher.py (unitaires et integration)
      
   [pytest](https://docs.pytest.org/en/7.0.x/)
   python -m pytest -v tests/unit_tests/tests_launcher.py)
   

   
      [locust](http://docs.locust.io/en/stable/)
      locust -f locustfile.py --master
      locust -f locustfile.py --worker
 