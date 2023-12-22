# Given data
male_game = 279
female_game = 200
total_game = 479

male_commercials = 81
female_commercials = 156
total_commercials = 237

male_wont_watch = 132
female_wont_watch = 160
total_wont_watch = 292

total_male = 492
total_female = 516
grand_total = 1008

# Calculate percentages
percent_male_game = (male_game / total_male) * 100
percent_female_game = (female_game / total_female) * 100

percent_male_commercials = (male_commercials / total_male) * 100
percent_female_commercials = (female_commercials / total_female) * 100

percent_male_wont_watch = (male_wont_watch / total_male) * 100
percent_female_wont_watch = (female_wont_watch / total_female) * 100

# Display the percentages
print(f"Percentage of males looking forward to watching the game: {percent_male_game:.2f}%")
print(f"Percentage of females looking forward to watching the game: {percent_female_game:.2f}%\n")

print(f"Percentage of males looking forward to watching commercials: {percent_male_commercials:.2f}%")
print(f"Percentage of females looking forward to watching commercials: {percent_female_commercials:.2f}%\n")

print(f"Percentage of males who won't watch: {percent_male_wont_watch:.2f}%")
print(f"Percentage of females who won't watch: {percent_female_wont_watch:.2f}%")
