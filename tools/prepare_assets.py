from PIL import Image
import os

A = os.path.join(os.path.dirname(__file__), "..", "assets")
A = os.path.abspath(A)

CHROMA = (255, 0, 255)
TOL = 70


def chroma_key(img, size):
    img = img.convert("RGBA")
    w, h = img.size
    px = img.load()
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            d = abs(r - CHROMA[0]) + abs(g - CHROMA[1]) + abs(b - CHROMA[2])
            if d <= TOL * 3:
                px[x, y] = (r, g, b, 0)
            elif d <= TOL * 4.5:
                f = (d - TOL * 3) / (TOL * 1.5)
                px[x, y] = (r, g, b, int(255 * f))
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    img = img.resize((size, size), Image.LANCZOS)
    return img


def flat_resize(img, size):
    if isinstance(size, tuple):
        return img.convert("RGB").resize(size, Image.LANCZOS)
    return img.convert("RGB").resize((size, size), Image.LANCZOS)


SPRITES = {
    "hero_raw.png": ("hero.png", 128),
    "paladin_raw.png": ("paladin.png", 96),
    "summoner_raw.png": ("summoner.png", 96),
    "archer_raw.png": ("archer.png", 96),
    "slime_raw.png": ("slime.png", 80),
    "bat_raw.png": ("bat.png", 80),
    "ghost_raw.png": ("ghost.png", 80),
    "snake_raw.png": ("snake.png", 80),
    "toad_raw.png": ("toad.png", 80),
    "imp_raw.png": ("imp.png", 80),
    "fire_imp_raw.png": ("fire_imp.png", 80),
    "skeleton_raw.png": ("skeleton.png", 80),
    "eye_raw.png": ("eye.png", 80),
    "shadow_raw.png": ("shadow.png", 80),
    "demon_raw.png": ("demon.png", 96),
    "fallen_raw.png": ("fallen.png", 96),
    "reaper_raw.png": ("reaper.png", 96),
    "frost_wolf_raw.png": ("frost_wolf.png", 96),
    "ice_wraith_raw.png": ("ice_wraith.png", 96),
    "lava_golem_raw.png": ("lava_golem.png", 96),
    "golem_raw.png": ("golem.png", 96),
    "death_knight_raw.png": ("death_knight.png", 96),
    "demon_guard_raw.png": ("demon_guard.png", 96),
    "mage_raw.png": ("mage.png", 96),
    "boss_karaage_raw.png": ("boss_karaage.png", 192),
    "summon_ken_raw.png": ("summon_ken.png", 96),
    "summon_ryu_raw.png": ("summon_ryu.png", 96),
    "summon_kame_raw.png": ("summon_kame.png", 96),
    "summon_hotori_raw.png": ("summon_hotori.png", 96),
    "summon_kitsune_raw.png": ("summon_kitsune.png", 96),
    "stairs_raw.png": ("stairs.png", 32),
    "gate_raw.png": ("gate.png", 64),
    "savepoint_raw.png": ("savepoint.png", 64),
    "chest_raw.png": ("chest.png", 48),
    "icon_gold_raw.png": ("icon_gold.png", 32),
    "icon_karaage_raw.png": ("icon_karaage.png", 32),
    "tile_floor_raw.png": ("tile_floor.png", 16),
    "tile_wall_raw.png": ("tile_wall.png", 16),
    "unemployed_raw.png": ("unjob.png", 96),
    # walk frames (差分生成: 基本画像からの2フレーム目)
    "hero_walk_raw.png": ("hero_walk.png", 128),
    "paladin_walk_raw.png": ("paladin_walk.png", 96),
    "summoner_walk_raw.png": ("summoner_walk.png", 96),
    "mage_walk_raw.png": ("mage_walk.png", 96),
    "unjob_walk_raw.png": ("unjob_walk.png", 96),
    "slime_walk_raw.png": ("slime_walk.png", 80),
    "bat_walk_raw.png": ("bat_walk.png", 80),
    "ghost_walk_raw.png": ("ghost_walk.png", 80),
    "snake_walk_raw.png": ("snake_walk.png", 80),
    "toad_walk_raw.png": ("toad_walk.png", 80),
    "imp_walk_raw.png": ("imp_walk.png", 80),
    "fire_imp_walk_raw.png": ("fire_imp_walk.png", 80),
    "skeleton_walk_raw.png": ("skeleton_walk.png", 80),
    "eye_walk_raw.png": ("eye_walk.png", 80),
    "shadow_walk_raw.png": ("shadow_walk.png", 80),
    "demon_walk_raw.png": ("demon_walk.png", 96),
    "fallen_walk_raw.png": ("fallen_walk.png", 96),
    "archer_walk_raw.png": ("archer_walk.png", 96),
    "reaper_walk_raw.png": ("reaper_walk.png", 96),
    "frost_wolf_walk_raw.png": ("frost_wolf_walk.png", 96),
    "ice_wraith_walk_raw.png": ("ice_wraith_walk.png", 96),
    "lava_golem_walk_raw.png": ("lava_golem_walk.png", 96),
    "golem_walk_raw.png": ("golem_walk.png", 96),
    "death_knight_walk_raw.png": ("death_knight_walk.png", 96),
    "demon_guard_walk_raw.png": ("demon_guard_walk.png", 96),
    "boss_karaage_walk_raw.png": ("boss_karaage_walk.png", 192),
    "summon_ken_walk_raw.png": ("summon_ken_walk.png", 96),
    "summon_ryu_walk_raw.png": ("summon_ryu_walk.png", 96),
    "summon_kame_walk_raw.png": ("summon_kame_walk.png", 96),
    "summon_hotori_walk_raw.png": ("summon_hotori_walk.png", 96),
    "summon_kitsune_walk_raw.png": ("summon_kitsune_walk.png", 96),
    "tile_floor_bone_raw.png": ("tile_floor_bone.png", 16),
    "tile_floor_fire_raw.png": ("tile_floor_fire.png", 16),
    "tile_floor_poison_raw.png": ("tile_floor_poison.png", 16),
    "tile_floor_ice_raw.png": ("tile_floor_ice.png", 16),
    "tile_floor_dark_raw.png": ("tile_floor_dark.png", 16),
    "icon_sword_raw.png": ("icon_sword.png", 32),
    "icon_blade_raw.png": ("icon_blade.png", 32),
    "icon_axe_raw.png": ("icon_axe.png", 32),
    "icon_spear_raw.png": ("icon_spear.png", 32),
    "icon_bow_raw.png": ("icon_bow.png", 32),
    "icon_orb_raw.png": ("icon_orb.png", 32),
    "icon_staff_raw.png": ("icon_staff.png", 32),
    "icon_scythe_raw.png": ("icon_scythe.png", 32),
    "icon_fang_raw.png": ("icon_fang.png", 32),
    "icon_holy_raw.png": ("icon_holy.png", 32),
    "icon_leather_raw.png": ("icon_leather.png", 32),
    "icon_mail_raw.png": ("icon_mail.png", 32),
    "icon_plate_raw.png": ("icon_plate.png", 32),
    "icon_shieldmail_raw.png": ("icon_shieldmail.png", 32),
    "icon_crown_raw.png": ("icon_crown.png", 32),
    "icon_ring_atk_raw.png": ("icon_ring_atk.png", 32),
    "icon_ring_mag_raw.png": ("icon_ring_mag.png", 32),
    "icon_ring_def_raw.png": ("icon_ring_def.png", 32),
    "icon_ring_spd_raw.png": ("icon_ring_spd.png", 32),
    "icon_potion_s_raw.png": ("icon_potion_s.png", 32),
    "icon_potion_l_raw.png": ("icon_potion_l.png", 32),
    "icon_ethers_raw.png": ("icon_ethers.png", 32),
    "icon_summonmat_raw.png": ("icon_summonmat.png", 32),
    "icon_exp_raw.png": ("icon_exp.png", 32),
    "icon_hp_raw.png": ("icon_hp.png", 32),
    "icon_mp_raw.png": ("icon_mp.png", 32),
    "ui_panel_raw.png": ("ui_panel.png", 128),
    "ui_button_raw.png": ("ui_button.png", 128),
    "ui_bar_raw.png": ("ui_bar.png", 128),
}


FLAT = {
    "tile_floor_raw.png", "tile_wall_raw.png",
    "tile_floor_bone_raw.png", "tile_floor_fire_raw.png", "tile_floor_poison_raw.png",
    "tile_floor_ice_raw.png", "tile_floor_dark_raw.png",
    "icon_gold_raw.png", "icon_karaage_raw.png",
    "ui_panel_raw.png", "ui_button_raw.png", "ui_bar_raw.png",
}


def main():
    for raw, (out, size) in SPRITES.items():
        src = os.path.join(A, raw)
        dst = os.path.join(A, out)
        if not os.path.exists(src):
            print("MISS", raw)
            continue
        img = Image.open(src)
        if raw in FLAT:
            img = flat_resize(img, size)
        else:
            img = chroma_key(img, size)
        img.save(dst)
        print("OK", out, img.size)


if __name__ == "__main__":
    main()
