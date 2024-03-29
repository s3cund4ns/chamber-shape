from dataclasses import dataclass


@dataclass
class CShapeTypes:
    Int = "<class 'int'>"
    Float = "<class 'float'>"
    String = "<class 'str'>"
    Vector2DInt = "<class 'list'> 2 int"
    Vector2DFloat = "<class 'list'> 2 float"
    Vector2DString = "<class 'list'> 2 str"
    Vector3DInt = "<class 'list'> 3 int"
    Vector3DFloat = "<class 'list'> 3 <class 'numpy.float32'>"
    Vector3DString = "<class 'list'> 3 str"
    Enum = "<class 'list'> 2 <class 'dict'>"
    List = "<class 'list'> <class 'list'>"
    Table = 'Table'
