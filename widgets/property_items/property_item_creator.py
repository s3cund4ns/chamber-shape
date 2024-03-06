from widgets.property_items.property_combo_box import PropertyComboBox
from widgets.property_items.property_float import PropertyFloat
from widgets.property_items.property_item import PropertyItemTypes
from widgets.property_items.property_list import PropertyList
from widgets.property_items.property_string import PropertyString
from widgets.property_items.property_vector3d_float import PropertyVector3DFloat

properties_types = {
    PropertyItemTypes.Float: PropertyFloat,
    PropertyItemTypes.String: PropertyString,
    PropertyItemTypes.Vector3DFloat: PropertyVector3DFloat,
    PropertyItemTypes.ComboBox: PropertyComboBox,
    PropertyItemTypes.ListBox: PropertyList
}


def create_property(property_type):
    return properties_types[property_type]()
