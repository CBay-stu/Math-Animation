from manim import *
class FixedInFrameMObjectTest(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cylinder = Surface(
            lambda u, v: np.array([
                2 * np.cos(u),
                1 * np.sin(u),
                v
            ]),
            u_range=[0, TAU],
            v_range=[-1, 1],
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(32, 32)
        )

        curve1 = ParametricFunction(
            lambda u: (
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u * 0.5
            ), color = RED, t_range=[-3*TAU, 5*TAU, 0.01],
        )
        self.renderer.camera.light_source.move_to(3*IN)
        self.set_camera_orientation(phi=72 * DEGREES, theta=-45 * DEGREES)
        self.add(axes, cylinder, curve1)
        self.wait()