#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

from dataclasses import dataclass
from typing import Text


@dataclass
class File:
    id: int
    file: Text
    shasum: Text
