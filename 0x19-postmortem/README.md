#0x19. Postmortem








 
##Outage Duration:
Our online education platform experienced an outage from May 7th, 2024, 07:00 GMT, to May 10th, 2024, 12:00 GMT.
Impact: Approximately 80% of our users were affected by this outage, reporting complete downtime. 

##Timeline:
•	7:00 AM GMT: Backend developer encountered the same issue.
•	9:35 AM GMT: Investigation initiated into controller and view inconsistencies.
•	10:40 AM GMT: Suspicions raised concerning the subdomain, a site dependency.
•	10:42 AM GMT: Verification of form field bindings in views conducted.
•	10:45 AM GMT: Controller hash generation scrutinized.
•	10:50 AM GMT: Speculation on password hashing accuracy.
•	11:00 AM GMT: Incident escalated to the backend development team.
•	12:00 PM GMT: Resolution achieved through an update to the  version.

##Root Cause and Resolution: 
The authentication failures stemmed from an outdated version of the subdomain, which caused compatibility issues with hash generation despite valid hashes. Backend developer swiftly addressed this by updating the subdomain to a newer version and reinstalling necessary gems, restoring functionality seamlessly.
##Corrective and Preventative Measures:
1.	Continuous Integration Pipeline: A pipeline has been implemented to validate pull request branches before merging, ensuring build stability.
2.	Monitoring System: Robust monitoring has been established for both database and application servers to promptly detect and address issues.
3.	Test Development: Rigorous testing protocols for new features have been enforced, requiring passage before integration into the deployment branch to prevent future disruptions."


