# -*- coding: utf-8 -*-
#
from __future__ import print_function

from betterbib.__about__ import (
    __version__,
    __author__,
    __author_email__,
    __website__,
    )

from betterbib.tools import (
    create_dict,
    decode,
    pybtex_to_dict,
    pybtex_to_bibtex_string,
    write,
    update,
    JournalNameUpdater,
    )
from betterbib.crossref import Crossref
from betterbib.dblp import Dblp

try:
    import pipdate
except ImportError:
    pass
else:
    if pipdate.needs_checking(__name__):
        print(pipdate.check(__name__, __version__))
