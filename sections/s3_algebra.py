"""
s3_algebra.py
=============
Part III: Vector Algebra (Addition, Subtraction, Properties).
Scenes 17 through 26.
"""

from __future__ import annotations
from manim import *
from manim_slides import Slide

from shared_helpers import (
    C_U, C_V, C_W, C_NEG, C_HL, C_AX, C_DIFF,
    _plane, _arrow, _title, _theory_block, _compress_to_header,
)


# ===========================================================================
# 17 · SumaIntroduccion   (pure-theory — no plot)
# ===========================================================================
class SumaIntroduccion(Slide):
    def construct(self) -> None:
        self.title = _title("17. Álgebra Vectorial: Introducción a la Suma")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"En este curso estudiaremos las operaciones algebraicas:\\ "
            r"1. La suma entre vectores.\\ "
            r"2. La diferencia entre vectores.\\ "
            r"3. El producto de un vector por un escalar.\\[0.25cm]"
            r"\textbf{La Suma}: La suma de dos vectores libres $\vec{u}$ y $\vec{v}$\\ "
            r"es otro vector resultante denotado $\vec{u} + \vec{v}$.",
            font_size=30,
        )
        self.play(Write(theory))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 18 · SumaProtocolo
# ===========================================================================
class SumaProtocolo(Slide):
    def construct(self) -> None:
        self.title = _title("18. Regla Cabeza-Cola (Protocolo)")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"\textbf{Protocolo}:\\ "
            r"1. Trasladamos $\vec{v}$ a continuación de $\vec{u}$ (origen de $\vec{v}$ en extremo de $\vec{u}$).\\ "
            r"2. El origen de la suma es el origen de $\vec{u}$.\\ "
            r"3. El extremo de la suma es el extremo de $\vec{v}$.",
            font_size=30,
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 5, 1], y_range=[-1, 4, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        u_v, v_v = np.array([2, 1, 0]), np.array([1, 2, 0])
        u_arr = _arrow(self.plane.c2p(0, 0), self.plane.c2p(*u_v), color=C_U)
        v_arr = _arrow(self.plane.c2p(0, 0), self.plane.c2p(*v_v), color=C_V)
        ul = MathTex(r"\vec{u}", color=C_U).next_to(u_arr, DOWN, buff=0.1)
        vl = MathTex(r"\vec{v}", color=C_V).next_to(v_arr, LEFT,  buff=0.1)

        self.play(GrowArrow(u_arr), Write(ul), GrowArrow(v_arr), Write(vl))
        self.next_slide()

        target_v = self.plane.c2p(*(u_v + v_v))
        self.play(
            v_arr.animate.put_start_and_end_on(self.plane.c2p(*u_v), target_v),
            vl.animate.shift(self.plane.c2p(*u_v) - self.plane.c2p(0, 0)),
        )
        self.next_slide()

        res = _arrow(self.plane.c2p(0, 0), target_v, color=C_W)
        rl  = MathTex(r"\vec{u}+\vec{v}", color=C_W).next_to(res.get_center(), UR * 0.3)
        self.play(GrowArrow(res), Write(rl))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 19 · SumaAnalitica   (pure-theory — two cascading blocks)
# ===========================================================================
class SumaAnalitica(Slide):
    def construct(self) -> None:
        self.title = _title("19. Expresión Analítica de la Suma")
        self.play(Write(self.title))
        self.next_slide()

        t1 = _theory_block(
            r"La suma de dos vectores es otro vector cuyas componentes es la\\ "
            r"suma de sus componentes homólogas:\\ "
            r"$\vec{u} + \vec{v} = (x_1, y_1) + (x_2, y_2) = (x_1+x_2, y_1+y_2)$"
        )
        self.play(Write(t1))
        self.next_slide()

        t2 = _theory_block(
            r"\textbf{Ejemplo Numérico}:\\ "
            r"Sean $\vec{u}=(-2, 3)$ y $\vec{v}=(1, 2)$.\\ "
            r"$\implies \vec{u}+\vec{v} = (-2+1, 3+2) = (-1, 5)$",
            font_size=30,
        ).next_to(t1, DOWN, buff=0.5)
        self.play(Write(t2))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 20 · ReglaParalelogramo
# ===========================================================================
class ReglaParalelogramo(Slide):
    def construct(self) -> None:
        self.title = _title("20. Regla del Paralelogramo")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"\textbf{Regla del Paralelogramo}:\\ "
            r"1. Dibujamos los dos vectores con el mismo origen.\\ "
            r"2. Trazamos segmentos paralelos por los extremos.\\ "
            r"3. La diagonal principal (desde el origen) es la suma."
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 5, 1], y_range=[-1, 4, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        u_v, v_v = np.array([3, 0.8, 0]), np.array([0.8, 2.5, 0])
        co   = self.plane.c2p(0, 0)
        cu   = self.plane.c2p(*u_v)
        cv   = self.plane.c2p(*v_v)
        csum = self.plane.c2p(*(u_v + v_v))
        u_arr = _arrow(co, cu, color=C_U)
        v_arr = _arrow(co, cv, color=C_V)
        self.play(GrowArrow(u_arr), GrowArrow(v_arr))
        self.next_slide()

        d1 = DashedLine(cu, csum, color=C_V)
        d2 = DashedLine(cv, csum, color=C_U)
        self.play(Create(d1), Create(d2))
        self.next_slide()

        s_arr = _arrow(co, csum, color=C_W)
        self.play(GrowArrow(s_arr))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 21 · ReglaPoligonal
# ===========================================================================
class ReglaPoligonal(Slide):
    def construct(self) -> None:
        self.title = _title("21. Regla de la Poligonal (3+ Vectores)")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"Se usa para sumar más de dos vectores. A partir de un punto,\\ "
            r"se trazan vectores equipolentes uno a continuación del otro.\\ "
            r"El origen del primero al extremo del último cierra el polígono y da la \textbf{resultante}.",
            font_size=30,
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 8, 1], y_range=[-1, 4, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        v1 = np.array([2, 1, 0])
        v2 = np.array([1, 2, 0])
        v3 = np.array([3, -1, 0])
        c0 = self.plane.c2p(0, 0)
        
        # Draw them at scattered locations
        s1 = self.plane.c2p(-1, 0)
        s2 = self.plane.c2p(1, 3)
        s3 = self.plane.c2p(5, 0)
        
        a1 = _arrow(s1, s1 + (self.plane.c2p(*v1) - c0), color=C_U)
        a2 = _arrow(s2, s2 + (self.plane.c2p(*v2) - c0), color=C_V)
        a3 = _arrow(s3, s3 + (self.plane.c2p(*v3) - c0), color=C_NEG)

        self.play(GrowArrow(a1))
        self.play(GrowArrow(a2))
        self.play(GrowArrow(a3))
        self.next_slide()
        
        # Shift them head to tail
        self.play(a1.animate.shift(c0 - s1))
        self.next_slide()
        self.play(a2.animate.shift(self.plane.c2p(*v1) - s2))
        self.next_slide()
        self.play(a3.animate.shift(self.plane.c2p(*(v1+v2)) - s3))
        self.next_slide()

        res_p = self.plane.c2p(*(v1+v2+v3))
        res   = _arrow(c0, res_p, color=C_W)
        rl    = MathTex(r"\text{Resultante}", font_size=24, color=C_W).next_to(res, UP * 0.2)
        self.play(GrowArrow(res), Write(rl))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 22 · PropiedadAsociativa   (purely algebraic — no plane)
# ===========================================================================
class PropiedadesSumaI(Slide):
    def construct(self) -> None:
        self.title = _title("22. Propiedades de la Suma (I)")
        self.play(Write(self.title))
        self.next_slide()

        t1 = _theory_block(
            r"Sean los vectores libres en $\mathbb{V}$. La suma algebraica verifica:\\[0.15cm]"
            r"1. \textbf{Composición interna}: $\forall\ \vec{v}_1, \vec{v}_2 \in \mathbb{V} \Rightarrow \vec{v}_1 + \vec{v}_2 \in \mathbb{V}$."
        )
        self.play(Write(t1))
        self.next_slide()
        
        t2 = _theory_block(
            r"2. \textbf{Existencia del neutro}: $\exists\ \vec{0} \in \mathbb{V} \ / \ \forall\ \vec{v} \in \mathbb{V}: \vec{v} + \vec{0} = \vec{v}$."
        ).next_to(t1, DOWN, buff=0.3).align_to(t1, LEFT)
        self.play(Write(t2))
        self.next_slide()

        t3 = _theory_block(
            r"3. \textbf{Elemento opuesto}: $\forall\ \vec{v} \in \mathbb{V}: \exists\ (-\vec{v}) \in \mathbb{V} \ / \ \vec{v} + (-\vec{v}) = \vec{0}$."
        ).next_to(t2, DOWN, buff=0.3).align_to(t1, LEFT)
        self.play(Write(t3))
        self.next_slide()
        
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

# ===========================================================================
# 22.5 · PropiedadAsociativaGeometrica
# ===========================================================================
class PropiedadAsociativaGeometrica(Slide):
    def construct(self) -> None:
        self.title = _title("22b. Propiedad Asociativa")
        self.play(Write(self.title))
        self.next_slide()

        t3 = _theory_block(
            r"4. \textbf{Propiedad Asociativa}: Permite agrupar términos en la suma:\\ "
            r"$(\vec{a} + \vec{b}) + \vec{c} = \vec{a} + (\vec{b} + \vec{c})$.",
            font_size=30,
        )
        self.play(Write(t3))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 6, 1], y_range=[-1, 5, 1], _scale=0.6).shift(DOWN*0.5)
        _compress_to_header(self, t3, self.title, self.plane)
        self.next_slide()

        co = self.plane.c2p(0, 0)
        va = np.array([2, 1, 0])
        vb = np.array([1, 2, 0])
        vc = np.array([2, 0, 0])
        ca = self.plane.c2p(*va)
        cb = self.plane.c2p(*(va+vb))
        cc = self.plane.c2p(*(va+vb+vc))

        arr_a = _arrow(co, ca, color=C_U)
        arr_b = _arrow(ca, cb, color=C_V)
        arr_c = _arrow(cb, cc, color=C_NEG)

        # Plot vectors
        self.play(GrowArrow(arr_a), Write(Tex(r"$\vec{a}$", color=C_U, font_size=24).next_to(arr_a.get_center(), DR*0.2)))
        self.play(GrowArrow(arr_b), Write(Tex(r"$\vec{b}$", color=C_V, font_size=24).next_to(arr_b.get_center(), UL*0.2)))
        self.play(GrowArrow(arr_c), Write(Tex(r"$\vec{c}$", color=C_NEG, font_size=24).next_to(arr_c.get_center(), UR*0.2)))
        self.next_slide()

        # Path 1: (a+b) + c
        g1 = MathTex(r"(\vec{a}+\vec{b}) + \vec{c}", font_size=36).to_edge(LEFT).shift(UP*1)
        self.play(Write(g1))
        
        arr_ab = _arrow(co, cb, color=C_W)
        lbl_ab = Tex(r"$\vec{a}+\vec{b}$", color=C_W, font_size=24).next_to(arr_ab.get_center(), UL*0.2)
        self.play(GrowArrow(arr_ab), Write(lbl_ab))
        self.next_slide()

        arr_res = _arrow(co, cc, color=C_HL)
        self.play(GrowArrow(arr_res))
        self.next_slide()

        # Path 2: a + (b+c)
        self.play(FadeOut(arr_ab), FadeOut(lbl_ab), FadeOut(arr_res))
        g2 = MathTex(r"\vec{a} + (\vec{b}+\vec{c})", font_size=36).to_edge(RIGHT).shift(UP*1)
        self.play(Write(g2))

        arr_bc = _arrow(ca, cc, color=C_W)
        lbl_bc = Tex(r"$\vec{b}+\vec{c}$", color=C_W, font_size=24).next_to(arr_bc.get_center(), DOWN*0.2)
        self.play(GrowArrow(arr_bc), Write(lbl_bc))
        self.next_slide()

        self.play(GrowArrow(arr_res))
        self.next_slide()

        eq = MathTex("=", font_size=42).move_to(UP*1)
        self.play(FadeIn(g1), Write(eq))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 23 · PropiedadConmutativa
# ===========================================================================
class PropiedadConmutativa(Slide):
    def construct(self) -> None:
        self.title = _title("23. Propiedades de la Suma (II)")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"5. \textbf{Propiedad Conmutativa}: El orden de los sumandos no altera el resultado.\\ "
            r"$\vec{u} + \vec{v} = \vec{v} + \vec{u}$"
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 5, 1], y_range=[-1, 4, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        u_v, v_v = np.array([3, 0.5, 0]), np.array([0.5, 2.5, 0])
        tip = self.plane.c2p(*(u_v + v_v))
        co  = self.plane.c2p(0, 0)

        u1 = _arrow(co, self.plane.c2p(*u_v), color=C_U)
        v1 = _arrow(self.plane.c2p(*u_v), tip, color=C_V)
        self.play(GrowArrow(u1), GrowArrow(v1))
        self.next_slide()

        v2 = _arrow(co, self.plane.c2p(*v_v), color=C_V)
        u2 = _arrow(self.plane.c2p(*v_v), tip, color=C_U)
        self.play(GrowArrow(v2), GrowArrow(u2))
        self.play(Flash(tip, color=C_HL, flash_radius=0.4))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 24 · RestaComoOpuesto
# ===========================================================================
class RestaComoOpuesto(Slide):
    def construct(self) -> None:
        self.title = _title("24. Diferencia de Vectores (como Opuesto)")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"La resta o diferencia se define como la suma del primero\\ "
            r"con el opuesto del segundo:\\ "
            r"$\vec{u} - \vec{v} = \vec{u} + (-\vec{v})$"
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 5, 1], y_range=[-2.5, 4, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        co    = self.plane.c2p(0, 0)
        u_p   = self.plane.c2p(3, 1)
        v_p   = self.plane.c2p(1, 2)
        u_arr = _arrow(co, u_p, color=C_U)
        v_arr = _arrow(co, v_p, color=C_V)
        self.play(GrowArrow(u_arr), GrowArrow(v_arr))
        self.next_slide()

        neg_v = _arrow(co, self.plane.c2p(-1, -2), color=C_NEG)
        self.play(ReplacementTransform(v_arr, neg_v))
        self.next_slide()

        self.play(neg_v.animate.shift(u_p - co))
        res = _arrow(co, self.plane.c2p(2, -1), color=C_DIFF)
        self.play(GrowArrow(res))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 25 · RestaOtraDiagonal
# ===========================================================================
class RestaOtraDiagonal(Slide):
    def construct(self) -> None:
        self.title = _title("25. Resta vía Regla del Paralelogramo")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"Alternativamente, si dibujamos $\vec{u}$ y $\vec{v}$ desde un mismo origen,\\ "
            r"la \textbf{diagonal principal} del paralelogramo es la suma,\\ "
            r"y la \textbf{otra diagonal} (desde $\vec{v}$ hacia $\vec{u}$) es la \textbf{resta}.",
            font_size=30,
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 5, 1], y_range=[-1, 4, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        cu = self.plane.c2p(3, 1)
        cv = self.plane.c2p(1, 2.5)
        co = self.plane.c2p(0, 0)
        u_arr = _arrow(co, cu, color=C_U)
        v_arr = _arrow(co, cv, color=C_V)
        self.play(GrowArrow(u_arr), GrowArrow(v_arr))
        self.next_slide()

        d_arr = _arrow(cv, cu, color=C_DIFF)
        dl    = MathTex(r"\vec{u}-\vec{v}", color=C_DIFF).next_to(d_arr.get_center(), UP * 0.2)
        self.play(GrowArrow(d_arr), Write(dl))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 26 · RestaAnalitica   (pure-theory — two cascading blocks)
# ===========================================================================
class RestaAnalitica(Slide):
    def construct(self) -> None:
        self.title = _title("26. Expresión Analítica de la Resta")
        self.play(Write(self.title))
        self.next_slide()

        t1 = _theory_block(
            r"La resta de dos vectores es otro vector con la resta de las\\ "
            r"componentes homólogas:\\ "
            r"$\implies \vec{u} - \vec{v} = (x_1-x_2, y_1-y_2)$"
        )
        self.play(Write(t1))
        self.next_slide()

        t2 = _theory_block(
            r"\textbf{Ejemplo Numérico}:\\ "
            r"Sean $\vec{u}=(-2, 3)$ y $\vec{v}=(1, 2)$.\\ "
            r"$\implies \vec{u}-\vec{v} = (-2-1, 3-2) = (-3, 1)$",
            font_size=30,
        ).next_to(t1, DOWN, buff=0.5)
        self.play(Write(t2))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 27 · VectorDosPuntos
# ===========================================================================
class VectorDosPuntos(Slide):
    def construct(self) -> None:
        self.title = _title("27. Vector determinado por dos puntos")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"Los puntos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$ determinan el vector $\vec{P_1P_2}$.\\ "
            r"Al restar los vectores de posición obtenemos sus componentes:\\ "
            r"$\vec{P_1P_2} = \vec{OP_2} - \vec{OP_1} = (x_2 - x_1, y_2 - y_1)$.",
            font_size=30,
        )
        self.play(Write(theory))
        self.next_slide()
        
        self.plane = _plane(x_range=[-1, 6, 1], y_range=[-1, 5, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        co = self.plane.c2p(0, 0)
        p1 = self.plane.c2p(1, 2)
        p2 = self.plane.c2p(5, 4)
        
        o_p1 = _arrow(co, p1, color=C_U)
        o_p2 = _arrow(co, p2, color=C_V)
        self.play(GrowArrow(o_p1), GrowArrow(o_p2))
        
        l1 = MathTex("P_1", font_size=24).next_to(p1, LEFT)
        l2 = MathTex("P_2", font_size=24).next_to(p2, UP)
        self.play(Write(l1), Write(l2))
        self.next_slide()

        p1_p2 = _arrow(p1, p2, color=C_HL)
        l3 = MathTex(r"\vec{P_1P_2}", color=C_HL).next_to(p1_p2.get_center(), UP*0.3)
        self.play(GrowArrow(p1_p2), Write(l3))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()

# ===========================================================================
# 28 · PuntoMedioSegmento
# ===========================================================================
class PuntoMedioSegmento(Slide):
    def construct(self) -> None:
        self.title = _title("28. Punto medio de un segmento")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"Las coordenadas del punto medio $P_m$ del segmento $\vec{P_1P_2}$\\ "
            r"se obtienen promediando las componentes de sus extremos:\\ "
            r"$P_m = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$.",
            font_size=30,
        )
        self.play(Write(theory))
        self.next_slide()
        
        self.plane = _plane(x_range=[-1, 6, 1], y_range=[-1, 5, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        p1 = self.plane.c2p(1, 2)
        p2 = self.plane.c2p(5, 4)
        pm = self.plane.c2p(3, 3)

        seg = Line(p1, p2, color=C_U, stroke_width=4)
        d1 = Dot(p1, color=C_U)
        d2 = Dot(p2, color=C_U)
        l1 = MathTex("P_1(1,2)", font_size=24).next_to(p1, UL)
        l2 = MathTex("P_2(5,4)", font_size=24).next_to(p2, UR)

        self.play(FadeIn(seg), Create(d1), Create(d2), Write(l1), Write(l2))
        self.next_slide()

        dm = Dot(pm, color=C_HL, radius=0.1)
        lm = MathTex("P_m(3,3)", font_size=24, color=C_HL).next_to(pm, DR, buff=0.1)
        self.play(FadeIn(dm), Write(lm))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()
