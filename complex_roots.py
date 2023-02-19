from manim import *
import numpy as np


class ComplexPlaneExample(Scene):
    def construct(self):
        intro = Text("Polynomials with random real coeffecients\nhave roots near the unit circle.")
        self.play(Write(intro))
        self.play(Unwrite(intro))
        def animate(degree=5):
            # Degree label
            text = Text(f"Degree: {degree}", font_size=60)
            self.play(Write(text, run_time=1.5))
            self.play(Unwrite(text))


            # polynomial and roots generation
            coefficients = np.random.uniform(-1000, 1000, degree+1)
            roots = np.roots(coefficients)

            # polynomial text generation
            if (degree < 100):
                polynomial = ""
                rootsText = "x = \{"
                for i, a in enumerate(coefficients):
                    exponent = '{' + str(degree - i) + '}'
                    polynomial += f"{a:.2f}{f'x^{exponent}+' if degree - i != 0 else ''}"
                for root in roots:
                    rootsText += f"{root:.2f},"
                rootsText = rootsText.replace("j", "i")
                screen_roots = Tex(f"${rootsText[:-1]}\{'}'}$", font_size=30)
                screen_polynomial = Tex(f"${polynomial}$", font_size=30)
                screen_polynomial.move_to(UP*2)
                screen_roots.next_to(screen_polynomial, DOWN)
                self.play(Write(screen_polynomial, run_time=1))
                self.play(Write(screen_roots, run_time=1))
                self.wait(5)
                self.play(Unwrite(screen_polynomial, run_time=1))
                self.play(Unwrite(screen_roots, run_time=1)) 
            else:
                t = Text("The polynomials are too large to display now.")
                self.play(Write(t))
                self.play(Unwrite(t))

            # Plane and Unit circle creation
            plane = ComplexPlane(x_range=(-4, 4), y_range=(-4, 4), x_length=16, y_length=16).add_coordinates()
            self.play(Create(plane))
            circle = Circle(2)
            self.play(Create(circle))

           
            # roots animation
            points = []
            group = VGroup()
            for root in roots:
                point = Dot(plane.n2p(root),  radius=(.1*np.log(degree))/np.sqrt(degree))
                points.append(point)
                group.add(point)
            self.play(Create(group), run_time=2)
        
        animate(100) 

