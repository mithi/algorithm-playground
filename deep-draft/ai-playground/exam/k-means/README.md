## K-Means  `kmeans(data)`
- This notebook `0-final-kmeans.ipynb` is working properly given the requirements
- For visualization, check the notebook `3-final-results-with-plot.ipynb`
- To see how my implementation compares to sklearn check the notebook `1-initial-comparisons.ipynb`
- Check the elbow graphs and discussion in `naive-elbow-inspection.ipynb`
- Determining the k programmatically I chose the point which makes the smallest angle (nearest 90 degrees) 
given the point before it and te point after it

# Kmeans Goal
- group data into distinct non overlapping groups

# Objective of this exercise
- Implement the kmeans algorithm using only `numpy`
- Use a method to get the (statistically likely) best number of clusters (`k`)
 - Call the function `kmeans(data)`
    - data is an `MxN` numpy array (`row` by `column`)
    - `M` is the number of samples , `N` is the number of feature of that sample
- This function returns:
    - an integer `K`, which should be programmatically identified
    - a vector of length `M` containing the cluster labels


# Purposely not implemented (maybe in the future, when I have more time)
- a `predict` function is not implemented
  - (IE, using the result of a kmeans to predict the label of a data sample
    that it hasn't seen before)
- Implement other algorithms to determine the best number of clusters
- I only implemented a modified "elbow method" for now, a technique 
I thought of myself (basing the number of clusters based on how small 
the angle the point is making with the adjacent points (before and after it)
It worked pretty well with my synthetic data but not sure how well it will 
generalize to other sets.


# K-means Algorithm
```
0. It is usually betteer to Scale/normalize the data
1. Specify # of clusters (K)
2. Initialize centroids by first shuffling the dataset
and then randomly getting the first `k` index
electing K data points for the centroids (don't remove them from dataset).
3. Keep iterating until there is no change to the centroids.
  [ i.e assignment of data points to clusters isn’t changing.
4. Compute the sum of the squared distance between data points and all centroids.
5. Assign each data point to the closest cluster (centroid).
6. Compute the centroids for the clusters by taking the average of the all data points that belong to each cluster.
```

# Trying to get the best centroids (Not implemented)
- You might not get the best centroids
- Because kmeans iterative nature and also
- centroids are differently initialized
- Centroids might get stuck at "local minimum"
- Solution: run the algorithm with different centroids
- pick the centroids set that resulted the lowest sum of squared distance.
- you still might not get the best, but it's  more probable
- and atleast you get a better centroid


# Determining the number of clusters
- optimize a criterion (elbow method, silhouette analysis)
- statistical methods ("gap statistic")


## Elbow Method
- Get the SSE ((sum of square error) for each cluster
- Compute the difference between the SSE's of adjacent clusters
- Get the cluster where the difference SSE flattens out
- When you graph it it looks somwhat like an elbow
- Elbow method sometimes doesn't work, if the SSE if
- each cluster is not decreasing as much between adjacent clusters
- IE (there is no "elbow"

## Silhouette Analysis (not implemented)
- Determines the degree of separation between clusters
- More computationally expensive than elbow method
```
For each data sample (data point):
    1. Get its the mean distance from all the data points from that cluster
       di_x (di_y is one data point i from cluster x)
    2. Get the its mean distance from all the data points from the closest cluster
        di_y (di_y is one data point i from cluster y closest to x)
    3. Normalize ( coefficient = (di_x - di_y) / max(di_x, di_y)

    if coefficient is near:
         0 - the sample is very close to closest cluster
        +1 - the sample is far away from the closest cluster
        -1 - the sample is assigned to wrong cluster

    Of course we want the coefficient to be close to one.
```

# Some drawbacks
- Kmeans work very well on almost spherical shapes of clusters,
for ellipical shapes and other shapes it doesn't work so well
- Given a data point it doesn't know statiscally where to assign
a data point which is at the same distance for two or more clusters
- it will still cluster data that doesn't make sense to
 be clustered like the uniform distributions
