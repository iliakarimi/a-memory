class GoalsMem():
    def __init__(self):
        self.context_goals = []
        self.recent_goal = None
        self.active_goal = None
        self.chat_facts = []
        self.cn = 0
        self.fn = 0

    def set_goals(
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


class ShortMem():
    def __init__(self):
        self.messages = []
        self.message_number = 0

    def store_messages(self, role:str | None, message:str | None) -> str:
        if self.message_number != 8:
            self.messages.append({"role": role, "content": message})
            self.message_number+=1

        else:
            self.messages.pop(0)
            self.message_number = 0
            self.messages.append({"role": role, "content": message})

    def remind_messages(self):
        return self.messages
