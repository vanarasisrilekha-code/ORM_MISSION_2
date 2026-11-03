-- CohortAi Labs | Users and Missions training database
-- Run as an authorized MySQL administrator. CHANGE the sample password.
-- Classroom-only DDL rights below are needed for init_db.py.
CREATE DATABASE IF NOT EXISTS cohortai_missions
  CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

CREATE USER IF NOT EXISTS 'cohort_student'@'localhost'
  IDENTIFIED BY 'CHANGE_THIS_TO_A_STRONG_LOCAL_PASSWORD';

GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, INDEX, REFERENCES
  ON cohortai_missions.* TO 'cohort_student'@'localhost';

-- Admin check: SHOW GRANTS FOR 'cohort_student'@'localhost';
-- After initial table setup, least-privilege apps should remove DDL rights:
-- REVOKE CREATE, ALTER, INDEX, REFERENCES ON cohortai_missions.*
-- FROM 'cohort_student'@'localhost';
