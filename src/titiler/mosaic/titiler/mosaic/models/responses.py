"""TiTiler.mosaic response models."""

from typing import List, Optional, Tuple

from pydantic import BaseModel


class Point(BaseModel):
    """
    Point model.

    response model for `/point` endpoints

    """

    coordinates: List[float]
    values: List[Tuple[str, List[Optional[float]], List[str]]]
