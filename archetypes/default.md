---
title: "{{ replace .Name "_" " " | title }}"
description: 
date: {{ .Date }}
lastmod: {{ .Date }}
slug: "{{ replace .Name " " "_" | lower }}"
image: covers/blue.png
hidden: false
draft: true
tags:
  - a
  - b
  - c
categories:
  - AA
---