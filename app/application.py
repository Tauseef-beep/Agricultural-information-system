
from data.crop_data import (
    cereals_data,
    Agriculture_data,
    Fruit_Data,
    Oil_Seed_data,
    Beverages_data,
)
def display_intro():
    print('-------------------- Welcome to the Agriculture information system ----------------------------')
    print('1. Select the crops \n 2. Add, remove or update the crops')
# ----------------------- SELECT CROPS -----------------------
def select_crops(crops):   
    if crops == 1:
        print(' The information for the Cereals are ')
        for item in cereals_data:
            print(item[0])
        cereals_crops = input(' Enter the names of the cereals crops to get the details: ')
        for item in cereals_data:
            if item[0].lower() == cereals_crops.lower():
                print(item[1])
    elif crops == 2:
        print(' The information ofr the Agriculture crops are')
        for items in Agriculture_data:
            print(items[0])
        Agriculture_crop = input(' Please enter the name of the Agriculture crop to get the details: ')
        for items in Agriculture_data:
            if items[0].lower() == Agriculture_crop.lower():
                print(items[1])
    elif crops == 3:
        print(' The information for the Fruit Crops is : ')
        for items in Fruit_Data:
            print(items[0])
        Fruit_Crop = input('Please eneter the name of the Fruit Crop: ')
        for items in Fruit_Data:
            if items[0].lower() == Fruit_Crop.lower():
                print(items[1])
    elif crops == 4:
        print(' The information for the Oil Seed Crops is : ')
        for items in Oil_Seed_data:
            print(items[0])
        Oil_Seed_crop = input('Please enter the name of the Oil Seed Crop: ')
        for items in Oil_Seed_data:
            if items[0].lower() == Oil_Seed_crop.lower():
                print(items[1])
    elif crops == 5:
        print(' The information for the Beverages crops are: ')
        for items in Beverages_data:
            print(items[0])
        Beverages_crop = input(' Please enter the name of the Beverages crops to get the details: ')
        for items in Beverages_data:
            if items[0].lower() == Beverages_crop.lower():
                print(items[1])

# ----------------------- FUNCTIONS TO ADD / UPDATE / REMOVE -----------------------

def add_crop(data, name, details):
    data.append([name, details])
def update_crop(data, name, new_details):
    for item in data:
        if item[0].lower() == name.lower():
            item[1] = new_details
            return True
    return False
def remove_crop(data, name):
    for item in data:
        if item[0].lower() == name.lower():
            data.remove(item)
            return True
    return False
# ----------------------- SELECT CATEGORY FOR MODIFICATION -----------------------
def select_category_data():
    print('\n Select the category:')
    print('1. Cereals')
    print('2. Vegetables and melons')
    print('3. Fruit and nuts')
    print('4. Oilseed crops')
    print('5. Beverage and spice crops')

    category = int(input(' Enter the category number: '))

    if category == 1:
        return cereals_data

    elif category == 2:
        return Agriculture_data

    elif category == 3:
        return Fruit_Data

    elif category == 4:
        return Oil_Seed_data

    elif category == 5:
        return Beverages_data

    else:
        print(' Invalid category!')
        return None


# ----------------------- ADD / UPDATE / REMOVE MENU -----------------------

def manage_crops():

    data = select_category_data()

    if data is None:
        return

    print('\n Select the operation:')
    print('1. Add a crop')
    print('2. Update a crop')
    print('3. Remove a crop')

    operation = int(input(' Please select the operation: '))

    if operation == 1:

        name = input(' Enter the new crop name: ')
        details = input(' Enter the crop details: ')
        add_crop(data, name, details)
        print(' Crop added successfully!')
    elif operation == 2:
        name = input(' Enter the crop name to update: ')
        new_details = input(' Enter the new crop details: ')
        result = update_crop(data, name, new_details)
        if result:
            print(' Crop updated successfully!')
        else:
            print(' Crop not found!')
    elif operation == 3:
        name = input(' Enter the crop name to remove: ')
        result = remove_crop(data, name)
        if result:
            print(' Crop removed successfully!')
        else:
            print(' Crop not found!')

    else:
        print(' Invalid operation!')
# ----------------------- MAIN FUNCTION -----------------------

def main():
    display_intro()
    select_features = int(input(' Please select the features: '))
    if select_features == 1:
        print(' Select the crop according to the Numbering \n 1. Cereals \n 2. Vegetables and melons \n 3. Fruit and nuts \n 4. Oilseed crops \n 5. Beverage and spice crops')
        crops = int(input(' Please enter the numbering of the crop to continue: '))
        select_crops(crops)
    elif select_features == 2:
        manage_crops()
    else:
        print(' Invalid feature selection!')
if __name__ == "__main__":
    main()
