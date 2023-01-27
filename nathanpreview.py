from manim import *

class preview(Scene):
    def construct(self):
        leibniz_formula = MathTex(r"\sum_{\sigma\in S_n}\mathrm{sgn}(\sigma) \prod_{i=0}^n a_{i,\sigma_i}").scale(2).shift(UP)
        words = Text("Leibniz Formula").shift(DOWN)
        g = VGroup(leibniz_formula, words)

        s = SurroundingRectangle(g, buff=MED_LARGE_BUFF).set_color(WHITE)

        rec = Tex("'The Leibniz Formula'",  "-Nathan Birkett").shift(DOWN * 2.4)
        rec[0].set_color(YELLOW)
        rec[1].set_color(RED)   

        self.play(Create(s), FadeIn(rec))
        self.play(Write(leibniz_formula))
        self.play(Write(words))
