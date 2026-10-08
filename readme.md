# Object Detection Model

Ett Python-projekt för objektdetektering med ett grafiskt användargränssnitt (GUI) och funktionalitet för insamling och hantering av dataset.

## Installation

Installera projektets nödvändiga Python-paket:

```bash
pip install opencv-python pillow keyboard
```

### Dependencies

Projektet använder följande externa bibliotek:

| Bibliotek | Användningsområde |
|-----------|-------------------|
| `opencv-python` (cv2) | Kamerahantering och bildbehandling |
| `pillow` (PIL) | Bildhantering och visning i GUI |
| `keyboard` | Hantering av tangenttryckningar |

Följande bibliotek ingår i Pythons standardbibliotek och behöver inte installeras separat:

| Bibliotek | Användningsområde |
|-----------|-------------------|
| `tkinter` | Grafiskt användargränssnitt (GUI) |
| `os` | Fil- och kataloghantering |
| `shutil` | Kopiering och flytt av filer |
| `datetime` | Generering av tidsstämplar |

> **Note:** Tkinter följer med de flesta vanliga Python-installationer, men kan behöva installeras separat på vissa operativsystem.

## Användning

### Starta gränssnittet

Starta applikationens grafiska gränssnitt med:

```bash
python interface/interface.py
```

### Dela upp datasetet

Kör följande kommando för att dela upp datasetet i tränings-, validerings- och testdata:

```bash
python trainModel/splitDataset.py
```

Datasetet delas upp enligt följande:

| Dataset | Andel |
|---------|-------|
| Training | 70 % |
| Validation | 15 % |
| Test | 15 % |

## Projektstruktur

```text
Object-Detection-Model/
├── interface/
│   └── interface.py
├── trainModel/
│   └── splitDataset.py
├── splittedDataset/
│   ├── train/
│   ├── validate/
│   └── test/
└── README.md
```