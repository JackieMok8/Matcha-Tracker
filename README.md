# 🍵 Matcha Tracker

Een gebruiksvriendelijke webapplicatie om al je matcha café-bezoekjes bij te houden, inclusief uitgaven, ratings en grafieken. Gemaakt met Flask, MySQL en Chart.js.

## 🔍 Functionaliteiten

- ➕ Nieuw café toevoegen met details zoals stad, bestelling, prijs, rating en opmerkingen
- 📋 Overzicht van alle ingevoerde cafés
- ✏️ Aanpassen of 🗑️ verwijderen van bestaande cafés
- 📈 Grafieken met totaaluitgaven en aantal bezoeken per week
- 📊 Dashboard met formulier, overzicht en grafiek in één pagina
- 💾 Data-opslag in MySQL database (`matcha_tracker`)

## ⚙️ Technologieën

- **Backend:** Python (Flask)
- **Database:** MySQL
- **Frontend:** HTML5, CSS3
- **Grafieken:** Chart.js
- **Versiebeheer:** Git & GitHub

## 🧪 Installatie & lokaal draaien

1. Clone deze repository:
   ```bash
   git clone https://github.com/JackieMok8/matcha-tracker.git
   ```

2. Navigeer naar de projectmap:
   ```bash
   cd /pad/naar/jouw/projectmap/webform
(Pas het pad aan afhankelijk van waar je de repository hebt opgeslagen)
   ```
```

3. Installeer dependencies:

```bash
pip install flask mysql-connector-python
```

4. Zorg dat MySQL draait en maak de database aan:

   ```sql
   CREATE DATABASE matcha_tracker;
   USE matcha_tracker;

   CREATE TABLE cafes (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100),
       city VARCHAR(100),
       address VARCHAR(255),
       visiting_date DATE,
       order_taken TEXT,
       price DECIMAL(10,2),
       rating DECIMAL(3,1),
       notes TEXT
   );
   ```

5. Start de Flask-app:
   ```bash
   python app.py
   ```

6. Open je browser en ga naar:
   ```
   http://localhost:5000
   ```

## 📸 Screenshots

*Optioneel: voeg hier een paar screenshots toe van je formulier, dashboard en grafieken.*

## 📁 Bestandsoverzicht

| Bestand/folder        | Beschrijving                      |
|-----------------------|------------------------------------|
| `app.py`              | Hoofdlogica van de Flask-app       |
| `templates/`          | HTML-bestanden (form, dashboard)   |
| `Matcha Tracker.sql`  | SQL-script om database op te bouwen|
| `README.md`           | Projectdocumentatie                |
| `requirements.txt`    | Benodigde Python packages          |

## 📬 Contact

Heb je feedback, vragen of wil je meedoen aan dit project?  
Neem contact op via [co_mok@hotmail.com](mailto:co_mok@hotmail.com)

---

Gemaakt met liefde voor matcha ☕ en code 💻 – door **Jackie Mok**
