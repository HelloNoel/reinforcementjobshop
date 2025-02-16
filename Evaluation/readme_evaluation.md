# **How to evaluate the results**
`statistics.py` features the creation of plots as well as statistical tests.
You should change the folder and file names according to your liking.

* Use the Shapiro-Wilk test to verify if your results follow a normal distribution
* Use the wilcoxon signed rank test to verify if your results 
are significantly different from a baseline (e.g. from the status quo of the simulation.
The wilcoxon signed rank test only works for paired samples which have the same random number stream.
In version 1.0 of this project, all used environments and algorithms have a fixed
random number stream, so you can use the wilcoxon signed rank test.
* Use a scatter plot to visualize the training success (either from `statistics.py` or `plot.sh`)
* To run `plot.sh` on your Linux system, open a terminal in the same folder and type `sh plot.sh `
* The job shop environment writes its results to the /Evaluation/ folder. 
You need to create subfolders if you want to store multiple experimental designs (e.g. BIL2-A and BIL3-B)
* Statistics.py requires that output/results files exist for all possible agents. 
If you do not wish to test all agents, comment out the ones you don't need from statistics.py

