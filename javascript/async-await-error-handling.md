# Handling Unhandled Promise Rejections in Async/Await

**Date:** 2026-11-16  
**Tags:** `javascript`, `async`, `error-handling`

## 🚨 The Problem
An API call failed due to a network timeout, causing the Node.js process to crash with an `UnhandledPromiseRejection` warning instead of returning a graceful error message to the user.

## 🔍 Root Cause
Using `await` without wrapping the asynchronous call in a `try/catch` block leaves rejected promises uncaught.

## ✅ The Solution

### ❌ Before (Buggy)
```javascript
async function fetchUserData(userId) {
  const response = await fetch(`https://example.com{userId}`);
  const data = await response.json();
  return data;
}
```

### ✔️ After (Fixed)
```javascript
async function fetchUserData(userId) {
  try {
    const response = await fetch(`https://example.com{userId}`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Failed to fetch user data:", error.message);
    return null;
  }
}
```

## 💡 Key Takeaway
Always wrap `await` operations in `try/catch` blocks and explicitly check `response.ok` when using the Fetch API.
