import art
import game_data
import random

print(art.logo)
countOfDataInSample = len(game_data.data)
score = 0
compare_list = []
def get_random_data_to_compare(compare_list, count):
    random_int_list=[]
    selected=[]
    if compare_list:
        selected.append(compare_list)
    while len(random_int_list)!= count:
        random_int = random.randint(0, countOfDataInSample-1)
        if random_int not in random_int_list:
            if len(compare_list)>0:
                if game_data.data[random_int]["name"] != compare_list["name"]:
                    random_int_list.append(random_int)
                    selected.append(game_data.data[random_int])
            else:
                random_int_list.append(random_int)
                selected.append(game_data.data[random_int])
    return selected

def compare_followers(comparelist, choice):
    if choice == 'A':
        return comparelist[0]["follower_count"] > comparelist[1]["follower_count"]
    else:
        return comparelist[1]["follower_count"] > comparelist[0]["follower_count"]

def render(compare_list, which):
    print(f"Compare {which}: {compare_list["name"]}, a {compare_list["description"]}, from {compare_list["country"]}")


compare_list = get_random_data_to_compare(compare_list, 2)
canContinue = True
while canContinue:
    if score>0:
        print("\n" * 20)
        print(art.logo)
        print(f"You're right! Current score: {score}")
        compare_list = compare_list.pop()
        compare_list = get_random_data_to_compare(compare_list,1)
    render(compare_list[0], 'A')
    print(art.vs)
    render(compare_list[1], 'B')
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if compare_followers(compare_list, choice):
        score+=1
    else:
        print("\n"*6)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        canContinue = False