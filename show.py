import re
import sys,os
import numpy as np
import matplotlib.pyplot as plt;

#define your reg
reg_iter    = re.compile(r"(?<= Iteration )\d+")
reg_loss    = re.compile(r"(?<= loss = )\d+\.\d+")

#define your variable to print
iter_list   = list()
reg_list    = list()

fname = "./" + sys.argv[1]

with open(fname) as f:
    for line in f.readlines():
        if "Iteration" in line and "loss" in line:
            match = reg_iter.search(line)
            if match:
                iter_list.append(match.group(0))
            match = reg_loss.search(line)
            if match:
                reg_list.append(match.group(0))

print "len of iter list: ", len(iter_list)
print "len of reg list:  ", len(reg_list)

#print your loss or acc curve

niter = len(iter_list)
loss = np.array([float(i) for i in reg_list])
_, ax1 = plt.subplots()

ax1.set_xlabel('Iters')
ax1.set_ylabel('Test loss')
ax1.plot(np.arange(niter), loss, label = "sphereface_train")
plt.legend()
plt.show()
