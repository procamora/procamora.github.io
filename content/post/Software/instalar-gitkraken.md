---
title: Instalar GitKraken
description: Script para instalar gitkraken
date: 2018-09-14
lastmod: 2018-09-14
slug: instalar-gitkraken
image: "covers/software.png"
tags:
  - gitkracken
  - git
categories:
  - Software
---


```bash
#!/bin/bash

# Download GitKraken
wget https://release.gitkraken.com/linux/gitkraken-amd64.tar.gz

# copy the downloaded file into /opt directory
cp gitkraken-amd64.tar.gz /opt/

cd /opt

# Extract the Kraken into /opt directory
tar -xvzf gitkraken-amd64.tar.gz

# you can apply ownership for a specific user too
# chown -R user:group /opt/gitkraken

# Add gitkraken to PATH
echo "export PATH=\$PATH:/opt/gitkraken" >> ~/.bashrc
source ~/.bashrc

# sudo ln -s /usr/lib64/libcurl.so.4 /opt/gitkraken/libcurl-gnutls.so.4
sudo ln -s /usr/lib64/libcurl.so.4 /usr/lib64/libcurl-gnutls.so.4

# Create gitkraken launcher icon
# download icon here: http://img.informer.com/icons_mac/png/128/422/422255.png
# or here: https://drive.google.com/file/d/0B-3KQ_ohu-RFVkJyS1Zfa2NLSVE/view
wget http://img.informer.com/icons_mac/png/128/422/422255.png -o gitkraken-icon.png

mv gitkraken-icon.png /opt/gitkraken/

cd /usr/share/applications

cat > gitkraken.desktop <<EOL
[Desktop Entry]
Name=GitKraken
Comment=Git Flow
Exec=/opt/gitkraken/gitkraken
Icon=/opt/gitkraken/gitkraken-icon.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Utility;Development;
EOL
```



Fuente: [github][0]

[0]: https://gist.github.com/aelkz/17528d2f6a5db73185c7dfbd28e49d18