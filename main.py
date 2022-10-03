from manim import *
class DefaultTemplate(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(BLUE, opacity=0.5)  # set color and transparency
        circle.set_stroke(BLUE_E, width=4)

        square = Square()  # create a square
        square.flip(RIGHT)  # flip horizontally
        square.rotate(-3 * TAU / 8)  # rotate a certain amount

        # self.play(Create(square))  # animate the creation of the square
        # self.play(Transform(square, circle))  # interpolate the square into the circle
        # self.play(FadeOut(square))  # fade out animation

        self.play(Create(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()
        self.play(FadeOut(circle))

        text = MathTex(
            "\\frac{d}{dx}f(x)g(x) = ","f(x)\\frac{d}{dx}g(x)", "+", 
            "g(x)\\frac{d}{dx}f(x)"
        )

        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        
        self.play(
            Create(framebox1), 
            )
        self.wait()
        self.play(
            ReplacementTransform(framebox1, framebox2),
        )
        self.play(FadeOut(text, framebox2))
        self.wait()

        eq1 = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!}x^n + \cdots"
        )
        eq1.set_color_by_tex("x", GREEN)
        text1 = MarkupText(
            "<u>Incorrect Substring Latex</u>"
        ).next_to(eq1, UP * 3)

        text_group = Group(eq1, text1).move_to(UP * 2)
        self.add(text_group)
        self.play(FadeIn(text_group))
        self.wait()

        eq2 = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!}x^n + \cdots",
            substrings_to_isolate = "x"
        )
        eq2.set_color_by_tex("x", GOLD)
        text2 = MarkupText(
            "<u>Correct Substring Latex</u>"
        ).next_to(eq2, UP*3)
        text_group2 = Group(eq2, text2).move_to(DOWN * 2)
        self.add(text_group2)
        self.play(FadeIn(text_group2))
        self.wait()

        self.play(FadeOut(text_group, text_group2))
