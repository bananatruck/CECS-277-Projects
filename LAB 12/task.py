class Task:
    def _init_(self, desc, date, time):
        self.description = desc
        self.date = date
        self.time = time

    def _str_(self):
        return f"{self.description} - Due: {self.date} at {self.time}"

    def _repr_(self):
        return f"{self.description},{self.date},{self.time}"

    def _lt_(self, other):
        self_parts = [int(x) for x in self.date.split('/')] + [int(x) for x in self.time.split(':')]
        other_parts = [int(x) for x in other.date.split('/')] + [int(x) for x in other.time.split(':')]
        if self_parts != other_parts:
            return self_parts < other_parts
        return self.description < other.description