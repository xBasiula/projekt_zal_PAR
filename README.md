
# Czat Rozproszony

## Opis
Aplikacja rozproszona składająca się z serwera i dwóch klientów, którzy mogą wymieniać między sobą wiadomości tekstowe za pośrednictwem serwera.

## Wykorzystane technologie
- **Flask** (Python) - do stworzenia serwera REST API.
- **Requests** (Python) - do obsługi żądań HTTP po stronie klientów.

## Struktura projektu
- `server.py`: Serwer aplikacji.
- `client1.py`: Klient 1.
- `client2.py`: Klient 2.

## Uruchamianie aplikacji
1. Uruchom serwer:
   ```bash
   python server.py
   ```
2. Uruchom klientów w osobnych terminalach:
   ```bash
   python client1.py
   python client2.py
   ```

## Przykład komunikacji
1. Klient 1 wysyła wiadomość: "Hello from Client 1!".
2. Klient 2 wysyła wiadomość: "Hello from Client 2!".
3. Obaj klienci mogą pobrać historię wiadomości za pomocą żądania `GET /messages`.

## Problemy i rozwiązania
1. **Problem:** Konflikty w dostępie do listy wiadomości.
   - **Rozwiązanie:** W Flasku obsługa żądań HTTP jest domyślnie sekwencyjna, więc nie występują konflikty.
2. **Problem:** Brak wiadomości przy błędnym formacie danych.
   - **Rozwiązanie:** Zaimplementowano walidację danych po stronie serwera.

## Autor
Twoje Imię i Nazwisko
