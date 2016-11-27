import random
from collections import deque

def createProblem(exampleNumber, problemType, numVertices, numPath=20, edgeDensity=0.15, branchingFactor = 3):
    f=open(str(exampleNumber) + ".in", 'w')
    f.write(str(numVertices) + "\n")
    adjMatrix = generateHorses(numVertices)
    if problemType == 'paths':
        generatePaths(adjMatrix, numVertices, numPath)
        generateEdges(adjMatrix, edgeDensity)
    if problemType == 'random':
        generateEdges(adjMatrix, edgeDensity)
    if problemType == 'branching': 
        generateBranching(adjMatrix, numVertices, branchingFactor)
        generateEdges(adjMatrix, 0.1)
    writeMatrix(adjMatrix, f)
    f.close()

def generateHorses(numVertices):
    adjMatrix = [[0 for _ in range(numVertices)] for _ in range(numVertices)]
    for i in range(numVertices):
        adjMatrix[i][i] = random.randint(0, 99)
    return adjMatrix
    
def generatePaths(adjMatrix, numVertices, numPath, freeHorse = 0.01):
    # Split into numPath groups randomly, with probability 1 - freeHorse
    # Create paths in adjMatrix from those groups
    paths = [set() for _ in range(numPath)]
    for i in range(numVertices):
        isFreeHorse = random.random()
        if isFreeHorse < freeHorse:
            pass
        j = random.randint(0, numPath-1)
        paths[j].add(i)
    for s in paths:
        head = None
        if len(s) > 0:
            tail = random.sample(s, 1)[0]
            s.remove(tail)
            while len(s) > 0:
                head = tail
                tail = random.sample(s, 1)[0]
                s.remove(tail)
                adjMatrix[head][tail] = 1

def generateEdges(adjMatrix, edgeDensity):
    for i in range(len(adjMatrix)):
        for j in range(len(adjMatrix[i])):
            if i != j and random.random() < edgeDensity:
                adjMatrix[i][j] = 1

def generateBranching(adjMatrix, numVertices, branchingFactor):
    # Soroush's way?
    s = set(range(numVertices))
    v = random.sample(s, 1)[0]
    s.remove(v)
    d = deque()  
    d.append(v)
    while len(s) > 0:
        i = d.popleft()
        branches = int(branchingFactor * random.uniform(0.5, 2.0))
        if len(s) > branches:
            v = random.sample(s, branches)
        else:
            v = list(s)
        for j in v:
            adjMatrix[i][j] = 1
            d.append(j)
            s.remove(j)

def writeMatrix(adjMatrix, f):
    for i in range(len(adjMatrix)):
        f.write(" ".join([str(j) for j in adjMatrix[i]]))
        #for j in range(len(adjMatrix[i])):
        #    f.write(str(adjMatrix[i][j]) + ", ")
        f.write("\n")

if __name__ == "__main__":
    createProblem(1, 'paths', 475)
    createProblem(2, 'paths', 500)
    createProblem(3, 'paths', 500)
