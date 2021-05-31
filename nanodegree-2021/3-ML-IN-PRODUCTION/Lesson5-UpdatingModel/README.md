## Updating model 

### 1. Updating a model 

https://youtu.be/7wI168JzBiU

In this lesson we are going to take a look at updating an existing endpoint so that it conforms to a different endpoint configuration. There are many reasons for wanting to do this, the two that we will look at are, performing an A/B test and updating a model which is no longer performing as well.

To start, we will look at performing an A/B test between two different models. Then, once we've decided on a model to use, updating the existing endpoint so that it only sends data to a single model.

For the second example, it may be the case that once we've built a model and begun using it, the assumptions on which our model is built begin to change.

For instance, in the sentiment analysis examples that we've looked at our models are based on a vocabulary consisting of the 5000 most frequently appearing words in the training set. But what happens if, over time, the usage of words changes? Then our model may not be as accurate.

When this happens we may need to modify our model, often this means re-training it. When we do, we'd like to update the existing endpoint without having to shut it down. Fortunately, SageMaker allows us to do this in a straightforward way.

### 2. Building a sentiment analysis model 

https://youtu.be/dwRkA0ig3uU

To begin with we will create an XGBoost model similar to the ones that we have constructed in the past in order to predict the median housing cost in Boston.

The difference this time is that we are using a hybrid approach, including both the high level and low level functionality. In this case we use the high level approach to train a model (to produce model artifacts) and then we use the low level approach to construct the model itself and to construct the endpoint configuration. The reason for this is so that we can have more control over how our endpoint behaves.


### 3. Building a sentiment analysis model 

https://youtu.be/7TdiVF6qS1k

### 4. Combining models (Important)

https://youtu.be/OYYJerDHu0o


Using the low level approach to creating endpoint configurations allows us to create endpoints that are more sophisticated. For example, endpoints which receive data and route that data to one of many different models. In the example here we are only using two different models but there may be situations in which you would want more.

In addition, SageMaker provides functionality to update an existing endpoint so that it conforms to a different endpoint configuration. Further, SageMaker does this in a way that does not require the existing endpoint to be shut down.

This is very beneficial as you may be working in an environment where there are other services that depend on your deployed endpoint.

Reference: https://mlinproduction.com/ab-test-ml-models-deployment-series-08/

### 5. Mini-Project: Updating a Sentiment Analysis Model

https://youtu.be/v7dYwxuKXzI

In this mini-project we will take a look at situation in which we have a trained model which is working well, but then something changes with the underlying distribution on which our model is based. First we need to take a look at what might be the problem. Then we want to create a new, updated model and replace our old model without taking down the corresponding endpoint.

This mini-project notebook is called IMDB Sentiment Analysis - XGBoost (Updating a Model).ipynb and can be found inside of the Mini-Projects folder

### 6. Mini-Project: Updating a Sentiment Analysis Model - Solution 

https://youtu.be/75RxW3R6674

### 6. Mini-Project: Exploring new data - Solution 

https://youtu.be/sEBK1dmiUfE

review: generator 

[changed_word_dist](changed_word_dist.png)