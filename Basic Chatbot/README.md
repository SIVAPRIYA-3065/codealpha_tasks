# ChatBot Application

This is a simple ChatBot application built using Kivy and KivyMD. The application includes user authentication (login and registration) using SQLite for user data storage.

## Features

- User Registration
- User Login
- Chatbot Interaction

## Requirements

- Python 3.x
- Kivy
- KivyMD
- SQLite

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chatbot-app.git
   cd chatbot-app
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate    #On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install kivy kivymd
   ```

## Running the Application
Create the SQLite database and user table by running the script
```bash
python chatbot_app.py
```

## Application Structure

- chatbot_app.py: The main application script containing the Kivy and KivyMD code.
- users.db: The SQLite database file for storing user data.

## Usage
- Launch the application:
  ```bash
  python chatbot_app.py
  ```
- Register a new user by providing a username and password.
- Login with the registered username and password.
- Interact with the chatbot by typing messages and clicking "Send".

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
Special thanks to the open-source community and everyone who provided support and guidance during the development of this project.

## Contact
If you have any questions, feel free to reach out:
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/sivapriya-b-3b2a72294/)
- Github: [Github Profile](https://github.com/SIVAPRIYA-3065)
