# 🟧 in progress
# ✅ working
# ⚠️ Untested
# 🐞Debugging

class Stack:
    # ✅ working
    def __init__(self) -> None:
        self.items = []

    # ✅ working
    def is_empty(self) -> bool:
        return self.items == []

    # ✅ working
    def push(self, item) -> None:
        self.items.append(item)

    # ✅ working
    def pop(self) -> list:
        return self.items.pop()
    
    # ✅ working
    def reset(self) -> None:
        self.items = []
    
    # ✅ working
    def get(self) -> list:
        return self.items