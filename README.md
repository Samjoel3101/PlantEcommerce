# PlantEcommerce
An Ecommerce Platform for buying and selling plants. 

Requirements:
    * pipenv 
    * npm 
    
Commands to setup the project:
```
  git clone https://github.com/Samjoel3101/PlantEcommerce.git
  cd PlantEcommerce
  pipenv install 
  cd Django_React_Project/frontend
  npm install 
```
Commands to run the project:
```
   pipenv shell
   cd Django_React_Project
   python manage.py makemigrations 
   python manage.py migrate
   python manage.py migrate --run-syncdb
   python manage.py runserver localhost:8000
```
Now go to your browser and go to the url localhost:8000 where the project is hosted.  

If you are a Linux Os, then:
```
git clone https://github.com/Samjoel3101/PlantEcommerce.git
cd PlantEcommerce
sh setup_project.sh 
sh run_project.sh
```

