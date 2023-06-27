# warehouseManagment
## WYMAGANIA
- Python >[3.10.11](https://www.python.org/downloads/release/python-31011/)
- Node.js [v18.15.0](https://nodejs.org/en/download)
## KONFIGURACJA BACKEND
1. Otwieramy projekt w wybranym IDE
2. W terminalu (w folderze z projektem) uruchamiamy:  `pip install -r requirements.txt` zainstaluje wymagane rzeczy 
3. W terminalu uruchamiamy aplikacje fastAPI za pomocą komendy: `uvicorn main:app --reload`, która uruchomi serwer. Dzięki `--reload` każda zmiana w projekcie automatycznie przeładuje serwer

## KONFIGURACJA FRONTEND
1. W terminalu (w folderze z projektem) wpisujemy polecenie `yarn`(zainstaluje wszystkie potrzebne rzeczy z pliku package.json)
2. W terminalu (w folderze z projektem) wpisujemy komendę: `yarn dev` 
