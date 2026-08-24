


class ShortMem():
    def __init__(self):
        self.context_goals = []
        self.recent_goal = None
        self.active_goal = None
        self.chat_facts = []

    def temp(self):
        pass

    def resault(self):
        return self.context_goals, self.active_goal, self.recent_goal, self.chat_facts