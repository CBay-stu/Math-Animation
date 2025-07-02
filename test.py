from manim import *


# Just drawing the squid game to test

class SquidGameLogo(Scene):
    def construct(self):
        
        square = Square()
        triangle = Triangle()

        square.set_fill(RED, opacity=0.5)
        triangle.set_fill(GREEN, opacity=0.5)

        square.shift(DOWN)
        triangle.next_to(square, UP, buff=0.5)

        self.play(FadeIn(square), FadeIn(triangle))