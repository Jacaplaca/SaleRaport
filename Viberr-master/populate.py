import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','website.settings')

import django
# Import settings
django.setup()

import random
from music.models import Album, Klienci
from faker import Faker
from faker import Factory
fake = Factory.create('pl_PL')
fakegen = Faker()


# for _ in range(0, 10):
#     print (fake.name())

aktywnosc = ['Praca biurowa', 'Wizyta', 'Urlop', 'Choroba']
nowyklient = ['Nawozy', 'Zboża']
tolubto = [0,1]


def random_act():
    a = random.choice(aktywnosc)
    return a

def random_nowyklient():
    a = random.choice(nowyklient)
    return a

def random_tolubto():
    a = random.choice(tolubto)
    return a





def populate(N=55):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Get Topic for Entry
        akt = random_act()
        nk = random_nowyklient()
        tt = random_tolubto()
        # Create Fake Data for entry
        # fake_url = fakegen.url()
        # fake_date = fakegen.date()
        # fake_name = fakegen.company()
        fake_name = fake.name()
        fake_city = fake.city()
        fake_kod = fake.postcode()
        fake_termin = fake.date_object()
        fake_bool = fake.random_int(min=0, max=1)
        fake_fifty = fake.boolean(chance_of_getting_true=50)
        fake_boo_null = fake.null_boolean()
        fake_random = fake.random_element(elements=(1,0))
        fake_nip = fake.ean8()
        fake_uwagi = fake.text(max_nb_chars=200)
        fake_numerwizyty = fake.random_int(min=1, max=3)
        fake_user = fake.random_int(min=4, max=6)
        fake_godzinastart = fake.time(pattern="%H:%M:%S")
        fake_godzinakoniec = fake.time(pattern="%H:%M:%S")
        fake_klient = fake.random_int(min=1, max=35)

        # Create new Webpage Entry
        alb = Album.objects.get_or_create(klient_id=fake_klient,  godzinastart=fake_godzinastart, godzinakoniec=fake_godzinakoniec, user_id=fake_user, numerwizyty=fake_numerwizyty, uwagi=fake_uwagi, zakonczono=fake_fifty, lunch=fake_random, sprzedaz=fake_bool, zamowienie=tt, aktywnosc=akt, nowyklient=nk, kodpocztowy=fake_kod, miejscowosc=fake_city, termin=fake_termin)[0]
        # klnt = Klienci.objects.get_or_create(nazwaklienta=fake_name, nipklienta=fake_nip)[0]
        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        # accRec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(58)
    print('Populating Complete')
