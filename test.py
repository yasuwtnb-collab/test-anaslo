import requests
from bs4 import BeautifulSoup

url = "https://ana-slo.com/%E3%83%9B%E3%83%BC%E3%83%AB%E3%83%87%E3%83%BC%E3%82%BF/%E6%9D%B1%E4%BA%AC%E9%83%BD/%E3%82%A8%E3%82%B9%E3%83%91%E3%82%B9%E6%97%A5%E6%8B%93%E6%96%B0%E5%AE%BF%E6%AD%8C%E8%88%9E%E4%BC%8E%E7%94%BA%E5%BA%97-%E3%83%87%E3%83%BC%E3%82%BF%E4%B8%80%E8%A6%A7/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8"
}

print("🌐 アナスロへリクエストを送信中...")
res = requests.get(url, headers=headers)
print(f"📊 ステータスコード: {res.status_code}")

if res.status_code == 200:
    soup = BeautifulSoup(res.text, "html.parser")
    tables = soup.find_all("table")
    print(f"🔍 取得出来たテーブル数: {len(tables)}")
    if tables:
        rows = tables[0].find_all("tr")
        print(f"🎉 成功！データ行数: {len(rows)} 行を取得しました！")
else:
    print(f"❌ ブロックされました (ステータス: {res.status_code})")
