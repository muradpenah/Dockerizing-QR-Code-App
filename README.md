Comprehensive Guide to Dockerizing a QR Code Generator and Decoder Project
This document details every step of building, configuring, and running a Python project within a Docker container. It includes a complete explanation of Docker's benefits, step-by-step implementation, and practical applications of the project.
Why Use Docker for This Project?
1. Isolation and Dependency Management
•	Avoid conflicts between the Python environment of your machine and project requirements.
•	Guarantee that the application will run consistently across different systems by packaging all dependencies.
2. Portability and Scalability
•	Once a Docker image is created, the project can be easily shared and executed on other machines, servers, or cloud environments.
•	Docker containers provide scalability by allowing multiple containers to run simultaneously.
3. Automatic Restart and Persistent State
•	Using Docker's --restart always feature ensures the container restarts after system reboots, providing constant availability.

Project Overview
The project consists of a Python application that can:
1.	Generate QR codes in PNG and PDF formats.
2.	Decode QR codes from images stored in a shared input folder.
3.	Maintain persistent state by using local folders (input/ and output/) mounted to the container.

Using Environment
       Ubuntu 24.04.1 LTS

Detailed Implementation Steps
1. Create the Project Structure
Set up the project folder with the following structure:
project/
├── app.py              # Python application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Configuration file for Docker image
├── input/              # Folder to store QR code images for decoding
└── output/             # Folder to store generated QR codes
Commands to Set Up Project Structure
mkdir my-python-project
cd my-python-project
mkdir input output

2. Write the Python Application
2.1 app.py - Python Code
This is the main application that handles QR code generation and decoding.
2.2 requirements.txt - Python Dependencies
List all required libraries for the project:

3. Create the Dockerfile
3.1 Dockerfile
The Dockerfile defines the instructions to build the Docker image for this project.

4. Build and Run the Docker Container
4.1 Build the Docker Image
Run the following command to build the Docker image:
docker build -t qr-code-app .
4.2 Run the Docker Container
Run the container with input and output folders mounted for persistence:
docker run -dit --restart always \
  -v "$(pwd)/input:/input" \
  -v "$(pwd)/output:/output" \
  --name qr-code-app qr-code-app

5. Testing the Application
5.1 Accessing the Container
To access the running container:
docker exec -it qr-code-app bash
5.2 Running the Application
Run the Python application inside the container:
python app.py
5.3 Generate QR Code
•	Enter the data to encode.
•	Provide a file name (e.g., example).
•	The generated PNG will be moved to input/ and the PDF will be saved in output/.
5.4 Decode QR Code
•	Select an available file from the input/ folder.
•	View the decoded data.
5.5 Additionally Using Aliases
• To configure ~/.bashrc file :
vi ~/.bashrc
alias start-app='sudo docker exec -it qr-code-app bash'
source ~/.bashrc

• And start app:
start-app
 


Conclusion
This project demonstrates the effective use of Docker for isolating and deploying a Python application. By combining Docker's portability with Python's flexibility, you have built a robust and reusable QR code generator and decoder.


