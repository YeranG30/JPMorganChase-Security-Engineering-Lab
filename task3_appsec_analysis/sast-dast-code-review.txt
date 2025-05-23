# task 3 – appsec static analysis lab

## overview

this task simulates a static application security test (sast) on a vulnerable flask web application. the objective is to identify insecure coding practices and recommend mitigations, reflecting real-world appsec workflows.

## objectives

- perform static code analysis to uncover security vulnerabilities
- document findings and propose remediation strategies
- understand common web application security flaws and their implications

## tools & technologies

- python
- flask
- manual code review
- markdown for documentation

## identified vulnerabilities

1. **hardcoded credentials**
   - storing plaintext credentials within source code poses a significant security risk.
   - *recommendation*: utilize environment variables or secure credential storage solutions.

2. **insecure password handling**
   - passwords are compared in plaintext without hashing, making them susceptible to interception.
   - *recommendation*: implement secure hashing algorithms like bcrypt or argon2 for password storage and verification.

3. **path traversal vulnerability**
   - user-supplied filenames are used directly in file paths without validation, leading to potential path traversal attacks.
   - *recommendation*: sanitize filenames using functions like `secure_filename()` from werkzeug and validate file paths.

4. **lack of input validation**
   - absence of input validation can lead to various injection attacks.
   - *recommendation*: implement comprehensive input validation and sanitization for all user inputs.

## recommendations

- **implement secure authentication mechanisms**
  - avoid hardcoded credentials; use secure authentication services or protocols.
  - hash and salt passwords before storage.

- **sanitize and validate all user inputs**
  - employ input validation libraries or frameworks to prevent injection attacks.

- **secure file handling**
  - validate and sanitize file names and paths.
  - restrict file upload directories and set appropriate permissions.

- **integrate security tools into the development lifecycle**
  - use static analysis tools like bandit or semgrep to detect vulnerabilities early.
  - incorporate security checks into continuous integration/continuous deployment (ci/cd) pipelines.

## conclusion

this exercise highlights the importance of secure coding practices and the need for regular code reviews to identify and mitigate potential security risks. by addressing the identified vulnerabilities, developers can enhance the security posture of web applications and protect against common attack vectors.

