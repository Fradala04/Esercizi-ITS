import random
positions:list = []
for i in range(1, 71):
    positions.append(i)

random_number = random.randint(1,10)

def tortoise_move():
    match random_number:
        case random_number if 1<=random_number<=5:
            tortoise_position += 3
        case random_number if 6<=random_number<=7:
            tortoise_position -= 6 
            if tortoise_position < 1:
                tortoise_position = 1
        case random_number if 8<=random_number<=10:
            tortoise_position += 1


def hare_move():
    match random_number:
        case random_number if 1<=random_number<=2:
            pass
        case random_number if 3<=random_number<=4:
            hare_position += 9
        case random_number if random_number == 5:
            hare_position -= 12
            if hare_position < 1:
                hare_position = 1
        case random_number if 6<=random_number<=8:
            hare_position += 1
        case random_number if 9<=random_number<=10:
            hare_position -= 2
            if hare_position < 1:
                hare_position = 1
