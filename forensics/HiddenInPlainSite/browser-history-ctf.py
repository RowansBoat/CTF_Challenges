#!/usr/bin/env python3
import sqlite3
import random
from datetime import datetime, timedelta
import base64
import os

flag = "CTF{Br0ws1ng_H1st0ry_T3lls_All}"
flag_b64 = base64.b64encode(flag.encode()).decode()

if os.path.exists('browsing_history.db'):
    os.remove('browsing_history.db')

conn = sqlite3.connect('browsing_history.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL,
        title TEXT,
        visit_count INTEGER DEFAULT 0,
        last_visit_time INTEGER
    )
''')

def chrome_timestamp(dt):
    epoch = datetime(1601, 1, 1)
    delta = dt - epoch
    return int(delta.total_seconds() * 1000000)

base_time = datetime.now() - timedelta(days=30)

normal_sites = [
    ("https://www.google.com/search?q=how+to+survive+a+meltdown", "Google Search - how to survive a meltdown"),
    ("https://www.google.com/search?q=nuclear+reactor+safety+protocols", "Google Search - nuclear reactor safety protocols"),
    ("https://www.google.com/search?q=how+to+survive+nuclear+fallout", "Google Search - how to survive nuclear fallout"),
    ("https://en.wikipedia.org/wiki/Nuclear_meltdown", "Wikipedia - Nuclear meltdown"),
    ("https://en.wikipedia.org/wiki/Chernobyl_disaster", "Wikipedia - Chernobyl disaster"),
    ("https://www.reddit.com/r/nuclear/comments/reactor_incident", "Reddit - Reactor incident discussion"),
    ("https://www.youtube.com/watch?v=radiation_exposure_symptoms", "YouTube - Radiation Exposure Symptoms"),
    ("https://www.amazon.com/Geiger-Counter/dp/B08N5WRWNW", "Amazon - Geiger Counter"),
    ("https://www.amazon.com/Nuclear-Survival-Guide/dp/B07X6K9PQR", "Amazon - Nuclear Survival Guide"),
    ("https://www.google.com/search?q=emergency+shutdown+procedures", "Google Search - emergency shutdown procedures"),
    ("https://news.ycombinator.com/item?id=nuclear_facility_breach", "Hacker News - Nuclear Facility Security Breach"),
    ("https://www.google.com/search?q=spectre+meltdown+vulnerability+exploit", "Google Search - spectre meltdown vulnerability exploit"),
    ("https://stackoverflow.com/questions/kernel-memory-leak", "Stack Overflow - Kernel memory leak question"),
    ("https://github.com/security/advisories/meltdown-spectre", "GitHub - Meltdown/Spectre Security Advisory"),
    ("https://www.hackthebox.com/", "Hack The Box"),
    ("https://tryhackme.com/dashboard", "TryHackMe Dashboard"),
    (f"https://pastebin.com/{flag_b64}", "Pastebin code"),  # FLAG HERE
    ("https://www.google.com/search?q=emergency+bunker+locations", "Google Search - emergency bunker locations"),
    ("https://www.reddit.com/r/preppers/emergency_supplies", "Reddit - Emergency Supplies Discussion"),
    ("https://www.youtube.com/watch?v=nuclear_disaster_documentary", "YouTube - Nuclear Disaster Documentary"),
    ("https://www.google.com/search?q=radiation+sickness+treatment", "Google Search - radiation sickness treatment"),
    ("https://twitter.com/NuclearNews/status/facility_alert", "Twitter - Nuclear Facility Alert"),
    ("https://www.amazon.com/Potassium-Iodide-Tablets/dp/B09K7HMXYZ", "Amazon - Potassium Iodide Tablets"),
    ("https://www.google.com/search?q=nuclear+plant+evacuation+zones", "Google Search - nuclear plant evacuation zones"),
    ("https://en.wikipedia.org/wiki/Fukushima_disaster", "Wikipedia - Fukushima disaster"),
    ("https://www.reddit.com/r/AskScience/nuclear_safety", "Reddit - Nuclear safety questions"),
    ("https://www.google.com/search?q=iodine+tablets+dosage", "Google Search - iodine tablets dosage"),
    ("https://www.youtube.com/watch?v=reactor_core_breach", "YouTube - Reactor Core Breach Explained"),
]

for i, (url, title) in enumerate(normal_sites, 1):
    visits = random.randint(1, 15)
    last_visit = chrome_timestamp(base_time + timedelta(days=random.randint(0, 30)))
    cursor.execute('INSERT INTO urls (id, url, title, visit_count, last_visit_time) VALUES (?, ?, ?, ?, ?)',
                   (i, url, title, visits, last_visit))

conn.commit()
conn.close()

print(f"Created browsing_history.db")
print(f"Flag: {flag}")
print(f"Flag (base64): {flag_b64}")
print(f"Hidden in: https://pastebin.com/{flag_b64}")
