import os
import time
import pyperclip
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import configparser
import subprocess

class ClipboardHandler:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.trigger_word = self.config['DEFAULT']['TriggerWord']
        self.saved_file = self.config['DEFAULT']['SavedFileName']
        self.last_clipboard_data = None
        self.init_file()
    
    def init_file(self):
        if not os.path.exists(self.saved_file):
            with open(self.saved_file, 'w') as file:
                file.write('')
        self.clear_clipboard()
    
    def clear_clipboard(self):
        pyperclip.copy('')
    
    def get_clipboard_data(self):
        return pyperclip.paste()
    
    def check_and_save_clipboard(self):
        data = self.get_clipboard_data()
        if self.trigger_word in data:
            if data != self.last_clipboard_data:
                with open(self.saved_file, 'r') as file:
                    saved_data = file.read().splitlines()
                if data not in saved_data:
                    with open(self.saved_file, 'a') as file:
                        file.write(data + '\n')
                    self.last_clipboard_data = data
                    self.show_notification("Data saved.")
                else:
                    self.show_notification("Data already saved. Clipboard cleared.")
                    self.clear_clipboard()
            else:
                self.last_clipboard_data = data

    def show_notification(self, message):
        print("Notification: ", message)  # Log for debugging
        subprocess.run(['notify-send', '-t', '500', "Clipboard App", message])

class ClipboardEventHandler(FileSystemEventHandler):
    def __init__(self, handler):
        self.handler = handler

    def on_modified(self, event):
        if event.src_path.endswith('.conf'):
            self.handler.config.read(event.src_path)
            self.handler.trigger_word = self.handler.config['DEFAULT']['TriggerWord']
            self.handler.saved_file = self.handler.config['DEFAULT']['SavedFileName']
        self.handler.check_and_save_clipboard()

def generate_default_config(config_file):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {
        'TriggerWord': 'facebook',
        'SavedFileName': 'clipboard_data.txt'
    }
    with open(config_file, 'w') as configfile:
        config.write(configfile)
    print("No configuration file detected. Generated default configuration.")

def main():
    config_file = 'clipwatch.conf'
    
    if not os.path.exists(config_file):
        generate_default_config(config_file)

    clipboard_handler = ClipboardHandler(config_file)
    event_handler = ClipboardEventHandler(clipboard_handler)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            clipboard_handler.check_and_save_clipboard()
            time.sleep(0.5)  # Small delay to prevent rapid re-checking
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
