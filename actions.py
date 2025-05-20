import csv
import os
from time import sleep
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from constants import BASE_URL, BROWSER


def write_error(user):
    with open("errors.txt", "a+") as file:
        file.write(user + "\n")


def log_action(user_id, username, status, reason=""):
    log_file = f"{user_id}.csv"
    if not os.path.exists(log_file):
        with open(log_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "username", "status", "reason"])
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), username, status, reason])


def follow(usernames, user_id="default", callback=None):
    for i, user in enumerate(usernames):
        print(f"Opening profile: {user}")
        BROWSER.get(f"{BASE_URL}/{user}/")
        sleep(2)
        try:
            buttons = BROWSER.find_elements(By.TAG_NAME, "button")
            for btn in buttons:
                label = btn.text.strip().lower()
                if "follow" in label and "following" not in label and "requested" not in label:
                    btn.click()
                    print(f"Followed: {user}")
                    log_action(user_id, user, "success", "Followed")
                    if callback:
                        callback(user, "success", "Followed", i, len(usernames))
                    break
            else:
                print(f"Follow button not found for {user}")
                log_action(user_id, user, "skipped", "Not followable")
                if callback:
                    callback(user, "skipped", "Not followable", i, len(usernames))
        except Exception as e:
            print(f"⚠️ Error with {user}: {e}")
            write_error(user)
            log_action(user_id, user, "error", str(e))
            if callback:
                callback(user, "error", str(e), i, len(usernames))
        sleep(2)


def unfollow(usernames, user_id="default", callback=None):
    for i, user in enumerate(usernames):
        print(f"\n[{i + 1}/{len(usernames)}] Opening profile: {user}")
        BROWSER.get(f"{BASE_URL}/{user}/")
        sleep(2)
        try:
            buttons = BROWSER.find_elements(By.TAG_NAME, "button")
            for btn in buttons:
                label = btn.text.strip().lower()
                if label in ["following", "requested"]:
                    btn.click()
                    sleep(1)
                    unfollow_items = BROWSER.find_elements(By.XPATH, "//*[contains(text(), 'Unfollow')]")
                    for item in unfollow_items:
                        try:
                            item.click()
                            print(f"Unfollowed: {user}")
                            log_action(user_id, user, "success", "Unfollowed")
                            if callback:
                                callback(user, "success", "Unfollowed", i, len(usernames))
                            break
                        except:
                            continue
                    else:
                        print(f"Unfollow option not found for {user}")
                        log_action(user_id, user, "error", "Unfollow option not found")
                        if callback:
                            callback(user, "error", "Unfollow option not found", i, len(usernames))
                    break
            else:
                print(f"Unfollow button not found for {user}")
                log_action(user_id, user, "skipped", "Not following")
                if callback:
                    callback(user, "skipped", "Not following", i, len(usernames))
        except Exception as e:
            print(f"Error with {user}: {e}")
            write_error(user)
            log_action(user_id, user, "error", str(e))
            if callback:
                callback(user, "error", str(e), i, len(usernames))
        sleep(2)
