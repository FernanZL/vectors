"""
main.py
=======
Unified entry point for the complete Vector Lecture presentation.

Usage:
    uv run manim -ql main.py CompleteVectorLecture

All sections are composed into a single Slide by temporarily grafting each
section class's private helpers onto the master instance before calling its
construct() method, then cleaning up so the next section starts fresh.
"""
from __future__ import annotations
import types

from manim import *
from manim_slides import ThreeDSlide   # ThreeDSlide is a superset of Slide

from sections import s1_intro, s2_equality, s3_algebra, s4_scalar


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _run_section(master: "CompleteVectorLecture", section_cls: type) -> None:
    """Temporarily bind *section_cls*'s own methods onto *master* and run construct.

    This lets every helper (``_setup``, ``_theory``, ``_visualize``, ``_cleanup``,
    or any other private method) be resolved correctly when the section's
    ``construct`` calls ``self.<method>()``.
    """
    patched: list[str] = []
    for name, val in vars(section_cls).items():
        # Bind every method the section defines (except dunder and construct itself)
        if callable(val) and not name.startswith("__") and name != "construct":
            setattr(master, name, types.MethodType(val, master))
            patched.append(name)

    section_cls.construct(master)

    # Clean up so no stale helpers leak into the next section
    for name in patched:
        try:
            delattr(master, name)
        except AttributeError:
            pass

    # After a 3D section, restore flat front-facing camera so 2D slides look correct.
    # zoom=1 is critical — without it the zoom=0.6 set by 3D sections persists.
    if issubclass(section_cls, ThreeDSlide):
        master.set_camera_orientation(phi=0, theta=-90 * DEGREES, gamma=0, zoom=1)


# ---------------------------------------------------------------------------
# Master class
# ---------------------------------------------------------------------------

class CompleteVectorLecture(ThreeDSlide):
    """Plays every section in chronological order as one continuous presentation."""

    def construct(self) -> None:
        # ── 1. Introduction to Vectors ──────────────────────────────────────
        _run_section(self, s1_intro.SegmentoRecta)
        _run_section(self, s1_intro.VectorOrigenExtremo)
        _run_section(self, s1_intro.VectorDirection)
        _run_section(self, s1_intro.VectorSense)
        _run_section(self, s1_intro.VectorMagnitude)
        _run_section(self, s1_intro.VectorNulo)
        _run_section(self, s1_intro.VectorUnitario)
        _run_section(self, s1_intro.SistemaCoordenadas)
        _run_section(self, s1_intro.ComponentesR2)
        _run_section(self, s1_intro.ComponentesR3)     # ThreeDSlide
        _run_section(self, s1_intro.ModuloPitagorasR2)
        _run_section(self, s1_intro.ModuloPitagorasR3) # ThreeDSlide

        # ── 2. Vector Equality ───────────────────────────────────────────────
        _run_section(self, s2_equality.VectorLibre)
        _run_section(self, s2_equality.IgualdadGeometrica)
        _run_section(self, s2_equality.IgualdadAnalitica)
        _run_section(self, s2_equality.VectorOpuesto)

        # ── 3. Vector Algebra (Addition & Subtraction) ───────────────────────
        _run_section(self, s3_algebra.SumaIntroduccion)
        _run_section(self, s3_algebra.SumaProtocolo)
        _run_section(self, s3_algebra.SumaAnalitica)
        _run_section(self, s3_algebra.ReglaParalelogramo)
        _run_section(self, s3_algebra.ReglaPoligonal)
        _run_section(self, s3_algebra.PropiedadesSumaI)
        _run_section(self, s3_algebra.PropiedadAsociativaGeometrica)
        _run_section(self, s3_algebra.PropiedadConmutativa)
        _run_section(self, s3_algebra.RestaComoOpuesto)
        _run_section(self, s3_algebra.RestaOtraDiagonal)
        _run_section(self, s3_algebra.RestaAnalitica)
        _run_section(self, s3_algebra.VectorDosPuntos)
        _run_section(self, s3_algebra.PuntoMedioSegmento)

        # ── 4. Scalar Operations ─────────────────────────────────────────────
        _run_section(self, s4_scalar.ProductoPorEscalarIntro)
        _run_section(self, s4_scalar.ProductoPorEscalarCasosA)
        _run_section(self, s4_scalar.ProductoPorEscalarCasosB)
        _run_section(self, s4_scalar.PropiedadesProductoPorEscalar)
        _run_section(self, s4_scalar.ParalelismoAnalitico)
        _run_section(self, s4_scalar.VersoresFundamentales)
        _run_section(self, s4_scalar.CombinacionLineal)
        _run_section(self, s4_scalar.DependenciaIndependenciaLineal)
        _run_section(self, s4_scalar.PropiedadesDependenciaLineal)
