# SonarQube Test Project

A collection of files with **intentional** security vulnerabilities and code quality issues to test your SonarQube scanner setup.

---

## File Structure

```
sonarqube-test/
├── sonar-project.properties   # SonarQube config
├── static/
│   ├── index.html             # HTML issues
│   ├── style.css              # CSS quality issues
│   └── app.js                 # JavaScript security & quality
├── src/
│   └── app.py                 # Python security & quality
└── tests/
```

---

## Issues by Severity

### 🔴 Critical / Security Vulnerabilities

| File | Issue |
|------|-------|
| `app.py` | SQL Injection via string concatenation |
| `app.py` | Command Injection via `shell=True` |
| `app.py` | Insecure deserialization with `pickle.loads()` |
| `app.py` | Path traversal in file read |
| `app.py` | Weak hashing (MD5, SHA1) for passwords |
| `app.py` | Unsafe YAML load (`yaml.load` vs `yaml.safe_load`) |
| `app.js` | XSS via `innerHTML` with user-controlled data |
| `app.js` | `eval()` usage — code injection risk |
| `app.js` | Hardcoded API keys and secrets |
| `app.py` | Hardcoded credentials and AWS keys |

### 🟠 High / Security Hotspots

| File | Issue |
|------|-------|
| `app.js` | `postMessage` without origin validation |
| `app.js` | Weak random token generation (`Math.random`) |
| `app.py` | Insecure temp file (`mktemp` race condition) |
| `app.py` | Server binding to `0.0.0.0` |
| `index.html` | Form using GET method for passwords |
| `index.html` | `target="_blank"` without `rel="noopener noreferrer"` |
| `index.html` | External script loaded without SRI integrity check |

### 🟡 Medium / Code Smells

| File | Issue |
|------|-------|
| `app.js` | `var` instead of `let`/`const` |
| `app.js` | `==` instead of `===` |
| `app.js` | Empty catch block |
| `app.js` | Dead code after `return` |
| `app.js` | Duplicate code blocks |
| `app.js` | `console.log` left in production code |
| `app.js` | Promise with no `.catch()` |
| `app.py` | Bare `except` clause |
| `app.py` | Mutable default argument `lst=[]` |
| `app.py` | `== None` instead of `is None` |
| `app.py` | Magic numbers without explanation |
| `app.py` | `__eq__` without `__hash__` |
| `app.py` | `assert` for input validation |
| `style.css` | Duplicate selectors |
| `style.css` | Empty CSS rules |
| `style.css` | Overuse of `!important` |
| `style.css` | `transition: all` (performance) |
| `style.css` | Zero values with units (`0px`) |

### 🔵 Info / Maintainability

| File | Issue |
|------|-------|
| `app.js` | Function cognitive complexity too high |
| `app.py` | Function with too many parameters (> 7) |
| `app.py` | `print()` instead of `logging` module |
| `app.py` | Unused variable assignment |
| `index.html` | Missing `lang` on `<html>` tag |
| `index.html` | Inline `onclick` event handlers |

---

## How to Run SonarQube Scan

### Option 1: SonarQube Server
```bash
sonar-scanner \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=your_token_here
```

### Option 2: GitHub Actions
```yaml
- name: SonarQube Scan
  uses: SonarSource/sonarqube-scan-action@master
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
    SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
```

### Option 3: Docker
```bash
docker run \
  --rm \
  -e SONAR_HOST_URL="http://your-sonar-server:9000" \
  -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=sonarqube-test-project" \
  -e SONAR_TOKEN="your_token" \
  -v "$(pwd):/usr/src" \
  sonarsource/sonar-scanner-cli
```

---

> ⚠️ These files contain **intentional vulnerabilities for testing only**. Do NOT use this code in production.
