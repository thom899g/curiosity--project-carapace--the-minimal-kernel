"""
Carapace Core Event Loop - The heartbeat of the minimal kernel
Architectural Rationale: Uses asyncio for efficient I/O-bound operations while
maintaining single-threaded simplicity to avoid Python GIL overhead.
"""
import asyncio
import logging
import signal
import sys
from typing import Dict, Any, Optional, Callable
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum
import traceback
import gc


class EventPriority(Enum):
    CRITICAL = 0
    HIGH = 1
    NORMAL = 2
    LOW = 3
    BACKGROUND = 4


@dataclass
class