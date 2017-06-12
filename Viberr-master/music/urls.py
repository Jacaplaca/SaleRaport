from django.conf.urls import url
from . import views
from . import filters

app_name = 'music'

urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^my/datatable/data/$', views.OrderListJson.as_view(), name='order_list_json'),
    # url(r'^datatables_110$', views.UsersList110.as_view(), name="datatables_110"),
    # url(r'^users_data_110/$', views.UsersList110Json.as_view(), name="users_list_json_110"),

    url(r'^datatables_19$', views.UsersList.as_view(), name="datatables_19"),
    url(r'^users_data_19/$', views.UsersListJson.as_view(), name="users_list_json_19"),

    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^$', views.IndexView.as_view(), name='listjs'),
    # url(r'^Dwa/$', views.IndexViewDwa.as_view(), name='index_old'),
    # url(r'^(?P<filtr>[a-zA_Z]+)/(?P<jaki>[a-zA_Z]+)/$', views.IndexFiltrowanyView.as_view(), name='index'),
    # url(r'^books/([\w-]+)/$', views.IndexView.as_view(), name='index'),
    # url(r'^books/([\w-]+)/$', views.IndexView.as_view(), name='index'),
    # url(r'^$', views.AdminIndexView.as_view(), name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^proba/$', views.ProbaView.as_view(), name='proba'),
    # url(r'^login_user/$', views.login_user, name='login_user'),
    # url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^login_user/$', views.LoginView.as_view(), name='login_user'),
    url(r'^logout_user/$', views.LogoutView.as_view(), name='logout_user'),

    url(r'^ajax/$', filters.dynamiczne_filtrowanie, name='dynamiczne_filtrowanie'),

    # url(r'^refresh/$', filters.refresh_filtrowanie, name='refresh_filtrowanie'),
    # url(r'^ajax/aktywnosc/(?P<aktywnosc>[-\w]+)/$', views.dynamiczne_filtrowanie, name='dynamiczne_filtrowanie'),

    # url(r'^filtrowany/$', views.FiltrowanyView.as_view(), name='search'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view(), name='detail'),
    url(r'^raporty/(?P<pk>[0-9]+)/$', views.RaportDetail.as_view(), name='raport_detail'),
    #odhaczyc
    url(r'^(?P<pk>[0-9]+)/$', views.IndexView.as_view(), name='detail'),
    url(r'^user/(?P<usern>[0-9]+)/$', views.UserView.as_view(), name='user_activities'),
    url(r'^wizyty/$', views.WizytyView.as_view(), name='wizyty_view'),
    url(r'^raporty/$', views.RaportyView.as_view(), name='raporty'),
    url(r'^raporty_wizyty/$', views.RaportyWizytyCreate.as_view(), name='raporty_wizyty'),
    # url(r'^wizytyuzytkownika/$', views.UserWizytyView.as_view(), name='user_wizyty_view'),
    # url(r'^user/(?P<usern>[0-9]+)/zakonczone$', views.UserZakonczoneView.as_view(), name='user_zakonczone_activities'),
    url(r'^zakonczone/$', views.ZakonczoneView.as_view(), name='zakonczone'),

    # url(r'^create_person/$', views.PersonCreate.as_view(), name='create_person'),
    # url(r'^create_person/$', views.PersonCreate, name='create_person'),
    url(r'^create_group/$', views.GroupCreate.as_view(), name='create_group'),


    # url(r'^create_client/$', views.KlienciCreate.as_view(), name='create_client'),
    url(r'^create_client/(?P<pk>[0-9]+)$', views.KlienciCreate.as_view(), name='create_client'),
    url(r'^wizyta_create_client/$', views.WizytaKlienciCreate.as_view(), name='wizyta_create_client'),

    # url(r'^create_client/$', views.KlienciCreate.as_view(), name='test_form'),
    url(r'^create_membership/$', views.MembershipCreate.as_view(), name='create_membership'),
    url(r'^czas/$', views.CzasView.as_view(), name='czas_form'),
    url(r'^create_album/$', views.AlbumCreate.as_view(), name='create_album'),
    url(r'^album/(?P<pk>[0-9]+)$', views.AlbumUpdate.as_view(), name='update_album'),
    # url(r'^album/(?P<pk>[0-9]+)/zakoncz/$', views.ZakonczoneUpdate.as_view(), name='update_zakonczone'),
    url(r'^album/(?P<pk>[0-9]+)/zakoncz/$', views.workDailyRecord, name='update_zakonczone'),
    url(r'^(?P<pk>[0-9]+)/delete_album/$', views.AlbumDelete.as_view(), name='delete_album'),

    url(r'^(?P<pk>[0-9]+)/zakoncz_album/$', views.zakoncz_album, name='zakoncz_album'),

    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^(?P<pk>[0-9]+)/raport/$', views.PersonCreate , name='update_person'),
    url(r'^stworz_raport/(?P<pk>[0-9]+)/$', views.RaportyCreate , name='create_raport'),
    # url(r'^stworz_raport_klient/(?P<pk>[0-9]+)/$', views.RaportyCreateKlient , name='create_raport_klient'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    url(r'^popup/$', views.popup, name='popup'),
    url(r'^dwa_formularze/$', views.DwaFormularze , name='dwa_formularze'),
    # url(r'^test-form/$', TestFormView.as_view(), name="test-form"),
    url(r'^nazwa/$', views.NazwaView.as_view() , name='create_nazwa'),
]
