from PySide6.Qt3DCore import Qt3DCore


class MultiParentEntity(Qt3DCore.QEntity):
    def __init__(self, parent):
        super().__init__(parent)
        self.parents = []

    def add_parent(self, parent):
        if parent not in self.parents:
            self.parents.append(parent)
            parent.addChildEntity(self)

    def remove_parent(self, parent):
        if parent in self.parents:
            self.parents.remove(parent)
            parent.removeChildEntity(self)

    def parents(self):
        return self.parents
