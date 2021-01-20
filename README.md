# Good-Morning-Image-Finder
An application that helps find "Good Morning" Images Automatically.

This is currently a Proof of Concept (POC). A full documentation will be written later.

## Installing Chrome
### Linux
Run the following as a superuser in a terminal:
```bash
sudo apt-get update
sudo apt-get install -y libappindicator1 fonts-liberation
mkdir temp
cd temp
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb
```

## Installing Chromedriver
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