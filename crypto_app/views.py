from django.shortcuts import render
import json
import requests

api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
raw_json_data = json.loads(api_request.content)

api_request_price = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
price_raw_data = json.loads(api_request_price.content)

#news_catagory_api = requests.get("https://min-api.cryptocompare.com/data/news/feedsandcategories?extraParams=YourSite")
#news_catagory_json = json.loads(news_catagory_api.content)








image_dict = {
   'BTC':'https://images.theconversation.com/files/194266/original/file-20171113-27585-1gdvg8x.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=496&fit=clip',
   'ETH':'https://i2.wp.com/asiatimes.com/wp-content/uploads/2018/12/Ethereum-e1545900837119.jpg?fit=1200%2C801&ssl=1',
   'XRP':'https://thumbs.dreamstime.com/z/golden-ripple-xrp-cryptocurrency-physical-concept-coin-isolated-white-background-d-render-golden-ripple-xrp-cryptocurrency-138682169.jpg',
   'BCH':'https://d1mjtvp3d1g20r.cloudfront.net/2019/06/11132626/Bitcoin-Cash.jpg',
   'LTC':'https://usethebitcoin.com/wp-content/uploads/2018/09/litecoin-3344894_1280.jpg',
   'XLM':'https://usethebitcoin.com/wp-content/uploads/2018/10/AdobeStock_190389761-770x433.jpeg',
   'ADA':'https://blockchainstock.blob.core.windows.net/features/2B0EDE033B79CD6B9F30D99676A86FA2423E0ADA82F012C9CA2CECFA1C361567.jpg',
   'USDT':'https://cryptomode.com/wp-content/uploads/2018/11/shutterstock_773287558.jpg',
   'MIOTA':'https://cryptalker.com/wp-content/uploads/2018/06/BREAKING-IOTA-Up-55-And-Has-Just-Passed-DASH-678x381.png',
   'TRX':'https://ethereumworldnews.com/wp-content/uploads/2018/08/TRON-TRX.jpg'
}

def cards_data(request):


   return render(request, 'Data_with_cards.html', {"api_data": raw_json_data})


def raw_api(request):
   return render(request, 'raw_api_data.html', {"api_data": raw_json_data})


def title_body(request):
   return render(request, 'title_with_body.html', {"api_data": raw_json_data})


def price_page(request):
   return render(request, 'price.html', {"price_data": price_raw_data})


def raw_price_api(request):
   return render(request, 'raw_price_data.html', {"price_data": price_raw_data})


def price_keys(request):
   return render(request, 'price_keys.html', {"price_data": price_raw_data})


def price_with_cards(request):
   return render(request, 'price_with_cards.html', {"price_data": price_raw_data,"photos":image_dict})


'''def test_image(request):
   return render(request,'image_test.html',)'''


def price_search(request):
   if request.method=='POST':
      #HTML to python variable
      search_data = request.POST['search_value']
      api_data =requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+search_data+"&tsyms=USD")
      api_json_data = json.loads(api_data.content)
      return render(request, 'price_search.html', {"key_data": search_data,
                                                   "result_data": api_json_data,
                                                   "photos": image_dict,
                                                   })
   else:
      not_found = "Enter text in search box"
      return render(request, 'price_search.html', {"warning":not_found})


