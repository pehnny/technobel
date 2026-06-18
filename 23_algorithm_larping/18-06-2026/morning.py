class MinStack:
    def __init__(self):
        self.stack: list[int] = []
        self.minimum: list[int] = []

    def __len__(self) -> int:
        return len(self.stack)

    def push(self, value: int) -> None:
        """
        :type value: int
        :rtype: None
        """
        minimum = value
        if len(self) > 0:
            minimum = min(value, self.minimum[-1])
        self.stack.append(value)
        self.minimum.append(minimum)

    def pop(self) -> int | None:
        """
        :rtype: None
        """
        if len(self) == 0:
            return
        self.minimum.pop()
        return self.stack.pop()
        

    def top(self) -> int | None:
        """
        :rtype: int
        """
        if len(self) == 0:
            return
        return self.stack[-1]

    def getMin(self) -> int | None:
        """
        :rtype: int
        """
        if len(self) == 0:
            return
        return self.minimum[-1]
