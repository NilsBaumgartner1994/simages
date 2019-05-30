# -*- coding: utf-8 -*-

from .dataset import PILDataset, SingleFolderDataset
from .models import BasicAutoencoder
from .embeddings import Embeddings
from .extractor import EmbeddingExtractor
from .main import find_duplicates

__version__ = "19.0.0.dev3"

__title__ = "simages"
__description__ = "Find similar images in a dataset"
__url__ = "https://github.com/justinshenk/simages"
__uri__ = __url__
__doc__ = __description__ + " <" + __url__ + ">"

__author__ = "Justin Shenk"
__email__ = "shenkjustin@gmail.com"

__license__ = "MIT"
__copyright__ = "Copyright (c) 2019 " + __author__

__all__ = [
    "Embeddings",
    "EmbeddingExtractor",
    "find_duplicates",
    "PILDataset",
    "SingleFolderDataset",
    "BasicAutoencoder",
]
