---
icon: rectangle-terminal
---

# The role of commands/

The **commands/** folder is useful for reusable prompt workflows.

These are not automatic like hooks. Instead, they package tasks you or your team run repeatedly, such as:

* Reviewing a pull request
* Writing missing tests
* Summarizing changes for release notes
* Debugging a reported issue
* Drafting migration steps

The value of **commands/** is that it reduces repeated prompting. Instead of rewriting the same instruction every time, you store that workflow once in a clear place.

For example:

```
.claude/
└── commands/
    ├── review-pr.md
    ├── fix-bug.md
    ├── write-tests.md
    └── prepare-release-notes.md
```

Each file should have one obvious purpose. That is the key to efficiency.

#### A practical command example <a href="#fe15" id="fe15"></a>

Suppose your team often asks Claude to review backend changes before merging. Instead of writing a fresh prompt each time, you create:

```
# review-pr

Review the current changes with a focus on:
- correctness
- missing edge cases
- API contract changes
- test coverage gaps
Summarize:
1. critical issues
2. medium-risk issues
3. suggested improvements
```

Saved as:

```
.claude/
└── commands/
    └── review-pr.md
```

That immediately makes the workflow easier to reuse and easier to improve over time.

<br>
