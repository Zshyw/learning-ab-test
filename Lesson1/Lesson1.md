# Lesson 1 - Overview of AB Testing 

## Binomial Distribution

Wiki: Discrete probability distribution of the number of successes in a sequence of n independent experiments
ELI5: When you have a number of 'trials' that have binary outcomes (e.g. yes/no, win/lose, success/fail), the "distribution" tells you about the probability of having a certain number of wins/successes over a certain number of trials 

<img src = "https://latex.codecogs.com/svg.latex?{p}"> = successes/wins

<img src = "https://latex.codecogs.com/svg.latex?{n}"> = trials

#### When to use this binomial  distribution? 
- Binary Outcomes
- Independent events
- Identical Distribution
    - <img src = "https://latex.codecogs.com/svg.latex?{p}"> is same for all <img src = "https://latex.codecogs.com/svg.latex?{n}">


## Other Stats good to knows

### PDF = Probability Density Function
A function that gives you probabilities for discrete random variables 



### CDF = Cumulative Distribution Function

Probability of an event equal to or less than a given value.
Intuitively, it's how much area is under the curve at a certain point. 



### PMF = Probability Mass Function

Wiki: The probability distribution of a discrete random variable, and provides the possible **values** and their associated **probabilities**. 
Summary: A function that gives you probabilities for discrete random variables. 

### PPF = percent point function
Inverse of CDF (Cumulative Distribution Function)

*Example of uses*: 
- to find the median of a distribution 
    - e.g. binom.ppf(0.5, n, p) given n, p parameters



### Confidence Intervals 

<img src = "https://latex.codecogs.com/svg.latex?\hat{p}=\frac{x}{n}">

where 

<img src = "https://latex.codecogs.com/svg.latex?{x}"> = unique clicks

<img src = "https://latex.codecogs.com/svg.latex?{n}"> = unique users 

<img src = "https://latex.codecogs.com/svg.latex?\hat{p}"> is essentially the proportion of successes

Assuming normal distribution 
check n * $\hat{p}$ > 5
and n*(1-$\hat{p}$) > 5

Margin of error 
m = z* standard error 

Standard Error

<img src="https://latex.codecogs.com/svg.latex?\Large&space;m=z*\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}" />


\alpha
\frac{n!}{k!(n-k)!}
${n}$


