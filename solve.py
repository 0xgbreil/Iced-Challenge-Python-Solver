#!/usr/bin/env python3
import re
import sys

s = open(sys.argv[1]).read()

# Extract the format string
fmt = re.search(r'\(\s*"([^"]+)"\s*-f', s).group(1)

# Extract the format arguments
args = re.findall(
    r"'([^']*)'",
    s[s.index('-f'):s.index(')).rEPLacE')]
)

# Reconstruct the string
out = fmt.format(*args)

# Remove the known obfuscation
out = out.replace('Cvx', "'").replace("'+'", "")

print("=== Deobfuscated PowerShell ===\n")
print(out)