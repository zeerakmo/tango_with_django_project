import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():

	python_cat = add_cat('Python', views=128, likes=64)
	add_page(cat=python_cat, title='Official Python Tutorial', url='http://docs.python.org/2/tutorial/', views=10)
	add_page(cat=python_cat, title='How to think like a CS', url='http://www.greenteapress.com/thinkpython/"', views=11)
	add_page(cat=python_cat, title='Learn Python in 10 mins', url='http://www.korokithakis.net/tutorials/python/', views=12)
	
	django_cat = add_cat("Django", views=64, likes=32)
	add_page(cat=django_cat,title="Official Django Tutorial",url='https://docs.djangoproject.com/en/1.9/intro/tutorial01/', views =3 )
	add_page(cat=django_cat,title="Django Rocks",url='http://www.djangorocks.com/',views =13)
	add_page(cat=django_cat,title="How to Tango with Django",url='http://www.tangowithdjango.com/',views =5)
	
	frame_cat = add_cat("Other Frameworks", views=32, likes=16)
	add_page(cat=frame_cat,title="Bottle",url='http://bottlepy.org/docs/dev/',views =4)
	add_page(cat=frame_cat,title="Flask",url='http://flask.pocoo.org',views =7)
	
	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    return c


if __name__ == "__main__":
    print("Populating the DB witht the script........")
    populate()
