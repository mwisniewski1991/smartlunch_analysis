# Lunch Data Analysis

## 1. How many meals were available the day before the order day at 18:00?

- Some meals with the same name have different IDs. I don't know the reason for this.
- I didn't find a situation where an ID has a different meal name.
- I assume that every small change in name, ingredients, or price requires a new ID for the meal.

Table: There are more meal IDs than meal names
| order_day   | count_meal_id | count_meal_name |
|-------------|---------------|-----------------|
| 2023-02-13  | 80            | 76              |
| 2023-02-15  | 86            | 86              |
| 2023-02-16  | 65            | 65              |
| 2023-02-17  | 116           | 105             |
| 2023-02-20  | 100           | 87              |

Changes in the number of available meals result from weekdays. One day there were 3 restaurants available, and another day, for example, 5.

![Meal availability chart](utils/charts/How%20many%20meals%20were%20available%20day%20before%20order%20day%20ay%2018%3A00%20o%27clock%3F.png)

## 2. Restaurant ranking by ratings (scale 0 - 5)

- TOP3: Cochise Burgers, Sandwicz Shop - Kraków, Sandwicz Szop
- Bar Alf-BISTRO: big star, 4th place in overall rating and many votes.
- Cochise Burgers has few ratings but very good rating.

![Restaurant ranking](utils/charts/Restaurants%20rate%20ranking.png)

Table: Restaurants sorted by overall rating from the table above.

![Number of restaurant ratings - sorted by overall rating](utils/charts/Restaurants%20number%20of%20rates%20-%20sorted%20by%20overall%20rate.png)

## 3. Restaurant rating history

- Śniadaniowcy: replacement for Sandwich Szop receives many ratings in a short time, which means they have many orders. Everyone wanted to check out the new provider.
- Cochise maintained a rating above 4.6 for a long time and then suddenly something went wrong. Lack of data to determine what happened.
- Bar ALF Bistro received 10,000 new ratings in 6 months.
- Sandwicz Shop was a very popular provider but at some point stopped delivering through the app but came personally and still sold. Potential commissions for SmartLunch turned out to be unprofitable?

![Restaurant ratings over time](utils/charts/Restaurants%20rate%20in%20time.png)

![Number of restaurant ratings over time](utils/charts/Restaurants%20number%20of%20rates%20in%20time.png)

## 4. Average meal price

- It looks like prices are not in an increasing trend. But I have the impression that meal sizes already are. Unfortunately, there's no data to confirm this. I also noticed a trend that lunches started to be available in versions with potatoes/rice/groats and without. Those without these additions lower the average price.
- Peak in May, probably caused by a long weekend in Poland and only a few restaurants offering meals.
- In April, some new most expensive meals appeared.

![Average meal price](utils/charts/Average%20meal%20price.png)

![Maximum meal price](utils/charts/Max%20meal%20price.png)

![Minimum meal price](utils/charts/Minimal%20meal%20price.png)

## 5. Average meal price by restaurant

- Sandwich restaurants (like SandwichSzop, Sniadaniowcy, Fit-Morning) with much lower prices than regular restaurants.
- The most expensive are restaurants appearing once a week: Tommy Burger, Hashtag Sushi, Cochise.

![Restaurant average price](utils/charts/Restaurants%20average%20price.png)

## 6. Most expensive meal

- Fit Morning is the only restaurant that regularly offers meals for meetings.
- Catering Karp dla TME - special meal for Easter.

TOP 5 most expensive meals and their providers.
| mean_name_pl | max_price | name |
|-------------|-----------|------|
| Conference tray - Sandwich set for 5 -... | 90 | Fit Morning- Kraków |
| Big Boss Burger | 56 | Tommy Burger |
| EASTER TAKEAWAY: Chicken galantine, roll... | 53 | Catering Karp dla TME |
| Burger Totem | 48 | Cochise Burgers |
| SUSHI large set with smoked fish | 42 | Sandwicz Szop - Gdynia |

![Most expensive meal](utils/charts/Most%20expensive%20meal.png)

## 7. Cheapest meal

**Comments:**
- Garlic sauce for pizza costs only 0.01 PLN. When the sauce was free, people ordered it but didn't eat it.

| order_day   | mean_name_pl                | max_price |
|-------------|-----------------------------|-----------|
| 2023-04-10  | Garlic sauce for pizza      | 0.01      |
| 2023-04-11  | Garlic sauce for pizza      | 0.01      |
| 2023-04-12  | Garlic sauce for pizza      | 0.01      |
| 2023-04-13  | Garlic sauce for pizza      | 0.01      |
| 2023-04-14  | Garlic sauce for pizza      | 0.01      |

![Cheapest meal](utils/charts/Cheapest%20meal.png)

## 8. Best meals ever - TOP 5

**Comments:**
- 3 meals have a 5.00 rating with 22, 40, and 35 ratings from customers.

| mean_name_pl | restaurant_name | max_rate | max_rates |
|-------------|----------------|----------|-----------|
| Double toast with pate and vegetables | Catering Karp dla TME | 5.00 | 22 |
| BEETROOT SALAD with pearl barley and smoked cottage... | Sandwicz Szop | 5.00 | 40 |
| Exotic - oatmeal with mango, peach, cherry... | Fit Morning-Łódzkie | 5.00 | 35 |
| BREAKFAST Breakfast burrito with scrambled eggs, ham... | Sandwicz Szop | 4.97 | 38 |
| Smoothie Abracababra 250 ml | Fit Morning-Łódzkie | 4.96 | 114 |

## 9. Worst meals ever - TOP 5

| mean_name_pl | restaurant_name | min_rate | max_rates |
|-------------|----------------|----------|-----------|
| NEW!! Burger Kukuryq | KukuryQ | 3.06 | 20 |
| VegeMiso | Hashtag Sushi | 3.07 | 15 |
| Thai beef with white rice, coleslaw... | Ha Long | 3.22 | 49 |
| Quinoa salad | Foodstacja bistro&cafe | 3.27 | 15 |
| Original Buffalo Wings 6pcs | Tommy Burger | 3.53 | 19 |

## 10. Meals - biggest difference in ratings - TOP 5

- examples of meals where there were the biggest differences between maximum and minimum ratings.

| mean_name_pl | restaurant_name | max_rate | min_rate | rate_diff |
|-------------|----------------|----------|----------|-----------|
| RASPBERRY YOGURT | Sandwicz Szop - Gdynia | 4.90 | 3.33 | 1.57 |
| Chicken sandwich | Śniadaniowcy Łódź | 4.36 | 2.85 | 1.51 |
| Green smoothie | Tommy Burger | 4.80 | 3.44 | 1.36 |
| Chicken salad | Śniadaniowcy Łódź | 4.64 | 3.35 | 1.29 |
| Grilled chicken salad | Śniadaniowcy Łódź | 4.21 | 2.94 | 1.27 | 