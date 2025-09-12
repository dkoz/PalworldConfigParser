import re

ValidationRules = {
    "Numeric": lambda v: v.isdigit() and int(v) >= 0,
    "Floating": lambda v: re.match(r'^\d+\.\d+$', v) is not None,
    "TrueFalse": lambda v: v in ["True", "False"],
    "String": lambda v: True,
    "AlphaDash": lambda v: re.match(r'^[a-zA-Z0-9_-]+$', v) is not None,
}
