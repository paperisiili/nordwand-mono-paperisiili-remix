from glyphs.accents import Accent
from draw.parallelogramm import draw_parallelogramm, parallelogramm_delta


class Grave(Accent):
    name = "grave"
    unicode = "0x60"
    height = 0.35
    width = 0.55
    stroke_ratio = 1.0

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset)
        x_scale, y_scale = 1.1, 1.45
        width_ratio = 0.85
        h = self.height * dc.x_height * y_scale
        w = self.width * dc.width * x_scale * width_ratio
        s = self.stroke_ratio * dc.stroke_x * x_scale
        d = parallelogramm_delta(s, 0, 0, w, h)
        self.draw_at(
            pen,
            dc,
            x=b.xmid + (w - d) / 2,
            y=b.y2 + h / 2,
            x_scale=x_scale,
            y_scale=y_scale,
            width_ratio=width_ratio)

    def draw_at(self, pen, dc, x, y, x_scale=1, y_scale=1, width_ratio=1):
        h = self.height * dc.x_height * y_scale
        w = self.width * dc.width * x_scale * width_ratio
        s = self.stroke_ratio * dc.stroke_x * x_scale
        # Base centered on x
        d = parallelogramm_delta(s, 0, 0, w, h)
        draw_parallelogramm(
            pen, s, x + d / 2, y - h / 2, x + d / 2 - w, y + h / 2, direction="top-left"
        )
