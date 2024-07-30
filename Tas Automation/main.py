from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock
import os
import shutil
import schedule
import time
from threading import Thread

KV = '''
BoxLayout:
    orientation: 'vertical'
    spacing: dp(10)
    padding: dp(10)

    MDRaisedButton:
        text: "Select Directory"
        pos_hint: {"center_x": .5}
        on_release: app.file_manager_open()

    MDRaisedButton:
        text: "Organize Files"
        pos_hint: {"center_x": .5}
        on_release: app.organize_files()

    MDTextField:
        id: interval_input
        hint_text: "Set interval (minutes)"
        pos_hint: {"center_x": .5}
        size_hint_x: 0.8
        input_filter: 'int'
        multiline: False

    MDRaisedButton:
        text: "Start Auto-Organize"
        pos_hint: {"center_x": .5}
        on_release: app.start_auto_organize()

    MDRaisedButton:
        text: "Stop Auto-Organize"
        pos_hint: {"center_x": .5}
        on_release: app.stop_auto_organize()

    MDLabel:
        id: status_label
        text: "Status: Idle"
        halign: "center"
'''

class FileOrganizerApp(MDApp):
    status = StringProperty("Status: Idle")

    def build(self):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )
        self.selected_path = None
        self.auto_organize_thread = None
        self.auto_organize_running = False
        return Builder.load_string(KV)

    def update_status(self, new_status):
        self.status = new_status
        self.root.ids.status_label.text = self.status

    def file_manager_open(self):
        home_directory = os.path.expanduser('~')
        self.file_manager.show(home_directory)  # Start browsing from the home directory

    def select_path(self, path):
        self.selected_path = path
        self.exit_manager()
        self.update_status(f"Selected directory: {self.selected_path}")

    def exit_manager(self, *args):
        self.file_manager.close()

    def organize_files(self):
        if not self.selected_path:
            self.show_alert_dialog("Please select a directory first!")
            return

        file_types = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif'],
            'Documents': ['.txt', '.pdf', '.docx', '.xlsx'],
            'Music': ['.mp3', '.wav', '.ogg'],
            'Videos': ['.mp4', '.mov', '.avi'],
            'Archives': ['.zip', '.rar', '.tar', '.gz'],
        }

        try:
            Clock.schedule_once(lambda dt: self.update_status("Status: Organizing files..."), 0)
            files_moved = False
            for folder, extensions in file_types.items():
                folder_path = os.path.join(self.selected_path, folder)
                os.makedirs(folder_path, exist_ok=True)
                for file_name in os.listdir(self.selected_path):
                    if file_name.startswith('.'):  # Ignore hidden files
                        continue
                    file_path = os.path.join(self.selected_path, file_name)
                    if os.path.isfile(file_path):
                        _, ext = os.path.splitext(file_name)
                        if ext.lower() in extensions:
                            shutil.move(file_path, folder_path)
                            files_moved = True
            if files_moved:
                self.show_alert_dialog("Files organized successfully!")
            else:
                self.show_alert_dialog("No files were moved. Please check the directory.")
            Clock.schedule_once(lambda dt: self.update_status("Status: Idle"), 0)
        except PermissionError as e:
            self.show_alert_dialog(f"Permission Error: {e}")
            Clock.schedule_once(lambda dt: self.update_status("Status: Error"), 0)
        except Exception as e:
            self.show_alert_dialog(f"An error occurred: {e}")
            Clock.schedule_once(lambda dt: self.update_status("Status: Error"), 0)

    def show_alert_dialog(self, message):
        dialog = MDDialog(
            text=message,
            size_hint=(0.8, 1),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                ),
            ],
        )
        dialog.open()

    def start_auto_organize(self):
        if not self.selected_path:
            self.show_alert_dialog("Please select a directory first!")
            return

        if self.auto_organize_running:
            self.show_alert_dialog("Auto-organize is already running!")
            return

        interval = self.root.ids.interval_input.text
        if not interval.isdigit() or int(interval) <= 0:
            self.show_alert_dialog("Please enter a valid interval (in minutes).")
            return

        interval = int(interval)
        self.auto_organize_running = True
        self.auto_organize_thread = Thread(target=self.auto_organize, args=(interval,))
        self.auto_organize_thread.start()
        self.update_status("Status: Auto-organize running")
        self.show_alert_dialog("Auto-organize started!")

    def stop_auto_organize(self):
        if not self.auto_organize_running:
            self.show_alert_dialog("Auto-organize is not running!")
            return

        self.auto_organize_running = False
        self.auto_organize_thread.join()
        self.update_status("Status: Idle")
        self.show_alert_dialog("Auto-organize stopped!")

    def auto_organize(self, interval):
        schedule.every(interval).minutes.do(self.organize_files)
        while self.auto_organize_running:
            schedule.run_pending()
            time.sleep(1)

if __name__ == '__main__':
    FileOrganizerApp().run()
