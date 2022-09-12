---
title: Script sacar ip linux
description: 
date: 2015-10-09
lastmod: 2015-10-09
slug: ip
image: "covers/linux.png"
tags:
  - console
  - network
  - ip
categories:
  - Linux
---


`ifconfig eth0 | awk '/inet addr/ {split ($2,A,":"); print A[2]}'`
