import asyncio
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from playwright.async_api import async_playwright
from pathlib import Path
from excel import create_main_sheet2, create_equipement_sheet2, init_excel, save_excel

load_dotenv()

pathfile = Path(__file__).parent / "webscraping"


url = "https://d-bk.net/fr/dw/25Ca"


async def run(pw):
    print("Connecting to Browser API...")
    browser = await pw.chromium.launch(headless=True)
    try:
        print("Connected! Navigating...")
        page = await browser.new_page()
        await page.goto(url, timeout=2 * 60 * 1000)
        print("Navigated! Scraping page content...")
        html = await page.content()
        return html
    finally:
        await browser.close()


def scrap(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="mb-10")
    equipements = soup.find_all("div", class_="widget full-height")
    equipements = equipements[1:]

    # Préparation des données pour Excel

    # Préparation des données items
    data_main = []  # [(nom_item, qty_item)]
    for item in items:
        compos = item.find_all("div", class_="wrapper")
        for compo in compos:
            # print(compo)
            nom_compo = compo.find("div", class_="mr-8").text.strip()
            qty_compo = (
                compo.find("div", class_="count text-nowrap").text.split("/")[1].strip()
            )
            data_main.append([nom_compo, int(qty_compo)])

    # Préparation des données équipements
    data_equipements = {}  # nom_item: [(nom_compo, qty_compo)]

    for equipement in equipements:
        nom_item = equipement.find("a", class_="title link-white").text.strip()
        compos = equipement.find_all("div", class_="ingredient py-1")
        data_equipements[nom_item] = []
        for compo in compos:
            nom_compo = compo.find("label", class_="ingredientName").text.strip()
            qty_compo = (
                compo.find("div", class_="ingredientQty").text.split("/")[1].strip()
            )

            data_equipements[nom_item].append((nom_compo, qty_compo))

    wb, ws, base_path, fileresult = init_excel()
    create_main_sheet2(ws, data_main)
    create_equipement_sheet2(wb, data_equipements)

    save_excel(wb, fileresult)


async def main():
    async with async_playwright() as playwright:
        html = await run(playwright)
        scrap(html)


if __name__ == "__main__":
    asyncio.run(main())
    # scrap()
    # print("Starting...")
