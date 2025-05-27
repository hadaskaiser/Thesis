# 📱 Instagram Follow/Unfollow Bot

This project automates the process of following and unfollowing Instagram users using Selenium and provides a user-friendly interface using Streamlit.

---

## 🚀 Features

- Login to Instagram (supports 2FA wait time)
- Automatically follow or unfollow a list of users
- Progress tracking with logs
- Streamlit-based web interface
- Chrome browser automation with Selenium

---

## 🧰 Requirements

- Windows
- Python 3.8+
- Google Chrome installed
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) compatible with your Chrome version

---

## 📦 Installation

### 1. Clone the repository or download the files

```bash
cd path\to\your\project
```

### 2. Create a virtual environment and activate it

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

> If you get a script execution error, run:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```

### 3. Install pip-tools and compile requirements

```bash
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
```


---

## 📄 Input Files

- Create a text file with Instagram usernames (one per line):
  - `users_follow.txt` → For following
  - `users_unfollow.txt` → For unfollowing

Example content:

```
natgeo
nasa
some_other_user
```

---

## 🖥 Running the App

Start the Streamlit dashboard:

```bash
streamlit run main_app.py
```

Then open the web browser that appears and:

1. Choose a participant ID.
2. Select action: Follow or Unfollow.
3. Press 🚀 Start.
4. Login will begin and then the bot will process the usernames.


---

## 📝 Logs

- CSV logs will be saved in the current folder for each session.
- Errors (e.g., failed follows) are recorded in `errors.txt`.

