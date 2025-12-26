from importlib import metadata

from terminus.core.cache import cache_manager
from terminus.interface.custom.custom_component import CustomComponent

# from terminus.processing.process import load_flow_from_json  # noqa: E402

try:
    # 通过ci去自动修改
    __version__ = '2.3.0-beta3'
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ''
del metadata  # optional, avoids polluting the results of dir(__package__)

__all__ = ['cache_manager', 'CustomComponent']
