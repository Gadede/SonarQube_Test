"""
SonarQube Python Security & Quality Test File
Contains intentional issues for scanner detection.
"""

import os
import sys
import subprocess
import hashlib
import pickle
import yaml
import sqlite3
import tempfile


# ─── SECURITY VULNERABILITIES ───────────────────────────────────────

# SONAR ISSUE: Hardcoded credentials (Critical)
DATABASE_PASSWORD = "admin1234"
SECRET_KEY = "hardcoded-jwt-secret-do-not-use"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

# SONAR ISSUE: SQL Injection vulnerability
def get_user(username):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # Dangerous: user input directly in query
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)  # SQL Injection!
    return cursor.fetchall()

# SONAR ISSUE: Command injection via shell=True
def run_command(user_input):
    # Dangerous: user_input passed directly to shell
    subprocess.call("ls " + user_input, shell=True)  # Command Injection!

# SONAR ISSUE: Insecure deserialization
def load_user_data(data):
    return pickle.loads(data)  # Arbitrary code execution risk

# SONAR ISSUE: Path traversal vulnerability
def read_file(filename):
    base_dir = "/var/app/files/"
    # No sanitization — attacker can use ../../etc/passwd
    with open(base_dir + filename, "r") as f:
        return f.read()

# SONAR ISSUE: Weak hashing algorithm (MD5 for passwords)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # MD5 is broken!

# SONAR ISSUE: Weak hashing algorithm (SHA1)
def hash_token(token):
    return hashlib.sha1(token.encode()).hexdigest()  # SHA1 is weak!

# SONAR ISSUE: YAML deserialization with full load (code execution risk)
def parse_config(yaml_string):
    return yaml.load(yaml_string)  # Should be yaml.safe_load()

# SONAR ISSUE: Insecure temp file creation
def write_temp(data):
    tmp = tempfile.mktemp()  # Race condition — use mkstemp() instead
    with open(tmp, "w") as f:
        f.write(data)
    return tmp

# SONAR ISSUE: Binding to all interfaces (0.0.0.0) — overly permissive
def start_server():
    import socket
    s = socket.socket()
    s.bind(("0.0.0.0", 8080))  # Should bind to specific interface


# ─── CODE QUALITY ISSUES ────────────────────────────────────────────

# SONAR ISSUE: Bare except (catches everything including SystemExit)
def risky_parse(data):
    try:
        return int(data)
    except:  # Should be: except ValueError:
        pass  # SONAR ISSUE: Empty except block

# SONAR ISSUE: Unused imports (sys, os used nowhere meaningful)
def unused_imports_example():
    pass

# SONAR ISSUE: Function with too many parameters (> 7)
def create_user(first_name, last_name, email, password, age, address, city, country, phone, zip_code):
    pass

# SONAR ISSUE: Mutable default argument (classic Python bug)
def append_item(item, lst=[]):
    lst.append(item)  # Shared across all calls!
    return lst

# SONAR ISSUE: Cognitive complexity too high
def complex_function(a, b, c, d):
    result = 0
    if a > 0:
        if b > 0:
            for i in range(a):
                if i % 2 == 0:
                    if c:
                        while d > 0:
                            result += i
                            d -= 1
                        if result > 100:
                            for j in range(result):
                                result -= j
    return result

# SONAR ISSUE: Duplicate code
def calculate_area_circle(radius):
    pi = 3.14159
    area = pi * radius * radius
    print("Calculating area...")
    return area

def calculate_area_circle_v2(radius):
    # Exact duplicate — should reuse calculate_area_circle
    pi = 3.14159
    area = pi * radius * radius
    print("Calculating area...")
    return area

# SONAR ISSUE: print() used instead of logging
def process_order(order_id):
    print(f"Processing order {order_id}")   # Use logging module instead
    print("Order complete")

# SONAR ISSUE: Magic numbers (unexplained literals)
def calculate_salary(hours):
    return hours * 23.75 * 52 * 0.79  # What do these numbers mean?

# SONAR ISSUE: Variable assigned but never used
def dead_variable():
    x = expensive_computation()
    result = 42  # x is never used after assignment
    return result

def expensive_computation():
    return sum(range(10000))

# SONAR ISSUE: assert used for input validation (disabled with -O flag)
def withdraw(amount):
    assert amount > 0, "Amount must be positive"  # Use if/raise instead
    return amount

# SONAR ISSUE: Using == to compare with None (should use 'is')
def check_none(value):
    if value == None:   # Should be: if value is None:
        return True
    if value != None:   # Should be: if value is not None:
        return False

# SONAR ISSUE: __eq__ defined without __hash__
class UserProfile:
    def __init__(self, user_id):
        self.user_id = user_id

    def __eq__(self, other):
        return self.user_id == other.user_id
    # Missing __hash__ — makes object unhashable in sets/dicts
