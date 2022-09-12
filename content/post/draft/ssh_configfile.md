---
title: ssh_configfile
description: 
date: 2015-12-20
lastmod: 2015-12-20
slug: ssh_configfile
image: "covers/draft.png"
tags:
  - ssh
categories:
  - Linux
---




.ssh/config

```
Host github.com
    User git
    HostName github.com
    IdentityFile ~/.ssh/github.project1.key
    
Host bitbucket.org
    User git
    HostName bitbucket.org
    IdentityFile ~/.ssh/github.org.key
    
Host github.com
    User git
    IdentityFile ~/.ssh/github.key
```


http://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/
