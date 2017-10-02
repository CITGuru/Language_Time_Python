from __future__ import absolute_import
import time


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from core import Time
    else:
    	from ..core import Time


timez = Time.Hausa

print timez.getTime(time)


