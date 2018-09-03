from django.conf.urls import include, url
from django.contrib import admin
from teacher import teacher_urls
from teacher import views as tv
urlpatterns = [
    # Examples:
    # url(r'^$', 'tl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # 之前views里面的函数
    # url(r'^do_1/', tv.do_1),
    #
    # url(r'^do_2/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])', tv.do_2),

    #嵌套参数
    #里面pn要和函数参数pn一样
    url(r'^book/(?:page-(?P<pn>\d+)/)',tv.book_page),

    #额外参数
    url(r'^myname/', tv.name, {"name":"charry"}),



    url(r'^render/', tv.do_render),
    # url(r'^$/',tv.index),
    url(r'^index', tv.index),

    url(r'^render2', tv.do_render2),
]
