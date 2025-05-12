class FlattenIterator:
    def __init__(self, nested_list):
        self.stack = [(nested_list, 0)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current_list, index = self.stack[-1]

            if index >= len(current_list):
                self.stack.pop()
                continue

            self.stack[-1] = (current_list, index + 1)
            item = current_list[index]

            if isinstance(item, list):
                self.stack.append((item, 0))
            else:
                return item

        raise StopIteration


class FlattenIterable:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        return FlattenIterator(self.nested_list)
        