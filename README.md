# ScreenSurfer
Python script that opens a specified website in fullscreen mode after detecting inactivity on the user's computer.

## Features
- Detects user inactivity.
- Launches a website in fullscreen after a defined idle period.

## Prerequisites
- **Python Version:** Ensure Python 3.X or later is installed.

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/YourUsername/YourRepo.git
   cd YourRepo

2. Install the required Python libraries:

   ```bash
   Copy code
   pip install -r requirements.txt

## Usage
1. Open a terminal in the project directory.
2. Run the script:

   ```bash
   python screensurfer.py

3. The script will monitor inactivity and open the specified website in fullscreen after the set period.

## Making an Executable (Optional)
If you'd like to distribute ScreenSurfer as a standalone executable, follow these steps:

1. Install PyInstaller: Ensure you have PyInstaller installed in your Python environment:

   ```bash
   pip install pyinstaller
 
2. Create the Executable: Run PyInstaller to package the script into a standalone executable:

   ```bash
   pyinstaller --onefile screensurfer.py

3. Locate the Executable:
   - After the process completes, the executable will be located in the dist folder within your project directory.
   - On Windows, the file will be named screensurfer.exe.

4. Test the Executable:

   - Navigate to the dist folder and double-click the executable (on Windows) or run it from the terminal on macOS/Linux to confirm it works as expected.
   
5. Distribute the Executable:

   - Share the file with others. Be aware of the following platform-specific considerations:

      - On Windows: Share the .exe file.
      - On macOS/Linux: Ensure the executable permissions are set:
        <br> <br>
      ```bash
      chmod +x screensurfer

## Customization
- **Inactivity threshold:** Modify the INACTIVITY_THRESHOLD variable in main.py to set the idle time in seconds.
- **Website URL:** Change the URL in the open_website_fullscreen function.

## Notes
- The GetLastInputInfo function may not capture true inactivity, as opening the website and fullscreening it can reset idle time. This occurs because the script's actions, like launching the browser and pressing F11, are registered as user activity. GRACE_PERIOD was implemented to disregard the first 5 seconds of activity. We recommend retaining this setting to ensure proper functionality.

## License
This project is licensed under the [MIT License](https://mit-license.org).   
