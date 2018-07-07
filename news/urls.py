from django.conf.urls import url,include
from django.contrib import admin
from news.views import UserForm,CommentsForm
admin.autodiscover()

urlpatterns = [
    # url(r'^admin/$', admin.site.urls),
    url(r'^login/$',UserForm.login),
    url(r'^regist/$',UserForm.regist),
    url(r'^logout/$',UserForm.logout),
    url(r'^comment/$',CommentsForm.post),

]