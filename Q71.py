#The author is Vinni Paradiso
def count_hashtags(string):
        total = 0
        index = 0
        while index < len(string):
            for ch in string:
                if ch == "#":
                    total += 1
                    index += 1
                else:
                    index += 0
                return total
print(count_hashtags("#living #my #best #life"))
