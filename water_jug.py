#author @shubhamphl

class jug:
    maxjug=[0,0]
    jugs = (0,0)
    jug1=jugs[0]
    jug2=jugs[1]
    goal_amount=[]

    visited_nodes=[(0,0)]
    parent={}
    j=(0,0)
    bfslist=[]


    def set_jugs(self):
        print("Preparing water jugs...")
        jug1_cap=0
        jug2_cap=0
        jug1_cap = int(input("Enter the capacity of first jug: "))
        while jug1_cap <1:
            print("Invalid capacity! jug 1 capacity should not be less than 1")
            jug1_cap = int(input("Enter the capacity of first jug: "))

        jug2_cap = int(input("Enter the capacity of second jug: "))
        while jug2_cap <1:
            print("Invalid capacity! jug 2 capacity should not be less than 1")
            jug2_cap = int(input("Enter the capacity of second jug: "))
        self.maxjug=[jug1_cap,jug2_cap]
        print("jug volume received successfully!")
        print()
        self.set_goals()

    def set_goals(self):
        print("setting the goal amount of water...")
        temp=int(input("Enter the amount of water to be poured:"))
        while temp>max(self.maxjug[0],self.maxjug[1]):
            print("invalid goal amount! goal amount should not be greater than the maximum capacity of both the jugs")
            temp = int(input("Enter the amount of water to be poured :"))
        for g in range(max(self.maxjug[0],self.maxjug[1])+1):

            self.goal_amount.append((temp,g))
            self.goal_amount.append((g,temp))
        print("goal amount set successfully!")
        print()
        self.select_searchtype()



    def select_searchtype(self):
        ch=3
        while ch>2 or ch<0:
            print("Enter the type of search to be performed to get the solution:")
            print("1: To use Breadth First Search")
            print("2: To use Depth First Search")
            print("0: To exit from the main menu")
            ch = int(input(ch))
            if ch>2 or ch<0:
                print("invalid choice! please try again")

        if ch == 1:
            self.bfs(self.jugs)
        elif ch == 2:
            self.dfs(self.jugs)
        elif ch==0:
            exit(0)

    def print_solution(self):

        print("steps: ")
        for i in self.visited_nodes:
            print(i)
        print("Graph: ",graph)
        exit(0)

    def dfs(self,jugs):
        flag = 0
        if jugs in self.goal_amount:
            print("Depth First Search solution: ")
            flag = 0
            self.print_solution()

        else:
                                                                                                                                # fill jug 1
                if not self.visited_nodes.__contains__((self.maxjug[0],jugs[1])):
                    graph[jugs]=[[self.maxjug[0],jugs[1]]]

                    graph[self.maxjug[0], jugs[1]] =[]
                    self.visited_nodes.append((self.maxjug[0],jugs[1]))
                    flag=1
                    j=(self.maxjug[0],jugs[1])
                    self.dfs(j)


                                                                                                                                # fill jug 2
                if not self.visited_nodes.__contains__((jugs[0],self.maxjug[1])):
                    graph[jugs].append([jugs[0],self.maxjug[1]])
                    graph[jugs[0],self.maxjug[1]] =[]
                    self.visited_nodes.append((jugs[0],self.maxjug[1]))
                    flag = 1
                    j=(jugs[0],self.maxjug[1])
                    self.dfs(j)


                                                                                                                                # transfer jug 1 to jug 2

                jug2left = self.maxjug[1] - jugs[1]
                if jugs[0]<=jug2left:
                    if not self.visited_nodes.__contains__((0, jugs[1] + jugs[0])):
                        graph[jugs].append([0, jugs[1] + jugs[0]])
                        self.visited_nodes.append((0, jugs[1] + jugs[0]))
                        graph[0, jugs[1] + jugs[0]] = []
                        flag = 1
                        j=(0, jugs[1] + jugs[0])
                        self.dfs(j)



                else:
                    if not self.visited_nodes.__contains__((jugs[0] - jug2left, jugs[1] + jug2left)):
                            graph[jugs].append([jugs[0] - jug2left, jugs[1] + jug2left])
                            graph[jugs[0] - jug2left, jugs[1] + jug2left] = []
                            self.visited_nodes.append((jugs[0] - jug2left, jugs[1] + jug2left))
                            flag = 1
                            j = (jugs[0] - jug2left, jugs[1] + jug2left)
                            self.dfs(j)


                                                                                                                                # empty jug 1
                if not self.visited_nodes.__contains__((0,jugs[1])):
                    graph[jugs].append([0, jugs[1]])
                    graph[0, jugs[1]] = []
                    flag = 1
                    self.visited_nodes.append((0,jugs[1]))
                    j = (0, jugs[1])
                    self.dfs(j)

                                                                                                                                #empty jug 2
                if not self.visited_nodes.__contains__((jugs[0],0)):
                    graph[jugs].append([jugs[0],0])
                    graph[jugs[0],0] = []
                    flag = 1
                    self.visited_nodes.append((jugs[0],0))
                    j = (jugs[0],0)
                    self.dfs(j)

                                                                                                                                #transfer jug 2 to jug 1

                jug1left = self.maxjug[0] - jugs[0]
                if jug1left >= jugs[1]:
                        if not self.visited_nodes.__contains__((jugs[1] + jugs[0],0)):
                                graph[jugs].append([jugs[1] + jugs[0],0])
                                graph[jugs[1] + jugs[0],0] = []
                                flag = 1
                                self.visited_nodes.append((jugs[1] + jugs[0],0))
                                j = (jugs[1] + jugs[0],0)
                                self.dfs(j)
                else:
                        if not self.visited_nodes.__contains__((jugs[0] + jug1left, jugs[1] - jug1left)):
                                graph[jugs].append([jugs[0] + jug1left, jugs[1] - jug1left])
                                graph[jugs[0] + jug1left, jugs[1] - jug1left] = []
                                self.visited_nodes.append((jugs[0] + jug1left, jugs[1] - jug1left))
                                flag=1
                                j = (jugs[0] + jug1left, jugs[1] - jug1left)
                                self.dfs(j)


    def bfs(self,jugs):

            flag = 0
                                                                                                                                # fill jug 1
            if not self.visited_nodes.__contains__((self.maxjug[0], jugs[1])):
                graph[jugs] = [[self.maxjug[0], jugs[1]]]
                graph[self.maxjug[0], jugs[1]] = []
                self.visited_nodes.append((self.maxjug[0], jugs[1]))
                flag = 1

                self.j = (self.maxjug[0], jugs[1])
                self.parent[self.j] = jugs
                self.check_bfs_goal(self.j)

                                                                                                                                # fill jug 2
            if not self.visited_nodes.__contains__((jugs[0], self.maxjug[1])):
                graph[jugs].append([jugs[0], self.maxjug[1]])
                graph[jugs[0], self.maxjug[1]] = []
                self.visited_nodes.append((jugs[0], self.maxjug[1]))
                flag = 1
                self.parent[jugs[0], self.maxjug[1]] = jugs
                self.j = (jugs[0], self.maxjug[1])
                self.parent[self.j] = jugs
                self.check_bfs_goal(self.j)

                                                                                                                                # transfer jug 1 to jug 2

            jug2left = self.maxjug[1] - jugs[1]
            if jugs[0] <= jug2left:
                if not self.visited_nodes.__contains__((0, jugs[1] + jugs[0])):
                    graph[jugs].append([0, jugs[1] + jugs[0]])
                    self.visited_nodes.append((0, jugs[1] + jugs[0]))
                    graph[0, jugs[1] + jugs[0]] = []
                    flag = 1
                    self.j = (0, jugs[1] + jugs[0])
                    self.parent[self.j] = jugs

                    self.check_bfs_goal(self.j)




            else:
                if not self.visited_nodes.__contains__((jugs[0] - jug2left, jugs[1] + jug2left)):
                    graph[jugs].append([jugs[0] - jug2left, jugs[1] + jug2left])
                    graph[jugs[0] - jug2left, jugs[1] + jug2left] = []
                    self.visited_nodes.append((jugs[0] - jug2left, jugs[1] + jug2left))
                    flag = 1
                    self.j = (jugs[0] - jug2left, jugs[1] + jug2left)
                    self.parent[self.j] = jugs
                    self.check_bfs_goal(self.j)


                                                                                                                                # empty jug 1
            if not self.visited_nodes.__contains__((0, jugs[1])):
                graph[jugs].append([0, jugs[1]])
                graph[0, jugs[1]] = []
                flag = 1
                self.visited_nodes.append((0, jugs[1]))
                self.j = (0, jugs[1])
                self.parent[self.j] = jugs
                self.check_bfs_goal(self.j)


                                                                                                                                # empty jug 2
            if not self.visited_nodes.__contains__((jugs[0], 0)):
                graph[jugs].append([jugs[0], 0])
                graph[jugs[0], 0] = []
                flag = 1
                self.visited_nodes.append((jugs[0], 0))
                self.j = (jugs[0], 0)
                self.parent[self.j] = jugs
                self.check_bfs_goal(self.j)

                                                                                                                                # transfer jug 2 to jug 1

            jug1left = self.maxjug[0] - jugs[0]
            if jug1left >= jugs[1]:
                if not self.visited_nodes.__contains__((jugs[1] + jugs[0], 0)):
                    graph[jugs].append([jugs[1] + jugs[0], 0])
                    graph[jugs[1] + jugs[0], 0] = []
                    flag = 1
                    self.visited_nodes.append((jugs[1] + jugs[0], 0))
                    self.j = (jugs[1] + jugs[0], 0)
                    self.parent[self.j] = jugs
                    self.check_bfs_goal(self.j)

            else:
                if not self.visited_nodes.__contains__((jugs[0] + jug1left, jugs[1] - jug1left)):
                    graph[jugs].append([jugs[0] + jug1left, jugs[1] - jug1left])
                    graph[jugs[0] + jug1left, jugs[1] - jug1left] = []
                    self.visited_nodes.append((jugs[0] + jug1left, jugs[1] - jug1left))
                    flag = 1
                    self.j = (jugs[0] + jug1left, jugs[1] - jug1left)
                    self.parent[self.j] = jugs
                    self.check_bfs_goal(self.j)

            i=self.visited_nodes.index(jugs)
            k=self.visited_nodes[i+1]
            self.bfs(k)


    def check_bfs_goal(self,jugs):
        if jugs in self.goal_amount:
            print("Breadth First Search solution: ")
            print("steps: ")
            flag = 0
            self.parents(self.j)



    def parents(self,j):
        while j!=self.jugs:
            self.bfslist.append(j)
            self.parents(self.parent[j])
        self.bfslist.append(self.jugs)
        for n in range(len(self.bfslist)-1,0,-1):
            print(self.bfslist[n])
        print(self.bfslist[0])
        print("Graph :", graph)
        exit(0)

j=jug()
graph={}
maxjug=j.set_jugs()


