"""
s0_title.py
===========
Initial title slide for the Vector Lecture presentation.
"""

from __future__ import annotations
from manim import *
from manim_slides import Slide

from shared_helpers import (
    C_U, C_V, C_W, C_NEG, C_HL, C_AX,
    _plane, _arrow,
)

# ===========================================================================
# 0 · TitleSlide
# ===========================================================================

class TitleSlide(Slide):
    def construct(self) -> None:
        # --- 1. Background (Subtle Grid) ---
        # Very basic plane with lower opacity
        plane = NumberPlane(
            x_range=[-10, 10, 1], y_range=[-6, 6, 1],
            background_line_style={"stroke_color": C_AX, "stroke_opacity": 0.15},
            axis_config={"stroke_color": C_AX, "stroke_opacity": 0.3},
        )
        self.add(plane)
        
        # --- 2. Main Title (Lecture Name) ---
        # PLACEHOLDER: Edit this string manually
        title_text = "VECTORES EN EL PLANO Y EL ESPACIO" 
        title = Text(title_text, font_size=48, color=C_V, weight=BOLD)
        title.shift(UP * 1.5)
        
        # --- 3. Subtitles (Assignature & Professor) ---
        # PLACEHOLDER: Edit these strings manually
        assignature_text = "Algebra y Geometria Analitica"
        professor_text   = "Prof. [NOMBRE DEL PROFESOR]"
        
        assignature = Text(assignature_text, font_size=32, color=C_W)
        assignature.next_to(title, DOWN, buff=0.5)
        
        professor = Text(professor_text, font_size=28, color=C_HL)
        professor.next_to(assignature, DOWN, buff=0.8)
        
        # --- 4. Basic Animation: Title Reveal ---
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(assignature, shift=UP * 0.3))
        self.play(FadeIn(professor, shift=UP * 0.3))
        self.next_slide()
        
        # --- 5. Basic Animation: Vector Plots ---
        # A couple of basic vectors as requested
        v1 = _arrow(ORIGIN, RIGHT * 2 + UP, color=C_U)
        v2 = _arrow(ORIGIN, LEFT + UP * 2, color=C_NEG)
        v1_lbl = MathTex(r"\vec{v}", color=C_U).next_to(v1.get_end(), UR, buff=0.1)
        v2_lbl = MathTex(r"\vec{w}", color=C_NEG).next_to(v2.get_end(), UL, buff=0.1)
        
        self.play(GrowArrow(v1), Write(v1_lbl))
        self.play(GrowArrow(v2), Write(v2_lbl))
        self.next_slide()
        
        # --- 6. Cleanup ---
        self.play(FadeOut(title, assignature, professor, v1, v2, v1_lbl, v2_lbl))
        self.next_slide()
