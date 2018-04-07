from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, UserView, UserDetailsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^todos/$', CreateView.as_view(), title="create"),
    url(r'^todos/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), title="details"),
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    url(r'^users/$', UserView.as_view(), title="users"),
    url(r'users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), title="user_details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
