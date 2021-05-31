## Hyperparam Tuning 


### 1. https://youtu.be/ohVX3RUTghg

### 2. Introduction to Hyperparameter Tuning

Video: https://youtu.be/nah8kxqp55U

### 3. Boston Housing to Hyperparameter Tuning

Video: https://youtu.be/lsYRtKivrGc

Notebook: [Boston Housing - XGBoost (Hyperparameter Tuning) - High Level](https://github.com/manas-mukherjee/machine-learning-nanodegree/blob/master/nanodegree-2021/3-ML-IN-PRODUCTION/sagemaker-deployment-master/Tutorials/Boston%20Housing%20-%20XGBoost%20(Hyperparameter%20Tuning)%20-%20High%20Level.ipynb)

Generally speaking, the way to think about hyperparameter tuning inside of SageMaker is that we start with a base collection of hyperparameters which describe a default model. We then give some additional set of hyperparameters ranges. These ranges tell SageMaker which hyperparameters can be varied, with the goal being to improve the default model.

We then describe how to compare models, which in our instance is just by way of specifying a metric. Then we describe how many total models we want SageMaker to train.

Note: In addition to creating a tuned model in this notebook, we also saw how the attach method can be used to create an Estimator object which is attached to an already completed training job. This method is useful in other situations as well.

You will notice that throughout this module we train the same model multiple times. In most of the Boston Housing notebooks, for example, we train an XGBoost model with the same hyperparameters. The reason for this is so that each notebook is self contained and can be run even if you haven't run the other notebooks.

In your case however, you've probably already created an XGBoost model on the Boston Housing training set with the standard hyperparameters. If you wanted to, you could use the attach method to avoid having to re-train the model.

### 3. Boston Housing to Hyperparameter Tuning

Video: https://youtu.be/lsYRtKivrGc

### 4. Mini-Project solution (hyper-param tuning)

[IMDB Sentiment Analysis - XGBoost (Hyperparameter Tuning) - Solution.ipynb](https://github.com/udacity/sagemaker-deployment/blob/master/Mini-Projects/IMDB%20Sentiment%20Analysis%20-%20XGBoost%20(Hyperparameter%20Tuning)%20-%20Solution.ipynb)

Video: https://youtu.be/Q2Vthdca49I
https://youtu.be/i-EjGkZ8z30

### 7/8/9. Hyperparam tuning - Low level.

[Boston Housing - XGBoost (Hyperparameter Tuning) - Low Level.ipynb](https://github.com/manas-mukherjee/machine-learning-nanodegree/blob/master/nanodegree-2021/3-ML-IN-PRODUCTION/sagemaker-deployment-master/Tutorials/Boston%20Housing%20-%20XGBoost%20(Hyperparameter%20Tuning)%20-%20Low%20Level.ipynb)

Video:

	- 1. https://youtu.be/vlsZ-jC5C8Y
	- 2. https://youtu.be/WXjIkSHYEyM (Hyperparam tuning jobs)
	- 3. https://youtu.be/ap7d7DZL0Ic


What's next?
In the next lesson we will take a look at updating a deployed model. Once you've developed a model and deployed it the story is rarely over. What happens if some of the built in assumptions about your model change over time?

We will look at how you can create a new model which more accurately reflects the current state of your problem and then update an existing endpoint so that it uses your new model rather than the original one. In addition, using SageMaker, we can do this without needing to shut down the endpoint. This means that whatever application is using your deployed model won't notice any sort of disruption in service.