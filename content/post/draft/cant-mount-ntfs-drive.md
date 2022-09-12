---
title: Can't Mount NTFS drive
description: 
date: 2016-02-11
lastmod: 2016-02-11
slug: cant-mount-ntfs-drive
image: "covers/draft.png"
tags:
  - ntfs
  - linux
categories:
  - Linux
---





http://askubuntu.com/questions/462381/cant-mount-ntfs-drive-the-disk-contains-an-unclean-file-system


```
Error mounting /dev/sdf1 at /media/root/Users: Command-line `mount -t "ntfs" -o "uhelper=udisks2,nodev,nosuid,uid=0,gid=0,dmask=0077,fmask=0177" "/dev/sdf1" "/media/root/Users"' exited with non-zero exit status 13: ntfs_attr_pread_i: ntfs_pread failed: Error de entrada/salida
Failed to read NTFS $Bitmap: Error de entrada/salida
NTFS is either inconsistent, or there is a hardware fault, or it's a
SoftRAID/FakeRAID hardware. In the first case run chkdsk /f on Windows
then reboot into Windows twice. The usage of the /f parameter is very
important! If the device is a SoftRAID/FakeRAID then first activate
it and mount a different device under the /dev/mapper/ directory, (e.g.
/dev/mapper/nvidia_eahaabcc1). Please see the 'dmraid' documentation
for more details.

```
