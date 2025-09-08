# Student_Complaint_Portal
A web-based grievance redressal system developed as part of the BCA mini-project. The portal provides students with a convenient way to register complaints online, while enabling administrators to view and manage them effectively.

Features:
1. Complaint Submission – Students can submit complaints with details like name, ID, department, year, contact info, and issue description.
2. Acknowledgment System – Displays confirmation after a successful submission.
3. Complaint Management – Stores complaints in structured format (currently in-memory).
4. Admin View – Displays all submitted complaints in a tabular format for administrators.
5. Responsive Frontend – Clean and accessible UI with HTML & CSS.

System Architecture:
1.Student submits complaint via web form.
2. Flask backend validates and stores data.
3. System provides acknowledgment.
4. Administrator reviews complaints in the admin panel.

Tech Stack:
1. Frontend: HTML, CSS
2. Backend: Python (Flask Framework)
3. Database: In-memory (future scope – SQLite/MySQL)
4. IDLE
5. Supported OS: Windows, Linux, Mac

Future Scope:
1. Database integration (SQLite/MySQL) for persistent storage.
2. Email/SMS notification system.
3. Complaint categorization & priority handling.
4. Analytics dashboard for administrators.
5. Secure login for students and admins.
6. Mobile application (Android/iOS).
