from goods.views import GetTokenApiView, GoodsApiView, NewGoodApiView
from django.urls import path


urlpatterns = [
    path(r'get_token/', GetTokenApiView.as_view(), name='get_token'),
    path(r'get_token', GetTokenApiView.as_view(), name='get_token'),
    path(r'goods/', GoodsApiView.as_view(), name='goods'),
    path(r'goods', GoodsApiView.as_view(), name='goods'),
    path(r'new_good/', NewGoodApiView.as_view(), name='new_good'),
    path(r'new_good', NewGoodApiView.as_view(), name='new_good'),
]

