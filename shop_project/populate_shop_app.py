import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_project.settings')
import django
django.setup()


import random
from faker import Faker
from shop_app.models import Customer, Product

# CONSIGNE
# creez 2 fonctions :
#   1. cree 1000 faux clients
#   2. cree 50 faux produits

fakegen = Faker()

def generate_brand():
	brands = ['Nike', 'Adidas', 'Rebook', 'Jordan', 'Balenciaga', 'Timberland', 'Scholl' ,'Tatan', 'Asics', 'Geox']
	index = random.randint(0, 9)
	return brands[index]


def generate_customers():
	for customer in range(0,1000):
		customer = Customer.objects.get_or_create(first_name=fakegen.first_name(), last_name=fakegen.last_name(), email=fakegen.email(), password=fakegen.password(), product=product)[0]
		print(customer)

def generate_product():
	for product in range(0, 50):
		price = random.randint(30, 150)
		brand = generate_brand()
		product = Product.objects.get_or_create(name=brand, price=price, description=fakegen.text(max_nb_chars=800))[0]
		print(product) 

def generate_maillots():
    for maillot in range(0,150):
        maillotprice = random.randint(79,499)
        maillot_brand = generate_maillot_brand()
        maillot = Maillot.objects.get_or_create(name=maillot_brand, description =fakegen.text(max_nb_chars=400),price=maillotprice )
        print(maillot)


def populate():
	# generate_customers()
	generate_product()
  
 
if __name__ == '__main__':
	print('starting populate...')
	populate()
	print('done populating')