## 02_command_line_chipotle.md ##

**Look at the head and the tail of chipotle.tsv in the data subdirectory of this repo. Think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)**
**_A: Each column looks to delineate each separate part of an order, while the rows show each item within an order_**

**How many orders do there seem to be?**
_Renees-MacBook-Pro:~ reneehosogi$ cd Documents/GitHub_Clones/GA-SEA-DAT1/data_
_Renees-MacBook-Pro:data reneehosogi$ tail chipotle.tsv_
**_A: 1834_**

**How many lines are in this file?**
_Renees-MacBook-Pro:data reneehosogi$ wc -l chipotle.tsv_
**_A: 4623_**

**Which burrito is more popular, steak or chicken?**
_Renees-MacBook-Pro:data reneehosogi$ grep -c Chicken chipotle.tsv 
1565
Renees-MacBook-Pro:data reneehosogi$ grep -c Steak chipotle.tsv 
706_
**_A: Chicken_**

**Do chicken burritos more often have black beans or pinto beans?**
_Renees-MacBook-Pro:data reneehosogi$ grep -c Chicken chipotle.tsv | grep -c Pinto chipotle.tsv 
582
Renees-MacBook-Pro:data reneehosogi$ grep -c Chicken chipotle.tsv | grep -c Black chipotle.tsv
1353_
**_A: Black beans_**

**Make a list of all of the CSV or TSV files in the DAT8 repo (using a single command). Think about how wildcard characters can help you with this task.**
_Renees-MacBook-Pro:GA-SEA-DAT1 reneehosogi$ find . -name *sv_
_./data/airlines.csv_
_./data/bank-additional.csv_
_./data/bikeshare.csv_
_./data/chipotle.tsv_
_./data/drinks.csv_
_./data/hitters.csv_
_./data/imdb_1000.csv_
_./data/sms.tsv_
_./data/titanic.csv_
_./data/ufo.csv_
_./data/vehicles_test.csv_
_./data/vehicles_train.csv_
_./data/yelp.csv_

**Count the approximate number of occurrences of the word "dictionary" (regardless of case) across all files in the DAT8 repo.**
_Renees-MacBook-Pro:GA-SEA-DAT1 reneehosogi$ grep -r Dictionary . | wc -l
       3
Renees-MacBook-Pro:GA-SEA-DAT1 reneehosogi$ grep -r dictionary . | wc -l
      45_
**_A: 48_**

