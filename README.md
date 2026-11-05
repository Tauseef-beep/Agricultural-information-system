# Agriculture Information System

A simple Python project to view and manage crop information. It has two ways to run:

1. **Terminal version** (original): works with text input in the terminal.
2. **Web version** (HTML + CSS): works in the browser using Flask.

## Folder structure

```text
Agricultural-information-system/
├── main.py              # starts the terminal version
├── web.py               # starts the web version (Flask)
├── app/
│   ├── __init__.py
│   └── application.py   # functions: select, add, update, remove crops
├── data/
│   ├── __init__.py
│   └── crop_data.py     # crop lists (cereals, vegetables, fruits, oilseeds, beverages)
├── templates/
│   └── index.html       # web page
├── static/
│   └── style.css        # web page styling
└── README.md
```

## Features

- Select a crop category and view crop details
- Add a new crop
- Update crop details
- Remove a crop

Categories: Cereals, Vegetables and melons, Fruit and nuts, Oilseed crops, Beverage and spice crops.

## How to run

Open the project folder in VS Code, then open **Terminal → New Terminal**.

### Terminal version

```bash
python main.py
```

### Web version

```bash
pip install flask
python web.py
```

Then open http://127.0.0.1:5000 in your browser. Press `Ctrl + C` in the terminal to stop.

## Note

Changes made with add, update or remove are stored in memory only. They are lost when the program stops.