---
title: "{{ replace .Name "_" " " | title }}"
description: 
date: {{ .Date }}
lastmod: {{ .Date }}
slug: "{{ replace .Name " " "_" | title }}"
image: covers/blue.jpg
hidden: false
draft: true
tags:
  - a
categories:
  - a
---