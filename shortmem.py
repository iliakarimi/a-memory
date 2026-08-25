class GoalsMem():
    def __init__(self):
        self.context_goals = []
        self.recent_goal = None
        self.active_goal = None
        self.chat_facts = []
        self.cn = 0
        self.fn = 0


    def temp(
            self, contextgoals=None, recentgoal=None, 
            activegoal=None, chatfacts=None
            ) -> str:

        if activegoal:
            self.active_goal = activegoal

        if recentgoal:
            self.recent_goal = recentgoal

        if contextgoals:
            self.context_goals.append(f"number{self.cn}: "+contextgoals)
            self.cn+=1

        if chatfacts:
            self.chat_facts.append(f"number{self.fn}: "+chatfacts)
            self.fn=+1


    def resault(
            self, cg=False, ag=False, 
            rg=False, cf=False, al=False
            ):
        resu = []

        if cg == True:
            resu.append(self.context_goals)

        if ag == True:
            resu.append(self.active_goal)

        if rg == True:
            resu.append(self.recent_goal)

        if cf == True:
            resu.append(self.chat_facts)

        if al == True:
            return f"Active Goal: {self.active_goal}\nRecent Goal: {self.recent_goal}\nContaxt Goals: {self.context_goals}\nChat Facts: {self.chat_facts}"
        if resu!=None:
            return resu


# gm = GoalsMem()

# gm.temp(contextgoals="IDK", recentgoal="hell", )
# print(gm.resault(al=True)+"\n\n")

# gm.temp(contextgoals="g", recentgoal="hello", )
# print(gm.resault(al=True)+"\n\n")

# gm.temp(contextgoals="oejfjeg", recentgoal="dw", chatfacts="ijdhie")
# gm.temp(chatfacts="dokwdwod")
# print(gm.resault(al=True, cg=True, cf=True))

