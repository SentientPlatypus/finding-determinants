from manim import *

class basicDet(MovingCameraScene):
    def construct(self):

        mtx = Matrix([["a", "b"], ["c", "d"]], color=BLUE)

        det = MathTex("\det\left(", mtx, "\right)", color= GREEN)
        self.play(Write(mtx))

        form = MathTex("\det",  "=", "ad", "-", "bc").move_to(DOWN * 2)
        form[0].set_color(YELLOW)

        self.wait(1)
        self.play(Write(form))

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


        ##SO if we wanted to solve this problem:

        self.wait(.5)
        self.play(FadeOut(itExists, form))
        self.play(mtx.animate.move_to(LEFT * 2.5))

        abcd = Matrix([["a", "b"], ["c", "d"]], color=BLUE)
        eq = MathTex("=").move_to(abcd.get_right() + [.5, 0, 0])
        six_10_9_13 = Matrix([[6, 10], [9, 13]], color=BLUE).move_to(abcd.get_right() + [2, 0, 0])

        self.play(Write(abcd), Write(eq), Write(six_10_9_13))

        self.wait(.5)

        self.play(six_10_9_13.animate.move_to(RIGHT * 6))

        inversemtx = MathTex(r"\begin{bmatrix}  2 & 4\\ 3 & 5 \end{bmatrix}^{-1}", font_size = 60).move_to(mtx.get_left() + [-1.3, 0, 0])
        inversemtxl = MathTex(r"\begin{bmatrix}  2 & 4\\ 3 & 5 \end{bmatrix}^{-1}", font_size = 60).move_to(six_10_9_13.get_left() + [-1.3, 0, 0])


        

        self.play(Write(inversemtx), Write(inversemtxl))

        tocancel = VGroup(inversemtx, mtx)

        identitymax = Matrix([[1, 0], [0, 1]]).move_to(tocancel)

        self.play(
            ShowCreationThenFadeOut(Line(mtx.get_edge_center(UR), inversemtx.get_edge_center(DL)).set_stroke(YELLOW, width=3)),
            ReplacementTransform(tocancel, identitymax)
            )

        self.wait(.5)
        self.play(
            FadeOut(identitymax), 
            VGroup(abcd, eq, inversemtxl, six_10_9_13).animate.move_to(ORIGIN)
        )

        self.wait(.5)
        self.play(ShowCreationThenFadeOut(
                SurroundingRectangle(inversemtxl),

        ))


        form_for_2x2 = MathTex(r"\begin{bmatrix}  a & b\\  c & d\\\end{bmatrix}^{-1} =\frac {1} {ad- bc}\begin{bmatrix}d & -b \\-c & a\end{bmatrix}").move_to([-3.5, -2, 0])
        pointer = Arrow([0, -4, 0], form_for_2x2.get_bottom()).set_color(YELLOW)
        determinanttex = Tex("The determinant!").move_to([0, -3, 0]).set_color(YELLOW)
        self.play(Write(form_for_2x2))
        self.play(Create(pointer), Write(determinanttex))
        self.wait(.5)
        self.play(FadeOut(form_for_2x2, pointer, determinanttex))



        
        self.play(six_10_9_13.animate.move_to(RIGHT * 3.8))

        oneoverdet = MathTex(r"\frac {1} {-2}").move_to(mtx.get_right() + [2, 0, 0])
        inversemtxex = MobjectMatrix([[MathTex("2"), MathTex("4")], [MathTex("3"), MathTex("5")]]).move_to(mtx.get_right() + [4, 0, 0])

        self.play(
            Write(oneoverdet),
            ReplacementTransform(inversemtxl,  inversemtxex)
        )
        elements = inversemtxex.get_entries()

        self.play(Swap(elements[0], elements[3]))
        self.play(
            Transform(elements[1], MathTex("-4").move_to(elements[1])), 
            Transform(elements[2], MathTex("-3").move_to(elements[2]))
        )
        afterscalar = MobjectMatrix([[MathTex("-"), MathTex("-")], [MathTex("-"), MathTex("-")]]).move_to(DOWN * 2).set_color(BLUE)
        elements = inversemtxex.get_entries()
        afterscalarentries = afterscalar.get_entries()

        resultsofscalar = [-5/2, 2, 3/2, -1]

        self.play(Write(afterscalar))

        for n, zet in zip([3, 1, 2, 0], [0,1,2,3,]):
            copy = oneoverdet.copy().set_color(RED)
            copyofn = elements[n].copy().set_color(RED)     
            totransform = VGroup(copy, copyofn, afterscalarentries[zet])
            s = resultsofscalar[zet]
            self.play(
                copy.animate.move_to(afterscalarentries[zet]),
                copyofn.animate.move_to(afterscalarentries[zet]),
                Transform(totransform, MathTex(f"{s}").move_to(afterscalarentries[zet])),
                run_time = 1
            )
            afterscalarentries[zet] = totransform

        

        self.play(
            FadeOut(oneoverdet, inversemtxex),
            afterscalar.animate.move_to(six_10_9_13.get_center() + [-3, 0, 0])
        )
        
        self.remove(oneoverdet, inversemtxex, inversemtxl)
        self.wait(.5)


        tosurround = [
            [0, 0, 3],
            [0, 1, 1],
            [1, 0, 0],
            [1, 1, 2]
        ]

        solution = MobjectMatrix([[MathTex("-"), MathTex("-")], [MathTex("-"), MathTex("-")]]).move_to(DOWN * 2).set_color(BLUE)

        self.play(Write(solution))

        counter = 0
        solutionentries = solution.get_entries()
        for r, c, s in tosurround:
            self.play(
                ShowCreationThenFadeOut(SurroundingRectangle(afterscalar.get_rows()[r])),
                ShowCreationThenFadeOut(SurroundingRectangle(six_10_9_13.get_columns()[c])),
                Transform(solutionentries[counter], MathTex(f"{s}").move_to(solutionentries[counter])),

            )
            counter +=1

        self.play(FadeOut(afterscalar, six_10_9_13))
        self.play(solution.animate.move_to(abcd.get_right() + [2,0,0]))
        self.play(problem.animate.move_to(ORIGIN))

        self.wait()
        

