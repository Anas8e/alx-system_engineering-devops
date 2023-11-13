# 0x19. Postmortem - My First Outage

## Issue Summary

**⏰ Duration:** November 9, 2023, 8:00 PM - November 10, 2023, 2:00 AM (UTC)

**💥 Impact:**
- The authentication service took a power nap for 2 hours.
- Users played hide-and-seek with their login credentials, affecting approximately 20% of our user base.

**🕵️‍♂️ Root Cause:** 
The authentication microservice decided it needed a timeout from the relentless authentication attempts, causing a service disco dance party.

## Timeline

- **🔍 Detection Time:** November 9, 2023, 8:00 PM (UTC)
- **🕵️‍♀️ Detection Method:** Monitoring alert went wild due to a spike in failed authentication attempts.
- **🚀 Actions Taken:**
  - Investigated authentication service logs - Sherlock style - and found the culprit.
  - Blamed it on a ghost in the machine and summoned the network team to perform an exorcism on our infrastructure.
- **🚧 Misleading Paths:**
  - Initially suspected a database rebellion, but turns out, it was just a microservice having a timeout tantrum.
  - Considered the possibility of a DDoS attack, but it was just our servers doing the electric slide.
- **🚨 Escalation:**
  - Incident escalated to the DevOps and SysAdmin teams, who brought their detective hats and magnifying glasses.
- **🎉 Resolution:**
  - Applied a magical spell (updated the microservice configuration).
  - Cast the spell (deployed the updated configuration).
  - Held a wizard council meeting (monitored the service) before declaring peace in the realm.

## Root Cause and Resolution

- **🤔 Root Cause Explanation:**
  - The authentication microservice had a timeout setting that needed a timeout itself, causing connections to go on a coffee break.
- **✨ Resolution Details:**
  - Adjusted the microservice configuration timeout settings, reminding it that breaks are for coffee, not services.
  - Conducted a thorough testing spell to ensure the issue was vanquished.

## Corrective and Preventative Measures

- **🔧 Improvements/Fixes:**
  - Implemented a daily standup for microservices to discuss their feelings and prevent timeouts.
  - Gave our monitoring system a personality makeover to detect anomalies with more flair.
- **📋 Specific Tasks:**
  - Scheduled weekly therapy sessions for microservices configurations.
  - Organized a dance-off for the authentication service to keep it on its toes.
  - Enrolled the microservices in a timeout management course.

---

**🎭 In Conclusion:**
This outage wasn't your typical tech drama; it was a saga of timeouts, misconfigurations, and a dash of magic. As we move forward, we pledge to keep our services entertained, well-configured, and always ready for the next adventure.

**🙏 Manual QA Review Request:**
I kindly request a manual QA review from my peers before the project deadline.

**🌐 URLs:**
- [GitHub Repository](https://github.com/Anas8e/alx-system_engineering-devops/tree/main/0x19-postmortem)
- [Postmortem Document](https://github.com/Anas8e/alx-system_engineering-devops/blob/main/0x19-postmortem/README.md)
