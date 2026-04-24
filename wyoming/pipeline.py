"""Pipeline events."""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional

from .event import Event, Eventable

_RUN_PIPELINE_TYPE = "run-pipeline"


class PipelineStage(str, Enum):
    """Stages of a pipeline."""

    WAKE = "wake"
    """Wake word detection."""

    ASR = "asr"
    """Speech-to-text (a.k.a. automated speech recognition)."""

    INTENT = "intent"
    """Intent recognition."""

    HANDLE = "handle"
    """Intent handling."""

    TTS = "tts"
    """Text-to-speech."""


@dataclass
class RunPipeline(Eventable):
    """Run a pipeline"""

    start_stage: PipelineStage
    """Stage to start the pipeline on."""

    end_stage: PipelineStage
    """Stage to end the pipeline on."""

    wake_word_name: Optional[str] = None
    """Name of wake word that triggered this pipeline."""

    restart_on_end: bool = False
    """True if pipeline should restart automatically after ending."""

    wake_word_names: Optional[List[str]] = None
    """Wake word names to listen for (start_stage = wake)."""

    announce_text: Optional[str] = None
    """Text to announce using text-to-speech (start_stage = tts)"""

    def __post_init__(self) -> None:
        raise NotImplementedError

    @staticmethod
    def is_type(event_type: str) -> bool:
        raise NotImplementedError

    def event(self) -> Event:
        raise NotImplementedError

    @staticmethod
    def from_event(event: Event) -> "RunPipeline":
        raise NotImplementedError
