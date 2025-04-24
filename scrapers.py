# scrapers.py
import requests
from bs4 import BeautifulSoup

def scrape_xiaomi(soup: BeautifulSoup):
    product_elements = soup.find_all("li", class_="mi-product__item-wrapper")
    products = []

    for product in product_elements[:100]:
        title_el = product.find("h3", class_="item__title")
        title = title_el.get_text(strip=True) if title_el else "Tidak ada nama"

        price_el = product.find("div", class_="mi-price item__price")
        price_text = price_el.find("strong").get_text(strip=True) if price_el else "Tidak ada harga"

        buy_button = product.find("a", class_="mi-btn mi-btn--primary mi-btn--normal mi-btn--light")
        in_stock = bool(buy_button and "Beli sekarang" in buy_button.get_text(strip=True))

        products.append({
            "title": title,
            "price": price_text,
            "in_stock": in_stock
        })

    return products

def scrape_topup(soup: BeautifulSoup):
    product_elements = soup.find_all("div", class_="pDRoot")
    products = []
    
    for product in product_elements:
        title_el = product.find("span", class_="fs-sm")
        title = title_el.get_text(strip=True) if title_el else "Tidak ada nama"

        quantity_el = product.find("span", class_="fs-xs")
        quantity = quantity_el.get_text(strip=True) if quantity_el else title

        price_el = product.find("p", class_="text-xplay")
        price_text = price_el.get_text(strip=True) if price_el else "Tidak ada harga"

        products.append({
            "title": title,
            "quantity": quantity,
            "price": price_text,
        })

    return products

def scrape_itemku(soup: BeautifulSoup):
    product_elements = soup.find_all("div", class_="ds-shadow-card")
    products = []
    
    for product in product_elements:
        title_el = product.find("span", class_="line-clamp-2")
        title = title_el.get_text(strip=True) if title_el else "Tidak ada nama"

        price_el = product.find("div", class_="text-persimmon-500")
        price = price_el.get_text(strip=True) if price_el else "Tidak ada harga"

        sold_el = product.find("div", string=lambda t: t and "terjual" in t)
        sold = sold_el.get_text(strip=True) if sold_el else "Tidak ada info terjual"

        time_el = product.find("p", class_="card-product-average-delivery-time")
        rata_kirim = time_el.get_text(strip=True).replace("Rata-rata kirim: ", "") if time_el else "Tidak ada info kirim"


        products.append({
            "title": title,
            "price": price,
            "sold": sold,
            "rata_kirim": rata_kirim,
        })

    return products

product_scrapers = {
    "xiaomi": {
        "url": "https://www.mi.co.id/id/product-list/",
        "scraper": scrape_xiaomi
    },
    "topup": {
        "url": "https://topupgim.com/product/magic-chess-go-go/1528273402",
        "scraper": scrape_topup
    },
    "itemku": {
        "url": "https://www.itemku.com/g/king-legacy-roblox/semua",
        "scraper": scrape_itemku
    }
}
