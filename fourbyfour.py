from manim import *

class dettricks(MovingCameraScene):
    def construct(self):
        problem = Tex("6.8 Problem 1k", color = PINK).to_corner(UL).add_updater(
            lambda x: x.to_corner(UL)
        )
        self.play(FadeIn(problem))
        mtx = Matrix([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]], color=BLUE)
        mtx4 = Matrix(
            [["a", "b", "c", "d"], 
            ["e", "f", "g", "h"], 
            ["i", "j", "k", "l"],
            ["m", "n", "o", "p"]], 
            color=BLUE
            ).move_to(mtx)

        mtx5 = Matrix(
            [["a", "b", "c", "d", "e"], 
            ["f", "g", "h", "i", "j"], 
            ["k", "l", "m", "n", "o"],
            ["p", "q", "r", "s", "t"],
            ["u", "v", "w", "x", "y"]], 
            color=BLUE
            ).move_to(mtx)
        

        movingvals = [
            3, 4, 5
        ]

        self.play(Write(mtx))

        for i, m in zip(movingvals, [mtx, mtx4, mtx5]):
            self.play(Transform(mtx, m))
            print(i)
            rowrect = SurroundingRectangle(m.get_rows()[0], color = GREEN).set_fill(GREEN, opacity = .7)
            colrect = SurroundingRectangle(m.get_columns()[0], color = YELLOW).set_fill(YELLOW, opacity = .7)
            self.play(Create(rowrect), Create(colrect))
            for x in range(1, i):
                self.play(colrect.animate.move_to(m.get_columns()[x]))
            self.play(FadeOut(rowrect, colrect))

        new_vals = [
            "a", "a", "a", "a", "a", 
            "0", "a", "a", "a", "a", 
            "0", "0", "a", "a", "a",
            "0", "0", "0", "a", "a",
            "0", "0", "0", "0", "a",
        ]

        ent = mtx.get_entries()
        print(len(mtx.get_entries()))
        for entry in range(len(ent)):
            self.play(Transform(ent[entry], MathTex(new_vals[entry]).move_to(ent[entry])), run_time = .06)
        det = get_det_text(mtx)
        self.remove(mtx)
        mtx = Matrix(
            [
            ["a", "a", "a", "a", "a"], 
            ["0", "a", "a", "a", "a"], 
            ["0", "0", "a", "a", "a"],
            ["0", "0", "0", "a", "a"],
            ["0", "0", "0", "0", "a"],
        ]
        )
        self.add(mtx)


        question = MathTex("= ?", font_size = 60).next_to(det)
        question.set_color(YELLOW)

        self.play(Write(det), Write(question))

        self.wait(.3)
        self.play(FadeOut(det, question))

        rowrect = SurroundingRectangle(mtx.get_rows()[-1], color = GREEN)
        colrect = SurroundingRectangle(mtx.get_columns()[-1], color = YELLOW).set_fill(YELLOW, opacity = .7)

        self.play(Create(rowrect))
        b = Brace(mtx.get_entries()[20:24])
        lbl = Tex("zeroes!").move_to(b.get_center() + [0, -1, 0])
        z = VGroup(b, lbl)
        self.play(Create(z))
        self.wait(.3)
        self.play(FadeOut(rowrect, z))


        self.play(mtx.animate.move_to(LEFT * 3))


        rowrect = SurroundingRectangle(mtx.get_rows()[-1], color = GREEN)
        colrect = SurroundingRectangle(mtx.get_columns()[-1], color = YELLOW).set_fill(YELLOW, opacity = .7)

        ent = mtx.get_entries()
        p = SurroundingRectangle(VGroup(*[ent[x] for x in [
            0, 18
        ]])).set_color(PURPLE)
        eq = MathTex("det = ", "a").move_to([2, 2, 0])
        self.play(rowrect.animate.set_fill(GREEN, opacity = .7), Create(colrect))
        self.play(Create(p), Write(eq))

        self.play(
            Transform(rowrect, SurroundingRectangle(VGroup(*[ent[x] for x in [15, 16, 17,18]]), color = GREEN).set_fill(GREEN, opacity = .7)),
            Transform(colrect, SurroundingRectangle(VGroup(*[ent[x] for x in [3, 8, 13, 18]]), color = YELLOW).set_fill(YELLOW, opacity = .7)),
            Transform(p, SurroundingRectangle(VGroup(*[ent[x] for x in [0, 12]]), color = PURPLE)),
            Transform(eq, MathTex("det = ", "a", "*a").move_to([2, 2, 0]))
        )

        self.play(
            Transform(rowrect, SurroundingRectangle(VGroup(*[ent[x] for x in [10, 12]]), color = GREEN).set_fill(GREEN, opacity = .7)),
            Transform(colrect, SurroundingRectangle(VGroup(*[ent[x] for x in [2, 12]]), color = YELLOW).set_fill(YELLOW, opacity = .7)),
            Transform(p, SurroundingRectangle(VGroup(*[ent[x] for x in [0, 6]]), color = PURPLE)),
            Transform(eq, MathTex("det = ", "a", "*a", "*a").move_to([2, 2, 0]))
        )

        ad = Line(ent[0].get_center(), ent[6].get_center())
        cb = Line(ent[1].get_center(), ent[5].get_center())

        self.play(Transform(eq, MathTex("det = ", "a", "*a", "*a", "*(a*d", "-", "b*c)").next_to(eq.get_left())))

        self.play(Create(ad), Transform(eq[4], MathTex("*(a*a").move_to(eq[4])))
        self.play(Create(cb), Transform(eq[6], MathTex("a*0)").move_to(eq[6])))
        self.play(Transform(eq[1:], MathTex("a^5").set_color(YELLOW).move_to(eq[1])))

        self.wait()
