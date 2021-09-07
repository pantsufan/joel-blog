title: YT-DLP on Android Using Termux
date: 2021-09-07
category: Android
tags: YouTube, Android
description: Download YouTube Videos With SponsorBlock on Android with Termux

### Info

yt-dlp is a youtube-dl fork based on the now inactive youtube-dlc. The main focus of this project is adding new features and patches while also keeping up to date with the original project

### List of Commands

1.  Grant Storage Permission
    ```
    termux-setup-storage
    ```
2.  Install Necessary Packages

    ```
    pkg install -y python
    ```

    ```
    pkg install -y ffmpeg
    ```

3.  Install yt-dlp
    ```
    pip install yt-dlp
    ```
4.  Create YouTube Donwload Folder

    ```
    mkdir /data/data/com.termux/files/home/storage/shared/YouTube
    ```

5.  Creating yt-dlp Config (Choose Depending on Resolution)

    ```
    mkdir -p ~/.config/yt-dlp
    ```

- Downloads videos in either 720p or 720p60fps

  ```
  echo "-f mp4 -f 136+140/298+140 -o /data/data/com.termux/files/home/storage/shared/YouTube/%(title)s-%(uploader)s.%(ext)s --no-mtime --sponsorblock-remove all" > ~/.config/yt-dlp/config
  ```

- Downloads videos in either 1080p or 1080p60fps
  ```
  echo "-f mp4 -f 137+140/299+140 -o /data/data/com.termux/files/home/storage/shared/YouTube/%(title)s-%(uploader)s.%(ext)s --no-mtime --sponsorblock-remove all" > ~/.config/yt-dlp/config
  ```

6. Configuring To Download From Share Menu

   ```
   mkdir ~/bin
   ```

   ```
   cd ~/bin
   ```

   ```
   echo yt-dlp \$1 > termux-url-opener
   ```
