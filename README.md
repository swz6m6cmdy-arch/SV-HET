# Kommunalbriefing Sachsen-Anhalt

Tägliche Nachrichtenübersicht für die kommunale Ebene in Sachsen-Anhalt,
zugeschnitten auf die **Stadt Hettstedt** im Landkreis Mansfeld-Südharz
(rund 14.000 Einwohner, kreisangehörige Einheitsgemeinde).

Der stehende Recherchekontext — was für diese Kommune einschlägig ist und was
nicht — steht in [`profil-hettstedt.md`](profil-hettstedt.md) und ist vor jeder
Ausgabe zu lesen und fortzuschreiben.

## Schwerpunkte

- **Gesetzesänderungen** mit Kommunalbezug (KVG LSA, FAG, Fachgesetze, Rechtsprechung)
- **Fördermittelprogramme** inkl. Fristen und Zuständigkeiten
- **Landespolitik**, soweit sie die kommunale Ebene betrifft

## Aufbau einer Ausgabe

Jede Ausgabe liegt unter `briefings/JJJJ-MM-TT-kommunalbriefing-sachsen-anhalt.md`
und folgt derselben Gliederung:

1. Lage des Tages
2. Kommunale Spitzenverbände
3. Kommunalfinanzen
4. Fördermittel
5. Gesetzesänderungen und Rechtsprechung
6. Aus der kommunalen Praxis
7. **Konkret für Hettstedt** — Übersetzung der Landesvorgänge auf die Stadt
8. Termine und Fristen
9. Empfohlene Handlungen
10. Quellennachweis

Optional folgt als **Anlage** eine datierte Wiedergabe von `profil-hettstedt.md`,
damit die Ausgabe als Druckstück für sich steht. Die Anlage liegt bei, wenn sich das
Profil **inhaltlich** geändert hat — nicht bei reinen Fundstellen- oder Datumspflegen.
Maßgeblich bleibt die Datei im Repository; die Anlage ist eine Momentaufnahme.

## Redaktionelle Regeln

- Jede Aussage ist mit einer Quelle belegt; die Quellen stehen gesammelt in der letzten Ziffer.
- Angaben aus nur einer Fundstelle werden mit ⚠️ als ungeprüft gekennzeichnet.
- Widersprüchliche Angaben werden benannt, nicht stillschweigend aufgelöst.
- Eigene Überschlagsrechnungen werden als solche gekennzeichnet und nie als Quelle ausgegeben.
- Liegt zu einem Schwerpunkt nichts Neues vor, wird das ausdrücklich geschrieben,
  statt Altes umzuformulieren.
- Für rechtsverbindliche Entscheidungen gelten ausschließlich die amtlichen
  Verkündungen im GVBl. LSA und die Originalverlautbarungen der Ressorts.

## PDF-Export

Jede Ausgabe laesst sich druckfertig als PDF ausgeben (A4, Seitenzahlen,
anklickbare Quellenlinks):

```
pip install markdown weasyprint
python3 tools/briefing2pdf.py briefings/2026-09-17-kommunalbriefing-sachsen-anhalt.md
```

Mehrere Dateien und ein abweichendes Zielverzeichnis sind moeglich:

```
python3 tools/briefing2pdf.py briefings/*.md --out-dir export/
```

Das Skript gleicht zwei Markdown-Eigenheiten aus, die sonst das Layout
zerstoeren: Listen, die ohne Leerzeile auf einen Absatz folgen, und Emoji,
die von den installierten Schriften nicht gedeckt sind.

## Ausgaben

- [17.09.2026](briefings/2026-09-17-kommunalbriefing-sachsen-anhalt.md)
- [20.09.2026](briefings/2026-09-20-kommunalbriefing-sachsen-anhalt.md) — Sammelausgabe für den Zeitraum 18.–20.09.2026
- [21.09.2026](briefings/2026-09-21-kommunalbriefing-sachsen-anhalt.md)
- [22.09.2026](briefings/2026-09-22-kommunalbriefing-sachsen-anhalt.md)
- [23.09.2026](briefings/2026-09-23-kommunalbriefing-sachsen-anhalt.md)
- [24.09.2026](briefings/2026-09-24-kommunalbriefing-sachsen-anhalt.md)
- [25.09.2026](briefings/2026-09-25-kommunalbriefing-sachsen-anhalt.md)
- [26.09.2026](briefings/2026-09-26-kommunalbriefing-sachsen-anhalt.md) — ohne Profil-Anlage (Profil unverändert)
- [27.09.2026](briefings/2026-09-27-kommunalbriefing-sachsen-anhalt.md)
- [28.09.2026](briefings/2026-09-28-kommunalbriefing-sachsen-anhalt.md)
- [29.09.2026](briefings/2026-09-29-kommunalbriefing-sachsen-anhalt.md) — ohne Profil-Anlage (Profil unverändert)
- [30.09.2026](briefings/2026-09-30-kommunalbriefing-sachsen-anhalt.md) — ohne Profil-Anlage (nur Fundstellenpflege)
- [01.10.2026](briefings/2026-10-01-kommunalbriefing-sachsen-anhalt.md)
- [02.10.2026](briefings/2026-10-02-kommunalbriefing-sachsen-anhalt.md) — ohne Profil-Anlage (nur eine korrigierte Zeile); enthält eine Korrektur zur Ausgabe vom 01.10.
- [03.10.2026](briefings/2026-10-03-kommunalbriefing-sachsen-anhalt.md)
- [04.10.2026](briefings/2026-10-04-kommunalbriefing-sachsen-anhalt.md)
- [05.10.2026](briefings/2026-10-05-kommunalbriefing-sachsen-anhalt.md)
- [06.10.2026](briefings/2026-10-06-kommunalbriefing-sachsen-anhalt.md)
- [07.10.2026](briefings/2026-10-07-kommunalbriefing-sachsen-anhalt.md)
- [08.10.2026](briefings/2026-10-08-kommunalbriefing-sachsen-anhalt.md)
- [09.10.2026](briefings/2026-10-09-kommunalbriefing-sachsen-anhalt.md)
- [10.10.2026](briefings/2026-10-10-kommunalbriefing-sachsen-anhalt.md)
- [11.10.2026](briefings/2026-10-11-kommunalbriefing-sachsen-anhalt.md)
- [12.10.2026](briefings/2026-10-12-kommunalbriefing-sachsen-anhalt.md)
- [13.10.2026](briefings/2026-10-13-kommunalbriefing-sachsen-anhalt.md)
- [14.10.2026](briefings/2026-10-14-kommunalbriefing-sachsen-anhalt.md)
- [15.10.2026](briefings/2026-10-15-kommunalbriefing-sachsen-anhalt.md)
- [16.10.2026](briefings/2026-10-16-kommunalbriefing-sachsen-anhalt.md)
- [17.10.2026](briefings/2026-10-17-kommunalbriefing-sachsen-anhalt.md)
- [18.10.2026](briefings/2026-10-18-kommunalbriefing-sachsen-anhalt.md) — enthält eine Korrektur der Einwohnerzahl
- [19.10.2026](briefings/2026-10-19-kommunalbriefing-sachsen-anhalt.md)
- [20.10.2026](briefings/2026-10-20-kommunalbriefing-sachsen-anhalt.md)
- [21.10.2026](briefings/2026-10-21-kommunalbriefing-sachsen-anhalt.md)
- [22.10.2026](briefings/2026-10-22-kommunalbriefing-sachsen-anhalt.md)
- [23.10.2026](briefings/2026-10-23-kommunalbriefing-sachsen-anhalt.md)
- [24.10.2026](briefings/2026-10-24-kommunalbriefing-sachsen-anhalt.md)
- [25.10.2026](briefings/2026-10-25-kommunalbriefing-sachsen-anhalt.md)
