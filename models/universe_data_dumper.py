from cshape_objects.universe import Universe


class UniverseDataDumper:
    def __init__(self):
        self.item_data: dict = {}

    def dump(self, item: Universe):
        source_item_data: dict = item.get_data()
        self.item_data = {'Type': item.get_type()}
        for key in source_item_data.keys():
            self.item_data[key] = source_item_data[key][1]

        return self.item_data
