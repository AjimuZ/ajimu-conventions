# Comment examples

## Module header

Every module states its responsibility in one sentence:

```python
"""Single-writer workspace supervisor with account preflight and durable controls."""
```

## Syntax narration: remove it

```python
# increment the counter by 1
count += 1

# return None if the list is empty
if not items:
    return None
```

These repeat the code and become wrong as soon as the code changes.

## Explaining why

```python
# A supervisor relaunch after a scheduled wait keeps the failure count, so
# the consecutive-error limit still applies across process restarts.
if not args.supervisor:
    state["consecutiveErrors"] = 0
```

The code shows *what* happens. The comment explains *why*, and so stops a later
"simplification" from reintroducing an endless retry loop.

## Contract docstring

```python
def verification_report(ctx):
    """Run the trusted finite checks and explain a failure in usable terms.

    Returns {'ok', 'missing', 'failure'}. `missing` lists tools the environment
    lacks, which no retry can fix; `failure` names the failing command with a
    bounded output tail. Never raises for a failing check; raises OSError only
    when the repository itself is unreadable.
    """
```

It states the return shape, the meaning of each field and the failure behavior,
so callers need not read the body.

## Invariant at a boundary

```javascript
// Polling must never overwrite an unsaved draft: render only when the owner
// has not edited the form since the last save.
if (draftFor === project.id) return;
```
