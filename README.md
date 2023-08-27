# Mobile Network 
Small API project that we can request with a textual address request and get 2G/3G/4G network coverage for each operator (if available) in the response.
# API Documentation:
An [external API][link1] is used to calculate the coordinate(4326 WGS 84) from an address. You can check the documentation how to use is at: [API-DOC][link2].
# Requirements
- python: version 3.9
- fastapi: version 0.101.1
- sqlite (insttaled by default in pycharm IDE)
> Note: `complete packages used are in requirements.txt`

# Installation:
Before make sure you have on your machine:
- Python ( at least version 3.8): ``` python -V ``` : command to check the version python if its installed;
- Virtual environment: ``` pipenv ```  is used in this project, see pipen documentaion for more information[DOC][link3]. You could also use any other virtual environment to run the program
-  Git:  ``` git --version ```: to check your git version if it is installed, if not you could download it at https://git-scm.com/downloads

######   Commands: open a terminal and : 

1)   Clone the repository on the terminal or command prompt :  ``` git git clone https://github.com/zohraDev/api_networks_test.git ```
2) Access to the directory of the project : ``` cd api_networks_test ``` 
3) Create a virtual environment: ``` pipenv install ```
> Note: `If you choose other virtual environment refer to own documentation how  to install and activate the victual environment `

4) Activate the virtual environment: ``` pipen shell```,
5) Install the packages with pip: ``` pip install -r requirements.txt ```
6) Create database and load data from CSV file:   *Sites_mobiles.csv*:
    - In the file ``` bash_file.bash ``` update the environment variable ``` PROJETC_PATH ``` the path to the directory ``` api_networks_test ```	
    - ``` cd api_networks_test/ ```
	- ``` source bash_file.bash ```
	- ``` python3  db/load_csv_file.py ```  for unix/macos
	  ``` py  db/load_csv_file.py ``` for windows 
			  
 		> Note:  wait until the end of the process
7) Lunch the API :
	- Execute on terminal:  ``` uvicorn app:app --reload --host localhost --port 8000 ```
        > Note:  you could choose another port number
    
     - On on the browser enter the url: 
         ``` sh  
         http://0.0.0.0:8000/api_networks_test/?address="enter the adresse hier" 
          ``` 
         Example: 
        ```sh 
       http://0.0.0.0:8000/api_networks_test/address=502+Kernigou+29242+Ouessant
        ```
     
     - Or enter the the following URL on the prowser:
       ```sh 
       http://0.0.0.0:8000/docs
        ```
    
    
[link1]: <https://adresse.data.gouv.fr/api-doc/adresse>
[link2]: <https://adresse.data.gouv.fr/api-doc>
[link3]:<(https://pypi.org/project/pipenv/>
