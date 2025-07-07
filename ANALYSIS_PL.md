# Analiza danych o lunchach

## 1. Ile posiłków było dostępnych dzień przed dniem zamówienia o 18:00?

- Niektóre posiłki o tej samej nazwie mają różne ID. Nie znam powodu tego.
- Nie znalazłem sytuacji gdzie ID ma różną nazwę posiłku.
- Zakładam, że każda mała zmiana w nazwie, składnikach lub cenie wymaga nowego ID dla posiłku.


Tabela: Jest wiecej ID posiłków od nazw posiłków 
| order_day   | count_meal_id | count_meal_name |
|-------------|---------------|-----------------|
| 2023-02-13  | 80            | 76              |
| 2023-02-15  | 86            | 86              |
| 2023-02-16  | 65            | 65              |
| 2023-02-17  | 116           | 105             |
| 2023-02-20  | 100           | 87              |

Zmiany ilości dostępnych posiłków wynika z dni tygodnia. Jednego dnia dostępnych było 3 restauracje a innego np 5.

![Wykres dostępności posiłków](utils/charts/How%20many%20meals%20were%20available%20day%20before%20order%20day%20ay%2018%3A00%20o%27clock%3F.png)

## 2. Ranking restauracji według ocen (skala 0 - 5)

- TOP3: Cochise Burgers, Sandwicz Shop - Kraków, Sandwicz Szop
- Bar Alf-BISTRO: duża gwiazda, 4 miejsce w ogólnej ocenie i dużo głosów.
- Cochise Burgers mało ocen ale bardzo dobra ocena.


![Ranking restauracji](utils/charts/Restaurants%20rate%20ranking.png)

Tabela: Restauracje posortowane według oceny ogólnej z tabeli powyżej.

![Liczba ocen restauracji - posortowane według ogólnej oceny](utils/charts/Restaurants%20number%20of%20rates%20-%20sorted%20by%20overall%20rate.png)

## 3. Historia rankingów restauracji

- Śniadaniowcy: zastępstwo dla Sandwich Szop otrzymuje dużo ocen w krótkim czasie, co oznacza, że mają dużo zamówień. Wszyscy chcieli sprawdzić nowego dostawcę.
- Cochise długo trzymał ocenę powyżej 4.6 a potem nagle coś się popsuło. Brak danych aby stwierdzić co się zadziało.
- Bar ALF Bistro w 6 miesięcy otrzymało 10_000 nowych ocen.
- Sandwicz Shop był bardzo popularnym dostawcą ale w pewnym momencie zrezygnował z dostarczania przez aplikację ale przyjeżdzał osobiście i nadal sprzedawał. Potencjalne prowizje dla SmartLuncha okazały się nieopłacalne?

![Oceny restauracji w czasie](utils/charts/Restaurants%20rate%20in%20time.png)

![Liczba ocen restauracji w czasie](utils/charts/Restaurants%20number%20of%20rates%20in%20time.png)

## 4. Średnia cena posiłku

- Wygląda na to, że ceny nie są w trendzie wzrostowym. Ale mam wrażenie, że rozmiary posiłków już tak. Brak niestety danych na potwierdzenie tego. Spostrzegłem też, że trend że obiady zaczeły być dostępne w wersji z ziemniakami/ryżem/kaszą i bez. Te bez tych dodatków obniżaja średnią cenę.
- Szczyt w maju, prawdopodobnie spowodowany długim weekendem w Polsce i tylko kilkoma restauracjami oferującymi posiłki.
- W kwietniu pojawiły się jakieś nowe najdroższe posiłki.

![Średnia cena posiłku](utils/charts/Average%20meal%20price.png)

![Maksymalna cena posiłku](utils/charts/Max%20meal%20price.png)

![Minimalna cena posiłku](utils/charts/Minimal%20meal%20price.png)

## 5. Średnia cena posiłku w restauracji

- Restauracje kanapkowe (jak SandwichSzop, Sniadaniowcy, Fit-Morning) z dużo niższą ceną niż regularne restauracje.
- Najdroższe to restauracje pojawiające się raz w tygodniu Tommy Burger, Hashtag Shushi, Cochise.

![Średnia cena restauracji](utils/charts/Restaurants%20average%20price.png)

## 6. Najdroższy posiłek

- Fit Morning to jedyna restauracja, która regularnie oferuje posiłki na spotkania.
- Catering Karp dla TME - specjalny posiłek na Wielkanoc.


TOP 5 najdroższych posiłków i ich dostawcy.
| mean_name_pl | max_price | name |
|-------------|-----------|------|
| Patera konferencyjna - Zestaw kanapek dla 5 -... | 90 | Fit Morning- Kraków |
| Big Boss Burger | 56 | Tommy Burger |
| WYNOS WIELKANOCNY:Galantyna z kurczaka, rolada... | 53 | Catering Karp dla TME |
| Burger Totem | 48 | Cochise Burgery |
| SUSHI duży zestaw z rybą wędzoną | 42 | Sandwicz Szop - Gdynia |


![Najdroższy posiłek](utils/charts/Most%20expensive%20meal.png)

## 7. Najtańszy posiłek

**Komentarze:**
- Sos czosnkowy do pizzy kosztuje tylko 0.01 PLN. Gdy sos był za darmo, ludzie go zamawiali, ale nie jedli.



| order_day   | mean_name_pl                | max_price |
|-------------|-----------------------------|-----------|
| 2023-04-10  | Sos czosnkowy do pizzy      | 0.01      |
| 2023-04-11  | Sos czosnkowy do pizzy      | 0.01      |
| 2023-04-12  | Sos czosnkowy do pizzy      | 0.01      |
| 2023-04-13  | Sos czosnkowy do pizzy      | 0.01      |
| 2023-04-14  | Sos czosnkowy do pizzy      | 0.01      |

![Najtańszy posiłek](utils/charts/Cheapest%20meal.png)

## 8. Najlepsze posiłki wszech czasów - TOP 5

**Komentarze:**
- 3 posiłki mają ocenę 5.00 z 22, 40 i 35 ocenami od klientów.


| mean_name_pl | restaurant_name | max_rate | max_rates |
|-------------|----------------|----------|-----------|
| Tostowa podwójna z pasztetem i warzywami | Catering Karp dla TME | 5.00 | 22 |
| SAŁATKA Burak z kaszą pęczak i wędzonym twaroż... | Sandwicz Szop | 5.00 | 40 |
| Egzotyczna - owsianka z mango, brzoskwinią, wi... | Fit Morning-Łódzkie | 5.00 | 35 |
| ŚNIADANIE Burrito śniadaniowe z jajecznicą, sz... | Sandwicz Szop | 4.97 | 38 |
| Smoothie Abracababra 250 ml | Fit Morning-Łódzkie | 4.96 | 114 |


## 9. Najgorsze posiłki wszech czasów - TOP 5

| mean_name_pl | restaurant_name | min_rate | max_rates |
|-------------|----------------|----------|-----------|
| NOWOŚĆ!! Burger Kukuryq | KukuryQ | 3.06 | 20 |
| VegeMiso | Hashtag Sushi | 3.07 | 15 |
| Wołowina po tajlandzku z ryżem białym, surówką... | Ha Long | 3.22 | 49 |
| Sałatka quinoa | Foodstacja bistro&cafe | 3.27 | 15 |
| Oryginalne Skrzydełka Buffalo 6szt | Tommy Burger | 3.53 | 19 |



## 10. Posiłki - największa różnica w ocenach - TOP 5

- przykłady posiłków gdzie były największe róznice między maksymalną a minimalną ocena.

| mean_name_pl | restaurant_name | max_rate | min_rate | rate_diff |
|-------------|----------------|----------|----------|-----------|
| JOGURT Malina | Sandwicz Szop - Gdynia | 4.90 | 3.33 | 1.57 |
| Kanapka kurczak | Śniadaniowcy Łódź | 4.36 | 2.85 | 1.51 |
| Smoothie zielone | Tommy Burger | 4.80 | 3.44 | 1.36 |
| Sałatka z kurczakiem | Śniadaniowcy Łódź | 4.64 | 3.35 | 1.29 |
| Sałatka z grillowanym kurczakiem | Śniadaniowcy Łódź | 4.21 | 2.94 | 1.27 |
