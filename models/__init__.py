#!/usr/bin/python3
"""initialize package"""

import FileStorage from models.engine.file_storage

storage = FileStorage()
storage.reload()
