# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from sys import path
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    closed = []
    open = []
    paths = {}

    open.append(problem.getStartState())
    paths[problem.getStartState()] = {'path':[]}
    while open:
        x = open.pop(0)
        if problem.isGoalState(x):
            return paths[x]['path']
        else:
            children = problem.getSuccessors(x)
            closed.append(x)
            for child in children:
                if not child[0] in closed and not child[0] in open:
                    open.insert(0, child[0])
                new_path = paths[x]['path'].copy()
                paths[child[0]] = {'path':new_path}
                paths[child[0]]['path'].append(child[1])

    return None
    

def breadthFirstSearch(problem):
    closed = []
    open = []
    paths = {}

    open.append(problem.getStartState())
    paths[problem.getStartState()] = {'path':[]}
    while open:
        x = open.pop(0)
        if problem.isGoalState(x):
            return paths[x]['path']
        else:
            children = problem.getSuccessors(x)
            closed.append(x)
            for child in children:
                if not child[0] in closed and not child[0] in open:
                    open.append(child[0])
                    new_path = paths[x]['path'].copy()
                    paths[child[0]] = {'path':new_path}
                    paths[child[0]]['path'].append(child[1])
    
    return None

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
  
def aStarSearch(problem, heuristic=nullHeuristic):
    closed = []
    open = []
    openq = util.PriorityQueue()
    paths = {}

    openq.push(problem.getStartState(), 0)
    open.append(problem.getStartState())
    paths[problem.getStartState()] = {'path':[], 'cost':0}

    while open:
        current = openq.pop()
        open.remove(current)
        if problem.isGoalState(current):
            return paths[current]['path']
        else:
            children = problem.getSuccessors(current)
            for child in children:
                if not child[0] in closed and not child[0] in open:
                    openq.push(child[0], paths[current]['cost'] + child[2] + heuristic(child[0], problem))
                    open.append(child[0])

                    new_path = paths[current]['path'].copy()
                    new_cost = paths[current]['cost'] + child[2]
                    paths[child[0]] = {'path':new_path, 'cost':new_cost}
                    paths[child[0]]['path'].append(child[1])
                elif child[0] in open:
                    if paths[child[0]]['cost'] + heuristic(child[0], problem) > (paths[current]['cost'] + child[2] + heuristic(child[0], problem)):
                        paths[child[0]]['cost'] = (paths[current]['cost'] + child[2])
                        openq.update(child[0], (paths[current]['cost'] + child[2]+ heuristic(child[0], problem)))
                        
                        new_path = paths[current]['path'].copy()
                        paths[child[0]]['path'] = new_path
                        paths[child[0]]['path'].append(child[1])
                elif child[0] in closed:
                    if paths[child[0]]['cost'] + heuristic(child[0], problem) > (paths[current]['cost'] + child[2] + heuristic(child[0], problem)):
                        closed.remove(child[0])
                        openq.push(child[0], (paths[current]['cost'] + child[2] + heuristic(child[0], problem)))
                        open.append(child[0])
            closed.append(current)
    return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
