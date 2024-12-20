from fvh3t.qgis_plugin_tools.tools.exceptions import QgsPluginException


class InvalidGeometryTypeException(QgsPluginException):
    pass


class InvalidDirectionException(QgsPluginException):
    pass


class InvalidLayerException(QgsPluginException):
    pass


class InvalidTrajectoryException(QgsPluginException):
    pass


class InvalidFeatureException(QgsPluginException):
    pass


class InvalidSegmentException(QgsPluginException):
    pass
