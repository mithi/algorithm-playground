import numpy as np
from numpy.linalg import norm

class KMeansClusterer: 
    def __init__(self, data, nclusters, niters):
        # Note: niters could be changed to tolerance
        self.nsamples = data.shape[0]
        self.nfeatures =  data.shape[1]
        self.niters = niters
        self.nclusters = nclusters
        self.centroids = None
        self.data = data
        # labels: an array which will be filled by
        # corresponding cluster of each datapoint
        self.labels = None 
        self.sse = None
        # Predict is unimplemented
        
    def initialize_centroids(self, rstate):
        np.random.seed(rstate)
        ids = np.random.permutation(self.nsamples)[:self.nclusters]
        self.centroids = self.data[ids]
        # centroids size = r: # features, c: # clusters
    
    def get_distances(self, centroids):
        # Compute the sum of the squared difference 
        # between data point and centroid
        # for each datapoint (row) and centroid
        distance_matrix = np.zeros((self.nsamples, self.nclusters))
        # si = sample index, ci = centroid index
        for si in range(self.nsamples):
            for ci in range(self.nclusters):
                # Frobius Norm: ((x1-c1)^2 + (x2-c2)^2 + (x3-c3)^2)^0.5
                frobius = norm(self.data[si] - centroids[ci])
                distance_matrix[si, ci] = np.square(frobius)
        return distance_matrix
    
    def update_labels(self, distance_matrix):
        # Get a vector that contains the index 
        # (index = current cluster/centroid id)
        # of the minimum distance for each sample (row)
        self.labels = np.argmin(distance_matrix, axis=1)
    
    def update_centroids(self, centroids):
        centroids = np.zeros((self.nclusters, self.nfeatures))
        for ci in range(self.nclusters):
            # Get all samples of the same cluster
            # by getting all the rows/samples that match the
            # centroid index, store at separate matrix
            cluster = self.data[self.labels==ci, :]
            # For each cluster, average each sample feature (col) 
            # this is its new centroid
            if len(cluster) != 0:
                centroids[ci] = np.mean(cluster, axis=0)
            else: 
                centroids[ci] = self.centroids[ci]
        self.centroids = centroids
        
    def compute_error(self):
        # error - sse - sum of square error/distance where
        # error between data samples corresponding centroid
        errs = np.zeros(self.nsamples)
        for k in range(self.nclusters):
            errs[self.labels == k] = norm(
                self.data[self.labels == k] - self.centroids[k], axis=1)
            
        self.sse = np.sum(np.square(errs))
    
    def fit(self, rstate):
        self.initialize_centroids(rstate)
        for i in range(self.niters):
            current_centroids = self.centroids
            distance_matrix = self.get_distances(current_centroids)
            self.update_labels(distance_matrix)
            self.update_centroids(current_centroids)
            # self.centroids is the updated centroids
            if np.allclose(current_centroids, self.centroids):
                break
        self.compute_error()

        
def preliminary_kmeans(data, nclusters, nr=10):
    km = KMeansClusterer(data, nclusters, niters=100)
    km.fit(rstate=0)
    err, r = km.sse, 0
    labels, centroids = km.labels, km.centroids
    
    # find the best r (random initialization of centroids)
    for i in range(1, nr):
        km.fit(rstate=i)
        if (err > km.sse ):
            err, r = km.sse, i
            labels, centroids = km.labels, km.centroids
            
    return labels, centroids, err


def get_angle_between_3points(x, y, z):  
    a = np.array(x)
    b = np.array(y)
    c = np.array(z)
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (norm(ba) * norm(bc))
    angle = np.arccos(cosine_angle)
    a = np.degrees(angle)    
    return a


def find_best_k(ys, nk):
    # estimate angles between 3 points
    # the smallest angle wins!
    
    angles, nys = [], len(ys) 
    n = max(ys) / nk # for normalizing the x
    
    for i in range(1, nys - 1):
        x = i + 1
        x1, x2, x3 = x - 1, x, x + 1
        y1, y2, y3 = ys[i - 1], ys[i], ys[i + 1]
        angle = get_angle_between_3points([n*x1, y1], [n*x2, y2], [n*x3, y3])    
        angles.append(angle)
    
    k = np.argmin(np.array(angles)) + 2
    return k


def kmeans_more(data, nk=10, niter=100):
    errorset, labelset, centroidset = [], [], []
    
    for nclusters in range(1, nk + 1):
        labels, centroids, err = preliminary_kmeans(data, nclusters)
        errorset.append(err)
        labelset.append(labels)
        centroidset.append(centroids)
        print(">", end="")
        
    k = find_best_k(errorset, nk)
    i = k - 1
    return k, labelset[i], centroidset[i]


def kmeans(data, nk=10, niter=100):
    k, labels, _ = kmeans_more(data, nk, niter)
    return k, labels


def find_k_elbow(errors):
    nk = len(errors) 
    x1, y1 = 1,  errors[0]
    x2, y2 = nk, errors[-1]
    m = (y1 - y2) / (x1 - x2)
    bias = (y1 + y2 - m * (x1 + x2)) / 2 
    # y = mx + bias,  -mx + y - bias= 0 
    # ax + by + c, 
    a, b, c = -m, 1, -bias
    
    # get the shortest distance from point to line
    # let x, y be the point
    # d = abs( a * x + b  * y + c) / sqrt( a**2 + b**2)
    distances = []
    for x, y in enumerate(errors):
        x += 1
        d = np.abs(a*x + b*y + c) / np.sqrt(a**2 + b**2)
        distances.append(d)
        
    k = np.argmax(np.array(distances)) + 1
    return k


def kmeans_elbow(data, nk=10, niter=100):
    errorset = []
    
    for nclusters in range(1, nk + 1):
        _, _, err = preliminary_kmeans(data, nclusters)
        errorset.append(err)
        print(".", end="")

    k = find_k_elbow(errorset)        
    return k, errorset