import importlib.metadata

try:
    __version__ = importlib.metadata.version('gorqflow')
except importlib.metadata.PackageNotFoundError:
    __version__ = 'unknown'