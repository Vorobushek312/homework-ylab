loss_combo_2 = []

x = 0
y = 0
row_combos = []
for rows in range(10):
    for row in range(7):
        row_combo = []
        for x_y in range(5):
            row_combo.append(x)
            row_combo.append(y)
            x += 120
            row_combos.append(row_combo)
            row_combo = []
        x -= 480
        loss_combo_2.append(row_combos)
        row_combos = []
    y += 80
    x = 0

x = 0
y = 0
collom_combos = []
for colloms in range(10):
    for collom in range(7):
        collom_combo = []
        for y_x in range(5):
            collom_combo.append(x)
            collom_combo.append(y)
            y += 80
            collom_combos.append(collom_combo)
            collom_combo = []
        y -= 320
        loss_combo_2.append(collom_combos)
        collom_combos = []
    x += 120
    y = 0

x = 0
y = 400
top_combos = []
for tops in range(11):
    for top in range(7):
        top_combo = []
        for xy_top in range(5):
            top_combo.append(x)
            top_combo.append(y)
            x += 120
            y += 80
            top_combos.append(top_combo)
            top_combo = []
        y -= 320
        x -= 480
        loss_combo_2.append(top_combos)
        top_combos = []
    y -= 640
    x = 0

x = 480
y = 0
bot_combos = []
for bots in range(11):
    for bot in range(7):
        bot_combo = []
        for xy_bot in range(5):
            bot_combo.append(x)
            bot_combo.append(y)
            x -= 120
            y += 80
            bot_combos.append(bot_combo)
            bot_combo = []
        y -= 320  
        x += 480
        loss_combo_2.append(bot_combos)
        bot_combos = []
    x += 960
    y = 0

