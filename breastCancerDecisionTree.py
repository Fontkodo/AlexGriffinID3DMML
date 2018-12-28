from id3 import observation, buildTree

'''
This breast cancer domain was obtained from the University Medical Centre,
Institute of Oncology, Ljubljana, Yugoslavia.
Thanks go to M. Zwitter and M. Soklic for providing the data.
Please include this citation if you plan to use this database.

Attribute Information:
   1. Class: no-recurrence-events, recurrence-events
   2. age: 10-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-79, 80-89, 90-99.
   3. menopause: lt40, ge40, premeno.
   4. tumor-size: 0-4, 5-9, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40-44,
                  45-49, 50-54, 55-59.
   5. inv-nodes: 0-2, 3-5, 6-8, 9-11, 12-14, 15-17, 18-20, 21-23, 24-26,
                 27-29, 30-32, 33-35, 36-39.
   6. node-caps: yes, no.
   7. deg-malig: 1, 2, 3.
   8. breast: left, right.
   9. breast-quad: left-up, left-low, right-up, right-low, central.
  10. irradiat: yes, no.
'''

CANCER_KEYS = "age menopause tumor-size inv-nodes node-caps deg-malig breast breast-quad irradiat".split()

def createData():
    '''
    Takes Zwitter and Soklic's Breast Cancer database and turns it into compatible data
    '''
    def lineToObservation(ln):
        '''
        Turns lines from the CSV into the observation objects used in the id3 code
        '''
        fields = ln.split(",")
        target = fields[0]
        values = fields[1:]
        attributes = {k:v for (k, v) in zip(CANCER_KEYS, values)}
        return observation(target, attributes)
    
    lines = [ln.strip() for ln in open("breast-cancer.data").readlines() if ('?' not in ln)]
    
    return [lineToObservation(ln) for ln in lines]

'''
Stores the data as cancerObservations
'''
cancerObservations = createData()
