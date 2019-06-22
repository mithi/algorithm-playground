import matplotlib.pyplot as plt

def initial_plots(pointset, pointcolor="#e84393", mark='x'):
    
    fig = plt.figure(figsize=(15,10))

    plt.subplot(221)
    plt.plot(pointset[0][:, 0], pointset[0][:, 1], mark, color=pointcolor)

    plt.subplot(222)
    plt.plot(pointset[1][:, 0], pointset[1][:, 1], mark, color=pointcolor)

    plt.subplot(223)
    plt.plot(pointset[2][:, 0], pointset[2][:, 1], mark, color=pointcolor)
    
    plt.subplot(224)
    plt.plot(pointset[3][:, 0], pointset[3][:, 1], mark, color=pointcolor)    
    plt.show()
    
    
def eval_plots(ys, x, pointcolor="#e84393", mark='-*', size=4000):
    
    fig = plt.figure(figsize=(15,10))

    plt.subplot(221)
    plt.plot(x, ys[0], mark, color=pointcolor)

    plt.subplot(222)
    plt.plot(x, ys[1], mark, color=pointcolor)

    plt.subplot(223)
    plt.plot(x, ys[2], mark, color=pointcolor)
    
    plt.subplot(224)
    plt.plot(x, ys[3], mark, color=pointcolor)    
    
    plt.xlabel('K')
    plt.ylabel('SSE');
    plt.show()
    
    
def initial_plots(pointset, pointcolor="#e84393", mark='x'):
    
    fig = plt.figure(figsize=(15,10))

    plt.subplot(221)
    plt.plot(pointset[0][:, 0], pointset[0][:, 1], mark, color=pointcolor)

    plt.subplot(222)
    plt.plot(pointset[1][:, 0], pointset[1][:, 1], mark, color=pointcolor)

    plt.subplot(223)
    plt.plot(pointset[2][:, 0], pointset[2][:, 1], mark, color=pointcolor)
    
    plt.subplot(224)
    plt.plot(pointset[3][:, 0], pointset[3][:, 1], mark, color=pointcolor)    
    plt.show()

    
def colored_subplot(data, labels, centroids, nclusters, n, centroid_color='#2d3436'):
    nsamples = len(data)    
    colors = ['#e84393', '#55efc4', '#74b9ff', '#fdcb6e', '#00cec9', '#ff7675']
    plt.subplot(n)
    
    for k in range(nclusters):
        cluster = data[labels == k, :]
        xs, ys = cluster[:, 0], cluster[:, 1]
        plt.plot(xs, ys, 'x', c=colors[k])
    
    cxs, cys = centroids[:, 0], centroids[:, 1] 
    plt.plot(cxs, cys, '*', color=centroid_color)

    
def colored_plots(idata, ilabels, icentroids, inclusters):
    fig = plt.figure(figsize=(15,10))
    colored_subplot(idata[0], ilabels[0], icentroids[0], inclusters[0], n=221)
    colored_subplot(idata[1], ilabels[1], icentroids[1], inclusters[1], n=222)
    colored_subplot(idata[2], ilabels[2], icentroids[2], inclusters[2], n=223)
    colored_subplot(idata[3], ilabels[3], icentroids[3], inclusters[3], n=224)
    plt.show()