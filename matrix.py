class Matrix():
    data = []
    
    def append(self, nums):
        self.data.append(nums)

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0]) if len(self.data) > 0 else 0

    def get_line(self, i):
        return self.data[i]

    def get_column(self, j):
        if len(self.data) < 1 or j >= len(self.data[0]):
            return []
        n = len(self.data)
        answer = []
        for i in range (n):
            answer.append(self.data[i][j])
        return answer