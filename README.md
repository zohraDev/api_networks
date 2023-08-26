# api_networks_test
# Mobile Network 
# Small API project that we can request with a textual address request and get 2G/3G/4G network coverage for each operator (if available) in the response.

API Documentation:
An external API is used to calculate the coordinate(4326 WGS 84) from an address. You can check the documentation how to use is it: https://adresse.data.gouv.fr/api-doc/adresse.
Requirements
	•	python: version 3.9
	•	fastapi: version 0.101.1
	•	sqlite
	•	complete packages used are in requirements.txt

Installation:
Before make sure you have on your machine:
	- Python ( at least version 3.8): « python -V » : command to check the version python if its installed;
	- Virtual environment: pipenv is used in this project(https://pypi.org/project/pipenv/). You could also use any other virtual environment to run the program
	- Git:  git --version : to check your git version if its installed or you could download it at https://git-scm.com/downloads
	
Commands:
How to run: 
	open a terminal and : 
	1	Clone the repository on the terminal or command prompt : git clone https://github.com/zohraDev/api_networks_test.git
	2	Create a virtual environment: 
		NOTE: « if you choose other virtual environment refer to own documentation how  to install and activate the victual environment )»
	◦	cd api_networks_test : to access the folder
	◦	pipenv install  to create the virtual environment
	1	Activate the virtual environment:
	◦	pipenv shell
	2	Install the packages with pip: pip install -r requirements.txt 
	3	Create database and load data from CSV file:

			1. in the file « bash_file.bash » update the environment variable PROJETC_PATH: the path to the directory «api_networks_test»		
			2. cd api_networks_test/
			3.source bash_file.bash
			4.python3  db/load_csv_file.py  for unix/macos
			   py  db/load_csv_file.py  for windows 
			  
 			  ==> wait until the end of the process

        
	6	Run the program :
	◦	  open a terminal and execute : uvicorn app:app --reload --host localhost --port 8000
			  you could choose another port number
	    

	
External file: mobile_operator.csv has been used to locate network provider and it's coverage which should be uploaded to the database.













