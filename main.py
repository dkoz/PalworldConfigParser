import os
from validation import ValidationRules
from mappings import envVars, envVarsValidationRules, envVarsQuotes
from utils import detect_os_folder, set_ini_value, copy_file

def main():
    print("Starting configuration...")
    osFolder = detect_os_folder()
    iniFilePath = os.path.abspath(f"Pal/Saved/Config/{osFolder}/PalWorldSettings.ini")
    defaultIniPath = "DefaultPalWorldSettings.ini"

    if not os.path.exists(iniFilePath):
        if os.path.exists(defaultIniPath):
            os.makedirs(os.path.dirname(iniFilePath), exist_ok=True)
            copy_file(defaultIniPath, iniFilePath)
            print("Copied DefaultPalWorldSettings.ini to:", iniFilePath)
        else:
            print("PalWorldSettings.ini not found and DefaultPalWorldSettings.ini missing.")
            return
    elif os.path.getsize(iniFilePath) < 1200:
        copy_file(defaultIniPath, iniFilePath)
        print("Replaced empty PalWorldSettings.ini with default.")

    with open(iniFilePath, "r", encoding="utf-8") as f:
        iniContent = f.read()

    for key, envKey in envVars.items():
        val = os.getenv(envKey)
        if val is None:
            continue
        if val == "":
            print(f"Updating empty key: {key}")
            iniContent = set_ini_value(iniContent, key, "", envVarsQuotes.get(key, False))
            continue

        ruleName = envVarsValidationRules.get(key)
        if ruleName and not ValidationRules[ruleName](val):
            print(f"Validation failed for {key} = {val}")
            continue

        print(f"Updating key: {key} with value: {val}")
        iniContent = set_ini_value(iniContent, key, val, envVarsQuotes.get(key, False))

    with open(iniFilePath, "w", encoding="utf-8") as f:
        f.write(iniContent)

    print("INI file updated successfully.")

if __name__ == "__main__":
    main()
