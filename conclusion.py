from manim import *

class credits(Scene):
    def construct(self):
        credit = Text("Credits").to_edge(UL)

        shaun = ImageMobject("rona.jpg").rotate(3 * PI/2)
        shaun.height = 6
        shaun.length = 4
        shaun.shift(RIGHT * 3, DOWN * .5)
        self.play(Write(credit))
        self.add(shaun)
        surrshaun = SurroundingRectangle(shaun, buff = .1, color = WHITE)
        surrshaun.add_updater(lambda x: x.become(SurroundingRectangle(shaun, buff = .1, color = WHITE)))
        shaunteaches = Text("I have the rona", color = YELLOW).move_to(shaun.get_top() + [0, .6, 0])
        shaunteaches.add_updater(lambda x: x.move_to(shaun.get_top() + [0, .6, 0]))
        self.play(
            Create(surrshaun),
            Write(shaunteaches)
            )
        self.wait(2)
        list = BulletedList(
            "Matrix project",
            "Shaun Errichiello",
            "Marlin's bagels",
        ).shift(LEFT * 3)

        list[0].set_color(YELLOW)
        list[1].set_color(RED)
        list[2].set_color(BLUE)

        bullets = [
            ["Vitamin C", "Team 639", "Junyoung sim"],
        ]


        self.play(Write(list))
        self.wait(3)
        for bullet in bullets:
            new_list = BulletedList(
                bullet[0],
                bullet[1],
                bullet[2],
            ).move_to(list)
            new_list[0].set_color(YELLOW)
            new_list[1].set_color(RED)
            new_list[2].set_color(BLUE)

            for i in range(len(bullet)):
                self.play(
                    Transform(
                        list[i],
                        new_list[i]
                    ),
                    run_time = 1
                )
                self.wait(2)
        self.play(FadeOut(list))
        self.play(shaun.animate.move_to(ORIGIN))
        self.play(FadeOut(shaun, surrshaun, shaunteaches, credit))
        self.play(Write(Text("Thanks for watching!")))
        self.wait()