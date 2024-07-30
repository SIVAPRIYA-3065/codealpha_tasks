# File Organizer Application

This is a File Organizer application built using Kivy and KivyMD. It helps you organize files in a selected directory into subfolders based on their file types (e.g., Images, Documents, Music, Videos, Archives). Additionally, it supports automated file organization at regular intervals.

## Features

- **Select Directory**: Choose the directory you want to organize.
- **Organize Files**: Manually organize files in the selected directory.
- **Set Interval**: Specify the interval (in minutes) for automated file organization.
- **Start Auto-Organize**: Begin the automated file organization process.
- **Stop Auto-Organize**: Stop the automated file organization process.
- **Status Updates**: Real-time updates on the current status of the application.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/SIVAPRIYA-3065/codealpha_tasks.git
    cd Task Automation
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python main.py
    ```

2. **Select Directory**: Click "Select Directory" to choose the folder you want to organize.

3. **Organize Files**: Click "Organize Files" to manually organize files in the selected directory. The status will update to show the current process.

4. **Set Interval**: Enter the interval (in minutes) in the text field.

5. **Start Auto-Organize**: Click "Start Auto-Organize" to begin the background process of organizing files at the specified interval. The status will update to show that auto-organize is running.

6. **Stop Auto-Organize**: Click "Stop Auto-Organize" to halt the background process. The status will update to show that the process is idle.

## Background Process

The application uses the `schedule` library to handle automated file organization at regular intervals. A separate thread is used to run the scheduling loop so that the main thread remains responsive to user interactions. 

### How It Works:

- **Organize Files**: This function categorizes files in the selected directory into subfolders based on their file types.
- **Auto-Organize**: When started, this function runs a background process that organizes files at the specified interval (default is every 10 minutes).

### Updating Status:

- The application uses Kivy's `Clock` to schedule status updates on the main thread, ensuring that the UI reflects the current state of the application.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Kivy](https://kivy.org/)
- [KivyMD](https://kivymd.readthedocs.io/)
- [schedule](https://schedule.readthedocs.io/)
