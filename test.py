
from rclog import set_log, get_log

config = {
    "handlers": ["console"],
    "console_class": "Console"
}
set_log.from_dict(config)
get_log().info("Hello, world!")
