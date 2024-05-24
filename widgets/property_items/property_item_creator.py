from cshape_objects.cshape_types import CShapeTypes
from widgets.property_items.property_array2d_int import PropertyArray2DInt
from widgets.property_items.property_color import PropertyColor
from widgets.property_items.property_combo_box import PropertyComboBox
from widgets.property_items.property_composite_combo_box_list import PropertyCompositeComboBoxList
from widgets.property_items.property_composite_item_list import PropertyCompositeItemList
from widgets.property_items.property_composite_widget_list import PropertyCompositeWidgetList
from widgets.property_items.property_float import PropertyFloat
from widgets.property_items.property_info import PropertyInfo
from widgets.property_items.property_int import PropertyInt
from widgets.property_items.property_label import PropertyLabel
from widgets.property_items.property_list import PropertyList
from widgets.property_items.property_referenced_form import PropertyReferencedForm
from widgets.property_items.property_slider import PropertySlider
from widgets.property_items.property_string import PropertyString
from widgets.property_items.property_table import PropertyTable
from widgets.property_items.property_vector2d_float import PropertyVector2DFloat
from widgets.property_items.property_vector2d_int import PropertyVector2DInt
from widgets.property_items.property_vector3d_combo_box import PropertyVector3DComboBox
from widgets.property_items.property_vector3d_float import PropertyVector3DFloat

properties_types = {
    CShapeTypes.Float: PropertyFloat,
    CShapeTypes.Label: PropertyLabel,
    CShapeTypes.Range: PropertySlider,
    CShapeTypes.String: PropertyString,
    CShapeTypes.Int: PropertyInt,
    CShapeTypes.Vector2DInt: PropertyVector2DInt,
    CShapeTypes.Vector2DFloat: PropertyVector2DFloat,
    CShapeTypes.Vector3DFloat: PropertyVector3DFloat,
    CShapeTypes.Vector3DComboBox: PropertyVector3DComboBox,
    CShapeTypes.Color: PropertyColor,
    CShapeTypes.Array2DInt: PropertyArray2DInt,
    CShapeTypes.Enum: PropertyComboBox,
    CShapeTypes.List: PropertyList,
    CShapeTypes.Table: PropertyTable,
    CShapeTypes.CompositeList: PropertyCompositeWidgetList,
    CShapeTypes.CompositeItems: PropertyCompositeItemList,
    CShapeTypes.CompositeEnums: PropertyCompositeComboBoxList,
    CShapeTypes.Reference: PropertyReferencedForm,
    CShapeTypes.Info: PropertyInfo
}


def create_property(property_type):
    return properties_types[property_type]()
