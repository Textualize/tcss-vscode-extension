template = r"""
"{style}-rule": {{
    "begin": "\\s*({style})\\s*:\\s*",
    "end": "\\s*;",
    "patterns": [
        {{
            "match": "{values}",
            "name": "comment"
        }},
        {{ "include": "#invalid-value" }}
    ],
    "beginCaptures": {{
        "1": {{ "name": "keyword" }}
    }}
}},"""


def make_rule(style, options):
    return template.format(style=style, values="|".join(options))
