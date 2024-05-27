from task import Task

class Tasklist:
    def __init__(self):
        self.tasklist = []
        try:
            with open('tasklist.txt', 'r') as file:
                for line in file:
                    desc, date, time = line.strip().split(',')
                    self.tasklist.append(Task(desc, date, time))
            self.tasklist.sort()
        except FileNotFoundError:
            pass

    def add_task(self, desc, date, time):
        self.tasklist.append(Task(desc, date, time))
        self.tasklist.sort()

    def get_current_task(self):
        if self.tasklist:
            return self.tasklist[0]
        return "All tasks are complete."

    def mark_complete(self):
        if self.tasklist:
            completed_task = self.tasklist.pop(0)
            return completed_task
        return "No tasks to complete."

    def save_file(self):
        with open('tasklist.txt', 'w') as file:
            for task in self.tasklist:
                file.write(repr(task) + '\n')

    def __len__(self):
        return len(self.tasklist)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.tasklist):
            result = self.tasklist[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration
