from manim import *
from numpy import diff

class BooleanOperations(Scene):
    def construct (self):
        ellipse1 = Ellipse(
            width=4.0,
            height=5.0,
            fill_opacity= 0.5,
            color= BLUE,
            stroke_width = 10
        ).move_to(LEFT)

        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)
        text = MarkupText(
            "<u>Boolean Operations</u>"
        ).next_to(ellipse1, UP * 3)
        ellipse_group = Group(text, ellipse1, ellipse2).move_to(LEFT * 3)

        self.play(FadeIn(ellipse_group))

        Intersec = Intersection(ellipse1, ellipse2, color=GOLD, fill_opacity=0.5)
        self.play(Intersec.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))
        Int_Tex = MathTex ("Intersection", font_size=23).next_to(Intersec, UP)
        self.play(FadeIn(Int_Tex))
        self.wait()

        Un = Union(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        Un_text = MathTex("Union", font_size=23)
        self.play(Un.animate.scale(0.3).next_to(Intersec, DOWN, buff=Un_text.height * 3))
        Un_text.next_to(Un, UP)
        self.play(FadeIn(Un_text))

        self.wait

        Ex = Exclusion(ellipse1, ellipse2, color=DARK_BROWN, fill_opacity=0.5)
        Ex_text = MathTex("Exclusion", font_size=23)
        self.play(Ex.animate.scale(0.3).next_to(Un, DOWN, buff=Ex_text.height * 3))
        Ex_text.next_to(Ex, UP)
        self.play(FadeIn(Ex_text))

        self.wait

        Diff = Difference(ellipse1, ellipse2, color=GRAY, fill_opacity=0.5)
        diff_text = MathTex("Difference", font_size=23)
        self.play(Diff.animate.scale(0.3).next_to(Un, LEFT, buff=diff_text.height * 3.5))
        diff_text.next_to(Diff, UP)
        self.play(FadeIn(diff_text))

        self.wait
