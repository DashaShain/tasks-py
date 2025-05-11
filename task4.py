class FlattenIterator:
    def __init__(self, nested_list):
        self.stack = [nested_list]       # Стек списков
        self.index_stack = [0]           # Индексы внутри каждого уровня

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current_list = self.stack[-1]
            index = self.index_stack[-1]

            if index >= len(current_list):
                self.stack.pop()
                self.index_stack.pop()
                continue

            self.index_stack[-1] += 1
            item = current_list[index]

            if isinstance(item, list):
                self.stack.append(item)
                self.index_stack.append(0)
            else:
                return item

        raise StopIteration