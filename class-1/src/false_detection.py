import re
from logger import logger

CHEAP = re.compile(r"(select|union|%27|%3Cscript%3E|<script)", re.I)
SQLI = re.compile(r"\bunion\s+select\b|(?:'|%27)\s*or\s*1=1", re.I)
XSS  = re.compile(r"(<script\b|javascript:|on\w+=)", re.I)

sus = []
with open("class-1/data/access.log","r",encoding="utf-8",errors="ignore") as f:
    for line in f:
        if not CHEAP.search(line):
            continue
        if SQLI.search(line) or XSS.search(line):
            sus.append(line.strip())

# print("Suspicious lines:", len(sus))
# print(sus)
logger.info("Suspicious lines:", len(sus))
