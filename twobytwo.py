from manim import *

class basicDet(Scene):
    def construct(self):

        mtx = Matrix([["a", "b"], ["c", "d"]], color=BLUE)

        det = MathTex("\det\left(", mtx, "\right)", color= GREEN)
        self.add(mtx)

        form = MathTex("\det",  "=", "ad", "-", "bc").move_to(DOWN * 2)
        form[0].set_color(YELLOW)
        self.add(form)

        self.wait(1)

        new_vals = [
            MathTex("2"), MathTex("4"),
            MathTex("3"), MathTex("5")
        ]

        print(mtx[1])

        ent = mtx.get_entries()

        problem = Tex("6.3 Problem 3a", color = PINK).to_corner(UL).add_updater(
            lambda x: x.to_corner(UL)
        )
        self.play(Write(problem), run_time = .3)
        for entry in range(len(ent)):
            self.play(Transform(ent[entry], new_vals[entry].move_to(ent[entry])))
        
        self.wait(1)

        adSurrounding = VGroup(
            SurroundingRectangle(mtx.get_entries()[0]),
            SurroundingRectangle(mtx.get_entries()[3])
        )

        bcSurrounding = VGroup(
            SurroundingRectangle(mtx.get_entries()[1]),
            SurroundingRectangle(mtx.get_entries()[2])
        )

        self.play(Create(adSurrounding))
        self.play(
            Transform(
                form[2], 
                MathTex("10").move_to(form[2])
                ),
            FadeOut(adSurrounding)
            )

        self.play(Create(bcSurrounding))
        self.play(
            Transform(
                form[4], 
                MathTex("12").move_to(form[4])
                ),
            FadeOut(bcSurrounding)
            )

        self.play(
            Transform(
                form[2:], 
                MathTex("-2").move_to(form[2])
                )
            )

        itExists = VGroup(Tex("An Inverse exists!", color = YELLOW).move_to([4, -1, 0]))
        itExists.add(Arrow(itExists[0], form.get_right(), color = YELLOW))

        self.play(Create(itExists[1]))
        self.play(Create(itExists[0]))
        

