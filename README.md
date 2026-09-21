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
damit die Ausgabe als Druckstück für sich steht. Maßgeblich bleibt die Datei im
Repository; die Anlage ist eine Momentaufnahme.

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
