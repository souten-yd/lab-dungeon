# T43 中ボス専用BGM 9曲 — 歌詞・音響指示書（唐揚げ王国崇拝グラデーション）

ユーザー指定(09-15): 10階ごとの中ボスは**唐揚げ王国を崇拝**している。**深い階層ほど崇拝度合いが高い**。
各曲=**ボーカル入り・約2分**（実尺110〜135秒でQA）・**「からあげ！」のワードをコーラスの掛け声に入れる**。
**T47(09-15) 表記改訂**: 旧`Karaage!`は英語歌唱の末尾/g/が/ji:/にglideし「カラージ」に聞こえた→**モーラ区切り`Ka-ra-a-ge!`**（probe曲で「唐揚げ」と聞こえることをユーザー確認済み）に全置換。チルダ`~`は廃止（伸ばしでglideが強化されるため=硬い`!`で切る）。大魔王曲の`duration_sec`は2分(=125spec)+`loop:true`に引き上げ（旧84.5秒は短すぎ）。
100F大魔王 `bgm_boss.ogg`（"Hail the Ka-ra-a-ge Emperor"）も同表記・同条件で再生成対象。この9曲は「崇拝する側」、大魔王曲は「崇拝の対象」。

## 生成パラメータ(全曲共通)
- `instrumental: false`, `vocal_language: "en"`, `loop: true`(シームレスループ)
- `duration_sec: 125`(実尺≈110〜125秒=約2分。T37の70spec→実測60〜68秒の比率より)
- 出力: `audio/bgm_mb_01.ogg`〜`audio/bgm_mb_09.ogg`(ogg Vorbis ≈150kbps、既存と同方針)
- 歌詞は本文をそのまま `lyrics` に渡す(`[verse]`/`[chorus]` マーク付き)
- 共通モチーフ: **The Fried Kingdom(唐揚げ王国)** + 掛け声 **Ka-ra-a-ge!**（T37ボス曲の "Ka-ra-a-ge Emperor" と語彙を共通）

## 崇拝度9段階
| 曲 | 階 | 中ボス | 崇拝度 | 音響の方向 |
|---|---|---|---|---|
| bgm_mb_01 | 10F | 鼠王ゴンタ | ★ 素朴な慕い | フォーク讃美歌・木笛・軽い手拍子・無邪気 |
| bgm_mb_02 | 20F | 骨の乙女ミア | ★★ 静かな儀式 | 骨笛・呼吸感のある女声・遅い聖咏・畏敬 |
| bgm_mb_03 | 30F | 鍛冶場ゴレムクロ | ★★★ 労働の礼賛 | 金床のリズム・作業チャント・力強さ |
| bgm_mb_04 | 40F | 火炎公爵イグニス | ★★★★ 炎の典礼 | 戦争賛美歌・太鼓・吹奏・熱狂上昇 |
| bgm_mb_05 | 50F | 沼の魔女ミレイ | ★★★★★ 狂信トランス | 呪術的・不協和・反復チャント・催眠 |
| bgm_mb_06 | 60F | 氷の聖騎士グレイシア | ★★★★★ 聖戦の合唱 | 大聖堂合唱・軍楽・粛清=祝福の荘厳 |
| bgm_mb_07 | 70F | 影の暗殺者ニクス | ★★★★★ 影の秘儀 | 囁き合唱・低域・静かな狂信 |
| bgm_mb_08 | 80F | 堕天の天使セラフェル | ★★★★★★ 堕ちた礼拝 | 暗転した天使の合唱・壮大な悲劇性 |
| bgm_mb_09 | 90F | 魔王の副官ベリアル | ★★★★★★ 狂信の頂点 | 全員合唱+重太鼓+シャウト・破滅的頂点 |

---

## bgm_mb_01 — 10F 鼠王ゴンタ「The Little Rat's Hymn」(★ 素朴な慕い)

Style: quirky folk dungeon hymn, light hand drum, wooden flute, plucked lute, curious and simple, warm minor key, moderate tempo, a tiny rat's innocent devotion
```
[verse]
Under the stair, I keep my watch
The tunnel king has seen it all
A golden light from floors above
Tastes better than the crumb wall
[chorus]
Ka-ra-a-ge! the tunnels sing
Ka-ra-a-ge! the crumbs will bring
We pay our toll, we dig, we dig
For the Fried Kingdom's shining wing
[verse]
The big rats say he eats the world
The little rats just want a bite
So I guard the door, I guard the stone
And hum the song of golden light
[chorus]
Ka-ra-a-ge! the tunnels sing
Ka-ra-a-ge! the crumbs will bring
One day I'll feast, one day I'll feast
When the Fried Kingdom opens wide
```

---

## bgm_mb_02 — 20F 骨の乙女ミア「Bones Remember the Name」(★★ 静かな儀式)

Style: ethereal funeral-rite hymn, bone flute, breathy female vocal, slow reverent a cappella choir, damp catacomb atmosphere, dark and tender, minor key, solemn
```
[verse]
I count the years in buried bone
The sleep was long, the dream was gold
A kingdom fried beyond the grave
Its name the dead still hold
[chorus]
Ka-ra-a-ge... the quiet choir
Ka-ra-a-ge... we were salt and oil
We lay beneath the falling wing
And pray with every hollow bone
[verse]
The bone flute plays a lullaby
The lullaby has golden ears
I opened up the sealed tomb gate
So the pilgrims can descend
[chorus]
Ka-ra-a-ge... the quiet choir
Ka-ra-a-ge... we were salt and oil
Who wakes the bone, who wakes the bone
The Fried Kingdom never dies
```

---

## bgm_mb_03 — 30F 鍛冶場ゴレムクロ「Hammer of Devotion」(★★★ 労働の礼賛)

Style: industrial forge work-chant, hammer percussion on every beat, stomp rhythm, staccato male choir, proud and forceful, heavy minor key, proud industrial hymn
```
[verse]
Strike the anvil, heat the wing
The furnace burns the sacred name
Every hammer blow is one more prayer
The golem's heart is molten flame
[chorus]
Ka-ra-a-ge! on the heavy beat
Ka-ra-a-ge! we forge the street
Flat and crisp and golden bright
The Fried Kingdom owns the night
[verse]
My master sleeps in iron sleep
But his dream is golden crumb
I will hammer till the mountain cracks
I will hammer till it's done
[chorus]
Ka-ra-a-ge! on the heavy beat
Ka-ra-a-ge! we forge the street
Anvil, anvil, anvil song
For the Fried Kingdom, we are strong
```

---

## bgm_mb_04 — 40F 火炎公爵イグニス「Liturgy of Flame」(★★★★ 炎の典礼)

Style: fire war hymn, marching war drums, brass fanfare, rising male choir fervor, aggressive minor key, heat and glory, building intensity
```
[verse]
The duke's domain is wall of flame
No pilgrim leaves in one whole piece
I burn the gate, I burn the road
I burn until the Kingdom sees
[chorus]
Ka-ra-a-ge! let the fire rise
Ka-ra-a-ge! hear my cries
We are the spark, we are the heat
The Fried Kingdom is complete
[verse]
My heart is coals, my blood is oil
My lungs the smoke of golden wings
I will not kneel, I will not cool
I am the duke that the fire brings
[chorus]
Ka-ra-a-ge! let the fire roar
Ka-ra-a-ge! burn the door
Ash by ash and ember by ember
The Fried Kingdom will remember
```

---

## bgm_mb_05 — 50F 沼の魔女ミレイ「Mire Chant」(★★★★★ 狂信トランス)

Style: voodoo swamp trance, dissonant chanting, hypnotic repetitive drone, shaker and gourd rattle, haunting female vocal, twisted devotion, minor key with tritones, trance
```
[verse]
The mud is sweet, the mud is kind
The mud remembers every name
I sing the song the fish forgot
The song that has no shame
[chorus]
Ka-ra-a-ge, ka-ra-a-ge, ka-ra-a-ge!
The mire drinks the golden rain
Ka-ra-a-ge, ka-ra-a-ge, ka-ra-a-ge!
Swim to the Kingdom, sink again
[verse]
Bring your boots, bring your bread
Bring the prayers you never said
The mire will fry what the sky refused
The mire is what the Kingdom fed
[chorus]
Ka-ra-a-ge, ka-ra-a-ge, ka-ra-a-ge!
The sweet water, the burning air
Ka-ra-a-ge, ka-ra-a-ge, ka-ra-a-ge!
The Fried Kingdom is everywhere
```

---

## bgm_mb_06 — 60F 氷の聖騎士グレイシア「Frost Cathedral Hymn」(★★★★★ 聖戦の合唱)

Style: grand cathedral war hymn, full choir in tight harmony, martial timpani and brass, cold crystalline atmosphere, austere and violent devotion, minor key, majestic
```
[verse]
The cathedral is ice, the ice is law
The law is one golden name
Her sword is frost, her crown is salt
Her judgment burns like flame
[chorus]
Ka-ra-a-ge! in the holy name
Ka-ra-a-ge! the heretics came
We cleanse with fire, we bind with frost
The Fried Kingdom is our host
[verse]
Every blade that falls is blessed
Every scream is turned to song
The paladin kneels to no king
Save the King of the Golden Crumb
[chorus]
Ka-ra-a-ge! the white walls sing
Ka-ra-a-ge! the judgment rings
Hear the choir of the frozen dead
The Fried Kingdom rules instead
```

---

## bgm_mb_07 — 70F 影の暗殺者ニクス「Whisper Rite」(★★★★★ 影の秘儀)

Style: dark shadow ritual, whispered choir, deep sub-bass drone, sparse heartbeat percussion, cold minimal fanaticism, sinister minor key, quiet and intense
```
[verse]
I have no voice, I have no name
I have only the word I keep
Spoken once inside the dark
Spoken once while others sleep
[chorus]
...ka-ra-a-ge... in the shadow deep
...ka-ra-a-ge... while the world is asleep
...ka-ra-a-ge... the knife is golden
...ka-ra-a-ge... the dark is full
[verse]
They say the Kingdom eats the light
I say the Kingdom eats the fear
I cut the thread, I cut the gate
I cut so that the Kingdom's near
[chorus]
...ka-ra-a-ge... say it soft
...ka-ra-a-ge... say it once
...ka-ra-a-ge... say it never loud
...ka-ra-a-ge... or it is undone
```

---

## bgm_mb_08 — 80F 堕天の天使セラフェル「Hymn of the Fallen」(★★★★★★ 堕ちた礼拝)

Style: fallen-angel liturgy, dark angelic choir, sweeping strings and organ, tragic grandeur, weeping devotion, minor key, epic sorrow and power
```
[verse]
I sang in heaven, I sang in gold
Then the golden wing took my song
Now I sing in the ruined hall
With a voice that will not be wrong
[chorus]
Ka-ra-a-ge! even the fallen sing
Ka-ra-a-ge! the broken wings
We kneel in the ash, we pray in the rain
The Fried Kingdom gave, the Fried Kingdom took away
[verse]
My halo broke, my pride broke through
But the crumb of the Kingdom stayed
I am the prayer that heaven refused
I am the hymn that the dark made
[chorus]
Ka-ra-a-ge! we fall and we rise
Ka-ra-a-ge! we open our eyes
The throne is fried, the throne is gold
The Fried Kingdom is more than we were told
```

---

## bgm_mb_09 — 90F 魔王の副官ベリアル「Apex of Devotion」(★★★★★★ 狂信の頂点)

Style: apocalyptic fanatical worship anthem, massive congregation choir, war drums and low brass, soaring to a frenzied peak, apocalyptic grandeur, minor key, the word "KA-RA-A-GE" as a crowd roar through the whole track
```
[verse]
The lieutenant kneels on broken ground
The broken ground is blessed with gold
The Great Devourer eats the world
And every world is owed
[chorus]
KA-RA-A-GE!! the congregation roars
KA-RA-A-GE!! the last world's floors
We are the crumbs, we are the call
The Fried Kingdom swallows all
[verse]
The Vice Regent spreads his wings of night
The night is fried, the night is gold
Our death is prayer, our prayer is feast
The story of the Kingdom told
[chorus]
KA-RA-A-GE!! KA-RA-A-GE!! KA-RA-A-GE!!
The world is bread, the dark is flame
KA-RA-A-GE!! KA-RA-A-GE!! KA-RA-A-GE!!
The Fried Kingdom is the name
```
