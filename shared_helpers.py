"""
shared_helpers.py
=================
Common colour palettes and UI layout helpers for the vector lecture presentation.
"""

from __future__ import annotations
from manim import *

# ---------------------------------------------------------------------------
# Global colour palette
# ---------------------------------------------------------------------------
C_U    = "#C77DFF"   # soft purple
C_V    = "#FF6EC7"   # hot pink
C_W    = "#FFD6FF"   # pale pink
C_NEG  = "#E040FB"   # magenta
C_HL   = "#F9F871"   # soft yellow
C_AX   = "#78909C"   # grey-blue
C_3D   = "#80CBC4"   # teal-mint
C_DIFF = "#FF4D6D"   # pink-red

# ---------------------------------------------------------------------------
# Shared layout helpers
# ---------------------------------------------------------------------------

def _plane(_scale: float = 0.7, **kw) -> NumberPlane:
    """Styled NumberPlane shifted to the lower half of the frame.

    Args:
        _scale: overall scale factor (default 0.7).  Use a smaller value
                (e.g. 0.5) for slides with a wide coordinate range so the
                plane does not overflow the visible frame.
        **kw:   forwarded verbatim to ``NumberPlane`` (e.g. x_range, y_range).
    """
    cfg: dict = dict(
        x_range=[-5, 5, 1], y_range=[-3, 3, 1],
        background_line_style={"stroke_color": C_AX, "stroke_opacity": 0.30},
        axis_config={"stroke_color": C_AX, "stroke_opacity": 0.80},
    )
    cfg.update(kw)
    return NumberPlane(**cfg).scale(_scale).shift(DOWN * 1.5)


def _arrow(start, end, color: str = C_U, **kw) -> Arrow:
    return Arrow(
        start, end,
        color=color, buff=0, stroke_width=4,
        max_tip_length_to_length_ratio=0.22,
        **kw,
    )


def _title(text_str: str) -> Text:
    """Fixed bold title anchored to the top edge."""
    t = Text(text_str, font_size=34, color=C_W, weight=BOLD)
    t.to_edge(UP, buff=0.25)
    return t


def _theory_text(text_str: str, **kw) -> Tex:
    """Small-format theory text (used for 3D fixed-in-frame captions)."""
    kw.setdefault("font_size", 26)
    kw.setdefault("tex_environment", "flushleft")
    return Tex(text_str, **kw)


def _theory_block(text_str: str, font_size: int = 34, **kw) -> Tex:
    """
    Large centred theory text for beat-1 of every slide.

    Positioned at ORIGIN so the text is truly centred on the frame.
    Slides that subsequently call ``_compress_to_header`` will reposition
    the block, so this default does not affect those slides.
    """
    kw.setdefault("tex_environment", "flushleft")
    return (
        Tex(text_str, font_size=font_size, **kw)
        .move_to(ORIGIN)
    )


def _compress_to_header(scene, theory, title, plane=None):
    """
    Beat-2 animation: shrink *theory* to a caption strip below *title* and
    simultaneously FadeIn *plane* (if provided).

    After this call the theory mobject lives in the upper-left zone and every
    subsequent visualisation on *plane* has room to breathe below it.
    """
    target = (
        theory.copy()
        .scale(0.72)
        .next_to(title, DOWN, buff=0.20)
        .to_edge(LEFT, buff=0.45)
    )
    anims = [Transform(theory, target)]
    if plane is not None:
        anims.append(FadeIn(plane))
    scene.play(*anims)
    return theory
