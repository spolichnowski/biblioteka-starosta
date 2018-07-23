from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import (
    AuthorCreateView,
    BookCreateView,
    AuthorListView,
    BookListView,
    AuthorDeleteView,
    BookDeleteView,
    AuthorDetailView,
    BookDetailView,
    AuthorUpdateView,
    BookUpdateView,
)
from . import views


urlpatterns = [
    url(r'^authors/$', AuthorListView.as_view(), name='author_list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', AuthorDetailView.as_view(), name='author_detail'),
    url(r'^create/$', AuthorCreateView.as_view(), name='author_create'),
    url(r'^(?P<pk>[0-9]+)/$', AuthorUpdateView.as_view(), name='author_update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', AuthorDeleteView.as_view(), name='author_delete'),

    url(r'^$', BookListView.as_view(), name='book_list'),
    url(r'^create-book/$', BookCreateView.as_view(), name='book_create'),
    url(r'^(?P<pk>[0-9]+)/$', BookUpdateView.as_view(), name='book_update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', BookDeleteView.as_view(), name='book_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
