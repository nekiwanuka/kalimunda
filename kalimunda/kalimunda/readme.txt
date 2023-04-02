Set up the virtual environment
we use pip install venv
Activate the virtual environment


Configuring Django
from the venv, we install Django, we create a project in Django using Django-admin 
we create an application in Django using manage.py
In the second folder we install our application in he insalled apps

In the seetings.py , you specify where your static and templates files should be found
Still from the settings, you specify the urls for login and logout redirection
If you're going to use crispy-bootstrap, you include it in the installed Apps section, and crispy-forms
dont forget to install migrate for the first time
run migrate for installed apps in django (this will create for you a database)
create a superuser
then run your server using manage.py

serving a custom template and static folders
    create a directory in the Apps folder called static 'static' for the images, css and javascript folders
    create a 'templates' directory for the html files
    from the urls files of the projects 'directory', specify to django to use the urls in the applicationfrom the urls files in the application
    we determine the url string and how it will be responded too
    views filesa are functions that match , recieve and respond to templates requests.
    from the urls file in the appp, we determine the url string and how it will be responded to ny the 'view'
    we attach a url request string to its corresponding view for response
    In Django, some views are in buit, so we jsut need to re-use them, for example the 'login' ang 'logout'

        note: before you even start the projet, you should be knowing which url you need. because a url is supposed to
        have a view, which is served also in the templates. urls mean the route or the navigation to html page requested for.
        
ABOUT SERVERS:
servers work with daemons, these are fucntions at a server level, they run and never stop. they keep waiting for requests.
in order to facilitate the webclient through a form to post data or retrieve data we need a third party such as python, c sharp
ruby or php. 

USING PYTHON AS THE THIRD PARTY ON THE SERVER TO STORE DATA, IN THE database
THE DECSRIPTION OF THE DATABASE IS FOUND IN THE MODELS.PY (modles mean something connected to database.)

REQUIREMENTS TO MODEL A STOCK, PRODUCT
MODELLING AN OBJECT CALLED 'PRODUCTS'
1. Category
2. Product name
3. The total Qauntity recieved
4. Batch number
5. Total qauntity issued(sales out) and recieved(stock in)
6. Unit Price

MODELLING sales:
1. Item should
2. Qauntity sold
3. Issued to (buyer)
4. Amount recieved

GO TO MODELS TO TURN THIS INTO A RUNNING CODE:

class Category(models.Model):
    name = models.CharField(max_length = 50, null = True, blank = True) 
    def __str__(self): # here were are giving our 
        return self.name


THEN GO TO THE TERMINAL AND MIGRATE, FIRST  USE CODE, 'python3 manage.py makemigrations
then migrate using python3 manage.py migrate

