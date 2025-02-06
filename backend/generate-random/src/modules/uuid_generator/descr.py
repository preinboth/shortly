from src.config.settings import settings

router_tag = "UUID"
router_summary = f"Generate up to {settings.UUID_QUANTITY_MAX} unique identifiers online, from version 1 to 4, with hash representation and results download. "
router_descr = """
## Generate random Uuids online with Hash and Base64

Versions:
* A = "Version 1: Time-based"
* B = "Version 3 UUIDs based on the MD5 hash of some data."
* C = "Version 4: Random (Recommanded)"
* D = "Custom: Version 4 & 5 md5 of UNIX microtime"
"""
router_response_descr = "the creates uuid"
