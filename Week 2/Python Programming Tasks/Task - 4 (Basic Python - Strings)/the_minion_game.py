# the-minion-game

def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    
    for i in range(len(string)):
        if s[i] in vowels:
            print("k",kevin_score)
            kevin_score += (len(s)-i)
        else:
            print("s",stuart_score)
            stuart_score += (len(s)-i)
    
    if kevin_score < stuart_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")

# BANANA
# k   s
# 0   0
# 0   6        
# 5   0
# 0   10
# 8   0
# 0   12
# 1   0

# ----STUART----
# B
# BA
# BAN
# BANA
# BANAN
# BANANA

# N
# NA
# NAN
# NANA

# N
# NA

# ----------------------------------------------------------------------------------------------

# ----KEVIN----
# A
# AN
# ANA
# ANAN
# ANANA

# A
# AN
# ANA

# A

if __name__ == '__main__':
    s = input()
    minion_game(s)