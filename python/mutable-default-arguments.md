# Avoiding Mutable Default Arguments in Python Functions

**Date:** 2026-11-16  
**Tags:** `python`, `functions`, `memory`

## 🚨 The Problem
Calling a function multiple times without passing the optional list argument caused items from previous function calls to persist in the list.

## 🔍 Root Cause
In Python, default argument values are evaluated only once when the function is defined, not each time the function is called. If the default is a mutable object (like a `list` or `dict`), it is shared across all calls.

## ✅ The Solution

### ❌ Before (Buggy)
```python
def add_task(task_name, task_list=[]):
    task_list.append(task_name)
    return task_list

print(add_task("Write tests")) # ['Write tests']
print(add_task("Fix bug"))     # ['Write tests', 'Fix bug'] -> Unexpected!
```

### ✔️ After (Fixed)
```python
def add_task(task_name, task_list=None):
    if task_list is None:
        task_list = []
    task_list.append(task_name)
    return task_list

print(add_task("Write tests")) # ['Write tests']
print(add_task("Fix bug"))     # ['Fix bug']
```

## 💡 Key Takeaway
Never use mutable objects like `[]` or `{}` as default function parameters in Python; always default to `None` and initialize inside the function body.
