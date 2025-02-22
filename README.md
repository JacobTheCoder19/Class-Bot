<h2><em>💎 Key Features 💎</em></h2>
<div>
  🟩 <strong>Automated Class Access</strong><br>
  &emsp;🔸 Automatically opens the necessary websites and applications for my scheduled classes, saving me time and effort.<br><br>
</div>
<div>
  🟩 <strong>Time-Based Functionality</strong><br>
  &emsp;🔸 Uses the current time to determine which class to access, ensuring I'm always prepared at the right time.<br><br>
</div>
<div>
  🟩 <strong>Multi-Class Support</strong><br>
  &emsp;🔸 Supports multiple classes, including Math, Spanish, PSA, Ethics, and Programming, with specific actions for each.<br><br>
</div>
<div>
  🟩 <strong>Clipboard Management</strong><br>
  &emsp;🔸 Automatically copies and pastes usernames and passwords for seamless logins to various platforms.<br><br>
</div>
<div>
  🟩 <strong>Interactive Notifications</strong><br>
  &emsp;🔸 Displays a pop-up notification to confirm that everything is set up for class, enhancing user experience.<br><br>
</div>
<div>
  🟩 <strong>Notepad Integration</strong><br>
  &emsp;🔸 Opens Notepad for note-taking during classes, allowing for easy documentation of important information.<br><br>
</div>

<h2><em>✨ Purpose / Inspiration ✨</em></h2>
&emsp;This projects inspiration cam from me wanting to have to do less work. I got tired of having to log into my online classroom and open up all the websites I need every time I get to class. So I decided that I could make something to automate it so I could just go to class and run the program and be completely ready before class starts. This program also made it easier so that I can run it and while it's getting my computer set up I can get my physical self set up like getting my folders and books out.

<h2><em>⚙️ How it works ⚙️</em></h2>

&emsp;The program begins by importing necessary libraries such as `pyautogui` for mouse control, `webbrowser` for opening websites, and `datetime` for managing time-based functionality. It retrieves the current time and day to determine which class is scheduled and executes the corresponding actions.

&emsp;Upon startup, the program opens the KSU website and navigates through the login process by clicking on the appropriate buttons at specified screen coordinates. It waits for the website to load before proceeding to the next step, ensuring a smooth user experience.

&emsp;For each class, the program checks if the current time falls within the designated class time range. If it does, it automatically clicks the corresponding button to access the class page. For classes that require additional logins, such as Spanish, it opens the relevant website, enters the username and password using clipboard management, and navigates through the login process.

&emsp;The program also includes a pop-up notification that confirms everything is set up for class, providing a friendly reminder to the user. Additionally, it opens Notepad for note-taking during classes, ensuring that important information can be documented easily.

&emsp;Finally, the program is designed to close Visual Studio Code once all tasks are completed, allowing for a clean exit. Overall, this automated class scheduling program demonstrates the power of Python in enhancing productivity and simplifying daily tasks for students.
