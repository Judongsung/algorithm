from sys import stdin

def find_min_price(potion, prev_subjects=list()):
    if potion in recipe_checked:
        return material_price_dict[potion]
    subjects = prev_subjects+[potion]
    price = -1
    recipes = []
    if potion in material_price_dict:
        price = material_price_dict[potion]
    if potion in recipe_dict and potion not in prev_subjects:
        recipes = recipe_dict[potion]
    
    for recipe in recipes:
        temp_price = 0
        for num_material in recipe.split('+'):
            num = int(num_material[0])
            material = num_material[1:]
            material_price = find_min_price(material, subjects)
            if material_price == -1:
                temp_price = -1
                break
            temp_price += num*material_price
            temp_price = min(temp_price, 1000000001)

        if price == -1 and temp_price > 0:
            price = temp_price
        elif price > 0 and temp_price > 0:
            price = min(price, temp_price)
    
    material_price_dict[potion] = price
    recipe_checked.add(potion)
    return price
    
n, m = map(int, stdin.readline().split())
material_price_dict = {}
recipe_dict = {}

for _ in range(n):
    material, price = stdin.readline().split()
    material_price_dict[material] = int(price)

for _ in range(m):
    potion, materials = stdin.readline().rstrip().split('=')
    if potion not in recipe_dict:
        recipe_dict[potion] = []
    recipe_dict[potion].append(materials)

for i in range(50):
    recipe_checked = set()
    find_min_price('LOVE')
result = material_price_dict['LOVE']
print(result)