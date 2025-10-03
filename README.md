# ✨ Sora Code Invite Generator ✨

---

> **⚠️ A Word of Caution**
>
> This script is intended for **educational exploration only**. Automating API requests may be a violation of the Sora/OpenAI Terms of Service. The use of this script could lead to the suspension or termination of your account. You bear the sole responsibility for your actions. The creator of this script assumes no liability. Please proceed with discretion.

---

![sora](https://github.com/user-attachments/assets/7f7a36d8-532b-45b1-96ec-5f3eef44af30)

---

### 🚀 Recommended Configuration

For optimal performance, it is strongly advised to use the **Mozilla Firefox** browser and connect through a **VPN server located in the USA**. This configuration helps in replicating the request headers that are most frequently accepted by the API.

---

## 🛠️ How It Operates

1.  **Code Generation**: The script fabricates random 6-character invitation codes following the `0A1B2C` pattern.
2.  **Concurrent Submission**: It employs multiple threads to submit these codes to the Sora API at a rapid pace.
3.  **Response Management**:
    *   A **successful** code (200 OK) is logged in `success.txt`.
    *   An **invalid** code (403 Forbidden) is recorded in `invalid_codes.txt` and is not retried.
    *   If **rate-limited** (429 Too Many Requests), the script will pause and re-attempt.
    *   In case of **authentication failure** (401 Unauthorized), the script will halt and prompt you to refresh your token.
4.  **Intelligent Caching**: The script is designed with a "blacklist cache" system. It utilizes `used_codes.txt` and `invalid_codes.txt` to prevent the re-testing of any code that has been previously attempted, whether it was successful, invalid, or simply used. This feature enhances efficiency, particularly when the script is stopped and restarted.

> **💡 Jumpstart Your Progress!** This package is pre-loaded with `invalid_codes.txt`, containing **10,000 known invalid codes**. This will save you time and minimize superfluous API requests, as the script will automatically bypass these codes.

---

## SETUP INSTRUCTIONS

Please follow these instructions meticulously to ensure the script runs smoothly.

### Step 1: Initial Setup

1.  Ensure you have [Python](https://www.python.org/downloads/) installed on your system.
2.  Execute the `install.bat` file by double-clicking it. This will establish a virtual environment and install the required libraries.

### Step 2: Acquiring Your Authentication Token (Using Firefox)

This is a crucial step. The script requires your personal authentication token to function.

1.  Launch **Mozilla Firefox** and sign in to `https://sora.chatgpt.com`.
2.  Open the **Developer Tools** by pressing the `F12` key.
3.  Navigate to the **Network** tab.
4.  If the panel is empty, either refresh the page or go to `https://sora.chatgpt.com/explore`.
5.  In the filter input box (🔍), enter `sora` to isolate requests made to the Sora server.
6.  Select any request from the filtered list.
7.  In the right-hand pane, locate the **Headers** section and scroll to **Request Headers**.
8.  Find the `authorization` header, which will appear as:
    `authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...`
9.  **Copy the extensive string of characters** that follows `Bearer `.
10. Paste the copied token into the `auth.txt` file. **Do not include `Bearer `**. Save the file.

### Step 3: Fine-Tuning Script Parameters (Optional)

You can adjust the script's performance by modifying the `params.txt` file.

-   `max_workers`: Determines the number of threads for code submission. A higher number can increase speed but also the likelihood of being rate-limited.
-   `delay`: The interval (in seconds) between code processing. A longer delay is generally safer.
-   `max_retries`: The number of times the script will attempt to resubmit a code after a rate-limit error.
-   `retry_delay`: The initial waiting period (in seconds) before a retry.

The default values in `params.txt` are a reliable starting point if you are uncertain.

### Step 4: Obtaining Your Device ID and User Agent (Using Firefox)

The script needs to emulate your specific browser's signature.

1.  Within the same **Network** tab where you located your token, find the `OAI-Device-Id` and `User-Agent` headers, which are typically listed below the authentication token.
2.  Copy the values for both of these headers.
3.  Open the `config.txt` file provided with the script.
4.  Substitute the placeholder values with your `OAI-Device-Id` and `User-Agent`. Save the file.

### Step 5: Executing the Script

After completing the preceding steps, you are ready to launch the script.

**For Windows users:**
-   Double-click the `run.bat` file.

The script will commence, displaying its progress. You can halt the script at any time by pressing `Ctrl+C`.

---

## 📂 File Directory

-   `sora.py`: The core Python script.
-   `auth.txt`: **(Your input required)** Your confidential authentication token.
-   `config.txt`: **(Your input required)** Your browser's Device ID and User Agent.
-   `params.txt`: **(Your input required)** Script settings such as thread count and delays.
-   `install.bat`: **(Run this initially)** Configures the Python virtual environment.
-   `run.bat`: **(Run this to begin)** Activates the environment and initiates the script.
-   `success.txt`: Created automatically. Stores all successfully submitted codes.
-   `invalid_codes.txt`: **Pre-populated with 10,000 invalid codes!** A "blacklist" of codes that are confirmed to be invalid. The script will not attempt to generate these codes.