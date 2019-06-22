import numpy as np
from numpy.random import multivariate_normal, shuffle

# Another way of generating data which I didn't use 
#from sklearn.datasets import make_blobs

# A more compact way of generating sample points
# which i discovered not soon enough
# this is also not used 
def generate_samples():
    data1 = np.random.multivariate_normal(mean=[4, 0], cov=[[1, 0], [0, 1]], size=75)
    data2 = np.random.multivariate_normal(mean=[6, 6], cov=[[2, 0], [0, 2]], size=250)
    data3 = np.random.multivariate_normal(mean=[1, 5], cov=[[1, 0], [0, 2]], size=20)
    return np.concatenate([data1, data2, data3])

def generate_synthetic_2dpoints(mean, cov, npoints):
    points = multivariate_normal(mean, cov, npoints).T
    return points

# generate random covariance
def rcov(r=9):
    np.random.seed(r)
    x = np.random.uniform(-0.35, 0.35, size = (2, 2))
    x = np.dot(x, x.transpose())
    return x 


# generate synthetic data 
def gen_set1():
    # 2 clusters
    cov1 = [[0.02, 0], [0, 0.15]]
    cov2 = [[0.02, 0], [0, 0.25]]
    
    means = [[-1.00, +1.10], 
             [+0.25, -0.75]]
    cov = [cov1, rcov()]

    npoints = [75, 90]
       
    p1 = generate_synthetic_2dpoints(means[0], cov[0], npoints[0])
    p2 = generate_synthetic_2dpoints(means[1], cov[1], npoints[1])
    pa = np.hstack((p1, p2))
    pa = pa.T
    
    # 3 clusters
    means = [[-0.50, -0.00], 
             [+1.65, -1.50], 
             [+1.50, +0.50]]
    cov = [cov1, rcov(), rcov()]
    npoints = [40, 60, 70]

    p1 = generate_synthetic_2dpoints(means[0], cov[0], npoints[0])
    p2 = generate_synthetic_2dpoints(means[1], cov[1], npoints[1])
    p3 = generate_synthetic_2dpoints(means[2], cov[2], npoints[2])
    pb = np.hstack((p1, p2, p3))
    pb = pb.T

    # 4 clusters
    means = [[+1.70, -1.15], 
             [+2.15, +1.10], 
             [-1.20, +1.50],
             [-1.20, -0.2]]
    cov = [rcov() for i in range(4)]
    npoints = [50, 75, 60, 95]

    p1 = generate_synthetic_2dpoints(means[0], cov[0], npoints[0])
    p2 = generate_synthetic_2dpoints(means[1], cov[1], npoints[1])
    p3 = generate_synthetic_2dpoints(means[2], cov[2], npoints[2])
    p4 = generate_synthetic_2dpoints(means[3], cov[3], npoints[3])
    pc = np.hstack((p1, p2, p3, p4))
    pc = pc.T


    # 5 clusters 
    means = [[-2.1, -1.5], 
             [-2.5, +1.5], 
             [+1.8, -1.6],
             [+2.3, +1.7],
             [+0.1, +0.1]]

    cov = [cov1, rcov(), rcov(), cov2, rcov()]
    npoints = [90, 55, 70, 40, 60]
    p1 = generate_synthetic_2dpoints(means[0], cov[0], npoints[0])
    p2 = generate_synthetic_2dpoints(means[1], cov[1], npoints[1])
    p3 = generate_synthetic_2dpoints(means[2], cov[2], npoints[2])
    p4 = generate_synthetic_2dpoints(means[3], cov[3], npoints[3])
    p5 = generate_synthetic_2dpoints(means[4], cov[4], npoints[4])
    pd = np.hstack((p1, p2, p3, p4, p5))
    pd = pd.T

    return [pa, pb, pc, pd]