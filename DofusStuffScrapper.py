import atelier_dofusDb
import dofusbook
import asyncio
import sys
import os

# Patch pour Playwright + PyInstaller
if hasattr(sys, "_MEIPASS"):
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = os.path.join(sys._MEIPASS, "ms-playwright")
    os.environ["PLAYWRIGHT_DRIVER_PATH"] = os.path.join(
        sys._MEIPASS, "playwright", "driver"
    )

if __name__ == "__main__":
    while True:
        choice = input(
            "Choisissez le script à exécuter (1 pour dofusbook, 2 pour atelier_dofusDb): "
        )
        if choice == "1":
            asyncio.run(dofusbook.main())
            break
        elif choice == "2":
            print(
                "Une fois le fichier Atelier - DofusDB.htm téléchargé, placez-le dans le même dossier que ce script."
            )
            input("Appuyez sur Entrée pour continuer...")
            atelier_dofusDb.main()
            break
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")
