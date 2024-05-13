from dataclasses import dataclass


@dataclass
class CShapeTypes:
    Label = 'Label'
    Int = "<class 'int'>"
    Float = "<class 'float'>"
    Range = 'Range'
    String = "<class 'str'>"
    Vector2DInt = "<class 'list'> 2 int"
    Vector2DFloat = "<class 'list'> 2 float"
    Vector2DString = "<class 'list'> 2 str"
    Vector3DInt = "<class 'list'> 3 int"
    Vector3DFloat = "<class 'list'> 3 <class 'numpy.float32'>"
    Vector3DString = "<class 'list'> 3 str"
    Vector3DComboBox = 'Vector3DComboBox'
    Color = 'Color'
    Array2DInt = "Array2DInt"
    Enum = "<class 'list'> 2 <class 'dict'>"
    List = "<class 'list'> <class 'list'>"
    Table = 'Table'
    CompositeList = 'CompositeList'
    CompositeItems = 'CompositeItems'
    CompositeEnums = 'CompositeEnums'
    Reference = 'Reference'
