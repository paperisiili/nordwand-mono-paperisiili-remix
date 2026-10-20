from glyphs.accents import Accent
from draw.parallelogramm import draw_parallelogramm


class Circumflex(Accent):
    name = "circumflex"
    unicode = "0x5E"
    height = 0.35
    width = 1
    stroke_ratio = 1.1

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset)
        self.draw_at(pen, dc, x=b.xmid, y=b.y2, x_scale=1.3, y_scale=1.8)

    def draw_at(self, pen, dc, x, y, x_scale=1, y_scale=1):
        h = self.height * dc.x_height * y_scale
        w = self.width * dc.width * x_scale
        x1, x2, xmid = x - w / 2, x + w / 2, x
        y1, y2 = y - h / 2, y + h / 2
        d = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.45)
        ov = 0.5 * d

        draw_parallelogramm(
            pen,
            dc.stroke_alt,
            dc.stroke_alt,
            x1,
            y1,
            xmid + ov,
            y2,
            delta=d,
        )
        draw_parallelogramm(
            pen,
            dc.stroke_alt,
            dc.stroke_alt,
            x2,
            y1,
            xmid - ov,
            y2,
            direction="top-left",
            delta=d,
        )
