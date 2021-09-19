# Dinesh is fond of video games. Due to the pandemic, he designs a video game called Corona world. In this game, the player enters the game with a certain energy. The player should defeat all the corona infected zombies to reach the next level. When time increases the zombies will increase double the previous minute. Anyhow the player can manage to fight against all the zombies. In this case, definitely the player can not achieve the promotion. Hence the player gets a superpower to destroy all the zombies in the current level when the current game time is a palindrome. Anyhow the player can manage only if he knows the time taken to get the superpower. Help the player by providing the minimum minutes needed to get the superpower by which he can destroy all the zombies. You will be provided with the starting time of the game.
str=input()
h=int(str[0:2])
m=int(str[3:5])
time=int(0)
while (h % 10 != m // 10 or h // 10 != m % 10):
    m=m+1
    if(m==60):
        m=0
        h=h+1
    if(h==24):
        h=0
    time=time+1
print(time)
