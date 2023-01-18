Instructions
pipenv shell
pipenv install(optional) ------> install dependencies
python manage.py runserver --noreload  ----->to run server on http://127.0.0.1:8000/

Routes:
News App ---- http://127.0.0.1:8000/app/news

News API ---- http://127.0.0.1:8000/api/news

News App Detail/comments ---- http://127.0.0.1:8000/app/news/item_id e.g. 
http://127.0.0.1:8000/app/news/34339640

News Detail/Delete/Update API ---- http://127.0.0.1:8000/api/news/<int:pk> 
e.g News API ---- http://127.0.0.1:8000/api/news/1

scheduled job - newsappAPI/hackernewsapi.py