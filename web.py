# web.py - NEW file. It does not change any of your old files.
# It reuses your data lists and your add_crop / update_crop / remove_crop functions.
from flask import Flask, render_template, request
from app.application import (
    cereals_data, Agriculture_data, Fruit_Data, Oil_Seed_data, Beverages_data,
    add_crop, update_crop, remove_crop,
)

web = Flask(__name__)

# category number -> (name shown on page, your data list)
CATEGORIES = {
    "1": ("Cereals", cereals_data),
    "2": ("Vegetables and melons", Agriculture_data),
    "3": ("Fruit and nuts", Fruit_Data),
    "4": ("Oilseed crops", Oil_Seed_data),
    "5": ("Beverage and spice crops", Beverages_data),
}


@web.route("/", methods=["GET", "POST"])
def home():
    message = ""
    category = request.values.get("category", "")
    crop = request.values.get("crop", "")
    details = ""

    # Part 2: add / update / remove (same functions you already wrote)
    if request.method == "POST" and request.form.get("form") == "manage":
        data = CATEGORIES.get(request.form.get("m_category"), (None, None))[1]
        operation = request.form.get("operation")
        name = request.form.get("name", "").strip()
        text = request.form.get("text", "").strip()
        if data is None or not name:
            message = "Please choose a category and type a crop name."
        elif operation == "add":
            add_crop(data, name, text)
            message = "Crop added successfully!"
        elif operation == "update":
            message = "Crop updated successfully!" if update_crop(data, name, text) else "Crop not found!"
        elif operation == "remove":
            message = "Crop removed successfully!" if remove_crop(data, name) else "Crop not found!"
        category, crop = "", ""

    # Part 1: show crops of a category and the details of the chosen crop
    crops = []
    if category in CATEGORIES:
        crops = [item[0] for item in CATEGORIES[category][1]]
        for item in CATEGORIES[category][1]:
            if crop and item[0].lower() == crop.lower():
                details = item[1]

    return render_template("index.html", categories=CATEGORIES, category=category,
                           crops=crops, crop=crop, details=details, message=message)


if __name__ == "__main__":
    web.run(debug=True)
