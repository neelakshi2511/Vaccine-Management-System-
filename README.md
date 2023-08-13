# Vaccine-Management-System-

The Vaccine Management System is a Python-based command-line application designed to manage vaccination records efficiently. The system allows authorized users, including administrators, to perform various tasks such as registering new users, adding vaccination records, displaying records, searching for records, updating records, and deleting records. The system enhances data management and retrieval for vaccination-related activities.

**Features:**

1. **User Authentication:** The system provides a secure login mechanism to ensure that only authorized users can access the application. It differentiates between administrators and non-administrators.

2. **User Registration:** Administrators can register new users by providing their usernames, passwords, and designating whether they should have admin privileges. This feature enhances the system's scalability and access control.

3. **Record Management:**
   - **Add Records:** Users can input vaccination details for individuals, including Aadhar number, name, age, vaccine type, and dose (1st or 2nd).
   - **Display Records:** The system can display all vaccination records in a tabular format using the PrettyTable library, providing an organized view of the data.
   - **Search Records:** Users can search for vaccination records by entering an Aadhar number, and the system retrieves and displays the corresponding record.
   - **Update Records:** Users can update existing vaccination records, modifying details such as Aadhar number, name, age, vaccine type, and dose.
   - **Delete Records:** Records can be deleted based on the provided Aadhar number, ensuring efficient data management.

4. **User Interaction:** The system's user-friendly command-line interface guides users through the available services and prompts for inputs to execute the desired functionality.

**Technologies Used:**

- **Python:** The entire application is developed in Python, making use of its rich libraries and functionalities.
- **Pickle:** The `pickle` library is used to serialize and deserialize data, allowing efficient storage and retrieval of records.
- **PrettyTable:** The `PrettyTable` library is used to create well-formatted and visually appealing tables for displaying records.


**Note:** This project provides a basic command-line interface for managing vaccination records. It can be further extended with additional features, security enhancements, and a graphical user interface (GUI) to provide a more comprehensive solution for vaccine management. 
