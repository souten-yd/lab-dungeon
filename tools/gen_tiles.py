#!/usr/bin/env python3
"""
ダンジョン床タイル(16x16)のシード固定プロシージャル生成スクリプト。
既存タイル(tile_floor.png等)と同じ「くすんだ画調・塊状ノイズ」に合わせている。
media-forgeの元画像が不要なため、ここから直接最終PNGを書き出す。
"""
from PIL import Image
import random, math, os

A = os.path.join(os.path.dirname(__file__), "..", "assets")
A = os.path.abspath(A)


def clump_noise(size, seed, scale=3):
    """粗いグリッドノイズをバイリニア補間した塊状ノイズ(0..1)"""
    random.seed(seed)
    gw = size // scale + 3
    grid = [[random.random() for _ in range(gw)] for _ in range(gw)]

    def at(x, y):
        gx, gy = x / scale, y / scale
        x0, y0 = int(gx), int(gy)
        fx, fy = gx - x0, gy - y0
        fx = fx * fx * (3 - 2 * fx)
        fy = fy * fy * (3 - 2 * fy)
        v00 = grid[y0][x0]; v10 = grid[y0][x0 + 1]
        v01 = grid[y0 + 1][x0]; v11 = grid[y0 + 1][x0 + 1]
        return (v00 * (1 - fx) + v10 * fx) * (1 - fy) + (v01 * (1 - fx) + v11 * fx) * fy

    return at


def clamp(v):
    return int(max(0, min(255, v)))


def gen_tile(name, base, amp, seed, feature=None, grain=0.35):
    im = Image.new("RGB", (16, 16))
    px = im.load()
    n = clump_noise(16, seed, 3)
    random.seed(seed * 7 + 13)
    for y in range(16):
        for x in range(16):
            d = (n(x, y) - 0.5) * amp + random.gauss(0, amp * grain)
            px[x, y] = (clamp(base[0] + d), clamp(base[1] + d), clamp(base[2] + d))
    if feature:
        feature(im, px)
    im.save(os.path.join(A, name))
    print("wrote", name)


def feat_grass(im, px):
    """苔むした草床: 明るい草の筋+暗い窪み"""
    random.seed(991)
    for _ in range(11):
        x = random.randint(1, 14); y = random.randint(1, 14)
        h = random.choice([1, 2, 2])
        for k in range(h):
            if 0 <= y - k < 16:
                px[x, y - k] = (clamp(58 + random.randint(-6, 10)), clamp(78 + random.randint(-6, 12)), clamp(44 + random.randint(-5, 8)))
    for _ in range(6):
        x = random.randint(0, 15); y = random.randint(0, 15)
        px[x, y] = (30, 42, 28)


def feat_stone(im, px):
    """石畳: 5px縦割りのレンガ模様+目地"""
    random.seed(777)
    for y in range(16):
        for x in range(16):
            row = y // 5
            off = 0 if row % 2 == 0 else 3
            if y % 5 == 0 or (x + off) % 5 == 0:
                d = random.randint(-4, 4)
                px[x, y] = (clamp(47 + d), clamp(47 + d), clamp(51 + d))  # 目地
            else:
                d = random.randint(-7, 7)
                r, g, b = px[x, y]
                px[x, y] = (clamp(r + d), clamp(g + d), clamp(b + d))
    for _ in range(4):
        x = random.randint(0, 15); y = random.randint(0, 15)
        px[x, y] = (58, 58, 63)


def feat_water(im, px):
    """水面: 波の明線+かすかな光"""
    random.seed(424)
    for y in range(16):
        for x in range(16):
            w = math.sin((x + 2.6 * math.sin(y * 0.8 + 1.3)) * 0.9)
            if w > 0.55:
                d = random.randint(6, 14)
                r, g, b = px[x, y]
                px[x, y] = (clamp(r + d), clamp(g + d + 3), clamp(b + d + 6))
    for _ in range(3):
        x = random.randint(0, 15); y = random.randint(0, 15)
        px[x, y] = (86, 128, 168)


def feat_rock(im, px):
    """割れた岩盤: ランダムウォークで亀裂"""
    random.seed(555)
    for _ in range(2):
        x = random.randint(2, 13); y = random.randint(0, 15)
        for _ in range(9):
            if 0 <= x < 16 and 0 <= y < 16:
                d = random.randint(-4, 2)
                px[x, y] = (clamp(26 + d), clamp(24 + d), clamp(30 + d))
            x += random.choice([-1, 0, 1, 1, 0, -1])
            y += random.choice([1, 1, 0, 1, 0])
    for _ in range(5):
        x = random.randint(0, 15); y = random.randint(0, 15)
        px[x, y] = (52, 50, 58)


def feat_marble(im, px):
    """褪せた白大理石: 淡い斜めの脈(2本)"""
    random.seed(666)
    for y in range(16):
        for x in range(16):
            d = (x + 2 * y) % 16
            dd = min(abs(d - 4.0), 16 - abs(d - 4.0))
            d2 = (x - y) % 16
            dd2 = min(abs(d2 - 9.0), 16 - abs(d2 - 9.0))
            if dd < 1.3 or dd2 < 1.0:
                r, g, b = px[x, y]
                px[x, y] = (clamp(r - 16 + random.randint(-3, 3)), clamp(g - 16 + random.randint(-3, 3)), clamp(b - 12 + random.randint(-3, 3)))
    for _ in range(4):
        x = random.randint(0, 15); y = random.randint(0, 15)
        px[x, y] = (168, 170, 176)


def feat_ash(im, px):
    """焦土: 炭の黒+残り火の点"""
    random.seed(313)
    for _ in range(5):
        x = random.randint(0, 15); y = random.randint(0, 15)
        px[x, y] = (128, 54, 30)
        if x + 1 < 16:
            px[x + 1, y] = (74, 34, 24)
        if y + 1 < 16:
            px[x, y + 1] = (66, 30, 22)
    for _ in range(7):
        x = random.randint(0, 15); y = random.randint(0, 15)
        px[x, y] = (16, 13, 15)


if __name__ == "__main__":
    gen_tile("tile_grass.png", (44, 58, 38), 18, 101, feat_grass)
    gen_tile("tile_stone.png", (64, 64, 68), 10, 202, feat_stone)
    gen_tile("tile_water.png", (24, 44, 72), 10, 303, feat_water)
    gen_tile("tile_floor_rock.png", (38, 36, 44), 12, 404, feat_rock)
    gen_tile("tile_floor_marble.png", (150, 152, 158), 10, 505, feat_marble)
    gen_tile("tile_floor_ash.png", (30, 22, 24), 10, 606, feat_ash)
    print("done.")
