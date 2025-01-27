from manim import *
from math import sqrt, floor
from modules.custom_mobjects import FullscreenAxes, create_axes
from modules.helpers import normalize_point_speed
from modules.interpolation import bounce, cubic_out
from numpy import sinc

def S_unnormalized(x):
    x1 = 5
    y1 = 7
    w1 = 0.3
    h = 1.2
    return h * (y1 / (sqrt((w1*(x - x1))**2 + 1)) + (x**3)/500)

S0 = S_unnormalized(0)

def S(x):
    return S_unnormalized(x) - S0

def f(x):
    return S(x) - S(x - 1)


class ProblemIntroduction(Scene):
    def construct(self):
        axes = FullscreenAxes(self, 5.5*LEFT + 2.5*DOWN)

        create_axes(self, axes)

        f_text = MathTex("f(x)").move_to(DOWN + LEFT * 0.5)
        curve = ParametricFunction(lambda t: axes.coords_to_point(t, f(t)), (-2, 13)).set_color(RED)
        curve.set_points(normalize_point_speed(curve.points))

        self.play(
            Create(curve, rate_func = linear, run_time = 0.7),
            Write(f_text)
        )


        sum_text = MathTex("\\sum_{k=1}^x f(k)").move_to(UP * 2)
        self.play(Write(sum_text))

        new_sum_text = MathTex("S(x) =", "\\sum_{k=1}^x f(k)").move_to(UP * 2)
        self.play(
            Transform(sum_text[0], new_sum_text[1]),
            FadeIn(new_sum_text[0], shift = RIGHT)
        )

        self.remove(*sum_text, *new_sum_text)
        sum_text = MathTex("S(x) = \\sum_{k=1}^x f(k)").move_to(UP * 2)
        self.add(sum_text)



        dots = VGroup(*[Dot(axes.coords_to_point(i, S(i)), 0.12, color=BLUE) for i in range(1,13)])
        for dot in dots:
            dot.set_z_index(1)

        self.play(
            sum_text.animate(run_time = 1.5).shift(RIGHT * 3),
            LaggedStart(
                *[FadeIn(dot, scale=3, rate_func=bounce()) for dot in dots],
                lag_ratio = 0.15
            )
        )


        s_curve = ParametricFunction(lambda t: axes.coords_to_point(t, S(t)), (-2, 13)).set_color(YELLOW)
        self.play(Create(s_curve, rate_func = linear))


        def straight_line_fun(x):
            if x < 1: return f(1)
            x_floor = floor(x)
            x_frac = x - x_floor
            return x_frac * S(x_floor + 1) + (1 - x_frac) * S(x_floor)

        new_s_curve = ParametricFunction(lambda t: axes.coords_to_point(t, straight_line_fun(t)), (-2, 13)).set_color(YELLOW)

        self.play(Transform(s_curve, new_s_curve))



        def sinc_fun(x):
            total = 0
            for i in range(1, 16):
                total += S(i) * sinc(x - i)
            return total

        new_s_curve = ParametricFunction(lambda t: axes.coords_to_point(t, sinc_fun(t)), (-2, 13)).set_color(YELLOW)

        self.play(Transform(s_curve, new_s_curve))



        self.wait()