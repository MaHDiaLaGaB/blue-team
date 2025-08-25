import re

IPV4 = re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d{1,2})\.){3}(?:25[0-5]|2[0-4]\d|1?\d{1,2})\b")
DOMAIN = re.compile(r"\b(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+(?:[a-z]{2,})\b", re.I)
URL = re.compile(r"https?://[^\s\"'<>]+", re.I)
EMAIL = re.compile(r"\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b", re.I)
MD5 = re.compile(r"\b[a-f0-9]{32}\b", re.I)
SHA256 = re.compile(r"\b[a-f0-9]{64}\b", re.I)


text = """User 203.0.113.5 fetched http://evil.example/mal.js (md5=a94a8fe5ccb19ba61c4c0873d391e987) contact: sec@corp.example"""

# print("IPs:", IPV4.findall(text))
# print("URLs:", URL.findall(text))
# print("Domains:", DOMAIN.findall(text))
# print("Emails:", EMAIL.findall(text))
# print("MD5:", MD5.findall(text))

APACHE = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<ts>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) (?P<proto>[^"]+)" (?P<status>\d{3}) (?P<size>\S+)'
)

apache_text = '198.51.100.10 - - [11/Aug/2025:12:01:00 +0000] "GET /?q=%3Cscript%3E HTTP/1.1" 200 512'

m = APACHE.search(apache_text)
# print(m.groupdict() if m else None)

SQLI = re.compile(r"(?:\bunion\b\s+\bselect\b|(?:'|%27)\s*or\s*1=1)", re.I)
XSS  = re.compile(r"(<script\b|javascript:|onerror\s*=)", re.I)

payloads = [
  "GET /item?id=1 UNION SELECT username,password FROM users",
  "GET /?q=<script>alert(1)</script>",
  "GET /?u=admin'%20OR%201=1--"
]
for p in payloads:
    print(p, "SQLi?" , bool(SQLI.search(p)), "XSS?", bool(XSS.search(p)))