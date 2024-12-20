from qgis.core import QgsProcessingProvider

from fvh3t.fvh3t_processing.count_trajectories_area import CountTrajectoriesArea
from fvh3t.fvh3t_processing.count_trajectories_gate import CountTrajectoriesGate
from fvh3t.fvh3t_processing.export_to_json import ExportToJSON


class TTTProvider(QgsProcessingProvider):
    def __init__(self) -> None:
        super().__init__()

        self._id = "traffic_trajectory_toolkit"
        self._name = "Traffic trajectory toolkit"

    def id(self) -> str:
        """The ID of your plugin, used to identify the provider.

        This string should be a unique, short, character only string,
        eg "qgis" or "gdal". This string should not be localised.
        """
        return self._id

    def name(self) -> str:
        """
        The display name of your plugin in Processing.

        This string should be as short as possible and localised.
        """
        return self._name

    def load(self) -> bool:
        self.refreshAlgorithms()
        return True

    def icon(self):
        """
        Returns a QIcon which is used for your provider inside the Processing toolbox.
        """
        return QgsProcessingProvider.icon(self)

    def loadAlgorithms(self) -> None:  # noqa N802
        """
        Adds individual processing algorithms to the provider.
        """
        self.addAlgorithm(CountTrajectoriesGate())
        self.addAlgorithm(CountTrajectoriesArea())
        self.addAlgorithm(ExportToJSON())
