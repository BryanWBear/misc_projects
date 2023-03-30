import pandas as pd

# raw txt from manually copying and pasting reviews
file1 = open('../data/shaman_king_raw.txt', 'r', encoding='utf-8-sig')
lines = file1.readlines()
 
count = 0
# Strips the newline character
reviews = []
new_review = []
for line in lines:
    if line.strip() == '@@@':
        reviews.append(new_review)
        new_review = []
        continue
    if line.strip() != '':
        new_review.append(line.strip())


all_reviews = [' '.join(rev[1:]) for rev in reviews]
all_ratings = [int(rev[0].strip()) for rev in reviews]
shaman_df = pd.DataFrame({'reviews': all_reviews, 'ratings': all_ratings})
shaman_df.to_csv('../data/shaman_king_reviews.csv', index=False)