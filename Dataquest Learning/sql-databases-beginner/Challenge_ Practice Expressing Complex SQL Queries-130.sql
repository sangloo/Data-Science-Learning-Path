## 2. Use SELECT and LIMIT to Filter Results ##

SELECT College_jobs, Median, Unemployment_rate FROM recent_grads
LIMIT 20;

## 3. Use WHERE to Filter Results ##

SELECT major FROM recent_grads
WHERE Major_category = 'Arts'
LIMIT 5;

## 4. Express Criteria With Operators ##

SELECT Major,Total,Median,Unemployment_rate FROM recent_grads 
WHERE (Major_category != 'Engineering') AND (Unemployment_rate > 0.065 OR Median <= 50000);

## 5. Order Your Results ##

SELECT major FROM recent_grads
WHERE Major_category!='Engineering'
ORDER BY major DESC
LIMIT 20;