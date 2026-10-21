from glyphs import Glyph
from draw.rect import draw_rect


class VerticalLineGlyph(Glyph):
    name = "vertical_line"
    unicode = "0x7C"
    offset = 0
    width_ratio = 1
    stroke_ratio = 1.17

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="ascent", width_ratio=self.width_ratio
        )
        ymid = dc.parenthesis
        s = dc.stroke_x * self.stroke_ratio
        x1, x2 = b.xmid - s / 2, b.xmid + s / 2
        y1, y2 = ymid - dc.parenthesis_length / 2, ymid + dc.parenthesis_length / 2
        draw_rect(pen, x1, y1, x2, y2)
