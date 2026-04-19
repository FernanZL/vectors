"""
s2_equality.py
==============
Part II: Vector Equality, Free Vectors, and Opposite Vectors.
Scenes 13 through 16.
"""

from __future__ import annotations
from manim import *
from manim_slides import Slide

from shared_helpers import (
    C_U, C_V, C_W, C_NEG, C_HL, C_AX,
    _plane, _arrow, _title, _theory_block, _compress_to_header,
)


# ===========================================================================
# 13 · VectorLibre
# ===========================================================================
class VectorLibre(Slide):
    def construct(self) -> None:
        self.title = _title("13. Vector Libre")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"\textbf{Vector libre:} es el vector que puede trasladarse sin modificar\\ "
            r"su módulo, dirección y sentido.\\ "
            r"Cualquier representante que mantenga estas características se\\ "
            r"considera el mismo vector."
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane()
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        v0 = _arrow(self.plane.c2p(-3, -2), self.plane.c2p(-1, -1), color=C_U)
        self.play(GrowArrow(v0))
        self.next_slide()
        self.play(v0.animate.shift(np.array([2, 1, 0])))
        self.next_slide()
        self.play(v0.animate.shift(np.array([1, -1, 0])))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 14 · IgualdadGeometrica
# ===========================================================================
class IgualdadGeometrica(Slide):
    def construct(self) -> None:
        self.title = _title("14. Igualdad de Vectores (Eq. Geométrica)")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"\textbf{Igualdad de Vectores}: Dos vectores libres son iguales\\ "
            r"si tienen igual \textbf{dirección, sentido y módulo}.\\ "
            r"Los vectores iguales se llaman también \textbf{vectores equipolentes}."
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane()
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        direction = np.array([1.5, 0.5, 0])
        starts    = [self.plane.c2p(-3, -1), self.plane.c2p(0, 0), self.plane.c2p(2, 1)]
        labels    = [r"\vec{v}", r"\vec{w}", r"\vec{z}"]
        colors    = [C_U, C_V, C_W]
        for s, lbl, color in zip(starts, labels, colors):
            v   = _arrow(s, s + direction, color=color)
            lab = MathTex(lbl, font_size=28, color=color).next_to(v, UP)
            self.play(GrowArrow(v), Write(lab), run_time=0.6)
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 15 · IgualdadAnalitica
# ===========================================================================
class IgualdadAnalitica(Slide):
    def construct(self) -> None:
        self.title = _title("15. Igualdad Analítica de Vectores")
        self.play(Write(self.title))
        self.next_slide()

        # Three sequential pure-theory beats — no plot
        t1 = _theory_block(
            r"Dos vectores de $\mathbb{V}$ son iguales si se verifica la igualdad\\ "
            r"de sus respectivas componentes (homólogas)."
        )
        self.play(Write(t1))
        self.next_slide()

        t2 = _theory_block(
            r"\textbf{En } $\mathbb{R}^2$:\\ "
            r"$\vec{u}=(x_1, y_1),\ \vec{v}=(x_2, y_2)$\\ "
            r"$\vec{u} = \vec{v} \iff x_1=x_2 \land y_1=y_2$",
            font_size=30,
        ).next_to(t1, DOWN, buff=0.45)
        self.play(Write(t2))
        self.next_slide()

        t3 = _theory_block(
            r"\textbf{En } $\mathbb{R}^3$:\\ "
            r"$\vec{u}=(x_1,y_1,z_1),\ \vec{v}=(x_2,y_2,z_2)$\\ "
            r"$\vec{u}=\vec{v} \iff x_1=x_2 \land y_1=y_2 \land z_1=z_2$",
            font_size=28,
        ).next_to(t2, DOWN, buff=0.35)
        self.play(Write(t3))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 16 · VectorOpuesto
# ===========================================================================
class VectorOpuesto(Slide):
    def construct(self) -> None:
        self.title = _title("16. Vectores Opuestos")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"Un vector $\vec{v}$ y otro $-\vec{v}$ son opuestos si tienen:\\ "
            r"\textbf{igual dirección y módulo, pero sentidos contrarios}.\\ "
            r"Analíticamente: si $\vec{v}=(x_1, y_1) \implies -\vec{v}=(-x_1, -y_1)$."
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane()
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        c0   = self.plane.c2p(0, 0)
        u_p  = self.plane.c2p(3, 1)
        nu_p = self.plane.c2p(-3, -1)
        v    = _arrow(c0, u_p,  color=C_U)
        vl   = MathTex(r"\vec{v}",  font_size=28, color=C_U).next_to(v,  UP)
        nv   = _arrow(c0, nu_p, color=C_NEG)
        nvl  = MathTex(r"-\vec{v}", font_size=28, color=C_NEG).next_to(nv, DOWN)

        self.play(GrowArrow(v), Write(vl))
        self.next_slide()
        self.play(GrowArrow(nv), Write(nvl))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()
