from manimlib.imports import *

class P1(Scene):
    def construct(self):
        basicText = TextMobject("Manim here we go")
        self.add(basicText)
        self.wait(3)

class P2(Scene):
    def construct(self):
        basicText = TextMobject("Manim here we go")
        self.play(Write(basicText))
        self.wait(3)

class P3(Scene):
    def construct(self): 
        text = TextMobject("Testing if I can remove this text")
        self.add(text)
        self.wait(1)
        self.remove(text)
        self.wait(1)

class P4(Scene):
    def construct(self):
        text = TextMobject("Testing to remove text with animation")
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(text))
        self.wait(1) 

class P5(Scene):
    def construct(self):
        text = TextMobject("Testing to remove text with remove after animating it in")
        self.play(FadeIn(text))
        self.wait(1)
        self.remove(FadeOut(text)) #does not work to remove objects that are animated in - must animate them out using self.play()
        self.wait(1) 

class P6(Scene):
    def construct(self):
        #testing adjusting the options of the animation functions 
        text = TextMobject("Testing options of fade in and fade out?")
        self.play(FadeInFrom(text, lag_ratio=0, direction=UP))
        self.wait(1)
        self.play(FadeOutAndShift(text, lag_ratio=0, direction=DOWN))
        self.wait(1)

class P7(Scene):
    def construct(self):
        #to test still :/
        #testing position changing, etc
        text = TextMobject("IDK")
        dot = Dot()
        dot.to_edge(np.array([0,1,0]))
        text.next_to(dot, DOWN, buff=1)
        self.add(dot, text)
        self.wait(3)
        self.play(FadeOut(text, dot), run_time=2)

class PythagorasTheorem(Scene):
    def construct(self):
        triangle = self.createTriangle((0,0,0), (2,0,0), (0,2,0))

        side1label = TextMobject("a").set_color(RED).move_to(UP*1 + LEFT*0.5)
        side2label = TextMobject("b").set_color(RED).move_to(DOWN*0.4 + RIGHT*1)
        side3label = TextMobject("c").set_color(RED).move_to(UP*1.3 + RIGHT*1.3)

        squarec = self.createSquareOfColor(PURPLE, (0,0,0), (1,0,0), (1,1,0), (0,1,0)).rotate(PI/4).scale(2.8284).move_to(2*UP+2*RIGHT)
        squarea = self.createSquareOfColor(PURPLE, (0,0,0), (1,0,0), (1,1,0), (0,1,0)).scale(2).move_to(1*LEFT+1*UP)
        squareb = self.createSquareOfColor(PURPLE, (0,0,0), (1,0,0), (1,1,0), (0,1,0)).scale(2).move_to(1*DOWN+1*RIGHT)

        #firstPart = VGroup(triangle, side1label, side2label, side3label, squarec, squarea, squareb)
        #firstPart.shift(DOWN*1+LEFT*1)

        self.play(ShowCreation(squarec), ShowCreation(squarea), ShowCreation(squareb), runtime=1)

        self.play(ShowCreation(triangle), runtime=2)

        self.play(Write(side1label), Write(side2label), Write(side3label), runtime=1)

        self.wait()

    def createTriangle(self, *coords):
        return Polygon(*coords).set_color(WHITE)

    def createSquareOfColor(self, color, *coords):
        return Polygon(*coords).set_color(color)

class testingPythagoras(Scene):
    def construct(self):
        pass