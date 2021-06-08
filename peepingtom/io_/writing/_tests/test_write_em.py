import numpy as np

from peepingtom.io_.writing.em import write_em
from peepingtom.datablocks import ImageBlock


def test_write_em(tmp_path):
    file_path = tmp_path / 'test.em'
    imageblock = ImageBlock(data=np.ones((3, 3, 3)))
    write_em(imageblock, str(file_path))
