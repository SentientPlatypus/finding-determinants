from manim import *

class detofthree(MovingCameraScene):
    def construct(self):
        problem = Tex("6.8 Problem 3c", color = PINK).to_corner(UL).add_updater(
            lambda x: x.to_corner(UL)
        )

        self.add(problem)
        mtx = Matrix([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]], color=BLUE)
        det = get_det_text(mtx)
        question = MathTex("= ?", font_size = 60).move_to(det.get_right() + [1, 0, 0])
        question.set_color(YELLOW)
        self.play(Write(mtx))
        self.play(Write(det))
        self.play(Write(question))

        self.wait(.5)

        new_vals = [
            MathTex("-1"), MathTex("3"), MathTex("1"), 
            MathTex("2"), MathTex("9"), MathTex("1"), 
            MathTex("5"), MathTex("-6"), MathTex("1"), 

        ]

        ent = mtx.get_entries()
        for entry in range(len(ent)):
            self.play(Transform(ent[entry], new_vals[entry].move_to(ent[entry])), run_time = .1)

        self.play(FadeOut(det, question))
        self.play(mtx.animate.move_to(UP * 1.5))

        rowrect = SurroundingRectangle(mtx.get_rows()[0])
        colrect = SurroundingRectangle(mtx.get_columns()[0])

        self.play(Create(rowrect))
        for x in range(1, 3):
            self.play(rowrect.animate.move_to(mtx.get_rows()[x]))

        self.play(FadeOut(rowrect))
        self.play(Create(colrect))
        for x in range(1, 3):
            self.play(colrect.animate.move_to(mtx.get_columns()[x]))
    
        colrect.move_to(mtx.get_columns()[0])
        rowrect.move_to(mtx.get_rows()[0]).set_color(GREEN)
        self.play(Create(colrect))
        self.wait(.5)
        self.play(Create(rowrect))

        self.play(
            colrect.animate.set_fill(YELLOW, opacity = .7),
            rowrect.animate.set_fill(GREEN, opacity = .7),
        )


        as_we_go_through = [
            [[5, 6, 8, 9]],
            [[2, 3], [8, 9]],
            [[2, 3, 5, 6]]
        ]

        ent = mtx.get_entries()
        rowcounter = 0
        for x in as_we_go_through:
            self.play(rowrect.animate.move_to(mtx.get_rows()[rowcounter]))
            s = []
            for lnums in x:
                t = VGroup(*[ent[z - 1] for z in lnums])
                sl = SurroundingRectangle(t).set_color(PURPLE)
                s.append(sl)
                self.play(Create(sl))
            self.play(FadeOut(*s))
            rowcounter += 1
            


        self.wait()




class showtriangle(Scene):
    def construct(self):
        problem = Tex("6.8 Problem 3c", color = PINK).to_corner(UL).add_updater(
            lambda x: x.to_corner(UL)
        )
        ax = Axes([-3, 8, 1], [-7, 10, 1])
        self.play(Create(ax), Write(problem))


        tricoords = [
            ax.c2p(*[-1, 3, 0]),
            ax.c2p(*[2, 9, 0]),
            ax.c2p(*[5, -6, 0]),
        ]

        labels = [
            [-1, 3, 0],
            [2,9,0],
            [5, -6, 0]
        ]

        triangle = Polygon(
            *tricoords,
            fill_color = BLUE
        )

        self.play(Create(triangle))

        for (x, y, z), (cx, cy, cz) in zip(tricoords, labels):
            px, py = np.around(ax.point_to_coords(ax.c2p(*[x, y, z])), decimals=2)
            circ = Dot([px, py, 0])

            blabel = MathTex(f"({cx}, {cy})").next_to([x, y, z])
            self.play(Create(blabel), Create(circ))

        A = Tex("A").move_to(triangle)

        self.play(triangle.animate.set_fill(BLUE, opacity = .5), FadeIn(A))


        Atop = MathTex(r"A= \frac {1} {2}").move_to([2, 2.5, 0])
        mtx = MobjectMatrix([
            [MathTex("-1"), MathTex("3"), MathTex("1")], 
            [MathTex("2"), MathTex("9"), MathTex("1")], 
            [MathTex("5"), MathTex("-6"), MathTex("1")], 
        ], 
        left_bracket = "|",
        right_bracket = "|"
        ).next_to(Atop)

        self.play(
            Write(Atop),
            Write(mtx)
        )

        self.wait()