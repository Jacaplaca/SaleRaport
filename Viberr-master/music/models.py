from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.urlresolvers import reverse



class Nazwy(models.Model):
    nazwa = models.CharField(max_length=40)

    def __str__(self):
        return self.nazwa



class Klienci(models.Model):
    nazwaklienta = models.CharField(max_length=40)
    nipklienta = models.CharField(max_length=25, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):              # __unicode__ on Python 2
        # return '%s %s' % (self.nazwaklienta, self.nipklienta)
        return self.nazwaklienta

    ordering = ['created_at']

class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    termin = models.DateField(null=True)
    GODZINY = (
                        (u'1', u'1'),
                        (u'2', u'2'),
                        (u'3', u'3'),
                        (u'4', u'4'),
                        (u'5', u'5'),
                        (u'6', u'6'),
                        (u'7', u'7'),
                        (u'8', u'8'),
                        (u'9', u'9'),
                        (u'10', u'10'),
                        (u'11', u'11'),
                        (u'12', u'12'),
                        (u'13', u'13'),
                        (u'14', u'14'),
                        (u'15', u'15'),
                        (u'16', u'16'),
                        (u'17', u'17'),
                        (u'18', u'18'),
                        (u'19', u'19'),
                        (u'20', u'20'),
                        (u'21', u'21'),
                        (u'22', u'22'),
                        (u'23', u'23'),
                        (u'24', u'24'),
                        )
    # godzinastart = models.CharField(max_length=2, choices=GODZINY, blank=True, verbose_name = 'Godzina rozpoczęcia')
    godzinastart = models.TimeField(blank=True, verbose_name = 'Godzina rozpoczęcia')
    godzinakoniec = models.TimeField(blank=True, verbose_name = 'Godzina zakończenia')
    # godzinakoniec = models.CharField(max_length=2, choices=GODZINY, blank=True, verbose_name = 'Godzina zakończenia')
    ZDARZENIA = (
                        (u'Praca biurowa', u'Praca biurowa'),
                        (u'Wizyta', u'Wizyta'),
                        (u'Urlop', u'Urlop'),
                        (u'Choroba', u'Choroba'),
                        )
    aktywnosc = models.CharField(max_length=25, choices=ZDARZENIA, null=True, blank=True, verbose_name = 'Aktywność')
    miejscowosc = models.CharField(max_length=20, blank=True, verbose_name = 'Miejscowość')
    kodpocztowy = models.CharField(max_length=6, blank=True, verbose_name = 'Kod pocztowy')
    is_favorite = models.BooleanField(default=False)
    uwagi = models.TextField(blank=True, max_length=1000)
    zakonczono = models.BooleanField(default=False, verbose_name = 'Zakończono')
    klient = models.ForeignKey(Klienci, default=69)
    # klient = models.CharField(max_length=50, blank=True, verbose_name = 'Klient')
    # nip = models.CharField(max_length=25, blank=True, verbose_name = 'NIP')
    sprzedaz = models.BooleanField(default=False, verbose_name = 'Sprzedaż')
    zamowienie = models.BooleanField(default=False, verbose_name = 'Zamówienie')
    lunch = models.BooleanField(default=False, verbose_name = 'Lunch')
    ASORT = (
                        (u'Nawozy', u'Nawozy'),
                        (u'Zboża', u'Zboża'),
                        )
    nowyklient = models.CharField(max_length=25, choices=ASORT, blank=True, verbose_name = 'Nowy klient')
    NRWIZYTY = (
                        (u'1', u'1'),
                        (u'2', u'2'),
                        (u'3', u'3'),
                        )
    numerwizyty = models.CharField(max_length=25, choices=NRWIZYTY, blank=True, verbose_name = 'Numer wizyty')

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.aktywnosc


class Raporty(models.Model):
    user = models.ForeignKey(User, related_name='user', default=1)
    termin = models.DateField(null=True)
    GODZINY = (
                        (u'1', u'1'),
                        (u'2', u'2'),
                        (u'3', u'3'),
                        (u'4', u'4'),
                        (u'5', u'5'),
                        (u'6', u'6'),
                        (u'7', u'7'),
                        (u'8', u'8'),
                        (u'9', u'9'),
                        (u'10', u'10'),
                        (u'11', u'11'),
                        (u'12', u'12'),
                        (u'13', u'13'),
                        (u'14', u'14'),
                        (u'15', u'15'),
                        (u'16', u'16'),
                        (u'17', u'17'),
                        (u'18', u'18'),
                        (u'19', u'19'),
                        (u'20', u'20'),
                        (u'21', u'21'),
                        (u'22', u'22'),
                        (u'23', u'23'),
                        (u'24', u'24'),
                        )
    godzinastart = models.TimeField(blank=True, verbose_name = 'Godzina rozpoczęcia')
    godzinakoniec = models.TimeField(blank=True, verbose_name = 'Godzina zakończenia')
    ZDARZENIA = (
                        (u'Praca biurowa', u'Praca biurowa'),
                        (u'Wizyta', u'Wizyta'),
                        (u'Urlop', u'Urlop'),
                        (u'Choroba', u'Choroba'),
                        )
    aktywnosc = models.CharField(max_length=25, choices=ZDARZENIA, blank=True, verbose_name = 'Aktywność')
    miejscowosc = models.CharField(max_length=20, blank=True, verbose_name = 'Miejscowość')
    kodpocztowy = models.CharField(max_length=6, blank=True, verbose_name = 'Kod pocztowy')
    is_favorite = models.BooleanField(default=False)
    uwagi = models.TextField(blank=True, max_length=1000)
    zakonczono = models.BooleanField(default=True, verbose_name = 'Zakończono')
    klient = models.ForeignKey(Klienci, default=69)
    # klient = models.CharField(max_length=50, blank=True, verbose_name = 'Klient')
    # nip = models.CharField(max_length=25, blank=True, verbose_name = 'NIP')
    sprzedaz = models.BooleanField(default=False, verbose_name = 'Sprzedaż')
    zamowienie = models.BooleanField(default=False, verbose_name = 'Zamówienie')
    lunch = models.BooleanField(default=False, verbose_name = 'Lunch')
    ASORT = (
                        (u'Nawozy', u'Nawozy'),
                        (u'Zboża', u'Zboża'),
                        )
    nowyklient = models.CharField(max_length=25, choices=ASORT, blank=True, verbose_name = 'Nowy klient')
    NRWIZYTY = (
                        (u'1', u'1'),
                        (u'2', u'2'),
                        (u'3', u'3'),
                        )
    numerwizyty = models.CharField(max_length=25, choices=NRWIZYTY, blank=True, verbose_name = 'Numer wizyty')

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.klient

# class Klient(models.Model):
#     nazwa = models.CharField(max_length=50, blank=True)
#     nip = models.CharField(max_length=25, blank=True)
#     # sprzedazilosc = models.PositiveIntegerField(default=0)
#
#     def __str__(self):
#         return self.nazwa



class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title




class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)

class Czas(models.Model):
    zegar = models.DateField(null=True)
    minutnik = models.TimeField(null=True)
