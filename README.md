# Chromecast Audio Controller 🎵

A lightweight Python toolkit built to discover, connect to, and control Google Home and Chromecast devices on your local network. Perfect for local media tinkering and smart home automation.

## 🛠 Tech Stack & Skills

* **Language:** Python 3
* **Libraries:** `pychromecast`
* **Core Concepts:** mDNS device discovery, remote media states, local network automation
* **Domain:** Smart Home & IoT Projects

## 🔑 Key Features

### 🚀 Features
* **Device Finder:** Instantly scans your local Wi-Fi/LAN for available Cast devices.
* **Remote Control:** Send play, pause, volume, and stream commands programmatically.
* **Status Polling:** Check what's currently playing and monitor device volume levels.

## ⚡ Quickstart & Setup

### 1. Prerequisites
* Python 3.8+ installed
* Local Cast-compatible device

### 2. Installation
Clone the repo and spin up your environment:

```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/chromecast-audio-controller.git](https://github.com/YOUR_GITHUB_USERNAME/chromecast-audio-controller.git)
cd chromecast-audio-controller

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1 # Windows
# source venv/bin/activate # Linux/Mac

# Install dependencies
pip install pychromecast