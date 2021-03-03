from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

   path('',views.cards_data,name='card_page_link'),
   path('apicheck',views.raw_api,name='api_check_link'),
   path('title_body',views.title_body,name='title_body_link'),
   path('price_page',views.price_page,name='price_page_link'),
   path('rawprice',views.raw_price_api,name='raw_price_api_link'),
   path('pricekeys',views.price_keys,name="price_keys_link"),
   path('pricecards',views.price_with_cards,name='price_card_link'),
   path('searchprice',views.price_search,name='price_search_link')

]
