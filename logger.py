import logging
import pathlib

pathlib.Path('./logs').mkdir(parents=False, exist_ok=True)

tags_inspector_log = logging.getLogger('tags_inspector')
check_presence_log = logging.getLogger('check_presence')

tags_inspector_log.setLevel(logging.INFO)
check_presence_log.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

tags_inspector_log_handler = logging.FileHandler('logs/tags_inspector.log')
tags_inspector_log_handler.setLevel(logging.INFO)
tags_inspector_log_handler.setFormatter(formatter)

check_presence_log_handler = logging.FileHandler('logs/check_presence.log')
check_presence_log_handler.setLevel(logging.INFO)
check_presence_log_handler.setFormatter(formatter)

tags_inspector_log.addHandler(tags_inspector_log_handler)
check_presence_log.addHandler(check_presence_log_handler)
