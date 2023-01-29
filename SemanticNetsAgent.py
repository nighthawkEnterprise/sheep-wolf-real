class SemanticNetsAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass


#given an array of [(1,1,), (0,0)];
# then generate possibilities of this; new array of tuples
#then run through array of child possibilities 
    def solve(self, initial_sheep, initial_wolves):
        leftSide = (initial_sheep, initial_wolves);
        rightSide = (0,0);
        startingState = [(leftSide, rightSide, ('R'))];
        totalTestCases= [startingState];
        
        print(totalTestCases);
        # print("Starting State: ", totalTestCases);

        parentalization = []
        finalRightState = set();
        finalLeftState = set();
        startingStateTuple = ((leftSide, rightSide, ('R')));
        finalRightState.add(startingStateTuple);
        direction = True;
        for index,stateSet in enumerate(totalTestCases): 
            # if direction: 
            #     print("Moving Right");
            # else: 
            #     print("Moving Left");
                #test state ([], [values]) to monitor direction
            print(f"**************Move {index+1} ***********************")
            for state in stateSet:
                print("STATE: ", state)
                possibleStates = [];
                possibleStates = self.generatePossibleStates(state, direction);
                print("Possible States: ", possibleStates);
                if direction: 
                    # print(f"Moving right, checking against finalLeftState")
                    finalPossibleState  = self.pruner(possibleStates, finalLeftState);
                else: 
                    # print(f"Moving lef, checking against finalRightState")
                    finalPossibleState = self.pruner(possibleStates, finalRightState);
                print('Final State: ', finalPossibleState);
                # totalTestCases.pop(0);
                # print(f"__ Found {len(finalPossibleState)} states");
                for finalState in finalPossibleState: 
                    # parentalization.append(state, finalState);
                    # print("STATE@@!@#@#!@: ", state);
                    # print("FINAFlkjLSDKFJS: ", finalState);
                    parentalization.append((state, finalState));
                    if(direction):
                        finalLeftState.add(finalState);
                    else:
                        finalRightState.add(finalState);
                # print("Final RIght State: ", finalRightState);
                # print("Final Left State: ", finalLeftState);
                # print("totalTestCases: ", totalTestCases)

                totalTestCases.append(finalPossibleState);

            print("total Test Cases: ", totalTestCases);
            direction = not direction;
        # print("Parentalization: ", parentalization);
        state_graph = Graph(parentalization);
    
        start = (((initial_sheep, initial_wolves), (0,0), "R"));
        end = (((0,0), (initial_sheep, initial_wolves), "L"));

        print(f"paths between: {start} and {end}: ", state_graph.get_paths(start, end))
        
        # test = [[((0, 0), (1, 1)), ((0, 1), (1, 0)), ((1, 0), (0, 1))]];

        # for state in test:
        #     print('test: ', test);
        #     print('state: ', state);
        #     for x in state: 
        #         print("X: ", x);
        #     test.pop();
                    
            # for child in finalPossibleState:
            #     # testState.append(child);
            #     childTuple = tuple(child);
            #     testState.append([childTuple]);
            #     parentalization.append((x, childTuple))
            #     if(direction): 
            #         finalRightState.add(childTuple);
            #     else:
            #         finalLeftState.add(childTuple);
            
            #     print("Final Right State: ", finalRightState);
            #     print("Final Left State: ", finalLeftState);
            #     # print("pateernalization: ", parentalization);
            #     print("NEW TEST STATE: ", testState);
            #     print("___________________________________")
            #     testState.append(state);
            #     if(direction):
            #         state = tuple(state)
            #         finalRightState.add(state)
            #     else:
            #         state = tuple(state)
            #         finalLeftState.add(state)
                
        #         print("Final Right State: ", finalRightState);
        #         print("Final Left State: ", finalLeftState);
                
        #         direction = not direction;

            
            

        # print("Parentalization: ", parentalization);
        # state_graph = Graph(parentalization);

      
        # startingState = [(3,2), (0,1)]
        # routes = [
    
        #     ("Mumbai", "Paris"),
        #     ("Mumbai", "Dubai"),
        #     ("Paris", "Dubai"),
        #     ("Paris", "New York"),
        #     ("Dubai", "New York"),
        #     ("New York", "Toronto")
        # ]
        # route_graph = Graph(routes);

        # print("Starting State for second child: ", startingState);
        # possibleStates = [];
        # possibleStates = self.generateLeftPossibleStates(startingState);
        # print("Possible States: ", possibleStates);
        # finalPossibleState  = self.pruner(possibleStates);
        # print('Final State: ', finalPossibleState, " Total: ", len(finalPossibleState));
        # print('Final State: ', finalPossibleState, " Total: ", finalPossibleState[0]);
        # # parentilization = []
        # for x in finalPossibleState:
        #     print("X: ", x);
        #     parentilization.append((startingState, x))
        # print("FINAL Parentalization:", parentilization);
        # state_graph_2 = Graph(parentilization);

   
            

        # possible moves: 
        # (2,0), (0,2), (1,1), (1,0), (0,1) 
        # Add your code here! Your solve method should receive
        # the initial number of sheep and wolves as integers,
        # and return a list of 2-tuples that represent the moves
        # required to get all sheep and wolves from the left
        # side of the river to the right.
        
        # If it is impossible to move the animals over according
        # to the rules of the problem, return an empty list of
        # moves.
        pass

    def generatePossibleStates(self, startingState, direction):
     #   print("Hello");
        # print("_____generator___");
        # print("Starting state to generate on : ", startingState);
        possibleState = [];
        startingSheepLeft = startingState[0][0];
        startingSheepRight = startingState[1][0];
        startingWolfLeft = startingState[0][1];
        startingWolfRight=  startingState[1][1]; 
        # leftTotal = startingSheepLeft + startingWolfLeft;
        if(direction): #direction true is right
            if startingSheepLeft >= 2:  # moving 2,0
            #  print("Sheep greater than 2, moving to right");
                sheepLeft = startingSheepLeft -2;
                sheepRight = startingSheepRight + 2; 
                # print("Moving (2,0) RIGHT")
                possibleState.append(((sheepLeft, startingWolfLeft), (sheepRight, startingWolfRight),('L')));
            if startingWolfLeft >= 2:
            # print("Wolf greater than 2, moving to right");
                # print("Moving (0,2) RIGHT")

                wolfLeft = startingWolfLeft -2;
                wolfRight = startingWolfRight +2;
                possibleState.append(((startingSheepLeft, wolfLeft), (startingSheepRight, wolfRight), ('L')))
            if startingSheepLeft >= 1 and startingWolfLeft >= 1:
            #  print("Wolf and Sheep greater than 1, moving to right (1,1) ");
                # print("Moving (1,1) RIGHT")

                sheepLeft = startingWolfLeft -1;
                wolfLeft = startingWolfLeft - 1;
                sheepRight = startingSheepRight + 1;
                wolfRight = startingWolfRight + 1;
                # print("Appending State: ", ((sheepLeft, wolfLeft), (sheepRight, wolfRight),('L')))
                possibleState.append(((sheepLeft, wolfLeft), (sheepRight, wolfRight),('L')))
            if startingSheepLeft >= 1:
                # print("Moving (1,0) RIGHT")
            # print(" Sheep greater than 1, moving to right (1,0) ");
                sheepLeft = startingSheepLeft -1;
                sheepRight = startingSheepRight + 1;
                # print("Appending State: ", ((sheepLeft, startingWolfLeft), (sheepRight, startingWolfRight),('L')))
                possibleState.append(((sheepLeft, startingWolfLeft), (sheepRight, startingWolfRight),('L')));
            if startingWolfLeft >=1:
                # print("Moving (0,1) RIGHT")
                # print(" Wolf greater than 1, moving to right (0,1) ");
                wolfLeft = startingWolfLeft -1;
                wolfRight = startingWolfRight + 1;
                # print("Appending State: ", ((startingSheepLeft, wolfLeft), (startingSheepRight, wolfRight),('L')))
                possibleState.append(((startingSheepLeft, wolfLeft), (startingSheepRight, wolfRight),('L')))
        else: 
            if startingSheepRight >= 2:  # moving 2,0
            #  print("Sheep greater than 2, moving to right");
                # print("Moving (2,0) LEFT")
                sheepRight = startingSheepRight -2;
                sheepLeft = startingSheepLeft + 2; 
                # print("Appending State: ", ((sheepLeft, startingWolfLeft), (sheepRight, startingWolfRight),('R')));
                possibleState.append(((sheepLeft, startingWolfLeft), (sheepRight, startingWolfRight),('R')));
            if startingWolfRight >= 2: #moving 0,2
            # print("Wolf greater than 2, moving to right"); 
                # print("Moving (0,2) LEFT");
                wolfLeft = startingWolfLeft +2;
                wolfRight = startingWolfRight -2;
                # print("Appending State: ",((startingSheepLeft, wolfLeft), (startingSheepRight, wolfRight),('R')));

                possibleState.append(((startingSheepLeft, wolfLeft), (startingSheepRight, wolfRight),('R')))
            if startingSheepRight >= 1 and startingWolfRight >= 1:
            #  print("Wolf and Sheep greater than 1, moving to right (1,1) "); moving (1,1)
                # print("Moving (1,1) LEFT")
                sheepLeft = startingSheepLeft + 1;
                wolfLeft = startingWolfLeft + 1;
                sheepRight = startingSheepRight - 1;
                wolfRight = startingWolfRight - 1;
                # print("Appending State: ", ((sheepLeft, wolfLeft), (sheepRight, wolfRight),('R')));
                possibleState.append(((sheepLeft, wolfLeft), (sheepRight, wolfRight),('R')))
            if startingSheepRight >= 1: # moving 1,0
                # print(" Sheep greater than 1, moving to right (1,0) ");
                # print("Moving (1,0) LEFT")
                sheepLeft = startingSheepLeft +1;
                sheepRight = startingSheepRight - 1;
                # print("Appending State: ", ((sheepLeft, startingWolfLeft), (sheepRight, startingWolfRight),('R')))
                possibleState.append(((sheepLeft, startingWolfLeft), (sheepRight, startingWolfRight),('R')));
            if startingWolfRight >=1: #moving 0, 1
                # print(" Wolf greater than 1, moving to right (0,1) ");
                # print("Moving (0,1) LEFT")
                wolfLeft = startingWolfLeft +1;
                wolfRight = startingWolfRight - 1;
                # print("Appending State: ", ((startingSheepLeft, wolfLeft), (startingSheepRight, wolfRight),('R')))
                possibleState.append(((startingSheepLeft, wolfLeft), (startingSheepRight, wolfRight),('R')))
        # print("Possible States Generated: ", possibleState);
        # print("_____end_generator___");

        return possibleState

    def pruner(self, possibleState, stateCheck):
        removeIndex = []
        for index, x in enumerate(possibleState): # Pruner by validater
            leftSheep = x[0][0];
            leftWolf = x[0][1];
            rightSheep = x[1][0];
            rightWolf = x[1][1];
            if((leftWolf > leftSheep and leftSheep > 0) or (rightWolf > rightSheep and rightSheep > 0 )):
            #   print("Flagged state: ", x, " due to invalide state");
              removeIndex.append(index);
            elif (tuple(x) in stateCheck):
                # print("Flagged state: ", x, " due to duplicate state found");
                removeIndex.append(index);
            removeIndex.sort(reverse=True)
        # print('Remove Index: ', removeIndex);     
        for x in removeIndex: # remove larger index first or find a way to remove without disturbing the queue!!!
            # print(f"REMOVING {possibleState[x]}")
            del possibleState[x];
        return possibleState;


class Graph:
    def __init__(self, edges):
        self.edges = edges;
        self.graph_dict = {}
        for start, end in self.edges:
            start = tuple(start);
            # print("START: ", start);
            if start in self.graph_dict:
                self.graph_dict[start].append(end);
            else: 
                self.graph_dict[start] = [end]
        # print("Graph dict: ", self.graph_dict);

    def get_paths(self, start, end, path=[]):
        path = path + [start];

        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return [];

        paths = []
        for node in self.graph_dict[start]:
            if(node not in path):
                new_paths = self.get_paths(node, end, path);
                for p in new_paths:
                    paths.append(p)
        
        return paths;

#  print("______________________________ NEW PROBLEM __________");
       

  # startingState = [(3,2), (0,1)]
        # routes = [
        #     ("Mumbai", "Paris"),
        #     ("Mumbai", "Dubai"),
        #     ("Paris", "Dubai"),
        #     ("Paris", "New York"),
        #     ("Dubai", "New York"),
        #     ("New York", "Toronto")
        # ]
        # route_graph = Graph(routes);
