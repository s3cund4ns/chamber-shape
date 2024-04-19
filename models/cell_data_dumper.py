from cshape_objects.cell import Cell


class CellDataDumper:
    def __init__(self):
        self.item_data: dict = {}

    def dump(self, item: Cell):
        source_item_data: dict = item.get_data()
        self.item_data = {'Type': item.get_type()}
        for key in source_item_data.keys():
            if key == 'Fill':
                self.item_data[key] = source_item_data[key][1][1]
                continue
            if (key == 'Material') or (key == 'Universe'):
                if item.entire == 'Empty':
                    self.item_data[key] = 'Empty'
                    continue
                self.item_data[key] = item.get_entire()
                continue
            if key == 'Surfaces':
                self.item_data[key] = item.get_surfaces_indices()
                continue
            self.item_data[key] = source_item_data[key][1]

        return self.item_data
