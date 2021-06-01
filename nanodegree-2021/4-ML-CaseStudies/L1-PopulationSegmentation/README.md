## Population Segmentation 

### 2. Sagemaker 

- What is sagemaker ? https://youtu.be/JWRtWcd92E4

- What applications does SageMaker make possible? https://youtu.be/iXN30g70PJ0

- Why should students gain skills in SageMaker and cloud services? https://youtu.be/Hp6qTdiqU3g

  big data, handling data, understaind the business problem, translating business problem to ML problem, data collection and analysis, 
  selecting ML algo, building the model, validating the model using metrics, put the model in production , continuous monitoring 

### 3. Course outline 

Course Outline
Throughout this course, we’ll be focusing on deployment tools and the machine learning workflow; answering a few big questions along the way:

How do you decide on the correct machine learning algorithm for a given task?
How can we utilize cloud ML services in SageMaker to work with interesting datasets or improve our algorithms?
To approach these questions, we’ll go over a number of real-world case studies, and go from task and problem formulation to deploying models in SageMaker. We’ll also utilize a number of SageMaker’s built-in algorithms.

Case Studies
Case studies are in-depth examinations of specific, real-world tasks. In our case, we’ll focus on three different problems and look at how they can be solved using various machine learning strategies. The case studies are as follows:

Case Study 1 - Population Segmentation using SageMaker

You’ll look at a portion of US census data and, using a combination of unsupervised learning methods, extract meaningful components from that data and group regions by similar census-recorded characteristics. This case study will be a deep dive into Principal Components Analysis (PCA) and K-Means clustering methods, and the end result will be groupings that are used to inform things like localized marketing campaigns and voter campaign strategies.

Case Study 2 - Detecting Credit Card Fraud

This case will demonstrate how to use supervised learning techniques, specifically SageMaker’s LinearLearner, for fraud detection. The payment transaction dataset we'll work with is unbalanced, with many more examples of valid transactions vs. fraudulent, and so you will investigate methods for compensating for this imbalance and tuning your model to improve its performance according to a specific product goal.

Custom Models - Non-Linear Classification

Adding on to what you have learned in the credit card fraud case study, you will learn how to manage cases where classes of data are not separable by a linear line. You'll train and deploy a custom, PyTorch neural network for classifying data.

Case Study 3 - Time-Series Forecasting

This case demonstrates how to train SageMaker's DeepAR model for forecasting predictions over time. Time-series forecasting is an active area of research because a good forecasting algorithm often takes in a number of different features and accounts for seasonal or repetitive patterns. In this study, you will learn a bit about creating features out of time series data and formatting it for training.

### 4. Model Design

Video: https://youtu.be/zxNoSTZ3s90

Ref: Ground Truth 

### 6. CaseStudy1: Population Segmentation 

Video: https://youtu.be/3pXFLrnk7q0

### 7. K-Means overview 

https://youtu.be/Cf_LSDCEBzk

K-Means Clustering
To perform population segmentation, one of our strategies will be to use k-means clustering to group data into similar clusters. To review, the k-means clustering algorithm can be broken down into a few steps; the following steps assume that you have n-dimensional data, which is to say, data with a discrete number of features associated with it. In the case of housing price data, these features include traits like house size, location, etc. features are just measurable components of a data point. K-means works as follows:

You select k, a predetermined number of clusters that you want to form. Then k points (centroids for k clusters) are selected at random locations in feature space. For each point in your training dataset:

You find the centroid that the point is closest to
And assign that point to that cluster
Then, for each cluster centroid, you move that point such that it is in the center of all the points that are were assigned to that cluster in step 2.
Repeat steps 2 and 3 until you’ve either reached convergence and points no longer change cluster membership _or_ until some specified number of iterations have been reached.
This algorithm can be applied to any kind of unlabelled data. You can watch a video explanation of the k-means algorithm, as applied to color image segmentation, below. In this case, the k-means algorithm looks at R, G, and B values as features, and uses those features to cluster individual pixels in an image!

Data Dimensionality
One thing to note is that it’s often easiest to form clusters when you have low-dimensional data. For example, it can be difficult, and often noisy, to get good clusters from data that has over 100 features. In high-dimensional cases, there is often a dimensionality reduction step that takes place before data is analyzed by a clustering algorithm. We’ll discuss PCA as a dimensionality reduction technique in the practical code example, later.

### 8. Creating notebook instance 

https://youtu.be/w2GBAnhUlOw




















