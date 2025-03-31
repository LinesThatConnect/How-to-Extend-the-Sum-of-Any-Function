from manim import *

from modules.helpers import create_double_arrow, fade_and_shift_in, highlight_animation, morph_text
from modules.interpolation import bounce, cubic_out, cubic_in



class Intro(Scene):
    def construct(self):
        sigma = MathTex("\\sum").scale(1.5)
        sigma.save_state()
        sigma.scale(0)

        self.play(sigma.animate(rate_func=cubic_out, run_time=0.5).restore())
        self.play(sigma.animate(rate_func=cubic_out, run_time=0.3).scale(1.35))
        self.play(sigma.animate(rate_func=cubic_out, run_time=0.3).scale(1.25))
        self.play(FadeOut(sigma, rate_func=cubic_in, scale=0))

        text_1 = MathTex("\\sum_{k=1}^x k =", "1 + 2 + 3 + \\cdots + x").move_to(UP)
        text_2 = MathTex("\\sum_{k=1}^x r^k =", "r^1", "+", "r^2", "+", "r^3", "+ \\cdots +", "r^x").move_to(DOWN)

        self.play(Write(text_1[0]), run_time=1)

        self.play(
            LaggedStart(
                *[fade_and_shift_in(t, LEFT) for t in text_1[1]],
                lag_ratio=0.25
            )
        )

        self.play(Write(text_2[0]), run_time=1)

        self.play(
            LaggedStart(
                *[fade_and_shift_in(t, LEFT) for t in text_2[1:6].submobjects + text_2[6].submobjects + text_2[7:].submobjects],
                lag_ratio=0.15
            )
        )

        new_text_1 = MathTex("\\sum_{k=1}^x k =", "1 + 2 + 3 + \\cdots + x", "=", "\\frac{x(x+1)}2").move_to(UP)
        new_text_2 = MathTex("\\sum_{k=1}^x r^k =", "r^1 + r^2 + r^3 + \\cdots + r^x", "=", "r\\frac{1-r^x}{1-r}").move_to(DOWN)

        self.play(
            text_1.animate.move_to(new_text_1[:-2]),
            FadeIn(new_text_1[-2:], shift = LEFT*1.5),
        )

        self.play(
            text_2.animate.move_to(new_text_2[:-2]),
            FadeIn(new_text_2[-2:], shift = LEFT*1.5)
        )

        self.remove(*text_1, *text_2)
        text_1 = new_text_1; text_2 = new_text_2
        self.add(text_1, text_2)

        new_text_1 = MathTex("\\sum_{k=1}^x k =", "\\frac{x(x+1)}2").move_to(UP)
        new_text_2 = MathTex("\\sum_{k=1}^x r^k =", "r\\frac{1-r^x}{1-r}").move_to(DOWN)

        self.play(
            morph_text(text_1, new_text_1, [0, None, None, 1], rate_func=bounce()),
            morph_text(text_2, new_text_2, [0, None, None, 1], rate_func=bounce()),
            run_time=1.5
        )

        self.remove(*text_1, *text_2, *new_text_1, *new_text_2)
        text_1 = MathTex("\\sum_{k=1}^x k", "=", "\\frac{x(x+1)}2").move_to(UP)
        text_2 = MathTex("\\sum_{k=1}^x r^k", "=", "r\\frac{1-r^x}{1-r}").move_to(DOWN)
        self.add(text_1, text_2)

        summary_text = Tex("$x$ must be a whole number.").move_to(text_1[0].get_top() + UP*0.75).set_color(RED)

        text_1.save_state()
        text_2.save_state()

        text_1[0].save_state()
        text_2[0].save_state()

        self.play(
            fade_and_shift_in(summary_text, shift=DOWN),
            highlight_animation(text_1[0], RED, rate_func=cubic_out),
            highlight_animation(text_2[0], RED, rate_func=cubic_out),
        )

        new_summary_text = Tex("$x$ can be anything!").move_to(text_1[2].get_top() + UP*0.75).set_color(BLUE)

        self.play(
            Transform(summary_text, new_summary_text),
            highlight_animation(text_1[2], BLUE, scale=1.05),
            highlight_animation(text_2[2], BLUE, scale=1.05),
            text_1[0].animate.restore(),
            text_2[0].animate.restore(),
        )

        text_3 = MathTex("\\sum_{k=1}^x f(k) = \\ \\ ???").move_to(DOWN*2 + LEFT*0.15)

        self.play(
            text_1.animate.restore().shift(UP),
            text_2.animate.restore().shift(UP),
            FadeIn(text_3, shift=UP*1.5),
            FadeOut(summary_text, shift=UP*1.5)
        )




class Integral(Scene):
    def construct(self):
        prerequisite_text = Tex("Prerequisites:", joint_type=LineJointType.ROUND).scale(1.5).move_to(UP*2)
        black_text = prerequisite_text.copy().set_stroke(width=10).set_color(BLACK)
        prerequisite_text.set_z_index(1); black_text.set_z_index(1)
        self.add(black_text)

        underline = Underline(prerequisite_text).shift(UP*0.12)

        self.play(
            Write(prerequisite_text),
            Create(underline)
        )


        point_1 = Tex("$\\bullet$", " Summation Notation ", "(lots of it)")
        point_2 = Tex("$\\bullet$", " Limits")

        point_1.shift(LEFT*3.5 + UP*0.5 - point_1[0].get_center())
        point_2.shift(LEFT*3.5 + DOWN*0.5 - point_2[0].get_center())

        self.play(
            Write(point_1[:2], run_time=1)
        )

        self.play(
            fade_and_shift_in(point_1[2], LEFT)
        )

        self.play(
            Write(point_2)
        )


        integral = MathTex("\\int")

        self.play(
            FadeOut(VGroup(underline, point_1, point_2, prerequisite_text), shift=UP),
            black_text.animate(remover=True).shift(UP),
            FadeIn(integral, shift=UP)
        )

        text = MathTex("\\int \\ \\ ", "\\approx \\ \\ ", "\\sum")
        text.move_to(-text[1].get_center())
        self.play(
            Transform(integral, text[0][:]),
            FadeIn(text[1:], shift=LEFT*1.5)
        )


        DIST_FROM_CENTER = 2.25

        continuous_header = Tex("Continuous").move_to(LEFT*DIST_FROM_CENTER + UP*1.5)
        discrete_header = Tex("Discrete").move_to(RIGHT*DIST_FROM_CENTER + UP*1.5)

        continuous_underline = Line(continuous_header.get_corner(DOWN + LEFT), continuous_header.get_corner(DOWN + RIGHT), stroke_width=3).shift(DOWN * 0.1)
        discrete_underline = Line(discrete_header.get_corner(DOWN + LEFT), discrete_header.get_corner(DOWN + RIGHT), stroke_width=3).shift(DOWN * 0.1)

        arrow_1 = create_double_arrow(LEFT, RIGHT, tip_length=0.3)
        arrow_1.save_state()
        arrow_1.scale(0).set_stroke(width=0).set_color(BLACK)


        sum = text[2]
        self.play(
            arrow_1.animate.restore(),
            integral.animate.move_to(LEFT*DIST_FROM_CENTER),
            sum.animate.move_to(RIGHT*DIST_FROM_CENTER),
            FadeOut(text[1], scale=0),
            LaggedStart(
                Write(continuous_header),
                Create(continuous_underline, rate_func=cubic_out),
                Write(discrete_header),
                Create(discrete_underline, rate_func=cubic_out),
                lag_ratio = 0.2
            )
        )


        derivative = MathTex("\\frac d{dx}").move_to(LEFT*DIST_FROM_CENTER + DOWN*0.25)
        delta = MathTex("\\Delta").scale(1.5).move_to(RIGHT*DIST_FROM_CENTER + DOWN*0.25)
        arrow_2 = create_double_arrow(LEFT, RIGHT, tip_length=0.3).move_to(DOWN*0.25)
        arrow_2.save_state()
        arrow_2.shift(DOWN*1.5).set_color(BLACK)


        taylor = MathTex("\\sum_{n=0}^\\infty \\frac{x^n}{n!} f^{(n)}(0)").scale(0.8).move_to(LEFT*1.25 + DOWN*2, RIGHT)
        newton = MathTex("\\sum_{n=0}^\\infty \\binom xn \\Delta^n f(0)").scale(0.8).move_to(RIGHT*1.25 + DOWN*2, LEFT)

        arrow_3 = create_double_arrow(LEFT, RIGHT, tip_length=0.3).move_to(DOWN*2)
        arrow_3.save_state()
        arrow_3.shift(DOWN*1.5).set_color(BLACK)


        self.play(
            LaggedStart(
                AnimationGroup(
                    VGroup(continuous_header, continuous_underline, discrete_header, discrete_underline, integral, arrow_1, sum).animate.shift(UP*1.5),
                    FadeIn(VGroup(derivative, delta), shift=UP*1.5),
                    arrow_2.animate.restore()
                ),
                AnimationGroup(
                    FadeIn(VGroup(taylor, newton), shift=UP*1.5),
                    arrow_3.animate.restore()
                ),
                lag_ratio=0.25
            )
        )

        self.play(
            VGroup(continuous_header, continuous_underline, integral, derivative, taylor).animate(rate_func=cubic_in).shift(LEFT*7),
            VGroup(discrete_header, discrete_underline, sum, delta, newton).animate(rate_func=cubic_in).shift(RIGHT*7),
            *[arrow.animate.scale(0) for arrow in [arrow_1, arrow_2, arrow_3]]
        )