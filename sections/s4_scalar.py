"""
s4_scalar.py
============
Part IV: Scalar Multiplication, Linear Combinations, and Linear Dependence.
Scenes 29 through 37.
"""

from __future__ import annotations
from manim import *
from manim_slides import Slide

from shared_helpers import (
    C_U, C_V, C_W, C_NEG, C_HL, C_AX,
    _plane, _arrow, _title, _theory_block, _compress_to_header,
)


# ===========================================================================
# 29 · ProductoPorEscalarIntro
# ===========================================================================
class ProductoPorEscalarIntro(Slide):
    def construct(self) -> None:
        self.title = _title("29. Producto de un Vector por un Escalar")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"Un número real $k$ multiplicado por un vector $\vec{v}$ da un nuevo vector.\\ "
            r"Analíticamente: $k \cdot (x_1, y_1) = (kx_1, ky_1)$.\\ "
            r"Su \textbf{dirección} es igual, y su \textbf{módulo} es $|k| \cdot |\vec{v}|$.\\ "
            r"El \textbf{sentido} depende del signo de $k$.",
            font_size=30,
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane(x_range=[-4, 4, 1], y_range=[-2, 3, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        co = self.plane.c2p(0, 0)
        v  = _arrow(co, self.plane.c2p(1.5, 0.7), color=C_U)
        vl = MathTex(r"\vec{v}", color=C_U).next_to(v, UP)
        self.play(GrowArrow(v), Write(vl))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 30 · ProductoPorEscalarCasosA
# ===========================================================================
class ProductoPorEscalarCasosA(Slide):
    def construct(self) -> None:
        self.title = _title("30. Casos Analíticos (k > 1 y k < -1)")
        self.play(Write(self.title))
        self.next_slide()

        # Plane + base arrow shown together as the visual context
        self.plane = _plane(x_range=[-4, 4, 1], y_range=[-2, 3, 1])
        base_v = np.array([1.5, 0.7, 0])
        co     = self.plane.c2p(0, 0)
        arr    = _arrow(co, self.plane.c2p(*base_v), color=C_U)
        self.play(FadeIn(self.plane), GrowArrow(arr))
        self.next_slide()

        textA = _theory_block(
            r"$\bullet\ k > 1$: mismo sentido, mayor módulo (se estira). Ej: $\mathbf{k = 2}$",
            font_size=30,
        ).next_to(self.title, DOWN, buff=0.3).to_edge(LEFT, buff=0.5)
        self.play(Write(textA))
        self.next_slide()

        self.play(arr.animate.put_start_and_end_on(co, self.plane.c2p(*(base_v * 2))).set_color(C_V))
        self.next_slide()

        textB = _theory_block(
            r"$\bullet\ k < -1$: sentido opuesto, mayor módulo. Ej: $\mathbf{k = -1.5}$",
            font_size=30,
        ).next_to(textA, DOWN, buff=0.3).align_to(textA, LEFT)
        self.play(Write(textB))
        self.next_slide()

        self.play(arr.animate.put_start_and_end_on(co, self.plane.c2p(*(base_v * -1.5))).set_color(C_NEG))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 31 · ProductoPorEscalarCasosB
# ===========================================================================
class ProductoPorEscalarCasosB(Slide):
    def construct(self) -> None:
        self.title = _title("31. Casos Analíticos (|k| < 1 y k = 0)")
        self.play(Write(self.title))
        self.next_slide()

        self.plane = _plane(x_range=[-4, 4, 1], y_range=[-2, 3, 1])
        base_v = np.array([1.5, 0.7, 0])
        co     = self.plane.c2p(0, 0)
        arr    = _arrow(co, self.plane.c2p(*base_v), color=C_U)
        self.play(FadeIn(self.plane), GrowArrow(arr))
        self.next_slide()

        textA = _theory_block(
            r"$\bullet\ -1 < k < 1$: se comprime ($|k| < 1$). Ej: $\mathbf{k = 0.5}$",
            font_size=30,
        ).next_to(self.title, DOWN, buff=0.3).to_edge(LEFT, buff=0.5)
        self.play(Write(textA))
        self.next_slide()

        self.play(arr.animate.put_start_and_end_on(co, self.plane.c2p(*(base_v * 0.5))).set_color(C_V))
        self.next_slide()

        textB = _theory_block(
            r"$\bullet\ k = 0$: el producto colapsa al vector nulo $\vec{0}$.",
            font_size=30,
        ).next_to(textA, DOWN, buff=0.3).align_to(textA, LEFT)
        self.play(Write(textB))
        self.next_slide()

        dot = Dot(co, color=C_HL, radius=0.1)
        self.play(ReplacementTransform(arr, dot))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 32 · PropiedadesProductoPorEscalar
# ===========================================================================
class PropiedadesProductoPorEscalar(Slide):
    def construct(self) -> None:
        self.title = _title("32. Propiedades del Producto por Escalar")
        self.play(Write(self.title))
        self.next_slide()

        intro = _theory_block(r"Se verifican las siguientes propiedades ($\forall k \in \mathbb{R}, \forall \vec{v} \in \mathbb{V}$):")
        self.play(Write(intro))
        
        t1 = _theory_block(
            r"1. \textbf{Composición externa}: $k \cdot \vec{v} \in \mathbb{V}$\\ "
            r"2. \textbf{Asociativa mixta}: $(k_1 k_2) \cdot \vec{v} = k_1 (k_2 \cdot \vec{v})$\\ "
            r"3. \textbf{Distributiva respecto a escalares}: $(k_1 + k_2) \cdot \vec{v} = k_1\vec{v} + k_2\vec{v}$\\ "
            r"4. \textbf{Distributiva respecto a vectores}: $k \cdot (\vec{u} + \vec{v}) = k\vec{u} + k\vec{v}$\\ "
            r"5. \textbf{Elemento neutro}: $1 \cdot \vec{v} = \vec{v}$",
            font_size=30,
        ).next_to(intro, DOWN, buff=0.3).align_to(intro, LEFT)
        self.play(Write(t1))
        self.next_slide()
        
        conc = _theory_block(
            r"Por todas estas propiedades (suma y producto), el conjunto\\ "
            r"$\mathbb{V}$ determina un \textbf{espacio vectorial}.",
            font_size=30, color=C_HL,
        ).next_to(t1, DOWN, buff=0.4).align_to(intro, LEFT)
        self.play(Write(conc))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 33 · ParalelismoAnalitico
# ===========================================================================
class ParalelismoAnalitico(Slide):
    def construct(self) -> None:
        self.title = _title("33. Condición Analítica de Paralelismo")
        self.play(Write(self.title))
        self.next_slide()

        t1 = _theory_block(
            r"Dos vectores $\vec{v}_1=(x_1, y_1)$ y $\vec{v}_2=(x_2, y_2)$ son paralelos si uno es\\ "
            r"múltiplo escalar del otro:"
        )
        self.play(Write(t1))
        self.next_slide()

        form = MathTex(
            r"\vec{v}_1 = k \cdot \vec{v}_2"
            r"\iff \begin{cases} x_1 = k \cdot x_2 \\ y_1 = k \cdot y_2 \end{cases}"
            r"\iff \frac{x_1}{x_2} = \frac{y_1}{y_2} = k",
            font_size=36, color=C_HL,
        ).next_to(t1, DOWN, buff=0.5)
        self.play(Write(form))
        self.next_slide()

        con = _theory_block(
            r"Sus \textbf{componentes homólogas son proporcionales}.",
            font_size=30,
        ).next_to(form, DOWN, buff=0.4)
        self.play(Write(con))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 34 · VersoresFundamentales
# ===========================================================================
class VersoresFundamentales(Slide):
    def construct(self) -> None:
        self.title = _title("34. Versores Fundamentales")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"Un \textbf{versor} o vector unitario es aquel cuyo módulo es igual a 1.\\ "
            r"En el plano cartesiano $\mathbb{R}^2$, se definen los versores fundamentales:\\ "
            r"$\bullet\ \hat{i} = (1, 0)$ sobre el eje $x$, y $\hat{j} = (0, 1)$ sobre el eje $y$.\\ "
            r"Todo vector se puede expresar en función de ellos: $\vec{v} = (x, y) = x\hat{i} + y\hat{j}$",
            font_size=28,
        )
        self.play(Write(theory))
        self.next_slide()
        
        self.plane = _plane(x_range=[-1, 4, 1], y_range=[-1, 3, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        co = self.plane.c2p(0, 0)
        vi = _arrow(co, self.plane.c2p(1, 0), color=C_U)
        vj = _arrow(co, self.plane.c2p(0, 1), color=C_V)
        t_i = MathTex(r"\hat{i}", color=C_U).next_to(vi, DOWN, buff=0.1)
        t_j = MathTex(r"\hat{j}", color=C_V).next_to(vj, LEFT, buff=0.1)
        self.play(GrowArrow(vi), GrowArrow(vj), Write(t_i), Write(t_j))
        self.next_slide()

        v_full = _arrow(co, self.plane.c2p(3, 2), color=C_HL)
        v_lbl = MathTex(r"\vec{v} = 3\hat{i} + 2\hat{j}", color=C_HL, font_size=32).next_to(v_full, UR, buff=0.1)
        
        lx = DashedLine(self.plane.c2p(3, 0), self.plane.c2p(3, 2), color=C_U)
        ly = DashedLine(self.plane.c2p(0, 2), self.plane.c2p(3, 2), color=C_V)
        self.play(Create(lx), Create(ly))
        self.play(GrowArrow(v_full), Write(v_lbl))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

# ===========================================================================
# 35 · CombinacionLineal
# ===========================================================================
class CombinacionLineal(Slide):
    def construct(self) -> None:
        self.title = _title("35. Combinación Lineal")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"Un vector $\vec{w}$ es \textbf{combinación lineal} de un conjunto de vectores\\ "
            r"si puede escribirse de la forma:\\ "
            r"$\vec{w} = k_1\vec{v}_1 + k_2\vec{v}_2 + \dots = \sum_{i=1}^{n} k_i \vec{v}_i$",
            font_size=30,
        )
        self.play(Write(theory))
        self.next_slide()
        
        theory2 = _theory_block(
            r"Por ejemplo, con $\vec{v}_1=(1,2)$ y $\vec{v}_2=(2,1)$:\\ "
            r"$\vec{w} = \mathbf{3}\vec{v}_1 + \mathbf{2}\vec{v}_2 = 3(1,2) + 2(2,1) = (7,8)$",
            font_size=30,
        ).next_to(theory, DOWN, buff=0.3).align_to(theory, LEFT)
        self.play(Write(theory2))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 8, 1], y_range=[-1, 9, 1], _scale=0.52)
        _compress_to_header(self, VGroup(theory, theory2), self.title, self.plane)
        self.next_slide()

        co  = self.plane.c2p(0, 0)
        av1 = _arrow(co, self.plane.c2p(1, 2), color=C_U)
        av2 = _arrow(co, self.plane.c2p(2, 1), color=C_V)
        self.play(GrowArrow(av1), GrowArrow(av2))
        self.next_slide()

        s1 = self.plane.c2p(*(np.array([1, 2, 0]) * 3))
        s2 = self.plane.c2p(*(np.array([2, 1, 0]) * 2))
        self.play(av1.animate.put_start_and_end_on(co, s1))
        self.play(av2.animate.put_start_and_end_on(co, s2))
        self.next_slide()

        self.play(av2.animate.shift(s1 - co))
        res = _arrow(co, self.plane.c2p(7, 8), color=C_W)
        rl  = MathTex(r"\vec{w}=(7,8)", color=C_W).next_to(res, UR * 0.3)
        self.play(GrowArrow(res), Write(rl))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 36 · Dependencia e Independencia Lineal
# ===========================================================================
class DependenciaIndependenciaLineal(Slide):
    def construct(self) -> None:
        self.title = _title("36. Dependencia e Independencia Lineal")
        self.play(Write(self.title))
        self.next_slide()

        # Formal part
        t_formal_1 = _theory_block(
            r"Un conjunto de vectores es \textbf{L.D.} (Linealmente Dependiente) si\\ "
            r"existe una combinación lineal que dé el \textbf{vector nulo} sin que\\ "
            r"todos los coeficientes sean cero: $\sum_{i=1}^{n} k_i \vec{v}_i = \vec{0}$, con algún $k_i \neq 0$."
        )
        t_formal_2 = _theory_block(
            r"Si la única forma de obtener el vector nulo es con todos los coeficientes\\ "
            r"$k_i=0$, el conjunto es \textbf{L.I.} (Linealmente Independiente).",
            font_size=30,
        ).next_to(t_formal_1, DOWN, buff=0.3).align_to(t_formal_1, LEFT)
        
        self.play(Write(t_formal_1))
        self.next_slide()
        self.play(Write(t_formal_2))
        self.next_slide()
        self.play(FadeOut(t_formal_1, t_formal_2))

        # Geometric part
        theory = _theory_block(
            r"En $\mathbb{R}^2$, la dependencia trata sobre si los vectores son múltiplos (paralelos).\\ "
            r"$\bullet$ \textbf{L.D.}: son paralelos ($k\cdot\vec{v}_1 = \vec{v}_2$).\\ "
            r"$\bullet$ \textbf{L.I.}: NO son paralelos.",
            font_size=30,
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane()
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        co = self.plane.c2p(0, 0)
        v1 = _arrow(co, self.plane.c2p(2, 1),  color=C_U)
        v2 = _arrow(co, self.plane.c2p(4, 2),  color=C_NEG)
        ld = MathTex(r"\text{L.D.} \rightarrow \vec{v}_2 = 2\vec{v}_1",
                     font_size=28, color=C_NEG).next_to(v2, RIGHT)
        self.play(GrowArrow(v1), GrowArrow(v2), Write(ld))
        self.next_slide()
        self.play(FadeOut(v1, v2, ld))
        self.next_slide()

        w1 = _arrow(co, self.plane.c2p(3, 0.5),  color=C_U)
        w2 = _arrow(co, self.plane.c2p(0.5, 2.5), color=C_V)
        li = MathTex(r"\text{L.I.}", font_size=28, color=C_V).next_to(w2, UP)
        self.play(GrowArrow(w1), GrowArrow(w2), Write(li))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

# ===========================================================================
# 37 · PropiedadesDependenciaLineal
# ===========================================================================
class PropiedadesDependenciaLineal(Slide):
    def construct(self) -> None:
        self.title = _title("37. Propiedades de L.D. y L.I.")
        self.play(Write(self.title))
        self.next_slide()

        p_ld = _theory_block(
            r"\textbf{Vectores Linealmente Dependientes (L.D.)}:\\[0.15cm]"
            r"1. Al menos un vector se puede expresar como C.L. de los demás.\\ "
            r"2. En $\mathbb{R}^2$, dos vectores L.D. son paralelos (componentes proporcionales).\\ "
            r"3. En $\mathbb{R}^3$, cuatro vectores son SIEMPRE L.D.",
            font_size=30,
        )
        self.play(Write(p_ld))
        self.next_slide()

        p_li = _theory_block(
            r"\textbf{Vectores Linealmente Independientes (L.I.)}:\\[0.15cm]"
            r"1. Ningún vector se puede expresar como C.L. de los demás.\\ "
            r"2. En $\mathbb{R}^2$, dos vectores L.I. no son paralelos.\\ "
            r"3. En $\mathbb{R}^3$, tres vectores no coplanares son L.I.",
            font_size=30,
        ).next_to(p_ld, DOWN, buff=0.4).align_to(p_ld, LEFT)
        self.play(Write(p_li))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()
