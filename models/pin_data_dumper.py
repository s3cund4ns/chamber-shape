from cshape_objects.pin import Pin


class PinDataDumper:
    def __init__(self):
        self.item_data: dict = {}

    def dump(self, item: Pin):
        source_item_data: dict = item.get_data()
        self.item_data = {'Type': item.get_type()}
        for key in source_item_data.keys():
            if key == 'Regions':
                self.item_data[key] = source_item_data[key][1][0]
                continue
            self.item_data[key] = source_item_data[key][1]

        return self.item_data
