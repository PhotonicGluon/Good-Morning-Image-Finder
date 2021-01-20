# Good-Morning-Image-Finder
An application that helps find "Good Morning" Images Automatically.

This project is no longer maintained. **Do not contact me for any assistance or any bugs that you may find in this project.**

## Installation
For this project, you will require Python 3.8.

### Installing Chrome
#### Linux
Run the following as a superuser in a terminal:
```bash
sudo apt-get update
sudo apt-get install -y libappindicator1 fonts-liberation
mkdir temp
cd temp
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb
```

### Installing Chromedriver
#### Linux
1. Before installing Chromedriver, run:
```bash
sudo apt-get update
sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
sudo apt-get install default-jdk 
```
2. Go to [https://sites.google.com/a/chromium.org/chromedriver/home](https://sites.google.com/a/chromium.org/chromedriver/home).
3. Under the heading "All versions available in Downloads", click on the link next to "Latest stable release".
4. Download your operating system's Chromedriver. Assumably it is in the `Downloads` folder.
5. Navigate to the downloads folder.
6. Unzip the `zip` file using `unzip chromedriver_*.zip`
7. Run the following commands:
```bash
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

### Main Installation Process
1. Download the repository and extract it into a folder. Let's call that folder the *Root Folder*.
2. Using a terminal, navigate to the *Root Folder*
3. **(Optional)** Create a virtual environment. Run the following commands:
```bash
python -m venv venv --prompt "Good Morning Image Finder"
source venv/bin/activate
```
4. Install the needed libraries by running:
```bash
pip install -r requirements.txt
```

## Configuring the Project For Your Needs
1. Within the *Root Directory*, create two things:
    - The first is a file named `settings.yaml`.
    - The second is a directory named `imgs`.
2. Copy and paste the following text into `settings.yaml`:
```
send_email:
  email_host: smtp.gmail.com
  email_user: your_email_here@gmail.com
  email_password: your_email_password
  email_port: 587

receive_email:
  recipients:
    - recipient_1@example.com
    - recipient_2@example.com
    - recipient_3@example.com
```
3. Replace `your_email_here@gmail.com` and `your_email_password` with your Gmail email address and password.
4. By replacing the example recipients in the `recipients` list, add in the recipients that you want to send the email to.
5. Next, open up `main.py`. Under `# CONSTANTS`, change the values of the variables as you wish.

## Running the Project
**Note: Read *Configuring the Project For Your Needs* first!**
While inside the *Root Directory* (and within your virtual environment, if you have created one), run:
```bash
python main.py
```

## License
```
MIT License

Copyright © Ryan-Kan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
