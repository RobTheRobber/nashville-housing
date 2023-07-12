## Overview

Nashville is the capital of the U.S. state of Tennessee and home to The Country Music Hall of Fame and Museum. From this music hub which is home to a population of nearly 700,000 people, we have a trove of data waiting to be explored. This presentation is going to be focused on the real estate data of the Nashville area. It is important to review this data to understand the zones and compositon of the Nashville area. The primary focus of this dataset is the different types of properties along with the the cost breakdown.

## Questions
- What are the most common types of properties?
- What is being paid for by each type of property?
- 
## Cleaning
- This data was luckily pretty easy to work with due to the smaller number of columns and with most of the data filled. For the initial cleaning I cut out columns that I didn't need and were unecessary. Afterwards I checked for any nulls or zeros and if there were any nulls within my numeric data then I changed them to zero. I did remove those values where the total value or acreage were zero. I did not remove every zero with things such as bedrooms and bathrooms since it wouldn't make sense to do so. It was also brought to my attention while I was calculating my averages and highest prices that for some strange reason the sales price column of my data was listed as a string instead of an integer so I had to go through my columns and make sure they all were integers. After my initial exploration into my dataset I noticed there were a large amount of groups that had very few entries and would throw off all of my charts and data so I ended up trimming those with fewer than 5 entries to limt the outliers when it came to finding averages and sums. After that I had a clean set of data ready to be used for my analysis.


## Visualization

To start off the visualization we can look at the most common type of data




## 🏆 The Most Popular Creators between Nov 2017 and June 2018 and Their View Count
<img src="https://github.com/RobTheRobber/nashville-housing/blob/main/img/land-use.png" width=60% height=50%/>

## 💬 The Most Popular Video Categories by View Count and Comments

<img src="https://github.com/tralinde/tralinde_EDA_group_presentation/assets/96899068/2264cf5b-2683-4bce-b174-d532f3136703" width=80% height=80%/>

## 🕗 Days until trending sorted by category 

<img src ="https://github.com/tralinde/tralinde_EDA_group_presentation/assets/96899068/ba4dc434-2b19-4867-9452-0dbfb5bb3011" width=80% height=80%/>


## 🤓 Data Cleaning Process
- Duplicate data
- Time formatting consistency
   - Converting time to integers
   - Date/time formatting
- Removing outliers
- Visual clarity on category ids


## 🛠️ Future Project Plans
- Trending tags, identifying what makes a video trend
- Duration of trending content
- Identifying social media platforms in descriptions
