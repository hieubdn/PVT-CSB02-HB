# Khai báo dictionary mô tả nhân vật
character = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': ['Shield', 'Bread Loaf'],
    'Gold': 100,
    'Level': 2
}

# In ra thông tin ban đầu của nhân vật
print("Thông tin ban đầu của nhân vật:")
print(character)

# Update 50 Gold cho nhân vật
character['Gold'] += 50

# Update FlintStone vào Backpack của nhân vật
character['Backpack'].append('FlintStone')

# Thêm mô tả Pocket cho nhân vật
character['Pocket'] = ['MonsterDex', 'Flashlight']

# In ra thông tin sau các cập nhật
print("\nThông tin sau các cập nhật:")
print(character)
