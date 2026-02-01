from manim import *

class SimpleScene(Scene):
    def construct(self):
        text = Text("Hello,OK").scale(1.5)
        self.play(FadeIn(text))
        self.wait(2)
#to run this ->manim -pql simple_scene.py SimpleScene
# Explanation of flags:

# -p → automatically plays the video after rendering

# -ql → quality low (fast render for testing; use -qh for high quality)

# simple_scene.py → your file name

# SimpleScene → the class name of your scene
