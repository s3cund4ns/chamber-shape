class Tree:
    def __init__(self):
        self.adjacency_lists: dict = {'root': [None, None, []]}

    def get(self):
        return self.adjacency_lists

    def insert_node(self, parent_key: any, key: str, value: any) -> None:
        self.adjacency_lists[key] = [value, parent_key, []]
        self.adjacency_lists[parent_key][2].append(key)

    def delete_node(self, key: str) -> None:
        parent_value = self.adjacency_lists[key][1]
        if parent_value == 'root':
            self.adjacency_lists[parent_value][2].remove(key)
        children_keys = self.adjacency_lists[key][2]
        for child_key in children_keys:
            if len(self.adjacency_lists[child_key][2]) != 0:
                self.delete_node(child_key)
            self.adjacency_lists.pop(child_key, None)
        self.adjacency_lists.pop(key, None)

    def move_node(self, index: int, parent_index: int) -> None:
        old_parent_index = self.adjacency_lists[str(index)][1]
        if old_parent_index == parent_index:
            print('The index of the new parent is the same as the old one')
        else:
            self.adjacency_lists[str(old_parent_index)][2].remove(index)
            self.adjacency_lists[str(parent_index)][2].append(index)
            self.adjacency_lists[str(index)][1] = parent_index

    def find_node(self, parent_key: any, index: int):
        key = self.adjacency_lists[parent_key][2][index]
        return self.adjacency_lists[key]

    def get_node(self, key: str):
        return self.adjacency_lists[key]

    def set_node_value(self, key: str, value: any) -> None:
        self.adjacency_lists[key][0] = value

    def get_node_value(self, key: str):
        return self.adjacency_lists[key][0]
