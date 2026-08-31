class JobMap():
    def __init__(self, data=None):
        self.job = []

    def addjob(self, data=None) -> str:

        words = ''
        symbol = '>'
        num = 1
        raw_data = data+symbol

        for j in raw_data:
        
            if not symbol in j:
                words+=j
            
            else:
                self.job.append(words)
                num+=1
                words=''
        # return self.job

    def usejob(self):
        try:
            self.job.reverse()

            return self.job.pop()
        
        except IndexError:
            return "JOB ENDED"

        except Exception as e:
            return f"An Unexpected error: {e}"

    def checkjob(self): # Temporary Method

        return self.job
