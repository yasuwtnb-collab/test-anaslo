import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright


async def main():
  # みんレポのエスパス日拓新宿歌舞伎町店タグページ
  url = "https://min-repo.com/tag/%E3%82%A8%E3%82%B9%E3%83%91%E3%82%B9%E6%97%A5%E6%8B%93%E6%96%B0%E5%AE%BF%E6%AD%8C%E8%88%9E%E4%BC%8E%E7%94%BA%E5%BA%97/"

  print("🌐 みんレポへアクセス中...")

  async with async_playwright() as p:
    browser = await p.chromium.launch(
        headless=True,
        args=["--no-sandbox", "--disable-setuid-sandbox"],
    )
    context = await browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        ),
        locale="ja-JP",
    )
    page = await context.new_page()

    # ページヘ遷移
    response = await page.goto(url, wait_until="domcontentloaded", timeout=60000)
    status = response.status
    print(f"📊 ステータスコード: {status}")

    content = await page.content()
    await browser.close()

    if status == 200:
      soup = BeautifulSoup(content, "html.parser")
      # みんレポの投稿記事リンク（記事一覧）を取得
      posts = soup.find_all("article") or soup.find_all("div", class_="post")
      print(f"🔍 検出された記事数: {len(posts)}")

      # ページタイトルの確認
      title = soup.find("title")
      title_text = title.text.strip() if title else "タイトル取得不可"
      print(f"📄 ページタイトル: {title_text}")

      if len(posts) > 0 or "エスパス" in title_text:
        print("🎉 成功！みんレポからのデータ取得を突破しました！")
      else:
        print("⚠️ ページの構造を確認する必要があります。")
    else:
      print(f"❌ ブロックされました (ステータス: {status})")


if __name__ == "__main__":
  asyncio.run(main())
