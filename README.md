## IOT-Project

# Clone the project

then cd backend/
then pip install -r requirements.txt

# Start Server

cd backend/src/

python3 manage.py createsuperuser --settings=core.settings
python3 manage.py runserver --settings=core.settings

then in the url, write /admin to access admin