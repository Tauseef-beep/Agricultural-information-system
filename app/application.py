# This will import the crop data from the folder ( data and the file crop_data ) and use it in the application.py
from data.crop_data import (
    cereals_data,
    Agriculture_data,
    Fruit_Data,
    Oil_Seed_data,
    Beverages_data,
)
# This function will import the crop_problems_data  from the data file 
# from the crop_problems variable 
from data.crop_problems_data import crop_problems

# Category number -> (display name, data list)
CATEGORIES = {
    1: ('Cereals', cereals_data),
    2: ('Vegetables and melons', Agriculture_data),
    3: ('Fruit and nuts', Fruit_Data),
    4: ('Oilseed crops', Oil_Seed_data),
    5: ('Beverage and spice crops', Beverages_data),
}


# ----------------------- HELPERS -----------------------
# The function will check if the input is a number or not .
def get_int(prompt):
    """Ask for a whole number. Returns None if the input is not a number."""
    try:
        return int(input(prompt))
    except ValueError:
        print(' Please enter a valid number!')
        return None
# This functionw will print all the categories with the correct numbering
def print_categories():
    for number, (name, _) in CATEGORIES.items():
        print(f' {number}. {name}')
# ----------------------- INTRO -----------------------
# This function will display the intro only 
def display_intro():
    print('-------------------- Welcome to the Agriculture information system ----------------------------')
    print(' 1. Select the crops \n 2. Add, remove or update the crops \n 3. Diagnose the disease in the crops')


# ----------------------- SELECT CROPS -----------------------
# This function is use to select the crops from the categories
def select_crops(category):
    if category not in CATEGORIES:
        print(' Invalid category!')
        return
# The name and the data variable points to categorries like cereal , maize 
    name, data = CATEGORIES[category]
    print(f'\n The available crops in {name} are:')
    for item in data:
        print(' -', item[0])
# This will get the crop name from the user
    crop_name = input('\n Enter the name of the crop to get the details: ').strip().lower()
# This function will compare the crop name with the data of the category and if it matches
# then it show all the data ,information of that crop name like for ( wheat, ,maize etc)
    for item in data:
        if item[0].strip().lower() == crop_name:
            print('\n', item[1])
            return
    print(' Crop not found!')
# ----------------------- ADD / UPDATE / REMOVE FUNCTIONS -----------------------
# This function will get 3 inputs data, name , details
def add_crop(data, name, details):
# we will add using the append function for name and detials
    data.append([name, details])
# we will update the crops with the names and the new details like in the function 
def update_crop(data, name, new_details):
    for item in data:
        if item[0].strip().lower() == name.strip().lower():
            item[1] = new_details
            return True
    return False
# This function will remove the crop with compare the data 
# and the name of the crop and .remove function will remove the crop in the data
def remove_crop(data, name):
    for item in data:
        if item[0].strip().lower() == name.strip().lower():
            data.remove(item)
            return True
    return False
# ----------------------- SELECT CATEGORY FOR MODIFICATION -----------------------
# This function will help us understanding and selecting the category 
def select_category_data():
    print('\n Select the category:')
    print_categories()
    category = get_int(' Enter the category number: ')
    if category in CATEGORIES:
        return CATEGORIES[category][1]

    if category is not None:
        print(' Invalid category!')
    return None
# ----------------------- ADD / UPDATE / REMOVE MENU -----------------------
# This function will manage the function of add , remove or update with the data variable
def manage_crops():
    data = select_category_data()
    if data is None:
        return
# This will print all the operations 
    print('\n Select the operation:')
    print(' 1. Add a crop')
    print(' 2. Update a crop')
    print(' 3. Remove a crop')
#  This function will get the numbering of the 
# operation to understand which function have to execute first
    operation = get_int(' Please select the operation: ')
# This function will run if the operation is int 1
    if operation == 1:
        name = input(' Enter the new crop name: ').strip()
        details = input(' Enter the crop details: ').strip()
        if not name or not details:
            print(' Name and details cannot be empty!')
            return
        add_crop(data, name, details)
        print(' Crop added successfully!')
# This function will execute if the operation input is int 2
    elif operation == 2:
        name = input(' Enter the crop name to update: ')
        new_details = input(' Enter the new crop details: ')
        if update_crop(data, name, new_details):
            print(' Crop updated successfully!')
        else:
            print(' Crop not found!')
    elif operation == 3:
        name = input(' Enter the crop name to remove: ')
        if remove_crop(data, name):
            print(' Crop removed successfully!')
        else:
            print(' Crop not found!')

    elif operation is not None:
        print(' Invalid operation!')

# ----------------------- DIAGNOSE THE DISEASE IN THE CROPS -----------------------
# This function will display the information for the available crops
def display_crops():
    """Display all crops that have disease information."""
    print("\n========== AVAILABLE CROPS ==========")
    for crop_name in crop_problems:
        print(f"- {crop_name.title()}")

# This function will display the crop_disease
def display_crop_diseases(crop_name):
    """Display all diseases of the selected crop."""
    diseases = crop_problems.get(crop_name)
    if diseases is None:
        print("\nInvalid crop name!")
        return None
    print(f"\n========== DISEASES OF {crop_name.upper()} ==========")
    for index, disease in enumerate(diseases, start=1):
        print(f"{index}. {disease['problem']}")
    return diseases
# This function will display the disease details
def display_disease_details(disease):
    """Display complete details of a selected disease."""
    print("\n========== DISEASE DETAILS ==========")
    print(f"\nDisease: {disease['problem']}")
    print(f"Symptoms: {disease['symptoms']}")
    print(f"Cause: {disease['cause']}")
    print(f"Solution: {disease['solution']}")
    print(f"Prevention: {disease['prevention']}")

# This function will diagnose the crop disease using the input of the crop name given from the user
def diagnose_crop_disease():
    """Manage the complete crop disease diagnosis process."""
    display_crops()

    crop_name = input("\nEnter the crop name: ").strip().lower()

    diseases = display_crop_diseases(crop_name)
    if diseases is None:
        return

    disease_number = get_int("\nEnter the disease number: ")
    if disease_number is None:
        return
    if not 1 <= disease_number <= len(diseases):
        print("\nInvalid disease number!")
        return
    display_disease_details(diseases[disease_number - 1])

# ----------------------- MAIN FUNCTION -----------------------
# This is the main function which will be executed first in the codebase
def main():
    display_intro()
    select_features = get_int(' Please select the features: ')

    if select_features == 1:
        print('\n Select the crop category according to the numbering:')
        print_categories()
        category = get_int(' Please enter the number of the category to continue: ')
        if category is not None:
            select_crops(category)
    elif select_features == 2:
        manage_crops()
    elif select_features == 3:
        diagnose_crop_disease()
    elif select_features is not None:
        print(' Invalid option!')
# This is the code for executing the main function first in the codebase
if __name__ == "__main__":
    main()
