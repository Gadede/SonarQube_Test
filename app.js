// SonarQube JavaScript Security & Quality Test File

// ─── SECURITY ISSUES ────────────────────────────────────────────────

// SONAR ISSUE: Hardcoded credentials (Critical Security Hotspot)
const API_KEY = "sk-prod-abc123secretkey9999";
const DB_PASSWORD = "SuperSecret@2024!";
const AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY";

// SONAR ISSUE: XSS vulnerability - innerHTML with user-controlled data
function displayUserInput() {
  const userInput = document.location.hash;
  document.getElementById("output").innerHTML = userInput; // Dangerous!
}

// SONAR ISSUE: eval() usage (code injection risk)
function calculate(expression) {
  return eval(expression); // Never use eval with user input
}

// SONAR ISSUE: document.write() usage
function writeToPage(data) {
  document.write(data); // Overrides entire document, XSS risk
}

// SONAR ISSUE: Insecure use of postMessage without origin check
window.addEventListener("message", function(event) {
  // Missing: if (event.origin !== "https://trusted.com") return;
  document.getElementById("output").innerHTML = event.data;
});

// SONAR ISSUE: Weak random number used for security purpose
function generateToken() {
  return Math.random().toString(36).substr(2); // Not cryptographically secure
}

// SONAR ISSUE: SQL-like string concatenation (pattern SonarQube flags)
function buildQuery(userId) {
  return "SELECT * FROM users WHERE id = " + userId; // SQL Injection pattern
}

// ─── CODE QUALITY ISSUES ────────────────────────────────────────────

// SONAR ISSUE: Unused variable
var unusedVariable = "I am never used";

// SONAR ISSUE: var instead of let/const
var globalCounter = 0;

// SONAR ISSUE: == instead of === (type coercion bug risk)
function checkLogin(input) {
  if (input == 0) {       // Should be ===
    console.log("Zero!");
  }
  if (input == false) {   // Should be ===
    console.log("Falsy!");
  }
}

// SONAR ISSUE: Empty catch block (swallowing errors silently)
function riskyOperation() {
  try {
    JSON.parse("{ bad json }}}");
  } catch (e) {
    // Doing nothing - error swallowed!
  }
}

// SONAR ISSUE: Function too long / too complex (cognitive complexity)
function doEverything(a, b, c, d, e) {
  if (a) {
    if (b) {
      if (c) {
        if (d) {
          if (e) {
            for (let i = 0; i < 100; i++) {
              if (i % 2 === 0) {
                if (i % 3 === 0) {
                  console.log("fizzbuzz", i);
                } else {
                  console.log("fizz", i);
                }
              } else if (i % 3 === 0) {
                console.log("buzz", i);
              } else {
                console.log(i);
              }
            }
          }
        }
      }
    }
  }
}

// SONAR ISSUE: Duplicate code block
function processUserA(user) {
  console.log("Processing user...");
  let result = user.name.trim().toLowerCase();
  result = result.replace(/[^a-z0-9]/g, "");
  return result;
}

function processUserB(user) {
  // Exact duplicate of processUserA — should be refactored
  console.log("Processing user...");
  let result = user.name.trim().toLowerCase();
  result = result.replace(/[^a-z0-9]/g, "");
  return result;
}

// SONAR ISSUE: console.log left in production code
function login() {
  console.log("User is logging in");        // Should be removed
  console.log("Password entered by user");  // Sensitive data log
}

// SONAR ISSUE: Returning different types from same function
function getValue(flag) {
  if (flag) {
    return 42;
  } else {
    return "forty-two"; // Inconsistent return type
  }
}

// SONAR ISSUE: Dead code after return
function deadCode() {
  return true;
  console.log("This will never run"); // Unreachable code
}

// SONAR ISSUE: Promise with no error handling / no .catch()
function fetchData() {
  fetch("https://api.example.com/data")
    .then(response => response.json())
    .then(data => console.log(data));
    // Missing: .catch(err => handle error)
}
