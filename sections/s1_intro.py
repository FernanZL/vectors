"""
s1_intro.py
===========
Part I: Introduction to Vectors and their Components.
Scenes 1 through 12.
"""

from __future__ import annotations
from manim import *
from manim_slides import Slide, ThreeDSlide

from shared_helpers import (
    C_U, C_V, C_W, C_NEG, C_HL, C_AX, C_3D,
    _plane, _arrow, _title, _theory_text, _theory_block, _compress_to_header,
)


# ===========================================================================
# 1 · SegmentoRecta
# ===========================================================================
class SegmentoRecta(Slide):
    def construct(self) -> None:
        self.title = _title("1. Introducción al Segmento de Recta")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"Dos puntos $a$ y $b$ que pertenecen a una recta $R$ determinan\\ "
            r"un segmento denotado por $\overline{ab}$."
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 6, 1], y_range=[-1, 5, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        pa, pb = self.plane.c2p(1, 1), self.plane.c2p(4, 3)
        R  = DashedLine(
            self.plane.c2p(-0.5, 0), self.plane.c2p(5.5, 4),
            color=C_AX, dash_length=0.15,
        )
        rl = MathTex("R", font_size=24, color=C_AX).next_to(R.get_end(), UP)
        dot_a = Dot(pa, color=C_V)
        dot_b = Dot(pb, color=C_V)
        la = MathTex("a(1,1)", font_size=24, color=C_V).next_to(dot_a, DOWN)
        lb = MathTex("b(4,3)", font_size=24, color=C_V).next_to(dot_b, UP)
        segment = Line(pa, pb, color=C_U, stroke_width=4)

        self.play(Create(R), Write(rl))
        self.play(FadeIn(dot_a), Write(la), FadeIn(dot_b), Write(lb))
        self.next_slide()
        self.play(Create(segment))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 2 · VectorOrigenExtremo
# ===========================================================================
class VectorOrigenExtremo(Slide):
    def construct(self) -> None:
        self.title = _title("2. Definición de Vector Geométrico")
        self.play(Write(self.title))
        self.next_slide()

        t1 = _theory_block(
            r"Si esos dos puntos se dan con un cierto \textbf{orden}, queda determinado un vector.\\"
            r"El primer punto, $a$, se llama \textbf{origen} o punto de aplicación.\\"
            r"El segundo, $b$, se llama \textbf{extremo}.",
            font_size=30,
        )
        self.play(Write(t1))
        self.next_slide()
        
        t2 = _theory_block(
            r"Se denota como $\vec{ab}$ o $\mathbf{ab}$. Es un \textbf{segmento orientado}.",
            font_size=30,
        ).next_to(t1, DOWN, buff=0.2).align_to(t1, LEFT)
        self.play(Write(t2))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 6, 1], y_range=[-1, 5, 1])
        _compress_to_header(self, VGroup(t1, t2), self.title, self.plane)
        self.next_slide()

        pa, pb = self.plane.c2p(1, 1), self.plane.c2p(4, 3)
        origin_dot = Dot(pa, color=C_U)
        ext_dot    = Dot(pb, color=C_U)
        lo  = Tex(r"$a$ (origen)",  font_size=24, color=C_U).next_to(origin_dot, DOWN)
        le  = Tex(r"$b$ (extremo)", font_size=24, color=C_U).next_to(ext_dot,    UP)
        arr = _arrow(pa, pb, color=C_U)
        lbl = MathTex(r"\vec{ab}", font_size=32, color=C_HL).next_to(arr.get_center(), UL * 0.5)

        self.play(FadeIn(origin_dot), Write(lo))
        self.next_slide()
        self.play(FadeIn(ext_dot), Write(le))
        self.next_slide()
        self.play(GrowArrow(arr), Write(lbl))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 3 · VectorDirection
# ===========================================================================
class VectorDirection(Slide):
    def construct(self) -> None:
        self.title = _title("3. Característica: Dirección")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"\textbf{Dirección}: La dirección del vector está determinada por la recta $R$\\ "
            r"que lo contiene (llamada \textbf{recta soporte}) o la dirección de sus paralelas."
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 6, 1], y_range=[-1, 5, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        pa, pb = self.plane.c2p(1, 1), self.plane.c2p(4, 3)
        arr = _arrow(pa, pb, color=C_U)
        self.play(GrowArrow(arr))
        sup = DashedLine(self.plane.c2p(-0.5, 0), self.plane.c2p(5.5, 4), color=C_AX)
        sl  = Tex(r"Recta soporte $R$", font_size=24, color=C_AX).next_to(sup.get_start(), DOWN)
        self.play(Create(sup), Write(sl))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 4 · VectorSense
# ===========================================================================
class VectorSense(Slide):
    def construct(self) -> None:
        self.title = _title("4. Característica: Sentido")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"\textbf{Sentido}: Determinado por el orden del origen $a$ al extremo $b$.\\ "
            r"Se indica mediante la punta de flecha, que muestra hacia qué lado\\ "
            r"de la línea de acción se dirige."
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 6, 1], y_range=[-1, 5, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        pa, pb = self.plane.c2p(1, 1), self.plane.c2p(4, 3)
        arr = _arrow(pa, pb, color=C_U)
        self.play(GrowArrow(arr))
        for _ in range(2):
            self.play(arr.animate.set_color(C_V), run_time=0.4)
            self.play(arr.animate.set_color(C_U), run_time=0.4)
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 5 · VectorMagnitude
# ===========================================================================
class VectorMagnitude(Slide):
    def construct(self) -> None:
        self.title = _title("5. Característica: Módulo")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"\textbf{Módulo} (o norma): Es la longitud física del vector.\\ "
            r"Se simboliza encerrando al vector entre barras: $|\vec{ab}|$."
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 6, 1], y_range=[-1, 5, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        pa, pb = self.plane.c2p(1, 1), self.plane.c2p(4, 3)
        arr   = _arrow(pa, pb, color=C_U)
        brace = BraceBetweenPoints(arr.get_start(), arr.get_end(), color=C_HL)
        mag   = brace.get_tex(r"|\vec{ab}|").set_color(C_HL)
        self.play(GrowArrow(arr))
        self.play(GrowFromCenter(brace), Write(mag))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 6 · VectorNulo
# ===========================================================================
class VectorNulo(Slide):
    def construct(self) -> None:
        self.title = _title("6. Vector Nulo o Cero")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"\textbf{Vector Nulo}: Aquel vector cuyo módulo es cero ($|\vec{0}| = 0$).\\ "
            r"Su origen y extremo coinciden en el mismo punto.\\ "
            r"Por lo tanto, \textbf{no tiene dirección ni sentido definidos}."
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane()
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        point = self.plane.c2p(2, 1)
        arr   = _arrow(self.plane.c2p(0, 0), point, color=C_U)
        al    = MathTex(r"\vec{v}", font_size=26, color=C_U).next_to(arr, UP)
        self.play(GrowArrow(arr), Write(al))
        self.next_slide()

        nul_dot = Dot(self.plane.c2p(0, 0), color=C_HL)
        nl      = MathTex(r"\vec{0}", font_size=32, color=C_HL).next_to(nul_dot, DOWN)
        self.play(
            arr.animate.put_start_and_end_on(self.plane.c2p(0, 0), self.plane.c2p(0, 0)),
            FadeOut(al),
            FadeIn(nul_dot), Write(nl),
        )
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 7 · VectorUnitario
# ===========================================================================
class VectorUnitario(Slide):
    def construct(self) -> None:
        self.title = _title("7. Versor o Vector Unitario")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"\textbf{Versor}: Es todo vector $\vec{v}_0$ cuyo módulo es exactamente igual a uno.\\ "
            r"Es decir: $|\vec{v}_0| = 1$."
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 4, 1], y_range=[-1, 4, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        c0    = self.plane.c2p(0, 0)
        c1    = self.plane.c2p(1, 0)
        arr   = _arrow(c0, c1, color=C_V)
        lbl   = MathTex(r"\vec{v}_0", font_size=26, color=C_V).next_to(arr, DOWN)
        brace = BraceBetweenPoints(c0, c1, color=C_HL)
        bl    = brace.get_tex("1").set_color(C_HL)
        self.play(GrowArrow(arr), Write(lbl))
        self.play(GrowFromCenter(brace), Write(bl))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 8 · SistemaCoordenadas
# ===========================================================================
class SistemaCoordenadas(Slide):
    def construct(self) -> None:
        self.title = _title("8. Sistemas de Coordenadas")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"Para trabajar numéricamente, introducimos \textbf{sistemas cartesianos}.\\ "
            r"1. \textbf{En el plano} ($\mathbb{R}^2$): $(x,y)$ (dos dimensiones).\\ "
            r"2. \textbf{En el espacio} ($\mathbb{R}^3$): $(x,y,z)$ (tres dimensiones).\\ "
            r"Utilizamos la notación $\mathbb{V}$ para hablar de forma simultánea de ambos.",
            font_size=30,
        )
        self.play(Write(theory))
        self.next_slide()

        # Compress theory then show comparison diagrams below (no plane needed)
        _compress_to_header(self, theory, self.title)
        self.next_slide()

        # ── Left: genuine 2D coordinate axes ─────────────────────────────
        ax2 = Axes(
            x_range=[-1, 3], y_range=[-1, 3],
            axis_config={"color": C_AX, "include_tip": True},
        ).scale(0.6).shift(LEFT * 3 + DOWN * 0.8)
        xl2 = Tex("x", font_size=22, color=C_AX).next_to(ax2.x_axis.get_end(), RIGHT, buff=0.05)
        yl2 = Tex("y", font_size=22, color=C_AX).next_to(ax2.y_axis.get_end(), UP,    buff=0.05)
        l2  = Tex(r"$\mathbb{R}^2$", font_size=34, color=C_W).next_to(ax2, UP, buff=0.25)

        # ── Right: hand-drawn isometric 3D axes ──────────────────────────
        o3  = np.array([2.6, -0.9, 0])
        arm = 1.3
        ax3x = Arrow(o3, o3 + np.array([ arm,  -0.25 * arm, 0]), color=C_AX, buff=0, stroke_width=3)
        ax3y = Arrow(o3, o3 + np.array([-0.7 * arm, -0.35 * arm, 0]), color=C_AX, buff=0, stroke_width=3)
        ax3z = Arrow(o3, o3 + np.array([0, arm, 0]), color=C_AX, buff=0, stroke_width=3)
        xl3  = Tex("x", font_size=22, color=C_AX).next_to(ax3x.get_end(), RIGHT + DOWN * 0.3, buff=0.05)
        yl3  = Tex("y", font_size=22, color=C_AX).next_to(ax3y.get_end(), DOWN + LEFT * 0.2, buff=0.05)
        zl3  = Tex("z", font_size=22, color=C_AX).next_to(ax3z.get_end(), UP, buff=0.05)
        l3   = Tex(r"$\mathbb{R}^3$", font_size=34, color=C_W).move_to(o3 + UP * 1.9)
        ax3_grp = VGroup(ax3x, ax3y, ax3z, xl3, yl3, zl3)

        self.play(Create(ax2), Write(xl2), Write(yl2), Write(l2))
        self.next_slide()
        self.play(Create(ax3_grp), Write(l3))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 9 · ComponentesR2
# ===========================================================================
class ComponentesR2(Slide):
    def construct(self) -> None:
        self.title = _title("9. Componentes en el Plano (\u211d\u00b2)")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"Un vector con origen en $(0,0)$ y extremo $P(x_1, y_1)$ queda\\ "
            r"totalmente identificado por las coordenadas de su extremo.\\ "
            r"Escribimos: $\vec{v} = \vec{OP} = (x_1, y_1)$."
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 5, 1], y_range=[-1, 4, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        p     = self.plane.c2p(4, 3)
        arr   = _arrow(self.plane.c2p(0, 0), p, color=C_U)
        pl    = MathTex("P(4,3)", font_size=26, color=C_U).next_to(p, UR * 0.3)
        xl    = DashedLine(p, self.plane.c2p(4, 0), color=C_V)
        yl    = DashedLine(p, self.plane.c2p(0, 3), color=C_NEG)
        x_tex = MathTex("x_1=4", font_size=24, color=C_V).next_to(self.plane.c2p(4, 0), DOWN)
        y_tex = MathTex("y_1=3", font_size=24, color=C_NEG).next_to(self.plane.c2p(0, 3), LEFT)

        self.play(GrowArrow(arr), Write(pl))
        self.play(Create(xl), Write(x_tex))
        self.play(Create(yl), Write(y_tex))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 10 · ComponentesR3   (3D — fixed-in-frame text, no compress animation)
# ===========================================================================
class ComponentesR3(ThreeDSlide):
    def construct(self) -> None:
        # phi=70° tilts the view to suppress the z-axis visually;
        # theta=-50° gives a clean isometric look.
        self.set_camera_orientation(phi=70 * DEGREES, theta=-50 * DEGREES)

        self.title = _title("10. Componentes en el Espacio (\u211d\u00b3)")
        self.add_fixed_in_frame_mobjects(self.title)
        self.play(Write(self.title))

        self.text = _theory_text(
            r"Un vector en $\mathbb{R}^3$ se expresa con 3 componentes ortogonales:\\ "
            r"$\vec{a} = (x_1, y_1, z_1)$.  Ejemplo: $\vec{a} = (2, 2, 1.5)$.",
        ).next_to(self.title, DOWN, buff=0.2).to_edge(LEFT, buff=0.5).scale(0.9)
        self.add_fixed_in_frame_mobjects(self.text)
        self.play(Write(self.text))
        self.next_slide()

        # Compact diagram: scale=0.4, shorter z_range, placed in lower-right
        ax = ThreeDAxes(
            x_range=[0, 3, 1], y_range=[0, 3, 1], z_range=[0, 2, 1],
            axis_config={"color": C_AX},
        ).scale(0.26).shift(RIGHT * 7 + DOWN * 6)
        self.play(Create(ax))

        O   = ax.c2p(0, 0, 0)
        P   = ax.c2p(2, 2, 1.5)
        Pxy = ax.c2p(2, 2, 0)
        arr = Arrow3D(O, P, color=C_U, thickness=0.025)
        proj = VGroup(
            DashedLine(P,   Pxy,             color=C_3D),
            DashedLine(Pxy, ax.c2p(2, 0, 0), color=C_V),
            DashedLine(Pxy, ax.c2p(0, 2, 0), color=C_NEG),
        )
        self.play(FadeIn(arr))
        self.play(Create(proj))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.remove_fixed_in_frame_mobjects(self.title, self.text)
        self.next_slide()


# ===========================================================================
# 11 · ModuloPitagorasR2
# ===========================================================================
class ModuloPitagorasR2(Slide):
    def construct(self) -> None:
        self.title = _title("11. Módulo vía Pitágoras en \u211d\u00b2")
        self.play(Write(self.title))
        self.next_slide()

        theory = _theory_block(
            r"Dado el vector $\vec{v} = (x_1, y_1)$, el módulo $|\vec{v}|$ es la hipotenusa\\ "
            r"del triángulo rectángulo donde $x_1, y_1$ son catetos.\\ "
            r"$\implies |\vec{v}|^2 = x_1^2 + y_1^2 \implies |\vec{v}| = +\sqrt{x_1^2 + y_1^2}$"
        )
        self.play(Write(theory))
        self.next_slide()

        self.plane = _plane(x_range=[-1, 5, 1], y_range=[-1, 4, 1])
        _compress_to_header(self, theory, self.title, self.plane)
        self.next_slide()

        p    = self.plane.c2p(4, 3)
        o    = self.plane.c2p(0, 0)
        arr  = _arrow(o, p, color=C_U)
        catx = Line(o, self.plane.c2p(4, 0), color=C_V,   stroke_width=4)
        caty = Line(self.plane.c2p(4, 0), p,  color=C_NEG, stroke_width=4)
        lx   = MathTex("x_1", font_size=24).next_to(catx, DOWN)
        ly   = MathTex("y_1", font_size=24).next_to(caty, RIGHT)
        lv   = MathTex(r"|\vec{v}|", font_size=28, color=C_HL).move_to(self.plane.c2p(1.5, 2))
        sq   = Square(side_length=0.2, color=C_AX).move_to(self.plane.c2p(3.9, 0.1))

        self.play(Create(catx), Write(lx))
        self.play(Create(caty), Write(ly))
        self.play(GrowArrow(arr), Write(lv))
        self.play(Create(sq))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


# ===========================================================================
# 12 · ModuloPitagorasR3   (3D — fixed-in-frame text, no compress animation)
# ===========================================================================
class ModuloPitagorasR3(ThreeDSlide):
    def construct(self) -> None:
        self.set_camera_orientation(phi=70 * DEGREES, theta=-50 * DEGREES)

        self.title = _title("12. Módulo vía Pitágoras doble en \u211d\u00b3")
        self.add_fixed_in_frame_mobjects(self.title)
        self.play(Write(self.title))

        t1 = _theory_text(r"En el espacio, Pitágoras se aplica dos veces:").next_to(self.title, DOWN, buff=0.2).to_edge(LEFT, buff=0.5).scale(0.85)
        self.add_fixed_in_frame_mobjects(t1)
        self.play(Write(t1))
        self.next_slide()

        # Compact diagram: scale=0.4, shorter ranges, placed in lower-right
        ax = ThreeDAxes(
            x_range=[0, 3, 1], y_range=[0, 3, 1], z_range=[0, 2, 1],
            axis_config={"color": C_AX},
        ).scale(0.26).shift(RIGHT * 7 + DOWN * 6)
        self.play(Create(ax))

        O  = ax.c2p(0, 0, 0)
        P  = ax.c2p(2, 2, 1.5)
        Q  = ax.c2p(2, 2, 0)
        Pxyz = ax.c2p(2, 0, 0)
        Pxyy = ax.c2p(0, 2, 0)

        lx = DashedLine(O, Pxyz, color=C_AX)
        ly = DashedLine(O, Pxyy, color=C_AX)
        proj_x = DashedLine(Pxyz, Q, color=C_AX)
        proj_y = DashedLine(Pxyy, Q, color=C_AX)
        self.play(Create(lx), Create(ly))
        self.play(Create(proj_x), Create(proj_y))
        self.next_slide()

        t2 = _theory_text(r"1. Diagonal de base: $\overline{OQ}^2 = x_1^2 + y_1^2$").next_to(t1, DOWN, buff=0.2).align_to(t1, LEFT).scale(0.85)
        self.add_fixed_in_frame_mobjects(t2)
        self.play(Write(t2))

        diag_base = DashedLine(O, Q, color=C_V)
        self.play(Create(diag_base))
        self.next_slide()

        t3 = _theory_text(r"2. Triángulo mayor: $|\vec{v}| = +\sqrt{x_1^2 + y_1^2 + z_1^2}$").next_to(t2, DOWN, buff=0.2).align_to(t1, LEFT).scale(0.85)
        self.add_fixed_in_frame_mobjects(t3)
        self.play(Write(t3))

        altura = DashedLine(Q, P, color=C_NEG)
        self.play(Create(altura))
        self.next_slide()

        arr = Arrow3D(O, P, color=C_U, thickness=0.025)
        self.play(FadeIn(arr))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))
        self.remove_fixed_in_frame_mobjects(self.title, t1, t2, t3)
        self.next_slide()
