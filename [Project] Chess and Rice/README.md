# The Chess Problem
Author: Lex Baker
Date: 9/6/22
This program calculates how many grains of rice the mathematician would have in the Chess Problem,
then calculates how many feet of rice deep that would be if it was solely contained within the surface area of South Carolina

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