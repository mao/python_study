favorite_nums = { 'Eric': 8, 'Rose': 13, 'Jack': 7, 'Abraham': 4, 'smith': 10, 'joHn': 6}

for key in favorite_nums.keys():
    print(key.lower().title(), 'is favorite ', str(favorite_nums[key]))