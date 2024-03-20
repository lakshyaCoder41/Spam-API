# Spam-API
This API is built as per client requirements assigned for detecting and marking spam to any number.


Spftware & package requirements:
0. Install Python
1. Install djangorestframework
2. Install mysqlclient
3. Install PyJWT
4. Install django-cors-headers
5. MySql Server or Mysql workbench
6. Postman

Instructions to run:

1. Go into the spam_detector folder where you can find manage.py file.
2. Open the terminal or cmd within the directory.
3. Run the comand "python manage.py runserver".
4. You can populate data by using populate_data.py located in the "api" folder.
5. You can register user using some json data in the postman.
	Examples:
		To register user use following json:
					{   
   		 "username":"Lakshya Saxena",
    		"phone_number":"8318018654",
    		"email":"lakshyasaxenaai@gmail.com",
    		"password":"asdyhg"
		}

		To Login:
			{   
    			"email":"shukla0498@gmail.com",
    			"password":"asdyhg"
			}


Urls: localhost/login/
	localhost/register/
	localhost/numbers/
	localhost/search/


To mark any number spam visit: http://127.0.0.1:8000/numbers/

