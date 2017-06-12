from django.contrib.auth.models import User
import django_filters
from django.http import JsonResponse, HttpResponse
from .models import Album
from django_filters import filters
from filters.views import FilterMixin
from . import views
import music.views
from django.shortcuts import get_object_or_404

UZYTKOWNICY = User.objects.all().order_by('username').values_list("id","username").distinct()
UZYTKOWNICY = list(UZYTKOWNICY)
# UZYTKOWNICY.insert(0, ('0','---------') )
UZYTKOWNICY.pop(3)

AKTYWNOWSCI = Album.objects.all().order_by('aktywnosc').values_list("aktywnosc","aktywnosc").distinct()
AKTYWNOWSCI = list(AKTYWNOWSCI)
# AKTYWNOWSCI.insert(0, ('','---------') )

MIASTA = Album.objects.all().order_by('miejscowosc').values_list("miejscowosc","miejscowosc").distinct()
MIASTA = list(MIASTA)
# MIASTA.insert(0, ('0','---------') )

KODY = Album.objects.all().values_list("kodpocztowy","kodpocztowy").distinct()
KODY = list(KODY)
# KODY.insert(0, ('0','---------') )

# TERMINY = Album.objects.all().values_list("termin","termin").distinct()
# IMPORTOWANA = music.views.ZMIENNAGLOBALNA
# INNEMIASTA = Album.objects.filter(aktywnosc='Urlop').values_list('miejscowosc', 'miejscowosc').distinct()

USER_IDs = []
AKTYWNOWSCI_IDs = []

def dynamiczne_filtrowanie(request):

    ajax_aktywnosc = request.GET.get('aktywnosc', False)
    ajax_user = request.GET.get('user', False)
    print ("To jest user ktory przyszedł %s." % ajax_user)
    print (type(ajax_user))

    global AKTYWNOWSCI_IDs
    global USER_IDs
    global uzytkownik
    print (ajax_aktywnosc)

    # if ajax_user == "user=":
    #     print ('jestem false')
    # else:
    #     print('nie jestm false')
    if not ajax_user:
        USER_IDs = []
    else:
        user_dane = ajax_user.split('&')
        USER_IDs = []
        for x in user_dane:
            y = x.split('=')[1]
            # USER_IDs = []
            if y=="0":
                user = User.objects.all()
                print(user)
            else:
                USER_IDs.append(int(y))

    print ("To sa uzytkownicy %s." % USER_IDs)
    print ("To jest aktywnoc ktora przyszla %s." % ajax_aktywnosc)


    if not ajax_aktywnosc:
        AKTYWNOWSCI_IDs = []
    else:
        aktywnosci_dane = ajax_aktywnosc.split('&')
        AKTYWNOWSCI_IDs = []
        print ("aktywnosci_dane %s." % aktywnosci_dane)
        for x in aktywnosci_dane:
            x = x.replace("+", " ")
            y = x.split('=')[1]
            AKTYWNOWSCI_IDs.append(y)
            # USER_IDs = []

    print ("To sa aktywnosci %s." % AKTYWNOWSCI_IDs)




    #     if y=="":
    #         user = User.objects.all()
    #         print(user)
    #         USER_IDs = []
    #         for a in user:
    #             USER_IDs.append(a.id)
    #             print (a.id)
    #         return (USER_IDs)
    #     else:
    #         USER_IDs.append(int(y))




    # if ajax_user != "user=":
    #     user_dane = ajax_user.split('&')
    #     USER_IDs = []
    #     for x in user_dane:
    #         y = x.split('=')[1]
    #         USER_IDs.append(int(y))
    # else:
    #     user = User.objects.all()
    #     USER_IDs = []
    #     for x in user:
    #         USER_IDs.append(x.id)




    # if ajax_aktywnosc != False:
    #     dane = ajax_aktywnosc.split("&")
    #     AKTYWNOWSCI_IDs =[]
    #     for x in dane:
    #         x = x.replace("+", " ")
    #         AKTYWNOWSCI_IDs.append(x.split('=')[1])
    #     print(x)
    #     print (AKTYWNOWSCI_IDs)
    #     return(AKTYWNOWSCI_IDs)

    # return JsonResponse(dane, safe=False)
    return HttpResponse(AKTYWNOWSCI_IDs, USER_IDs)



class UserFilter(django_filters.FilterSet):
    # product_choices = {
    #     '': ('---------', ''),
    #     'fresh': ('Fresh', { 'method': 'age_group', 'args': ('fresh', ), }),
    #     'regular': ('Regular', {'method': 'age_group', 'args': ('regular', ), }),
    #     'old': ('Old', {'method': 'age_group', 'args': ('old', ), }),}
    user = django_filters.MultipleChoiceFilter(choices=UZYTKOWNICY)
    aktywnosc = django_filters.MultipleChoiceFilter(choices=AKTYWNOWSCI)
    miejscowosc = django_filters.MultipleChoiceFilter(choices=MIASTA)
    kodpocztowy = django_filters.MultipleChoiceFilter(choices=KODY)
    # miejscowosc = django_filters.ModelMultipleChoiceFilter(queryset=Album.objects.all().values_list('miejscowosc').distinct())
    # miejscowosc = QuerySetFilter(product_choices, label='Product age choices')

    termin = django_filters.DateFromToRangeFilter()


    class Meta:
        model = Album
        fields = ['aktywnosc', 'miejscowosc', 'kodpocztowy', 'termin', 'user']

    def __init__(self, *args, **kwargs):
        super(UserFilter, self).__init__(*args, **kwargs)

    # def __init__(self, *args, **kwargs):
    #     print('to jest init')
    #     super(UserFilter, self).__init__(*args, **kwargs)
    #     print("to jest AKTYWNOWSCI_IDs %s." % AKTYWNOWSCI_IDs)
    #     print("AKTYWNOWSCI_IDs uzytkownikow %s." % USER_IDs)
    #
    #
        if USER_IDs == [] and AKTYWNOWSCI_IDs == []:
            print ('AKTYWNOWSCI_IDs jest pusta')
            self.filters['aktywnosc'].extra.update(
            {
            'choices': AKTYWNOWSCI
            })
            self.filters['miejscowosc'].extra.update(
            {
                'choices': MIASTA
            })
            self.filters['kodpocztowy'].extra.update(
            {
            'choices': KODY
            })
        else:
            aktywnosci_temp = []
            for x in USER_IDs:
                x = Album.objects.filter(user_id=x).values_list('aktywnosc', 'aktywnosc').distinct()
                aktywnosci_temp.extend(x)
            # aktywnosci_temp.insert(0, ('','---------') )
            aktywnosci = list(set(aktywnosci_temp))
            self.filters['aktywnosc'].extra.update(
            {
            'choices': sorted(aktywnosci)
            })

            cities = []
            for x in AKTYWNOWSCI_IDs:
                x = Album.objects.filter(aktywnosc=x).values_list('miejscowosc', 'miejscowosc').distinct()
                cities.extend(x)
            print ("to są miasta %s." % cities)

            self.filters['miejscowosc'].extra.update(
            {
                'choices': sorted(cities)
            })




            self.filters['kodpocztowy'].extra.update(
            {
            'choices': []
            })




        #
        #

        #
        #
        #
        #
        # print("aktywnosci w inicie %s." % aktywnosci)
        #
        #                             # if USER_IDs == []:
        #                             #     self.filters['aktywnosc'].extra.update(
        #                             #     {
        #                             #     'choices': sorted(ZDARZENIA_FILTR)
        #                             #     })
        #                             # else:
        #                             #     self.filters['aktywnosc'].extra.update(
        #                             #     {
        #                             #     'choices': sorted(aktywnosci)
        #                             #     })
        #
        # cities = []
        # cities.insert(0, ('','---------') )
        # for x in USER_IDs:
        #     x = Album.objects.filter(user_id=x).values_list('miejscowosc', 'miejscowosc').distinct()
        #     cities.extend(x)
        # # print ("to są miasta %s." % cities)
        # codes = []
        # for x in USER_IDs:
        #     x = Album.objects.filter(user_id=x).values_list('kodpocztowy', 'kodpocztowy').distinct()
        #     codes.extend(x)
        #     print (codes)
        # if cities == []:
        #
        # # else:
        #     self.filters['kodpocztowy'].extra.update(
        #     {
        #     'choices': codes
        #     })
        #
        #
        # if cities == []:
        #     self.filters['miejscowosc'].extra.update(
        #     {
        #         'choices': sorted(MIASTALISTA)
        #     })
        # else:
        #     self.filters['miejscowosc'].extra.update(
        #     {
        #         'choices': sorted(cities)
        #     })







            # print(Album.objects.filter(aktywnosc=AKTYWNOWSCI_IDs[0]).values_list('miejscowosc', 'miejscowosc').distinct())
        # INNEMIASTA = Album.objects.filter(aktywnosc='Wizyta').values_list('miejscowosc', 'miejscowosc').distinct()
        # miejscowosc = django_filters.MultipleChoiceFilter(choices=INNEMIASTA)
        # return(miejscowosc)
        # print(MIASTA)
        # print(miastab)
    #     # cos['aktywnosc'].choices = Album.objects.all().values_list("miejscowosc","miejscowosc").distinct()
    #     # print(choices)
    #
    #     for name, field in self.filters.items():
    #         if isinstance(field, django_filters.ChoiceFilter):
    #             # Add "Any" entry to choice fields.
    #             field.extra['choices'] = tuple([("", "Any"), ] + list(field.extra['choices']))
