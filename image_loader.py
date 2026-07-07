import os
from collections.abc import Sequence

from PIL import Image, ImageTk


class LazyImageList(Sequence):
    """List-like image collection that creates PhotoImages on first access."""

    def __init__(self, path, suffix):
        self.path = path
        self.suffix = suffix.lower()
        self.filenames = [
            filename
            for filename in sorted(os.listdir(path), key=str.lower)
            if filename.lower().endswith(self.suffix)
        ]
        self._cache = {}

    def __len__(self):
        return len(self.filenames)

    def __iter__(self):
        for index in range(len(self.filenames)):
            yield self[index]

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [self[i] for i in range(*index.indices(len(self)))]

        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise IndexError("image index out of range")

        if index not in self._cache:
            image_path = os.path.join(self.path, self.filenames[index])
            with Image.open(image_path) as image:
                self._cache[index] = ImageTk.PhotoImage(image.copy())
        return self._cache[index]

    @property
    def loaded_count(self):
        return len(self._cache)
