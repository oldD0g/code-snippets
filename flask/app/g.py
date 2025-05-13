"""

  This is g.py for sharing global objects across the modules in this app.

"""

from app.srx import SRXConfig

my_config = None # This holds the SRXConfig Class object
srx_json = "" # This holds the JSON itself retrieved from the file

