#!/bin/bash

sudo apt-get update -y
sudo apt-get install -y git
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
ssh-keygen -t ed25519 -C "your_email@example.com" -f ~/.ssh/id_ed25519 -N ""
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
ssh -T git@github.com
sudo apt-get install -y ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update -y
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
wget https://download1.rstudio.org/electron/jammy/amd64/rstudio-2024.04.2-764-amd64.deb
sudo apt-get install -y ./rstudio-2024.04.2-764-amd64.deb
wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
unzip sonar-scanner-cli-5.0.1.3006-linux.zip -d /opt/
export PATH=$PATH:/opt/sonar-scanner-5.0.1.3006-linux/bin
echo "----------------------------------"
git --version
docker --version
sonar-scanner --version
echo "----------------------------------"
mkdir devsecops-lab && cd devsecops-lab
git init
echo "# DevSecOps Lab" > README.md
git add README.md
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:username/devsecops-lab.git
git push -u origin main
