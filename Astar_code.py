from math import sqrt

def dist_between(M,n1,n2):
    (x1,y1) = M.intersections[n1]
    (x2,y2) = M.intersections[n2]
    return sqrt(pow((x2-x1),2)+pow((y2-y1),2))

def heuristic_cost_estimate(M,n1,goal):
    return dist_between(M,n1,goal)

def the_smallest_fScore(openSet,fScore):
    node_list=[]
    m = 0
    for node in openSet:
        node_list.append(fScore[node])
    m = min(node_list)
    for node in openSet:
        if fScore[node] == m:
            return node
        continue


def shortest_path(M,start, goal):
    
    closedSet = set()
    openSet = set()
    openSet.add(start)
    
    cameFrom = {}
    
    gScore = {}
    gScore[start] = 0
    fScore = {}
    fScore[start] = heuristic_cost_estimate(M,start, goal)
    
    while openSet:
        current=the_smallest_fScore(openSet,fScore)
        
        if current == goal:
            return reconstruct_path(cameFrom, current)
        openSet.remove(current)
        closedSet.add(current)
        
        for neighbor in M.roads[current]:
            if neighbor in closedSet:
                continue
            
            tentative_gScore = gScore[current] + dist_between(M,current,neighbor)
            if neighbor not in openSet:
                openSet.add(neighbor)
            
                tentative_is_better = True
            
            elif tentative_gScore < gScore[neighbor]:
                tentative_is_better = True
             
            else:
                tentative_is_better = False
            
            if tentative_is_better == True:
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(M,neighbor, goal)
                cameFrom[neighbor] = current
    
    return Fail

def reconstruct_path(cameFrom, current):
    total_path = [current]
    
    while current in cameFrom.keys():
        
        current = cameFrom[current]
        total_path.append(current)
    total_path.reverse()
    print("shortest path called",total_path)
    return total_path


