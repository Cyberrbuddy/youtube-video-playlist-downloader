# **youtube-video-playlist-downloader**

I also improved formatting, fixed spacing issues, added a proper title section, and made everything consistent.

---

# ⭐ YouTube Video & Playlist Downloader

A simple Python tool that lets you download YouTube **videos** and **playlists** in the video quality you choose.
Beginner-friendly, clean, and easy to use.

---

## 🚀 Features

* Download **single videos** or **entire playlists**
* Choose your **video quality** (1080p, 720p, 480p, etc.)
* Automatically downloads the **best quality** if you skip selection
* Saves files in neat folders
* Works on **Windows, macOS, and Linux**

---

# 📥 Installation & Setup

Follow these simple steps to get everything working.

---

## ✅ 1. Install Python

If you don't have Python installed:

* **Windows:** Download from [https://www.python.org/downloads](https://www.python.org/downloads)
  → Make sure to check **“Add to PATH”** during installation.
* **macOS:** Python usually comes pre-installed.
* **Linux:** Python is usually already installed.

Check version:

```sh
python --version
```

---

## ✅ 2. Install yt-dlp

Run this in Terminal or CMD:

```sh
pip install yt-dlp
```

If you face any issue:

```sh
pip install --upgrade yt-dlp
```

---

## ✅ 3. Download This Project

Two options:

### ✔ Option A — Download ZIP

* Click **Code → Download ZIP**
* Extract it anywhere on your computer

### ✔ Option B — Clone via Git

```sh
git clone https://github.com/your-username/youtube-video-playlist-downloader.git
```

*(Replace with your actual GitHub username.)*

---

## ✅ 4. Run the Program

Open your terminal inside the project folder and run:

```sh
python main.py
```

*(Or whatever name you used for your script.)*

---

# 🎯 How to Use

After starting the program, simply follow the instructions.

---

## ✔ Step 1 — Choose Download Type

The script will ask:

```
Single Video (1) or Playlist (2)?
```

Select:

* **1** for a single YouTube video
* **2** for a full playlist

---

## ✔ Step 2 — Paste Your YouTube Link

Example:

```
Enter the YouTube URL: https://youtube.com/xyz...
```

---

## ✔ Step 3 — Choose Quality (Video Only)

You’ll see something like:

```
1. 1080p60
2. 720p30
3. 480p
```

Now you can:

* Enter the number you want
  **OR**
* Press **Enter** to download the *best available* quality

---

# 📂 Download Location

Your downloads will be stored automatically:

```
Downloaded_Videos/        → for single videos
Downloaded_Playlist/      → for playlist videos
```

These folders are created for you automatically.

---

# 🛠 Troubleshooting

### ❗ yt-dlp not working?

Update it:

```sh
pip install --upgrade yt-dlp
```

### ❗ “python not recognized”?

On Windows:

* Reinstall Python
* Check **“Add to PATH”**

### ❗ Video not downloading?

Private or age-restricted videos may not work.

---

# ❤️ Done!

You're all set 🎉
Enjoy downloading videos and playlists easily.

---
