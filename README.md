# Auction CSV Parser – USA Vehicle Auctions
## Projekt zaliczeniowy z przedmiotu "Zaawansowane programowanie w Pythonie" SGGW 2026
### Autor: Michał Wroński

Projekt w Pythonie do przetwarzania danych z plików CSV dotyczących aukcji samochodów w USA.  
Dzięki modularnej architekturze i zastosowaniu dobrych praktyk (SOLID, wzorce projektowe, dataclasses, pydantic, multithreading) projekt jest wydajny, czytelny i łatwy do rozbudowy.

---

## 📁 Struktura repozytorium
```text
data/
├── raw/ # surowe pliki CSV z danymi aukcji
└── processed/ # przetworzone pliki CSV (generowane przez program)

src/
├── init.py
├── csv_parser.py # ładowanie i parsowanie CSV, obsługa multithreadingu
├── enums.py # definicja Enumów (FuelType, SellerType)
├── factory.py # fabryki tworzące obiekty Vehicle i Auction z CSV
├── main.py # punkt wejścia programu, zapis wyników do CSV
├── models.py # dataclasses: Vehicle, Auction
└── validation_models.py # pydantic dataclasses do walidacji danych

tests/
├── init.py
├── test_csv_parser.py # testy integracyjne parsera CSV
└── test_factory.py # testy jednostkowe fabryk i walidacji danych
```

📌 **Uwaga:** Pliki w `data/raw/` są częścią repozytorium i **nie są ignorowane** w `.gitignore`, aby program miał dostęp do danych.

---

## ⚙️ Co zostało zrobione

Projekt spełnia wszystkie kryteria wymagane do oceny:

1. **Dataclasses** – `models.py` zawiera klasy `Vehicle` i `Auction`; `validation_models.py` używa pydantic dataclasses do walidacji danych.  
2. **Async / multithreading** – `csv_parser.py` używa `ThreadPoolExecutor` do równoległego wczytywania CSV.  
3. **SOLID / wzorce projektowe** – fabryki (`VehicleFactory`, `AuctionFactory`) implementują wzorzec **Factory Method**; separacja logiki od modeli danych.  
4. **Testy jednostkowe** – `tests/test_factory.py` i `tests/test_csv_parser.py` testują parser CSV, walidację pól, konwersje i Enumy.  
5. **Typowanie zmiennych** – wszystkie dataclasses i funkcje posiadają adnotacje typów (`Optional`, `List`, `str`, `int`).  
6. **Enumy i Pydantic** – `enums.py` definiuje FuelType i SellerType; `validation_models.py` waliduje dane wejściowe.  

---

## 🚀 Uruchomienie projektu

> Projekt wymaga Pythona 3.12 i aktywnego wirtualnego środowiska (`venv`).

1. Aktywuj środowisko:

```bash
venv\Scripts\activate
```

2. Zainstaluj zależności (jeśli nie są jeszcze zainstalowane):

```bash
pip install -r requirements.txt
```
3. Uruchom program:

```bash
python -m src.main
```

Wynik zostanie zapisany w:
data/processed/vehicles_out.csv


## 🧪 Uruchamianie testów

Testy znajdują się w katalogu tests/ i są uruchamiane przy użyciu pytest:

```bash
pytest tests/
```

Testy sprawdzają:
- poprawność walidacji i parsowania pól liczbowych,
- poprawność parsowania Enumów,
- poprawne wczytywanie i agregowanie danych z CSV.
