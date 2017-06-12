from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import Album, Song, Person, Group, Membership, Klienci, Raporty, Nazwy, Czas
from django.forms import TextInput, Textarea
from django.contrib import admin
import datetime
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset, HTML, MultiField, ButtonHolder
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from bootstrap3_datetime.widgets import DateTimePicker


# class ItemForm(forms.ModelForm):
#     ref = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=255)
#     category =  forms.ModelChoiceField(queryset=Klienci.objects.all(), empty_label="(choose from the list)")
#
#
# class ItemCategoryForm(forms.ModelForm):
#     category = forms.CharField(
#         max_length=255,
#         required=True,
#         help_text='Add a new category')
class NazwaForm(forms.ModelForm):
    # name = forms.CharField()
    # klientdouzupelnienia = Album.objects.get(pk=pk)
    # album = get_object_or_404(Album, pk=album_id)

    # name = forms.CharField(label='Nazwa')
    # name = forms.ModelMultipleChoiceField(queryset=Album.objects.all())
    class Meta:
        model = Nazwy
        fields = ['nazwa']



class KlienciForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     if  kwargs != None:
    #         print ("nie ma")
    #     else:
    #         print ('sa')
        # self.fields['nazwaklienta'].initial=my_arg
        # super(EpisodeCreateForm, self).__init__(*args, **kwargs)
    # name = forms.CharField()
    # klientdouzupelnienia = Album.objects.get(pk=pk)
    # album = get_object_or_404(Album, pk=album_id)
    title = "Testing"
    adres = forms.CharField(widget=forms.HiddenInput(), initial="asdfd")
    nazwaklienta = forms.CharField(label='Imię i nazwisko')
    nipklienta = forms.CharField(label='ddNIP', required=False, initial=3233)
    # # name = forms.ModelMultipleChoiceField(queryset=Album.objects.all())
    helper = FormHelper()
    helper.form_tag = False # don't render form DOM element
    helper.render_unmentioned_fields = True # render all fields
    helper.form_class = 'form-inline'
    helper.field_template = 'bootstrap3/layout/inline_field.html'
    helper.labels_uppercase = True
    # helper.layout = Layout(
    #     TabHolder(
    #         Tab(
    #             'Basic Information',
    #             'nazwaklienta'
    #         ),
    #         Tab(
    #             'Address',
    #             'nipklienta'
    #         )
    #     )
    # )



    class Meta:
        model = Klienci
        fields = ['nazwaklienta', 'nipklienta', 'adres']

class RaportyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RaportyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'wizytaformularz'
        self.helper.form_method = 'post'
        self.helper.label_class = 'formlabel'
        self.helper.field_class = 'formfield'
        # self.helper.form_action = reverse('submit_form')
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
                Fieldset('Czas',
            Div('termin', css_class='col-lg-4'),
            Div('godzinastart', css_class='col-lg-4'),
            Div('godzinakoniec', css_class='col-lg-4'),
                css_class='row-fluid'),

                Fieldset('Miejsce',
            Div('miejscowosc', css_class='col-lg-4'),
            Div('kodpocztowy', css_class='col-lg-4'),
                css_class='row-fluid'),

                Fieldset('Klient',
            Div('klient', css_class='col-lg-4'),
            Div('nowyklient', css_class='col-lg-4'),
            Div('numerwizyty', css_class='col-lg-4'),
            HTML("""<a href="{% url 'music:wizyta_create_client' %}" class="btn btn-primary btn-sm js-popup-link col-lg-3" role="button">Dodaj nowego klienta</a>"""),

                css_class='row-fluid'),

           Fieldset('Raport',

                    Div(
                       Div('sprzedaz', css_class='col-lg-12'),
                       Div('zamowienie', css_class='col-lg-12'),
                       Div('lunch', css_class='col-lg-12'),

                        css_class='col-lg-4 wyroznienieform'),
                        Div('uwagi', css_class='col-lg-6'),
                        Field('aktywnosc', type="hidden"),
                       css_class='row-fluid'),

            ButtonHolder(
                Submit('submit', 'Dodaj raport', css_class='button white')
            )
           )

    class Meta:
        model = Raporty
        fields = ['termin', 'godzinastart', 'godzinakoniec', 'aktywnosc', 'miejscowosc', 'kodpocztowy', 'klient', 'sprzedaz', 'zamowienie', 'lunch', 'nowyklient', 'numerwizyty', 'uwagi' ]

class RaportyWizytyForm(forms.ModelForm):
    # helper = FormHelper()
    # helper.layout = Layout(
    #     MultiField('Tell us your favorite stuff {{ username }}',))

    def __init__(self, *args, **kwargs):
        super(RaportyWizytyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'wizytaformularz'
        self.helper.form_method = 'post'
        self.helper.label_class = 'formlabel'
        self.helper.field_class = 'formfield'
        # self.helper.form_action = reverse('submit_form')
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
                Fieldset('Czas',
            Div('termin', css_class='col-lg-4'),
            Div('godzinastart', css_class='col-lg-4'),
            Div('godzinakoniec', css_class='col-lg-4'),
                css_class='row-fluid'),

                Fieldset('Miejsce',
            Div('miejscowosc', css_class='col-lg-4'),
            Div('kodpocztowy', css_class='col-lg-4'),
                css_class='row-fluid'),

                Fieldset('Klient',
            Div('klient', css_class='col-lg-4'),
            Div('nowyklient', css_class='col-lg-4'),
            Div('numerwizyty', css_class='col-lg-4'),
            HTML("""<a href="{% url 'music:wizyta_create_client' %}" class="btn btn-primary btn-sm js-popup-link col-lg-3" role="button">Dodaj nowego klienta</a>"""),

                css_class='row-fluid'),

           Fieldset('Raport',

                    Div(
                       Div('sprzedaz', css_class='col-lg-12'),
                       Div('zamowienie', css_class='col-lg-12'),
                       Div('lunch', css_class='col-lg-12'),

                        css_class='col-lg-4 wyroznienieform'),
                        Div('uwagi', css_class='col-lg-6'),

                       css_class='row-fluid'),

            ButtonHolder(
                Submit('submit', 'Dodaj raport', css_class='button white')
            )


                    # Div('sprzedaz', css_class='col-lg-2'),
                    # Div('zamowienie', css_class='col-lg-2'),
                    # Div('lunch', css_class='col-lg-2'),
                    # Div('uwagi', css_class='col-lg-7'),
                    # css_class='row-fluid', css_id="check"),




        #     Fieldset('Czas',
        #             Field('termin', placeholder='Podaj dzień', css_class="some-form-class"),
        #             Field('godzinastart', placeholder='Początek', css_class="some-form-class"),
        #             Field('godzinakoniec', placeholder='Koniec', css_class="some-form-class"),
        #             # HTML("""<p><a href="{% url "music:wizyta_create_client"%}" class="js-popup-link">POP</a></p>"""),
        #             # Div('godzinastart', 'godzinakoniec'),
        #             ),
        #    Fieldset('Dane Klienta',
        #             Field('miejscowosc', 'kodpocztowy'),
        #             Field('klient', css_id = 'favorite-stuff'),
        #             HTML("""<p><a href="{% url "music:wizyta_create_client"%}" class="js-popup-link">POP</a></p>"""),
        #             Field('nowyklient', 'numerwizyty'),),
        #    Fieldset('Raport',
        #             Div('sprzedaz', 'zamowienie', 'lunch', css_id = 'favorite-stuff'),
        #              'uwagi'),
           )

    class Meta:
        model = Raporty
        fields = ['termin', 'godzinastart', 'godzinakoniec', 'miejscowosc', 'kodpocztowy', 'klient', 'sprzedaz', 'zamowienie', 'lunch', 'nowyklient', 'numerwizyty', 'uwagi' ]

        # widgets = {
        #     'termin': forms.TextInput(attrs={'class': 'form-control'}),
        #     'godzinastart': forms.TextInput(attrs={'class': 'form-control'}),
        #     'godzinakoniec': forms.TextInput(attrs={'class': 'form-control'}),
        #     'miejscowosc': forms.TextInput(attrs={'class': 'form-control'}),
        #     'kodpocztowy': forms.TextInput(attrs={'class': 'form-control'}),
        #     'klient': forms.ChoiceField(attrs={'class': 'form-control'}),
        # }






class CzasForm(forms.ModelForm):
    # zegar = forms.DateField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    class Meta:
        model = Czas
        fields = ['zegar', 'minutnik']
        # widgets = {
        # #Use localization and bootstrap 3
        # 'zegar': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3)
        # }


# class RaportyKlientForm(forms.ModelForm):
#     class Meta:
#         model = Raporty
#         fields = ['klient']



class PersonForm(forms.ModelForm):
    # name = forms.CharField()
    # klientdouzupelnienia = Album.objects.get(pk=pk)
    # album = get_object_or_404(Album, pk=album_id)

    name = forms.CharField(label='Imię')
    # name = forms.ModelMultipleChoiceField(queryset=Album.objects.all())
    class Meta:
        model = Person
        fields = ['name']

    # def has_changed(self):
    #     changed_data = super(ModelForm, self).has_changed()
    #     return bool(self.initial or changed_data)

# class KlienciForm(forms.ModelForm):
#     # name = forms.CharField()
#     # klientdouzupelnienia = Album.objects.get(pk=pk)
#     # album = get_object_or_404(Album, pk=album_id)
#     title = "Testing"
#     nazwaklienta = forms.CharField(label='Imię i nazwisko')
#     nipklienta = forms.CharField(label='NIP', required=False)
#     # # name = forms.ModelMultipleChoiceField(queryset=Album.objects.all())
#     helper = FormHelper()
#     helper.form_tag = False # don't render form DOM element
#     helper.render_unmentioned_fields = True # render all fields
#     helper.form_class = 'form-inline'
#     helper.field_template = 'bootstrap3/layout/inline_field.html'
#     # helper.layout = Layout(
#     #     TabHolder(
#     #         Tab(
#     #             'Basic Information',
#     #             'nazwaklienta'
#     #         ),
#     #         Tab(
#     #             'Address',
#     #             'nipklienta'
#     #         )
#     #     )
#     # )
#
#
#
#     class Meta:
#         model = Klienci
#         fields = ['nazwaklienta', 'nazwaklienta']
#
#


    # @property
    # def helper(self):
    #     helper = FormHelper()
    #     helper.form_tag = False # don't render form DOM element
    #     helper.render_unmentioned_fields = True # render all fields
    #     helper.label_class = 'col-md-2'
    #     helper.field_class = 'col-md-10'
    #     helper.text_input = 'popupform'
    #     helper.form_class = 'form-horizontal'
    #     return helper



class GroupForm(forms.ModelForm):
    # name = forms.CharField(label='Nazwa grupy')
    name = forms.ModelChoiceField(queryset=Nazwy.objects.all(), empty_label="(choose from the list)")
    class Meta:
        model = Group
        fields = ['name']

class MembershipForm(forms.ModelForm):
    invite_reason = forms.CharField(label='Powód wprodzenia')
    class Meta:
        model = Membership
        fields = ['group', 'person', 'inviter','invite_reason']


class AlbumForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'wizytaformularz'
        self.helper.form_method = 'post'
        self.helper.label_class = 'formlabel'
        self.helper.field_class = 'formfield'
        # self.helper.form_action = reverse('submit_form')
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
                Fieldset('Czas',
            Div('termin', css_class='col-lg-4'),
            Div('godzinastart', css_class='col-lg-4'),
            Div('godzinakoniec', css_class='col-lg-4'),
                css_class='row-fluid'),

                Fieldset('Miejsce',
            Div('aktywnosc', css_class='col-lg-4'),
            Div('miejscowosc', css_class='col-lg-4'),
            Div('kodpocztowy', css_class='col-lg-4'),
                css_class='row-fluid'),

                Fieldset('Uwagi',

            Div('nowyklient', css_class='col-lg-4'),
            Div('numerwizyty', css_class='col-lg-4'),
            Div('uwagi', css_class='col-lg-6'),
            Field('zakonczono', type="hidden"),
            # HTML("""<a href="{% url 'music:wizyta_create_client' %}" class="btn btn-primary btn-sm js-popup-link col-lg-3" role="button">Dodaj nowego klienta</a>"""),

                css_class='row-fluid'),

            ButtonHolder(
                Submit('submit', 'Dodaj raport', css_class='button white')
            )
           )




    class Meta:
        model = Album
        fields = ['termin', 'godzinastart', 'godzinakoniec', 'aktywnosc', 'miejscowosc', 'kodpocztowy', 'zakonczono' ,'uwagi']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Użytkownik')
    password = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    email = forms.CharField(label='Adres email')
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
