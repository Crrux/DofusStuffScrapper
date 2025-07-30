from bs4 import BeautifulSoup
import excel
from excel import create_main_sheet2, create_equipement_sheet2, init_excel, save_excel


def create_equipement_sheet(wb, equipement):
    nom_equipement = equipement.find("div", class_="text-body1").text.strip()
    compos = equipement.find_all("div", class_="workbench-recipe-ingredient")
    excel.create_equipement_sheet(wb, nom_equipement, compos)


def main():
    wb, ws, base_path, fileresult = init_excel()

    filepath = base_path / "Atelier - DofusDB.htm"
    if not fileresult.parent.exists():
        fileresult.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        soup = BeautifulSoup(content, "html.parser")
    items = soup.find_all("div", class_="row items-center text-bold text-body2 q-mt-xs")
    data_main = []  # [(nom_item, qty_item)]
    for item in items:
        nom_item = item.find("div", class_="item q-img overflow-hidden q-pa-xs").get(
            "aria-label"
        )
        qty_item = item.text.strip().split("/")[1].strip()
        data_main.append([nom_item, qty_item])
    data_equipements = {}  # nom_item: [(nom_compo, qty_compo)]
    equipements = soup.find_all("div", class_="workbench-recipe")
    for equipement in equipements:
        nom_equipement = equipement.find("div", class_="text-body1").text.strip()
        compos = equipement.find_all("div", class_="workbench-recipe-ingredient")
        data_equipements[nom_equipement] = []
        for compo in compos:
            nom_compo = compo.find("div", class_="text-body1").text.strip()
            qty_compo = compo.find("span", class_="text-body2")
            qty_compo = int(qty_compo.text.strip()) if qty_compo else 1

            data_equipements[nom_equipement].append((nom_compo, qty_compo))
    create_main_sheet2(ws, data_main)
    create_equipement_sheet2(wb, data_equipements)
    save_excel(wb, fileresult)


if __name__ == "__main__":
    main()
