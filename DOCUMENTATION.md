# Documentation

This file explains how the Agricultural Information System is put together and what each function does. If you only want to run the program, the README is enough. Read this one if you want to change the code or just understand it.

## 1. How the program is organised

There are three parts:

| Part | File | Job |
|------|------|-----|
| Entry point | `main.py` | Imports `main()` and runs it |
| Logic | `app/application.py` | Menus, input handling, and all the functions |
| Data | `data/crop_data.py`, `data/crop_problems_data.py` | The actual crop and disease information |

Keeping the data away from the logic means you can add a new crop without touching any function.

### Program flow

1. `main.py` calls `main()`.
2. `main()` shows the welcome menu and asks which feature you want.
3. Depending on your answer it goes to one of three places:
   - **1** goes to `select_crops()` to read about a crop
   - **2** goes to `manage_crops()` to add, update or remove crops
   - **3** goes to `diagnose_crop_disease()` to look up diseases

The program does one task and then ends. It does not loop back to the menu.

## 2. The data files

### `data/crop_data.py`

This file holds five lists, one per crop category. Each list contains smaller lists with two items: the crop name and its description.

```python
['Wheat', 'Wheat is a cereal crop widely grown for its grains...']
#   [0]            [1]
# name          description
```

The five lists are:

- `cereals_data`
- `Agriculture_data` (vegetables and melons)
- `Fruit_Data`
- `Oil_Seed_data`
- `Beverages_data` (beverage and spice crops)

Some descriptions contain `\n`, which just breaks the line when the text is printed.

### `data/crop_problems_data.py`

This file holds one dictionary called `crop_problems`.

- The **key** is the crop name in lowercase, for example `"wheat"`.
- The **value** is a list of diseases. Each disease is a dictionary with five fields.

```python
crop_problems = {
    "wheat": [
        {
            "problem": "Yellow Rust",
            "symptoms": "...",
            "cause": "...",
            "solution": "...",
            "prevention": "...",
        },
    ],
}
```

The crop key must be lowercase, because the program lowercases whatever the user types before looking it up. If you add a crop with capital letters in the key, it will never be found.

## 3. Constants

### `CATEGORIES`

A dictionary that connects a menu number to a category name and its data list:

```python
CATEGORIES = {
    1: ('Cereals', cereals_data),
    2: ('Vegetables and melons', Agriculture_data),
    ...
}
```

Several functions use it, so the menus, the lookups and the editing all stay in sync. To add a new category, add one more line here (and a new list in `crop_data.py`).

## 4. Function reference

### Helper functions

#### `get_int(prompt)`

Asks the user for a number and returns it as an integer.

- **Takes:** `prompt`, the text to show before waiting for input.
- **Returns:** the number, or `None` if the user typed something that is not a whole number (and it prints "Please enter a valid number!").
- **Why it exists:** a plain `int(input(...))` crashes the program if someone types a letter. This function catches that error so the program can exit politely instead. Callers check for `None` before carrying on.

#### `print_categories()`

Prints the numbered list of categories (1. Cereals, 2. Vegetables and melons, and so on) by looping through `CATEGORIES`. It returns nothing.

### Intro

#### `display_intro()`

Prints the welcome banner and the three main options. It does not ask for input; that is left to `main()`.

### Feature 1: selecting crops

#### `select_crops(category)`

Shows the crops in one category and prints the description of the one the user picks.

- **Takes:** `category`, the category number (1 to 5).
- **What it does:**
  1. Checks the number exists in `CATEGORIES`. If not, it prints "Invalid category!" and stops.
  2. Prints the names of every crop in that category.
  3. Asks for a crop name, then removes extra spaces and lowercases it.
  4. Compares it against each crop name (also lowercased) and prints the description on the first match.
  5. If nothing matches, prints "Crop not found!".
- **Returns:** nothing.

### Feature 2: adding, updating and removing crops

#### `add_crop(data, name, details)`

Adds a new `[name, details]` entry to the end of a category list.

- **Takes:** the category list, the crop name, and its description.
- **Returns:** nothing.
- **Note:** it does not check for duplicates, so adding the same crop twice creates two entries.

#### `update_crop(data, name, new_details)`

Finds a crop by name and replaces its description.

- **Takes:** the category list, the crop name to find, and the new description.
- **Returns:** `True` if the crop was found and changed, `False` if it was not found.
- **Note:** matching ignores capital letters and extra spaces around the name.

#### `remove_crop(data, name)`

Finds a crop by name and deletes it from the list.

- **Takes:** the category list and the crop name.
- **Returns:** `True` if it was removed, `False` if it was not found.
- It returns right after removing, which is what makes it safe to delete from a list while looping over it.

#### `select_category_data()`

Asks the user which category they want to edit and gives back the matching list.

- **Returns:** the list (for example `Fruit_Data`), or `None` if the input was not a number or not a valid category.
- It works on the real list, not a copy, so any change made afterwards affects the data the program is using.

#### `manage_crops()`

The menu for feature 2. It ties the three functions above together.

1. Calls `select_category_data()`. If that returns `None`, it stops.
2. Shows the operations: add, update, or remove.
3. Depending on the choice, asks for the details it needs and calls `add_crop()`, `update_crop()` or `remove_crop()`.
4. Prints a success message, or "Crop not found!" if an update or removal could not find the crop.

When adding, it refuses an empty name or description. When the operation number is not 1, 2 or 3, it prints "Invalid operation!".

### Feature 3: diagnosing crop diseases

#### `display_crops()`

Prints every crop that has disease information, taken from the keys of `crop_problems`. The names are shown with a capital first letter.

#### `display_crop_diseases(crop_name)`

Prints a numbered list of diseases for one crop.

- **Takes:** `crop_name`, in lowercase.
- **Returns:** the list of disease dictionaries for that crop, or `None` if the crop is not in `crop_problems` (it prints "Invalid crop name!" in that case).
- The numbers shown to the user start at 1, even though Python lists start at 0. That is why other code subtracts 1 later.

#### `display_disease_details(disease)`

Prints the full information about a single disease: name, symptoms, cause, solution and prevention.

- **Takes:** `disease`, one of the dictionaries from the crop's disease list.
- **Returns:** nothing.

#### `diagnose_crop_disease()`

The main function for feature 3. It runs the whole diagnosis from start to finish:

1. Shows the available crops with `display_crops()`.
2. Asks the user for a crop name (spaces removed, converted to lowercase).
3. Shows that crop's diseases with `display_crop_diseases()`. If the crop does not exist, it stops.
4. Asks for a disease number using `get_int()`. If the input is not a number, it stops.
5. Checks the number is within range. If not, it prints "Invalid disease number!".
6. Shows the full details with `display_disease_details()`, using `disease_number - 1` to turn the user's number into the right list position.

### Main

#### `main()`

The starting point of the program.

1. Calls `display_intro()`.
2. Reads the user's choice with `get_int()`.
3. Option 1 shows the category list, asks for a number, and calls `select_crops()`.
4. Option 2 calls `manage_crops()`.
5. Option 3 calls `diagnose_crop_disease()`.
6. Any other number prints "Invalid option!".

## 5. Error handling

The program is written so that wrong input gives a message instead of a crash:

| Situation | What happens |
|-----------|--------------|
| Typing a letter where a number is expected | "Please enter a valid number!" and the current task ends |
| Category number that does not exist | "Invalid category!" |
| Crop name that is not in the list | "Crop not found!" |
| Crop name with no disease data | "Invalid crop name!" |
| Disease number out of range | "Invalid disease number!" |
| Empty name or details when adding a crop | "Name and details cannot be empty!" |

## 6. How to extend it

**Add a crop to an existing category.** Add a new `['Name', 'Description']` line to the right list in `data/crop_data.py`. You can also do it while the program is running through option 2, but that will not be saved.

**Add disease information for a crop.** Add a new key in `crop_problems` (lowercase) with a list of disease dictionaries. All five fields (`problem`, `symptoms`, `cause`, `solution`, `prevention`) must be present, or `display_disease_details()` will raise a `KeyError`.

**Add a new category.**
1. Create a new list in `crop_data.py`.
2. Import it at the top of `application.py`.
3. Add it to `CATEGORIES` with the next number.

The menus pick it up automatically.

## 7. Known limitations

- Data changes made while the program is running are lost when it closes.
- The program handles one task per run and does not return to the main menu.
- `add_crop()` does not stop duplicate names.
- Disease data covers only a dozen crops, and the advice is general rather than specific to a region or season.
