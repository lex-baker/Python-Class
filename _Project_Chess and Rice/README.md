TITLE: The Chess Problem
AUTHOR: Lex Baker
DTE DUE: 9/8/22
DATE SUBMITTED: 9/7/22
COURSE TITLE: Python I
MEETING TIME(S): Monday, Wednesday, Friday @ 9am
DESCRIPTION: This program calculates how many grains of rice the mathematician would have in the Chess Problem,
then calculates how many feet of rice deep that would be if it was solely contained within the surface area of South Carolina
HONOR CODE: On my honor, I neither gave nor receieved unauthorized help on this assignment. <Lex Baker>
HOWTO: Open this file in the IDE of your choice and click run
INPUT FILE: N/A
OUTPUT FILE: N/A
BIBLIOGRAPHY:
-https://www.themeasureofthings.com/singleresult.php?comp=weight&unit=gms&amt=0.021&i=362
-https://fdc.nal.usda.gov/fdc-app.html#/food-details/169704/measures
-https://www.census.gov/geographies/reference-files/2010/geo/state-area.html
-https://www.statista.com/statistics/242364/rice-production-in-china/
-https://www.statista.com/statistics/1282575/japan-milled-rice-production-volume/
RESOURCES: N/A
TUTORS: N/A
COMMENTS: The code is explained in comments within the chess.py file. This assignment was originally submitted on time, but resubmitted to modify the README to add in the required information.
REFLECTION: This assignment took me around 5 hours to complete, although the vast majority of that time was spent researching rice specifications. Measurements seemed to wildly vary, but I pinned down both the weight of a single grain of rice and the weight of a cup of rice. On that note, I commented out adding void space, because the method I used to calculate included the void in the first place since I found the weight of a cup of rice and divided it by the weight of a single grain of rice to find grains per cup. Because the cup of rice already has voids in between the rice, adding in the void afterwards actually doubles the amount of void, which is unnecessary.

My math and notations/explanations on this work:

Assuming the type of rice to be brown rice:

Measure of Things claims the average weight of a grain of rice is 0.021 grams
-https://www.themeasureofthings.com/singleresult.php?comp=weight&unit=gms&amt=0.021&i=362

The USDA says that 1 cup of uncooked, long grain, brown rice is equal to 202 grams
-https://fdc.nal.usda.gov/fdc-app.html#/food-details/169704/measures

202g / 0.021g = 9619 grains of rice in a cup

The conversion ratio from cups to cubic miles is (1 / 1.762e13)

South Carolina has a surface are of 32,020 square miles
-https://www.census.gov/geographies/reference-files/2010/geo/state-area.html

# BONUS

Annual rice production of China (as per 2021): 212.84 million metric tons
-https://www.statista.com/statistics/242364/rice-production-in-china/

Annual rice production of Japan (as per 2021): 7.56 million metric tons
-https://www.statista.com/statistics/1282575/japan-milled-rice-production-volume/

1 metric ton = 1,000 kilograms = 1,000,000 grams

As found earlier, 1 cup of rice is approximately 202 grams, so:

China: (212,840,000 metric tons * 1,000,000 grams per metric ton) / (202 grams per cup) = 1.05e12 cups of rice produced

Japan: (7,560,000 metric tons * 1,000,000 grams per metric ton) / (202 grams per cup) = 3.74e10 cups of rice produced

Python calculated amount of required cups of rice to be 1.918e15, which is three orders of magnitude larger than China's 2021 output,
which was already the largest internationally

Further math was completed in Python, showing that it would take over 17 centuries at a constant production rate to fufill the mathematician's request

Therefore, despite years of advancements and modern technology, even we would be unable to meet the mathematician's seemingly simple request