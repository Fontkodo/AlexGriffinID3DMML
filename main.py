from id3 import buildTree
from breastCancerDecisionTree import createData
from id3Display import html

CANCER_KEYS = "age menopause tumor-size inv-nodes node-caps deg-malig breast breast-quad irradiat".split()

cancerObservations = html(buildTree(createData(), CANCER_KEYS), "output.html")
