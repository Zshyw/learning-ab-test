# Lesson 1 - Overview of AB Testing 

## 13. Binomial Distribution

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



## 14. Confidence Intervals 

<img src = "https://latex.codecogs.com/svg.latex?\hat{p}=\frac{x}{n}">

where 

<img src = "https://latex.codecogs.com/svg.latex?{x}"> = unique clicks

<img src = "https://latex.codecogs.com/svg.latex?{N}"> = unique users 

<img src = "https://latex.codecogs.com/svg.latex?\hat{p}"> is essentially the proportion of successes

Assuming normal distribution 
check <img src = "https://latex.codecogs.com/svg.latex?{N}*\hat{p}>5">
and  <img src = "https://latex.codecogs.com/svg.latex?{N}*(1-\hat{p})>5">

When we can use the normal distribution, then the width of the confidence interval, i.e. margin of error, will be equal to the below

Margin of error (<img src = "https://latex.codecogs.com/svg.latex?{m}">)

<img src = "https://latex.codecogs.com/svg.latex?{m}"> = <img src = "https://latex.codecogs.com/svg.latex?{z}"> * standard error 

<img src = "https://latex.codecogs.com/svg.latex?{z}"> = z score of confidence interval (commonly taken at 95%)

Standard Error (binomial distribution)

<img src="https://latex.codecogs.com/svg.latex?\Large&space;{\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}" />

Note that the margin of error is a function of both the proportion of successes and the size of the sample. If <img src = "https://latex.codecogs.com/svg.latex?\hat{p}"> is further from 0.5 then standard error will be smaller meaning that the distribution is tighter so the confidence interval will be smaller.



## 17. Establishing Statistical Significance using Hypothesis Testing
Going down this approach, you need to calculate how likely it is that your results are due to chance. You will need to have a hypothesis about what the results would be if your experiment had no effect, call this null hypothesis. 

Say <img src = "https://latex.codecogs.com/svg.latex?{p_{control}}"> and <img src = "https://latex.codecogs.com/svg.latex?{p_{experiment}}"> are probabilities for control and experiment groups respectively, both of which have different distributions. 

If the experiment had no effect then we would expect both distributions to be equivalent to each other i.e. <img src = "https://latex.codecogs.com/svg.latex?{p_{control}}={p_{experiment}}"> or <img src = "https://latex.codecogs.com/svg.latex?{p_{experiment}}-{p_{control}}=0">. 

Here we establish the Null Hypothesis, <img src = "https://latex.codecogs.com/svg.latex?{h_0}"> where

<img src = "https://latex.codecogs.com/svg.latex?{h_0}:{p_{experiment}}-{p_{control}}=0">

Alternative Hypothesis, <img src = "https://latex.codecogs.com/svg.latex?{h_a}:{p_{experiment}}-{p_{control}}\neq0"> 

Once we've defined both hypotheses, we estimate <img src = "https://latex.codecogs.com/svg.latex?{p_{control}}"> and <img src = "https://latex.codecogs.com/svg.latex?{p_{experiment}}"> and calculate the difference (<img src = "https://latex.codecogs.com/svg.latex?{p_{experiment}}-{p_{control}}">). 

Then compute probability that this difference would hav arisen by chance if the null hypothesis were true

<img src = "https://latex.codecogs.com/svg.latex?P({p_{experiment}}-{p_{control}}|{h_0})">

We will reject the null hypothesis if the experiment has had an effect and the probability is small enough e.g. <img src = "https://latex.codecogs.com/svg.latex?P<0.05"> 

This cutoff is called alpha, <img src = "https://latex.codecogs.com/svg.latex?\alpha"> , i.e. the probability you reject null hypothesis

### Comparing Two Samples with Pooled Standard Error
Say we have variables

<img src = "https://latex.codecogs.com/svg.latex?{x_{control}},{x_{experiment}},{n_{control}},{n_{experiment}}"> 
where x = clicks and n = size. 

<img src = "https://latex.codecogs.com/svg.latex?\hat{p}_{pool}=\frac{(x_{control}+x_{experiment})}{(n_{control}+n_{experiment})}">
 

<img src = "https://latex.codecogs.com/svg.latex?SE_{pool}=\sqrt{\hat{p}_{pool} * (1-\hat{p}_{pool}) *(\frac{1}{n_{control}}+\frac{1}{n_{experiment}})}">

<img src = "https://latex.codecogs.com/svg.latex?\hat{d}=\hat{p}_{experiment}-\hat{p}_{control}">

If null hypothesis is true then 
<img src = "https://latex.codecogs.com/svg.latex?h_0:\hat{d}=0">

We know <img src = "https://latex.codecogs.com/svg.latex?\hat{d}"> is normally distributed

<img src = "https://latex.codecogs.com/svg.latex?\hat{d}\sim N(0,SE_{pool})">

If <img src = "https://latex.codecogs.com/svg.latex?\hat{d}>1.96*SE_{pool}"> or <img src = "https://latex.codecogs.com/svg.latex?\hat{d}<-1.96*SE_{pool}">   then we can reject our null hypothesis and say that our difference represents a statistically significant difference. 

From a business perspective, need to consider whather the results are practically significant. i.e. What size change matters to us. Need to be clear that it's worth the change to action upon these results. If the return is high enough (practical significance) then action. 


## 21. Size vs Power Trade Off
When designing experient, we have to decide the size of experiment we need in order to get a statistically significant result -> Statistical Power. 

i.e. we want to ensure we have enough power to conclude with high probability that the result is statistically significant.

Statistical power has an inverse trade-off with size. The smaller the change you want to detect, then the greater the size you'll need in your control and experiment. 

Statistical Power = the probability that if there is a difference of a certain size, you'll detect it and reject the null hypothesis. 

Normally you run a power analysis at the beginning as you may find there's no point in running a test - in case you your sample is limited. 

## 22. How Page Views affect Sensitivity


