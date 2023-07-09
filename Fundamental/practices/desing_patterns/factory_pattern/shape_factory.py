from practices.desing_patterns.factory_pattern.circle_Imp import CircleImp
from practices.desing_patterns.factory_pattern.reactangle_imp import ReactAngleImp
from practices.desing_patterns.factory_pattern.shape_type import ShapeType


class ShapeFactory:

    @staticmethod
    def create_shape(context):
        if context.shape_type == ShapeType.CIRCLE:
            return CircleImp(context.x, context.y)
        elif context.shape_type == ShapeType.RECTANGLE:
            return ReactAngleImp(context.x, context.y)
        else:
            raise ValueError("Invalid shape type: %s" % context.shape_type)
