# Agricultural Information System

A small command-line program written in Python that works like a pocket guide for farmers and agriculture students. You can look up information about common crops, add or edit crop entries yourself, and check what is wrong with a crop by browsing its common diseases.

I built it as a university project, so it keeps things simple on purpose: no database, no external libraries, just plain Python lists and dictionaries.

## What it can do

1. **Look up crops.** Pick a category (cereals, vegetables, fruits, oilseeds, or beverage and spice crops), see the list of crops in it, and read a short description of the one you choose.
2. **Add, update or remove crops.** If a crop is missing or a description needs fixing, you can change it from inside the program.
3. **Diagnose crop diseases.** Choose a crop, pick one of its common diseases, and the program shows the symptoms, the cause, what to do about it, and how to stop it coming back.

## What you need

- Python 3.8 or newer
- Nothing else. There are no packages to install.

## How to run it

Open a terminal in the project folder (the one that contains `main.py`) and run:

```
python main.py
```

You will see a small menu. Type the number of the option you want and press Enter.

## A quick example

```
-------------------- Welcome to the Agriculture information system ----------------------------
 1. Select the crops
 2. Add, remove or update the crops
 3. Diagnose the disease in the crops
 Please select the features: 3

========== AVAILABLE CROPS ==========
- Wheat
- Rice
- Maize
...

Enter the crop name: wheat

========== DISEASES OF WHEAT ==========
1. Yellow Rust
2. Loose Smut
3. Powdery Mildew

Enter the disease number: 1
```

After that the program prints the symptoms, cause, solution and prevention for Yellow Rust.

## Project structure

```
Agricultural-information-system/
├── main.py                      # Starts the program
├── app/
│   ├── __init__.py
│   └── application.py           # All the menus and logic
└── data/
    ├── __init__.py
    ├── crop_data.py             # Crop descriptions, grouped by category
    └── crop_problems_data.py    # Diseases for each crop
```

If you want to know what every function does, read `DOCUMENTATION.md`.

## Things to know

- **Changes are not saved.** When you add, update or remove a crop, it only lasts until the program closes. The next time you run it, you get the original data back. Saving to a file (for example JSON) would be a good next step.
- **Disease information covers only some crops.** Right now there are entries for wheat, rice, maize, sorghum, tomatoes, eggplants, cabbages, mangoes, bananas, mustard, sunflowers and chillies. You can add more in `data/crop_problems_data.py`.
- **The disease advice is general.** It is meant for learning and for a first idea of what might be wrong. For a real field problem, check with a local agriculture officer before spraying anything.
- **Spelling matters a little.** Crop names are not case sensitive (`wheat`, `Wheat` and `WHEAT` all work), but they must be spelled the same way as in the list.

## Ideas for later

- Save changes to a JSON file so they stay between runs
- Add more crops and diseases
- Let users search by symptom instead of by crop name
- Build a simple graphical interface

## Author

*Add your name, course and university here.*
