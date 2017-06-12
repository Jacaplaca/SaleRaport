from django.contrib.auth import authenticate, login
from django.db.models import Q
import json
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .forms import AlbumForm, SongForm, UserForm, PersonForm, GroupForm, MembershipForm, KlienciForm, RaportyForm, NazwaForm, CzasForm, RaportyWizytyForm
from .models import Album, Song, Person, Group, Membership, User, Klienci, Raporty, Czas
from django.forms import TextInput, Textarea, CharField, PasswordInput, DateField, DateInput
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View, TemplateView
from django.views.generic import *
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from django.template import RequestContext
import datetime
from django.utils.http import is_safe_url
from .filters import UserFilter
import django_filters
from filters.views import FilterMixin
from django.core import serializers
from django_datatables_view.base_datatable_view import BaseDatatableView


# class OrderListJson(BaseDatatableView):
#     # The model we're going to show
#     model = Album
#
#     # define the columns that will be returned
#     columns = ['aktywnosc']
#
#     # define column names that will be used in sorting
#     # order is important and should be same as order of columns
#     # displayed by datatables. For non sortable columns use empty
#     # value like ''
#     order_columns = ['aktywnosc']
#
#     # set max limit of records returned, this is used to protect our site if someone tries to attack our site
#     # and make it return huge amount of data
#     max_display_length = 500
#
#     def render_column(self, row, column):
#         # We want to render user as a custom column
#         if column == 'user':
#             return '{0} {1}'.format(row.customer_firstname, row.customer_lastname)
#         else:
#             return super(OrderListJson, self).render_column(row, column)
#
#     def filter_queryset(self, qs):
#         # use parameters passed in GET request to filter queryset
#
#         # simple example:
#         search = self.request.GET.get(u'search[value]', None)
#         if search:
#             qs = qs.filter(name__istartswith=search)
#
#         # more advanced example using extra parameters
#         filter_customer = self.request.GET.get(u'customer', None)
#
#         if filter_customer:
#             customer_parts = filter_customer.split(' ')
#             qs_params = None
#             for part in customer_parts:
#                 q = Q(customer_firstname__istartswith=part)|Q(customer_lastname__istartswith=part)
#                 qs_params = qs_params | q if qs_params else q
#             qs = qs.filter(qs_params)
#         return qs
#


# class UsersList110(TemplateView):
#     template_name = 'music/datatables110.html'
#
#
# class UsersList110Json(BaseDatatableView):
#     model = Album
#     columns = ['termin', 'aktywnosc']
#     order_columns = ['termin', 'aktywnosc']
#
#     def filter_queryset(self, qs):
#         sSearch = self.request.GET.get('sSearch', None)
#         if sSearch:
#             qs = qs.filter(Q(termin__iendswith=sSearch) | Q(aktywnosc__iendswith=sSearch))
#         return qs







class UsersList(TemplateView):
    template_name = 'music/datatables.html'
#
#
# class UsersList110Json(BaseDatatableView):
#     model = Album
#     columns = ['aktywnosc', 'termin', 'miejscowosc', 'user']
#     order_columns = ['aktywnosc', 'termin', 'miejscowosc', 'user']


class UsersListJson(BaseDatatableView):
    model = Album
    columns = ['user', 'termin','aktywnosc', 'miejscowosc', 'kodpocztowy']
    order_columns = ['user', 'termin','aktywnosc', 'miejscowosc', 'kodpocztowy']

    def filter_queryset(self, qs):
        sSearch = self.request.GET.get('sSearch', None)

        if sSearch:
            qs = qs.filter(Q(termin__icontains=sSearch) | Q(aktywnosc__istartswith=sSearch) | Q(miejscowosc__istartswith=sSearch) | Q(kodpocztowy__icontains=sSearch) |Q(user__username__istartswith=sSearch))
            # print(user)
        return qs


class UsersListJson(BaseDatatableView):
    model = Album
    columns = ['miejscowosc']
    order_columns = ['miejscowosc']

    def filter_queryset(self, qs):
        sSearch = self.request.GET.get('sSearch', None)

        if sSearch:
            qs = qs.filter(Q(__istartswith=sSearch))
            # print(user)
        return qs














def search(request):
    user_list = Album.objects.all()
    print(user_list)
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'music/users.html', {'filter': user_filter})

class IndexView(LoginRequiredMixin, FilterMixin, django_filters.views.FilterView):
    login_url = '/login_user/'
    redirect_field_name = 'redirect_to'
    template_name = 'music/index.html'
    context_object_name = 'albums'
    filterset_class = UserFilter

    def get_queryset(self):
        if self.request.user.is_superuser:
            # print(self.request)
            # print("to jestem jad")

            return Album.objects.filter(zakonczono = False)
        else:
            # print(self.request)
            # self.aktywnosc = get_object_or_404(Album, aktywnosc=self.args[0])
            un_miejscowosc = Album.objects.order_by().values_list('miejscowosc').distinct()
            # print (un_miejscowosc) # See for yourself.
            slownik=[]
            for cos in un_miejscowosc:
                slownik += cos
            # print (slownik)
            return Album.objects.filter(user = self.request.user, zakonczono = False)


AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

# def add(request):
#     if request.method == 'POST':
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             item= Item()
#             item.ref = form.cleaned_data.get('ref')
#             item.save()
#             return redirect('/item_list/')
#     else:
#         form = ItemForm()
#         form1 = ItemCategoryForm()
#     return render(request, 'item/add.html', {'form': form, 'form1':form1})



def add_category(request):
    data = {}
    if request.method == 'POST' :
        form = NazwaForm(request.POST)
        if form.is_valid():
            itemCategory = Nazwy()
            itemCategory.name = form.cleaned_data.get('nazwa')
            itemCategory.save()
            data['new_itemcategory_value'] =  itemCategory.nazwa;
            data['new_itemcategory_key'] =  itemCategory.pk;
            data['stat'] = "ok";
            return HttpResponse(json.dumps(data), mimetype="application/json")
        else:
            data['stat'] = "error";
            return render(request, 'music/nazwa_form.html', {'form': form})
    else:
        form = NazwaForm()
        return render(request, 'music/nazwa_form.html', {'form': form})


class NazwaView(CreateView):
	template_name = 'music/nazwa_form.html'
	success_url = '/create_nazwa/'
	form_class = NazwaForm

class CzasView(CreateView):
	template_name = 'music/czas_form.html'
	success_url = '/create_nazwa/'
	form_class = CzasForm

# @render_to('your_app_name:music/form_template.html')
    # Render the index.html template with a context dictionary
    # that has a key called 'time' with current time obtained from
    # the datetime module as the value.

class AjaxTemplateMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)



	# def jakas(request):
	# 	now = datetime.datetime.now()
	# 	print(now)
	# 	return render(request, "music/proba.html", {'time' : datetime.datetime.now()})

	# def get_queryset(self):
	# 	print(self.request.user)
	# 	return Album.objects.filter(user = self.request.user, is_favorite = False)
# class AdminIndexView(LoginRequiredMixin, generic.ListView):
# 	login_url = '/login_user/'
# 	redirect_field_name = 'redirect_to'
# 	template_name = 'music/index.html'
# 	context_object_name = 'albums'
#
# 	def get_queryset(self):
# 		# uzyt = self.request.user
# 		print(self.request.user)
# 		if self.request.user.is_superuser:
# 			print("to jestem ja")
# 			return Album.objects.filter(zakonczono = False)
# 		else:
# 			print('to jest else')


class ProbaView(LoginRequiredMixin, generic.ListView):
	login_url = '/login_user/'
	redirect_field_name = 'redirect_to'
	template_name = 'music/proba.html'
	context_object_name = 'albums'

	def get_queryset(self):
		print(self.request.user)
		return Album.objects.filter(user = self.request.user)

# class IndexView(LoginRequiredMixin, generic.ListView, FilterMixin, django_filters.views.FilterView):
#     login_url = '/login_user/'
#     redirect_field_name = 'redirect_to'
#     template_name = 'music/index.html'
#     context_object_name = 'albums'
#     filter_set = UserFilter
#     var1 = Album.objects.order_by().values_list('aktywnosc').distinct()
#     var2 = 1
#     akt = ''
#     # paginate_by = 10
#
#     # def post(self):
#     #     user_list = Album.objects.all()
#     #     print(user_list)
#     #     user_filter = UserFilter(self.request.GET, queryset=user_list)
#     #     return render(self.request, 'music/index.html', {'filter': user_filter})
#
#     def get_context_data(self, **kwargs):
#         print (self.var1)
#         print(**kwargs)
#         slownik = []
#         for cos in self.var1:
#             slownik += cos
#         context = super(IndexView, self).get_context_data(**kwargs)
#         print (slownik)
#         context.update({'var1': slownik, 'var2': self.var2})
#         return context
#
#
#     def get_tags():
#         tags = timezone.now()
#         print (tags)
#         return tags
#
#     # def post(request, self):
#     #     unikalne = Album.objects.order_by().values_list('aktywnosc').distinct()
#     #     print(unikalne)
#     #     aaa = "adfa"
#     #     context = {'unikalne':aaa}
#     #     return redirect(request, 'music/index.html', context)
#
#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             print(self.request)
#             print("to jestem jad")
#
#             return Album.objects.filter(zakonczono = False)
#         else:
#             print(self.request)
#             # self.aktywnosc = get_object_or_404(Album, aktywnosc=self.args[0])
#             return Album.objects.filter(user = self.request.user, zakonczono = False)
#
#
# class IndexFiltrowanyView(LoginRequiredMixin, generic.ListView):
#     login_url = '/login_user/'
#     redirect_field_name = 'redirect_to'
#     template_name = 'music/index.html'
#     context_object_name = 'albums'
#     # var1 = Album.objects.order_by().values_list('aktywnosc').distinct()
#     # var2 = 1
#     # akt = ''
#     # paginate_by = 10
#
#     def get_queryset(self):
#         print(self.request)
#         print("to jestem jad")
#         print(self.kwargs['filtr'])
#         print(self.kwargs['jaki'])
#         return Album.objects.filter()


class UserView(LoginRequiredMixin, generic.ListView):
    login_url = '/login_user/'
    redirect_field_name = 'redirect_to'
    template_name = 'music/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        if self.request.user.is_superuser:
            print(self.kwargs['usern'])
            return Album.objects.filter(user_id=self.kwargs['usern'])


class WizytyView(LoginRequiredMixin, generic.ListView):
	login_url = '/login_user/'
	redirect_field_name = 'redirect_to'
	template_name = 'music/index_wizyt.html'
	context_object_name = 'albums'

	def get_queryset(self):
		if self.request.user.is_superuser:
			return Album.objects.filter(zakonczono = True, aktywnosc='Wizyta')
		else:
			return Album.objects.filter(user = self.request.user, zakonczono=True, aktywnosc='Wizyta')


class RaportyView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'albums'
    login_url = '/login_user/'
    redirect_field_name = 'redirect_to'
    template_name = 'music/raporty.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Raporty.objects.filter()
        else:
            # nowyklient = 'Nawozy'
            return Raporty.objects.filter(user = self.request.user)


# class UserWizytyView(LoginRequiredMixin, generic.ListView):
# 	login_url = '/login_user/'
# 	redirect_field_name = 'redirect_to'
# 	template_name = 'music/index_wizyt.html'
# 	context_object_name = 'albums'
#
# 	def get_queryset(self):
# 		if self.request.user.is_superuser:
# 			return Album.objects.filter(user = self.request.user, zakonczono = True)





class ZakonczoneView(LoginRequiredMixin, generic.ListView):
	login_url = '/login_user/'
	redirect_field_name = 'redirect_to'
	template_name = 'music/index.html'
	context_object_name = 'albums'


	def get_queryset(self):
		if self.request.user.is_superuser:
			print("to jestem ja")
			return Album.objects.filter(zakonczono = True)
		print(self.request.user)
		return Album.objects.filter(zakonczono = True, user = self.request.user)




# class PersonCreate(UpdateView):
# 	# album = Album.objects.get(pk=pk)
# 	template_name = 'music/person_form.html'
# 	success_url = '/create_membership/'
# 	model = Person
#
# 	def get_context_data(self, **kwargs):
# 		context['pk'] = self.get_form()
# 		# context = super(AlbumUpdate, self).get_context_data(**kwargs)
# 		return context





	# def get_object(self):
	# 	obj = get_object_or_404(Calification, pk=self.request.POST.get('pk'))
	# 	return obj

	# def get_object(self, queryset=None):
	# 	if queryset is None:
	# 		queryset = self.get_queryset()
    # # Next, try looking up by primary key.
	# 	pk = self.kwargs.get(self.pk_url_kwarg, None)
	# def get_object(self):
	# 	return Album.objects.get(pk=self.request.GET.get('pk')) # or request.POST

	# def post(self, request, **kwargs):
	# 	request.POST = request.POST.copy()
	# 	request.POST['some_key'] = 'some_value'
	# 	return super(SomeUpdateView, self).post(request, **kwargs)




	# form.fields["name"].queryset = Photo.objects.filter(user=request.user)

	# def get_context_data(self):
	# 	context = super(AlbumUpdate, self).get_context_data(**kwargs)
	# 	return context

# def createraport(request, id):
# 	klient = get_object_or_404(Album, id=id)
# 	form = PersonForm(instance=klient)
# 	context = RequestContext(request)
# 	return render_to_response('music/person_form.html', context)

			# context = {
	# 	'album': album,
	# 	'form': form,
	# 	'error_message': 'You already added that song',
	# }
	# return render(request, 'music/create_song.html', context)

	# def get_context_data(self, **kwargs):
	# 	context = super(AlbumUpdate, self).get_context_data(**kwargs)
	# 	return context

	# def get_success_url(self):
	# 	referer_url = HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

def popup(request):
    return render(request, 'music/popup.html')



# def DwaFormularze(request):
# 	if request.method == 'POST':
# 		form1 = KlienciForm( request.POST,prefix="form1")
# 		form2 = GroupForm( request.POST,prefix="form2")
# 		print(request.POST)
# 		if form1.is_valid() or form2.is_valid():
# 			zmienna = form1.save(commit=False)
# 			zmienna2 = form2.save(commit=False)
# 			zmienna.save()
# 			zmienna2.save()
# 			return redirect('music:index')
# 	else:
# 		form1 = KlienciForm(prefix="form1")
# 		form2 = GroupForm(prefix="form2")
# 		return render(request, 'music/dwa_formularze.html', {'form1':form1, 'form2':form2})

def DwaFormularze(request):
	if request.method == 'POST':
		form1 = KlienciForm( request.POST,prefix="form1")
		form2 = GroupForm( request.POST,prefix="form2")
		print(request.POST)
		if form1.is_valid() or form2.is_valid():
			zmienna = form1.save(commit=False)
			zmienna2 = form2.save(commit=False)
			zmienna.save()
			zmienna2.save()
			return redirect('music:index')
	else:
		form1 = KlienciForm(prefix="form1")
		form2 = GroupForm(prefix="form2")
		return render(request, 'music/dwa_formularze.html', {'form1':form1, 'form2':form2})

class WizytaKlienciCreate(SuccessMessageMixin, AjaxTemplateMixin, CreateView):
    template_name = 'music/test_form.html'
    success_url = reverse_lazy('music:index')
    form_class = KlienciForm

    def post(self, request):
        # print(godzinastart)
        if request.method == "POST":
            form = KlienciForm(request.POST)
            if form.is_valid():
                Klienci = form.save(commit=False)
                Klienci.save()
                query = request.GET.get('request_path')
                print (query)
                print(request.method)
                print(request.POST)
                my_param = request.POST.get('nazwaklienta')
                print (my_param)
                print(request.POST.getlist('nazwaklienta'))
                # print(godzinastart)
                # return render(request, 'music/detail.html', {'pk':pk})
                return redirect('music:raporty_wizyty')

                # return HttpResponseRedirect(reverse('music:create_raport'))
                # return reverse_lazy('music:create_raport', {"pk":pk})
        else:
            print(request.method)

class KlienciCreate(SuccessMessageMixin, AjaxTemplateMixin, CreateView):
    template_name = 'music/test_form.html'
    success_url = reverse_lazy('music:index')
    form_class = KlienciForm

    def post(self, request, pk):
        # print(godzinastart)
        if request.method == "POST":
            form = KlienciForm(request.POST)
            if form.is_valid():
                Klienci = form.save(commit=False)
                Klienci.save()
                query = request.GET.get('request_path')
                print (query)
                print(request.method)
                print(request.POST)
                my_param = request.POST.get('nazwaklienta')
                print (my_param)
                print(request.POST.getlist('nazwaklienta'))
                print("to jest teraz ostatnie pk")
                print(pk)
                # print(godzinastart)
                # return render(request, 'music/detail.html', {'pk':pk})
                return redirect('music:create_raport', pk=pk)

                # return HttpResponseRedirect(reverse('music:create_raport'))
                # return reverse_lazy('music:create_raport', {"pk":pk})
        else:
            print(request.method)

    # def get_form_kwargs(self):
    #     kwargs = super(KlienciCreate, self).get_form_kwargs()
    #     # update the kwargs for the form init method with yours
    #     kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
    #     print("będą kwargs ")
    #     print (kwargs)
    #     return kwargs

    # def get_success_url(self, **kwargs):
    #
    #     if  kwargs != None:
    #         return reverse_lazy('music:index')
    #     else:
    #         return reverse_lazy('music:zakonczone')



	# def post(self, request):
	# 	if request.method == "POST":
	# 		form = KlienciForm(request.POST)
	# 		if form.is_valid():
	# 			Klienci = form.save(commit=False)
	# 			Klienci.save()
	# 			return redirect('music:index')
	# 	else:
	# 		form = RaportyForm()
	# 		return render(request, 'music/test_form.html', {'form': form})














# class KlienciCreate(SuccessMessageMixin, AjaxTemplateMixin, CreateView):
# 	template_name = 'music/test_form.html'
# 	success_url = reverse_lazy('music:index')
# 	form_class = KlienciForm

class GroupCreate(CreateView):
	template_name = 'music/group_form.html'
	success_url = '/create_group/'
	form_class = GroupForm

class MembershipCreate(CreateView):
	template_name = 'music/membership_form.html'
	success_url = '/create_membership/'
	form_class = MembershipForm




class AlbumCreate(LoginRequiredMixin, CreateView):
	template_name = 'music/nowa_aktywnosc.html'
	success_url = '/'
	form_class = AlbumForm

    # login_url = '/login_user/'
	# redirect_field_name = 'redirect_to'
	# model = Album
	# fields = ['termin', 'godzinastart', 'godzinakoniec', 'aktywnosc', 'miejscowosc', 'kodpocztowy', 'zakonczono' ,'uwagi', 'probny']
	# widgets = {
    #         'termin': DateField(),
    #     }
    # class Meta:
	# 	labels = {'godzinastart': _('Godzina rozpoczecia'),}

	def form_valid(self, form):
		object = form.save(commit=False)
		object.user = self.request.user
		object.save()
		return super(AlbumCreate, self).form_valid(form)

#dobry
class AlbumDetail(LoginRequiredMixin, generic.DetailView):
	login_url = '/login_user/'
	redirect_field_name = 'redirect_to'
	model = Album
	template_name = 'music/detail.html'

class RaportDetail(LoginRequiredMixin, generic.DetailView):
	login_url = '/login_user/'
	redirect_field_name = 'redirect_to'
	model = Raporty
	template_name = 'music/raport_detail.html'



class AlbumUpdate(LoginRequiredMixin, UpdateView):
	login_url = '/login_user/'
	redirect_field_name = 'redirect_to'
	model = Album
	fields = ['termin', 'godzinastart', 'godzinakoniec', 'aktywnosc', 'miejscowosc', 'kodpocztowy']

	def get_context_data(self, **kwargs):
		context = super(AlbumUpdate, self).get_context_data(**kwargs)
		return context
		print (kwargs)


	def form_valid(self, form):
		object = form.save(commit=False)
		object.user = self.request.user
		object.save()
		return super(AlbumUpdate, self).form_valid(form)


class WizytaUpdate(LoginRequiredMixin, UpdateView):
	login_url = '/login_user/'
	redirect_field_name = 'redirect_to'
	model = Album
	fields = ['zakonczono', 'klient', 'sprzedaz', 'zamowienie', 'lunch', 'nowyklient', 'numerwizyty', 'uwagi']

	def get_context_data(self, **kwargs):
		context = super(WizytaUpdate, self).get_context_data(**kwargs)
		return context

	def form_valid(self, form):
		object = form.save(commit=False)
		object.user = self.request.user
		object.save()
		return super(WizytaUpdate, self).form_valid(form)


#jesli wiersz zawiera aktywnosc jako wizyte to wybiera inny view
def workDailyRecord(request, pk):
	album = Album.objects.get(pk=pk)
	aktywnosc = Album.objects.get(pk=pk).aktywnosc
	if aktywnosc != 'Wizyta':
		return ZakonczoneUpdate.as_view()(request, pk=pk)
	else:
		return WizytaUpdate.as_view()(request, pk=pk)


class ZakonczoneUpdate(LoginRequiredMixin, UpdateView):
	login_url = '/login_user/'
	redirect_field_name = 'redirect_to'
	model = Album
	fields = ['zakonczono' ,'uwagi']


	def get_context_data(self, **kwargs):
		context = super(ZakonczoneUpdate, self).get_context_data(**kwargs)
		return context


	def form_valid(self, form):
		object = form.save(commit=False)
		object.user = self.request.user
		object.save()
		return super(ZakonczoneUpdate, self).form_valid(form)

class AlbumDelete(LoginRequiredMixin, DeleteView):
	login_url = '/login_user/'
	redirect_field_name = 'redirect_to'
	model = Album
	success_url = reverse_lazy('music:index')

def create_song(request, album_id):
	form = SongForm(request.POST or None, request.FILES or None)
	album = get_object_or_404(Album, pk=album_id)
	if form.is_valid():
		albums_songs = album.song_set.all()
		for s in albums_songs:
			if s.song_title == form.cleaned_data.get("song_title"):
				context = {
					'album': album,
					'form': form,
					'error_message': 'You already added that song',
				}
				return render(request, 'music/create_song.html', context)
		song = form.save(commit=False)
		song.album = album
		song.audio_file = request.FILES['audio_file']
		file_type = song.audio_file.url.split('.')[-1]
		file_type = file_type.lower()
		if file_type not in AUDIO_FILE_TYPES:
			context = {
				'album': album,
				'form': form,
				'error_message': 'Audio file must be WAV, MP3, or OGG',
			}
			return render(request, 'music/create_song.html', context)

		song.save()
		return render(request, 'music/detail.html', {'album': album})
	context = {
		'album': album,
		'form': form,
	}
	return render(request, 'music/create_song.html', context)


def delete_album(request, album_id):
	album = Album.objects.get(pk=album_id)
	album.delete()
	albums = Album.objects.filter(user=request.user)
	return render(request, 'music/index.html', {'albums': albums})

def zakoncz_album(request, pk):
    album = Album.objects.get(pk=pk)
    album.zakonczono = True
    album.save()
    albums = Album.objects.filter(user=request.user)
    return render(request, 'music/index.html', {'albums': albums})




def delete_song(request, album_id, song_id):
	album = get_object_or_404(Album, pk=album_id)
	song = Song.objects.get(pk=song_id)
	song.delete()
	return render(request, 'music/detail.html', {'album': album})




class LogoutView(View):
	def get(self, request):
		logout(request)
		form = UserForm(request.POST or None)
		context = {
			"form": form,
		}
		return render(request, 'music/login.html', context)

#co po zalogowaniu
class LoginView(View):
	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				if user.is_superuser:
					login(request, user)
					albums = Album.objects.filter(zakonczono=False)
					return render(request, 'music/index.html', {'albums': albums})
				else:
					login(request, user)
					albums = Album.objects.filter(user=request.user, zakonczono=False)
					return render(request, 'music/index.html', {'albums': albums})
			else:
				return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'music/login.html', {'error_message': 'Invalid login'})

	def get(self, request):
		return render(request, 'music/login.html')

def favorite_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
	    if album.is_favorite:
	        album.is_favorite = False
	    else:
	        album.is_favorite = True
	    album.save()

    except (KeyError, Album.DoesNotExist):
        print('Json False')
        return JsonResponse({'success': False})
    else:
		# return JsonResponse({'success': False})
        print('Json True')
        return JsonResponse({'success': True})
		# return render(request, 'music/index.html', {'albums': albums})

def register(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				albums = Album.objects.filter(user=request.user)
				return render(request, 'music/index.html', {'albums': albums})
	context = {
		"form": form,
	}
	return render(request, 'music/register.html', context)


def songs(request, filter_by):
	if not request.user.is_authenticated():
		return render(request, 'music/login.html')
	else:
		try:
			song_ids = []
			for album in Album.objects.filter(user=request.user):
				for song in album.song_set.all():
					song_ids.append(song.pk)
			users_songs = Song.objects.filter(pk__in=song_ids)
			if filter_by == 'favorites':
				users_songs = users_songs.filter(is_favorite=True)
		except Album.DoesNotExist:
			users_songs = []
		return render(request, 'music/songs.html', {
			'song_list': users_songs,
			'filter_by': filter_by,
		})

def PersonCreate(request, pk):
	klientzaktywnosci = get_object_or_404(Album, pk=pk)
	uzyt = Album.objects.get(pk=pk).user_id
	# uzytname = Album.objects.get(id=uzyt)
	# print(uzytname.id)
	# ktos = user.username
	# print (ktos)
	# userzuser = User.object.get(pk=user_id).username
	uzytkownik = Album.objects.filter(pk=uzyt)
	# Album.objects.filter(user_id=self.kwargs['usern'])
	print(uzyt)
	print(klientzaktywnosci)
	print(uzytkownik)
	if request.method == "POST":
		# form = PersonForm()
		form = PersonForm(request.POST)
		if form.is_valid():
			Person = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
			Person.save()
			# return redirect('post_detail', pk=post.pk)
			return redirect('music:index')
	else:
		form = PersonForm(initial={'name':klientzaktywnosci})
		# form = PersonForm()
		return render(request, 'music/person_form.html', {'form': form})

def PersonUpdate(request, pk):
	post = get_object_or_404(Person, pk=pk)
	# klientzaktywnosci = get_object_or_404(Album, pk=pk)
	# imie = Album.objects.get(pk=pk).klient
	# print(pk)
	# print(imie)
	if request.method == "POST":
		form = PersonForm(request.POST, instance=post)
		if form.is_valid():
			print('form is valid')
			u = form.save(commit=False)
			# post.author = request.user
			# post.published_date = timezone.now()
			u.save()
			# return HttpResponseRedirect(reverse_lazy('music:index'))
			return redirect('music:index')
	else:
		print('form is invalid')
		form = PersonForm(instance=post)
	return render(request, 'music/person_form.html', {'form': form})


def RaportyUpdate(request, pk):
	post = get_object_or_404(Raporty, pk=pk)
	# klientzaktywnosci = get_object_or_404(Album, pk=pk)
	# imie = Album.objects.get(pk=pk).klient
	# print(pk)
	# print(imie)
	if request.method == "POST":
		form = RaportForm(request.POST, instance=post)
		if form.is_valid():
			print('form is valid')
			u = form.save(commit=False)
			# post.author = request.user
			# post.published_date = timezone.now()
			u.save()
			# return HttpResponseRedirect(reverse_lazy('music:index'))
			return redirect('music:index')
	else:
		print('form is invalid')
		form = RaportForm(instance=post)
	return render(request, 'music/raport_form.html', {'form': form})

# def RaportyCreateKlient

class RaportyWizytyCreate(CreateView):
    template_name = 'music/wizyta_raport_form.html'
    success_url = '/'
    form_class = RaportyWizytyForm

    def get_initial(self):
        klient = Klienci.objects.all().last()
        print(klient)
        return { 'klient': klient, 'aktywnosc':'Wizyta' }





def RaportyCreate(request, pk):
    # return {"message" : "textowanie"}
    # print(request.resolver_match.url_name)
    print(pk)
    # context = RequestContext(request)
    #
    # print("context")
    # print (context)
    klient = Klienci.objects.all().last()
    user = request.user
    godzinastart = get_object_or_404(Album, pk=pk).godzinastart
    godzinakoniec = get_object_or_404(Album, pk=pk).godzinakoniec
    termin = get_object_or_404(Album, pk=pk).termin
    aktywnosc = get_object_or_404(Album, pk=pk).aktywnosc
    godzinastart = get_object_or_404(Album, pk=pk).godzinastart
    kodpocztowy = get_object_or_404(Album, pk=pk).kodpocztowy
    miejscowosc = get_object_or_404(Album, pk=pk).miejscowosc
	# uzyt = Album.objects.get(pk=pk).user_id
	# uzytname = Album.objects.get(id=uzyt)
	# print(uzytname.id)
	# ktos = user.username
	# print (ktos)
	# userzuser = User.object.get(pk=user_id).username
	# uzytkownik = Album.objects.filter(pk=uzyt)
	# Album.objects.filter(user_id=self.kwargs['usern'])
	# print(uzyt)
	# print(klientzaktywnosci)
	# print(uzytkownik)
    print(request.user)
    if request.method == "POST":
        form = RaportyForm(request.POST)

		# form = PersonForm()
        if form.is_valid():

            Raporty = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            Raporty.user = request.user
            Raporty.save()
            # album = Album.objects.get(pk=pk)
            # album.zakonczono = True
            # album.save()
            # album.delete()
			# return redirect('post_detail', pk=post.pk)
            return redirect('music:index')
    else:
        form = RaportyForm(initial={'klient':klient, 'godzinastart':godzinastart, 'godzinakoniec':godzinakoniec, 'termin':termin, 'miejscowosc':miejscowosc, 'kodpocztowy':kodpocztowy, 'aktywnosc':aktywnosc})
		# form = PersonForm()
        context = {'form': form, 'zmienna':pk, 'godzinastart':godzinastart}
        print(context)
        # return render(request, 'music/raport_form.html', {'form': form, 'zmienna':pk, 'godzinastart':godzinastart})
        return render(request, 'music/raport_form.html', context)
