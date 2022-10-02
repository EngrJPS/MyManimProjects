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
        self.wait()


