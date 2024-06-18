<h1 align="center">ClipWatch</h1>


**ClipWatch** is a Python application designed to monitor your clipboard for specific keywords and save the clipboard data to a file. It provides notifications to inform you if the data has been saved or if it has already been recorded. This app is particularly useful for tracking and saving specific pieces of information that you frequently copy.

## Features

- Monitors clipboard for changes.
- Detects specific trigger words in the clipboard data.
- Saves clipboard data to a text file if it contains the trigger word.
- Notifies the user when data is saved or if it has already been saved.
- Clears the clipboard after notifying the user to prevent duplicate notifications.
- Generates a default configuration file if none is found.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- `pyperclip` library
- `watchdog` library
- `libnotify-bin` (for notifications)

You can install the required Python libraries using pip:

```sh
pip install pyperclip watchdog
```

Install `libnotify-bin` on Linux:

```sh
sudo apt-get install libnotify-bin
```

### Installation

1. Clone the repository:

```sh
git clone https://github.com/Bluu-whale/clipwatch.git
cd clipwatch
```
2. Ensure all dependencies are installed as mentioned in the prerequisites.

3. Run the application:

```sh
python clipwatch.py
```

### Usage

Upon the first run, if no configuration file is found, ClipWatch will generate a default configuration file `clipwatch.conf` with the following contents:

```ini
[DEFAULT]
TriggerWord = facebook
SavedFileName = clipboard_data.txt
```

You can edit this configuration file to change the trigger word and the file name where clipboard data will be saved.

### Configuration

The configuration file `clipwatch.conf` supports the following options:

- `TriggerWord`: The word to be monitored in the clipboard data. If this word is found, the data will be saved.
- `SavedFileName`: The name of the file where the clipboard data will be saved.
Example configuration:

```ini
[DEFAULT]
TriggerWord = google
SavedFileName = google_clip.txt
```

### Notification

ClipWatch uses `notify-send` to provide desktop notifications. You will receive a notification when:

- Data containing the trigger word is saved.
- Data has already been saved, and the clipboard is cleared.

### Contribution

We welcome contributions to ClipWatch! If you have suggestions, issues, or feature requests, feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgements

- [pyperclip](https://github.com/asweigart/pyperclip) - For clipboard functionality
- [watchdog](https://github.com/gorakhargosh/watchdog) - For filesystem monitoring
- [libnotify](https://github.com/GNOME/libnotify) - For desktop notifications

---

`ClipWatch`: Effortlessly monitor and save your clipboard data.
