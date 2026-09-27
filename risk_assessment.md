# Risk Assessment

## 1. Assets, Vulnerabilities and Consequences

| Asset | Vulnerability | Consequence |
|---|---|---|
| Student records server | Guest network access | Unauthorized access to student records |
| Staff accounts | Weak passwords | Account compromise |
| File-transfer system | Unencrypted transfers | Data interception |

## 2. Risk Ranking

| Risk | Likelihood | Impact | Reason |
|---|---|---|---|
| Guest access | High | High | Guests can reach sensitive records |
| Weak passwords | High | High | Passwords can be guessed |
| Unencrypted transfers | Medium | High | Data can be intercepted |

## 3. Recommended Controls

- Guest access: Use firewall rules and network segmentation.
- Weak passwords: Enforce a strong password policy.
- Unencrypted transfers: Use SFTP.
