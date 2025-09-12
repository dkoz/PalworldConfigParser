import os
import sys
import shutil
import platform

def detect_os_folder():
    system = platform.system().lower()
    if system == "windows":
        return "WindowsServer"
    elif system == "linux":
        if os.getenv("WINEPREFIX") or shutil.which("proton"):
            return "WindowsServer"
        return "LinuxServer"
    else:
        print("Unsupported operating system")
        sys.exit(1)

def set_ini_value(content: str, key: str, value: str, add_quotes: bool) -> str:
    block_start = content.find("OptionSettings=(")
    if block_start == -1:
        return content
    block_end = content.find(")", block_start)
    if block_end == -1:
        return content
    block = content[block_start:block_end+1]

    search_str = f"{key}="
    pos = block.find(search_str)
    if pos == -1:
        return content

    start = pos + len(search_str)

    if key == "CrossplayPlatforms":
        end = block.find(")", start)
        if end == -1:
            end = len(block)
        new_value = f"({value})"
        new_block = block[:start] + new_value + block[end+1:]
    else:
        end = block.find(",", start)
        if end == -1:
            end = block.find(")", start)
            if end == -1:
                end = len(block)
        if add_quotes:
            value = f"\"{value}\""
        new_block = block[:start] + value + block[end:]

    return content[:block_start] + new_block + content[block_end+1:]

def copy_file(src, dst):
    shutil.copyfile(src, dst)
