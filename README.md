# Alex Griffin ID3 Data Mining and Machine Learning
This is Alex Griffin implementing the ID3 algorithm for
John Doucette's Data Mining and Machine Learning course.

The file id3.python contains all of the code for the ID3 algorithm itself.
The file id3Display.py allows one to create an HTML file that is
a visualization of the decision tree output by the id3.py file.
For the dataset in question, the output file has already been made,
and included in the form of [output.html](https://htmlpreview.github.io/?https://github.com/Fontkodo/AlexGriffinID3DMML/blob/master/output.html).
main.py generates output.html.

Also included is the dataset "Breast Cancer" by Zwitter and Soklič
from UC Irvine's Machine Learning Repository.
It is a collection of data regarding breast cancer patients and
whether or not they had recurrence.
The purpose is to create a decision tree that roughly predicts
whether individuals will have recurring cancer based on
the characteristics of their prior cancer.
To do this, another file, breastCancerDecisionTree.py, was made,
which takes the data from the cancer dataset and turns it into
a format suitible for use with the ID3 algorithm as implemented here.

REQUIRED CITATION NOTICE FOR CANCER DATASET:
_This breast cancer domain was obtained from the University Medical Centre,
Institute of Oncology, Ljubljana, Yugoslavia. Thanks go to M. Zwitter
and M. Soklic for providing the data. Please include this citation if you plan to use this database._
