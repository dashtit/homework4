import re


def fix_duplicates(sentence):
    return re.sub(r'\b(\w+)\b\s+\b\1\b', r'\1', sentence)
