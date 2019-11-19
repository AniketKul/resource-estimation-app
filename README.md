# Problem Statement

Your team is moving from two corporate data centers to a public cloud provider. You have picked up the following User Story from the team's backlog:

### User Story

As a DevOps Engineer, I need to know how many applications we are hosting in our two corporate data centers so the team can start planning the migration to AWS

### Acceptance Criteria:
* Data must be pulled from Excel file embedded in this GitHub repo, hardware.xlsx.
* Data must be parsed using either Go (preferred) or Python.
* Application/script should generate a list of all departments that have hardware hosted.
* Application/script should generate a list of all the applications for each department.
* Application/script should calculate the number of CPUs and memory used by each department.
* Application/script should calculate the number of CPUs and memory used by each application.
* Application/script should calculate the number of CPUs and memory used in each of the data centers.
* Application/script should be completed by sending a pull request to the master branch.
