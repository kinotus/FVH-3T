from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple

from qgis.core import QgsGeometry, QgsPointXY, QgsVectorLayer, QgsWkbTypes

if TYPE_CHECKING:
    from fvh3t.core.gate import Gate


class TrajectoryNode(NamedTuple):
    """
    A simple data container representing one node in a
    trajectory.
    """

    point: QgsPointXY
    timestamp: int

    @classmethod
    def from_coordinates(cls, x: float, y: float, timestamp: int):
        return cls(QgsPointXY(x, y), timestamp)


class Trajectory:
    """
    Class representing a trajectory which consists
    of nodes which have a location and a timestamp
    """

    def __init__(self, nodes: tuple[TrajectoryNode, ...]) -> None:
        self.__nodes: tuple[TrajectoryNode, ...] = nodes

    def as_geometry(self) -> QgsGeometry:
        return QgsGeometry.fromPolylineXY([node.point for node in self.__nodes])

    def intersects_gate(self, other: Gate) -> bool:
        return self.as_geometry().intersects(other.geometry())

    def average_speed(self) -> float:
        # TODO: implement function
        return 0.0


class TrajectoryLayer:
    """
    Wrapper around a QgsVectorLayer object from which trajectories
    can be instantiated, i.e.

    1. is a point layer
    2. has a valid identifier field
    3. has a valid timestamp field
    """

    def __init__(self, layer: QgsVectorLayer, id_field: str, timestamp_field: str) -> None:
        self.__layer: QgsVectorLayer = layer
        self.__id_field: str = id_field
        self.__timestamp_field: str = timestamp_field

    def is_valid(self) -> bool:
        is_point_layer: bool = self.__layer.geometryType() == QgsWkbTypes.GeometryType.PointGeometry
        id_field_exists: bool = self.__layer.fields().indexFromName(self.__id_field) != -1
        timestamp_field_exists: bool = self.__layer.fields().indexFromName(self.__timestamp_field) != -1

        return is_point_layer and id_field_exists and timestamp_field_exists
