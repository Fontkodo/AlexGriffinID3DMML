from id3 import buildTree
from breastCancerDecisionTree import createData, CANCER_KEYS
from id3Display import html

html(buildTree(createData(), CANCER_KEYS), "output.html")
