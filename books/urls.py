from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^categories/$',
            views.CategoryList.as_view(),
            name=views.CategoryList.name),
    url(r'^categories/(?P<pk>[0-9]+)/$',
            views.CategoryDetail.as_view(),
            name=views.CategoryDetail.name),
    url(r'^books/$',
            views.BookList.as_view(),
            name=views.BookList.name),
    url(r'^books/(?P<pk>[0-9]+)/$',
            views.BookDetail.as_view(),
            name=views.BookDetail.name),
    url(r'^authors/$',
            views.AuthorList.as_view(),
            name=views.AuthorList.name),
    url(r'^authors/(?P<pk>[0-9]+)/$',
            views.AuthorDetail.as_view(),
            name=views.AuthorDetail.name),
]
