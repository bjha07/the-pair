from django.conf.urls import patterns, url


urlpatterns = patterns('api.views',
                      url(r'^$','index'),
                      url(r'^auth/$','auth'),
                      url(r'^user_registraion/$','user_registraion'),
                      url(r'^walletmoney_show/$','walletmoney_show'),
                      url(r'^product_list/$','product_list'),
                      url(r'^dashboard_details/$','dashboard_details'),
                      )

