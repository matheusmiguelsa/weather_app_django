How to use if (In your localhost)
- To view the weather in your city, you must type the city in the input field and click on Submit button.

How to run this

Type the code below in your terminal

git clone https://github.com/matheusmiguelsa/weather_app_django.git

After clone this repository, you might install the virtual machine(venv) and the libs before run this:

In Linux:
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py makemigrations
6. python manage.py runserver

So, access in your favorite browser: https://localhost:8000

In Windows:
1. python -m venv venv
2. cd venv/Scripts && activate
3. cd .. && cd ..
4. pip install -r requirements.txt
5. python manage.py migrate
6. python manage.py makemigrations
7. python manage.py runserver

So, access in your favorite browser: https://localhost:8000

In Docker:
1. docker compose build
2. docker compose up

So, access in your favorite browser: https://localhost:8000