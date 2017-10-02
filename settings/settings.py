from __future__ import absolute_import


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from core import language_pack
    else:
    	from ..core import language_pack

