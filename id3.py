import math

class observation:
    '''
    Represents one observation in the dataset;
    target refers to the class of the observation,
    and attribs to a list of values of its attributes
    '''
    def __init__(self, target, attribs):
        self.target = target
        self.attribs = attribs
        
        if type(self.attribs) != type({}):
            raise Exception("expected dictionary for attribs")
    def __repr__(self):
        return "<{},{}>".format(self.target, self.attribs)

def extractColumn(obs, key):
    '''
    If one were to imagine the dataset as a table,
    with each observation as a row, this would extract an entire column of the table
    obs is the collection of observations, key is a particular attribute
    '''
    return[o.attribs[key] for o in obs]

def entropy(obs):
    '''
    This function calculates the entropy of the dataset, obs
    '''
    counts = {}
    for o in obs:
        counts[o.target] = counts.get(o.target, 0) + 1
    accumulator = 0
    for (target, count) in counts.items():
        proportion = count / len(obs)
        accumulator -= proportion * math.log(proportion, 2)
    return accumulator

def attributeEntropy(obs, key):
    '''
    This calculates entropy after splitting obs with respect to a particular attribute, key
    '''
    column = extractColumn(obs, key)
    uniqueValues = set(column)
    accumulator = 0
    for val in uniqueValues:
        group_obs = [o for o in obs if o.attribs[key] == val]
        group_proportion = len(group_obs) / len(obs)
        group_entropy = entropy(group_obs)
        accumulator += (group_entropy * group_proportion)
    return accumulator

def attributeWithMinimalEntropy(obs, keys):
    '''
    Returns which attribute in keys causes the most information to be gained after splitting obs
    '''
    return min([(attributeEntropy(obs,k), k) for k in keys])[1]

def groupObservations(obs, key):
    '''
    This groups the observations in obs with respect to an attribute key
    '''
    result = {}
    for o in obs:
        attribVal = o.attribs[key]
        collector = result.get(attribVal, [])
        result[attribVal] = collector
        collector.append(o)
    return result

def majorityRule(obs):
    '''
    Returns what the most common class of a collection obs is
    '''
    targetCounts = {}
    for o in obs:
        targetCounts[o.target] = targetCounts.get(o.target,0) + 1
    flippedTuples = [(count, target) for (target,count) in targetCounts.items()]
    return max(flippedTuples)[1]

def numericKey(pair):
    '''
    Used internally for ordering nodes in a tree, so that, for example,
    "5-9" is ordered before "45-49", in constrast to the standard sorting.
    '''
    try:
        return int(pair[0].split("-")[0])
    except:
        return pair[0]

def buildTree(obs, keys):
    '''
    Returns the decision tree produced by the ID3 algorithm,
    which is a list of triples, and each triple consists of an attribute,
    a value for said attribute, and a decision,
    which is either one of the target classes or another such triple.
    '''
    bestAttr = attributeWithMinimalEntropy(obs, keys)
    remainingKeys = [k for k in keys if k != bestAttr]
    grouped = groupObservations(obs, bestAttr)
    if len(grouped) == 1 or len(keys) == 1:
        return majorityRule(obs)
    acc = []
    for (k, subset) in sorted(grouped.items(), key=numericKey):
        groupEntropy = entropy(subset)
        if not entropy(subset):
            acc.append([bestAttr, k, subset[0].target])
        else:
            acc.append([bestAttr, k, buildTree(subset, remainingKeys)])
    return acc
