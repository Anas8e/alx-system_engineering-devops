# 0x19. Postmortem - My First Outage

## Issue Summary

**Duration:** November 9, 2023, 8:00 PM - November 10, 2023, 2:00 AM (UTC)

**Impact:**
- The authentication service was down for 2 hours.
- Users experienced login failures, affecting approximately 20% of our user base.

**Root Cause:** 
A misconfiguration in the authentication microservice resulted in a connection timeout, causing service unavailability.

## Timeline

- **Detection Time:** November 9, 2023, 8:00 PM (UTC)
- **Detection Method:** Monitoring alert triggered due to a spike in failed authentication attempts.
- **Actions Taken:**
  - Investigated authentication service logs and identified the source of the connection timeout.
  - Assumed it might be a network issue and checked network configurations.
  - Engaged the network team to validate network infrastructure.
- **Misleading Paths:**
  - Initially suspected a database issue, leading to unnecessary database server checks.
  - Explored the possibility of a DDoS attack, which diverted attention from the actual misconfiguration.
- **Escalation:**
  - Incident escalated to the DevOps and SysAdmin teams for collaboration.
- **Resolution:**
  - Corrected the misconfiguration in the authentication microservice.
  - Deployed the updated configuration.
  - Monitored the service for stability before confirming the resolution.

## Root Cause and Resolution

- **Root Cause Explanation:**
  - The authentication microservice had an incorrect timeout setting, causing connections to fail prematurely.
- **Resolution Details:**
  - Updated the authentication microservice configuration to adjust the timeout.
  - Conducted thorough testing to ensure the issue was resolved.
  
## Corrective and Preventative Measures

- **Improvements/Fixes:**
  - Implement regular configuration audits to identify and rectify potential misconfigurations.
  - Enhance monitoring for critical services to detect anomalies promptly.
- **Specific Tasks:**
  - Establish a recurring audit schedule for microservice configurations.
  - Enhance monitoring alerts for authentication service health.
  - Implement automated testing for critical microservice configurations.
  
---

**In Conclusion:**
This outage provided a valuable lesson in the importance of precise configuration management and the need for vigilant monitoring. Moving forward, we commit to proactive measures to prevent similar incidents. Our corrective actions aim to fortify our system against misconfigurations and enhance our ability to detect and respond to potential issues swiftly.

**Manual QA Review Request:**
I kindly request a manual QA review from my peers before the project deadline.

**URLs:**
- [GitHub Repository](https://github.com/Anas8e/alx-system_engineering-devops/tree/main/0x19-postmortem)
- [Postmortem Document](https://github.com/Anas8e/alx-system_engineering-devops/blob/main/0x19-postmortem/README.md)
