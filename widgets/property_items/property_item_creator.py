from cshape_objects.cshape_types import CShapeTypes
from widgets.property_items.property_combo_box import PropertyComboBox
from widgets.property_items.property_composite_widget_list import PropertyCompositeWidgetList
from widgets.property_items.property_float import PropertyFloat
from widgets.property_items.property_list import PropertyList
from widgets.property_items.property_referenced_form import PropertyReferencedForm
from widgets.property_items.property_string import PropertyString
from widgets.property_items.property_table import PropertyTable
from widgets.property_items.property_vector3d_float import PropertyVector3DFloat

properties_types = {
    CShapeTypes.Float: PropertyFloat,
    CShapeTypes.String: PropertyString,
    CShapeTypes.Vector3DFloat: PropertyVector3DFloat,
    CShapeTypes.Enum: PropertyComboBox,
    CShapeTypes.List: PropertyList,
    CShapeTypes.Table: PropertyTable,
    CShapeTypes.CompositeList: PropertyCompositeWidgetList,
    CShapeTypes.Reference: PropertyReferencedForm
}


def create_property(property_type):
    return properties_types[property_type]()
