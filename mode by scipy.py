import scipy.stats
n_num = [1,2,2,3,2,4,2,2]
n = len(n_num)
x = scipy.stats.mode(n_num)
print(x)
