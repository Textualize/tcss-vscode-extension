# Textual CSS Syntax Highlighter

## Features

Does syntax highlighting for Textual CSS files (files with the extension `.tcss`).

![A view of a highlighted file.](./tcss.png)

It also does highlighting inside `CSS` and `DEFAULT_CSS` class variables in Python files:

![A Python file and a `CSS` class variable highlighted.](./python_injection.png)


## Grammar dependency

This extension uses the grammar `tcss.tmGrammar.json` that is converted from the YAML grammar in the [TCSS TextMate grammar repository](https://github.com/Textualize/tcss-textmate-grammar).
To convert the YAML grammar into this JSON grammar, use

```bash
npx js-yaml ../tcss-textmate-grammar/grammar.yaml > syntaxes/tcss.tmGrammar.json
```

## Release Notes

See the [change log](./CHANGELOG.md).
