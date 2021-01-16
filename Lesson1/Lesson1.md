# Lesson 1 - Overview of AB Testing 

PPF = percent point function = inverse of CDF (Cumulative Distribution Function)

CDF = probability of an event equal to or less than a given value 
PDF = probability density function
Returns a probability of a given continuous outcome 



### Confidence Intervals 

$\hat{p}$ = x/n where x = unique clicks, n = unique users 
$\hat{p}$ is essentially the proportion of successes
Assuming normal distribution 
check n * $\hat{p}$ > 5
and n*(1-$\hat{p}$) > 5

Margin of error 
m = z* standard error 
m = z * $\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$
