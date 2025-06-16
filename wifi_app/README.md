# WiFi Connection App

This simple Flask application allows a phone and a PC to communicate over WiFi. It starts a web server on your system that you can access from your phone's browser while both devices are on the same network.

## Setup

1. Install Python 3.
2. Install Flask:
   ```bash
   pip install Flask
   ```
3. Run the app:
   ```bash
   python app.py
   ```

## Usage

After running the app, open your phone's browser and navigate to `http://<PC_IP>:5000/`. You should see the message **"Phone connected to system via WiFi!"**.

Replace `<PC_IP>` with the local IP address of your computer (for example `192.168.1.10`).
