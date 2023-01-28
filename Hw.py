def choose_coffee(*process):
    global ingredients
    recept = {'Эспрессо': {'cof': 1, 'milk': 0, 'sl': 0},
                 'Капучино': {'cof': 1, 'milk': 3, 'sl': 0},
                 'Кофе по-венски': {'cof': 1, 'milk': 0, 'sl': 2},
                 'Латте Маккиато': {'cof': 1, 'milk': 2, 'sl': 1},
                 'Кон Панна': {'cof': 1, 'milk': 0, 'sl': 1},
                 'Маккиато': {'cof': 2, 'milk': 1, 'sl': 0}}
    cof = ingredients[0]
    milk = ingredients[1]
    sl = ingredients[2]
    for i in process:
        one = cof - recept[i]['cof']
        two = milk - recept[i]['milk']
        three = sl - recept[i]['sl']
        if one >= 0 and two >= 0 and three >= 0:
            ingredients[0] -= recept[i]['cof']
            ingredients[1] -= recept[i]['milk']
            ingredients[2] -= recept[i]['sl']
            return i
    return 'К сожалению, мы не можем предложить Вам напиток'