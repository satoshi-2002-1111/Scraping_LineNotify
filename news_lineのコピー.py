import requests
from bs4 import BeautifulSoup
import time



def yahooNewsdata():
    """スクレピング
    Yahoo!newsのトピックスからスクレピングして辞書型のlistを返す
    """
    #urlからのデータを取得
    url = "https://news.yahoo.co.jp/"
    req = requests.get(url)
    #ページを綺麗にremakeする
    soup = BeautifulSoup(req.text, "html.parser")
    #大まかに特定する
    getdata = soup.find_all("li", "sc-esjQYD hOkRCB")
    #一個ずつリストに入れていく
    newsurl = []
    newstext = []
    for a in range(0, 7):
        data = getdata[a]
        a = data.find('a')
        url = a.get('href')
        newsurl.append(url)
        Data = data.getText()
        newstext.append(Data)
    #データを二つのリストにまとめたから次は一つにまとめる
    nwes_all ={}
    for (t, u) in zip(newstext, newsurl):
        nwes_all[t] = u
    return nwes_all　　# ここでスクレピングしたデータを返します。


news = yahooNewsdata()　　#先ほど、値を返してもらったのでインスタンス化して
                         #line_notifu関数の引数に渡して下さい。


def line_notify(text, url):
    """送信
    スクレピングした内容をlineに送信する関数です。
    """

    TOKEN = ''　#ここには自分でトークンを発行して、入力してください
    api_url = 'https://notify-api.line.me/api/notify'           
    send_contents = text, url
    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
    send_dic = {'message': send_contents}
    return requests.post(api_url, headers=TOKEN_dic, data=send_dic)

          

for t, u in news.items():
    line_notify(t,u)
    print("こちらの,{}内容を送信しました。".format(t))







 



    



