# T37 BGM30曲 + ボスBGM — 歌詞・音響指示書

ユーザー指定: 各曲=**英語歌詞のボーカル曲**・**1分以上**・テーマ(10階層帯)にちなんだ内容。
ボスBGM(`bgm_boss.ogg`)=**唐揚げ帝国への崇拝**をテーマに盛り上げるボーカル曲(上層階ほど信仰度が上がる=荘厳な祈り→狂信の頂点へクライマックスする構成)。

## 生成パラメータ(全曲共通)
- `instrumental: false`, `vocal_language: "en"`, `loop: true`(シームレスループ)
- `duration_sec: 70`(ループトリム後≈66秒=1分超保証)。**ボス曲のみ `duration_sec: 90`**(≈86秒)
- 出力: `audio/bgm_dun_XX_Y.ogg` / `audio/bgm_boss.ogg`(ogg Vorbis ≈150kbps、既存と同方針)
- 歌詞は本文をそのまま `lyrics` に渡す(`[verse]`/`[chorus]` マーク付き)

## テーマ対応表
| XX | 10F帯 | テーマ | 音響方向 |
|---|---|---|---|
| 00 | 1-10F | 地下回廊 | 暗い探索・マイナー |
| 01 | 11-20F | 骨の地下墓 | 湿った不穏・低弦 |
| 02 | 21-30F | ゴレムの石殿 | 重厚・石打(打撃) |
| 03 | 31-40F | 溶岩洞窟 | 緊張・熱 |
| 04 | 41-50F | 毒沼の底 | 病み・不協和 |
| 05 | 51-60F | 氷の聖堂 | 冷たい・結晶 |
| 06 | 61-70F | 暗黒の深淵 | 深い・低域 |
| 07 | 71-80F | 亡霊王の城塞 | 幽々・霊的 |
| 08 | 81-90F | 天使の遺跡 | 哀愁・エセリアル |
| 09 | 91-99F | 魔王の巣窟 | 悪魔的・激しい |

---

## 00 地下回廊 (1-10F)

### bgm_dun_00_a — 「Through the Dark We Walk」(パイロット生成済み・歌詞固定)
Style: dark minor-key fantasy dungeon exploration BGM, slow torch-lit cave, drips and distant echoes, uneasy but hopeful
```
[verse]
Through the dark we walk
Echoes in the stone
The corridor is long
But we are not alone
[chorus]
Step by step
The shadow bends
A light in caverns deep
We carry, we carry, we carry
```

### bgm_dun_00_b — 「Dust and Drip」
Style: very slow, cautious dungeon crawl, low cello and sparse piano, water drips, quiet unease
```
[verse]
Dust and drip
The way is blind
I follow where the torchlight ends
No door, no day
Only stone on stone
I keep my voice a whisper low
[chorus]
Listen, listen
The dark is breathing
Something old has not yet slept
```

### bgm_dun_00_c — 「Footsteps Ring」
Style: medium-tempo curious exploration, light percussion and warm strings, sense of discovery
```
[verse]
Footsteps ring
On the old stone road
Every crack holds a story
Down, down
Where the rivers sleep
A city built in hollow earth
[chorus]
We are not lost
We are only finding
The way, the way, the way
```

## 01 骨の地下墓 (11-20F)

### bgm_dun_01_a — 「Beneath the Bone White Halls」
Style: damp and eerie crypt, low strings and muted flute, slow funeral pulse, wet darkness
```
[verse]
Beneath the bone white halls
The dead keep quiet watch
Every ribcage holds a name
No one left to call them
[chorus]
I walk on what they were
And they do not move
The crypt is long
The dark is wet
And the dead remember us
```

### bgm_dun_01_b — 「Bone by Bone」
Style: slow funeral dirge, deep male-choir hums, low organ, dread building quietly
```
[verse]
Bone by bone
They built this place
A garden grown in silence
What sleeps below
Does not dream
It only waits with hollow eyes
[chorus]
Do not turn around
The footsteps behind you
Are not your own
```

### bgm_dun_01_c — 「The Crypt Is Not Empty」
Style: tense and restless crypt march, plucked low strings, ticking rhythm, something counting
```
[verse]
The dust falls slow
On the burial floor
I hear a click
Like a jaw at dawn
[chorus]
Something here
Has been counting my steps
One, two, three
The bones are shaking
The crypt is not empty
```

## 02 ゴレムの石殿 (21-30F)

### bgm_dun_02_a — 「Stone Upon Stone」
Style: heavy stone-hall anthem, big toms and stone-strike percussion, driving minor march
```
[verse]
Stone upon stone
In the great hall
Where the giants sleep
Where the anvils rang
Hammer and heart
Beat the same time
[chorus]
A thunder that learned to walk
Feel the floor shake
Feel the floor shake
The stone has risen
```

### bgm_dun_02_b — 「Footfalls Like Falling Towers」
Style: slow, ominous heavy march, deep drums and grinding bass, sense of immense weight
```
[verse]
I hear them coming
Through the mountain
Footfalls like falling towers
They were forged in fire
To guard what was buried
[chorus]
And I am small
I am small
Under the stone
```

### bgm_dun_02_c — 「Ring the Mountain Bell」
Style: percussive stone march, mid-fast, war-drums and chimes, determined
```
[verse]
Ring, ring
The mountain bell
The golem's march has no end
Shoulders of granite
A chest of the earth
[chorus]
Every step a heartbeat
Follow the thunder
Follow the thunder
Down the stone road
```

## 03 溶岩洞窟 (31-40F)

### bgm_dun_03_a — 「The River Burns」
Style: hot and tense lava cave, distorted low riffs, crackling fire texture, urgent minor key
```
[verse]
The river burns
Under red stone
I walk where the fire breathes
The heat rolls in
Like a living thing
[chorus]
It knows I am here
Step quick, step light
The ground is not solid
The lava is watching
```

### bgm_dun_03_b — 「A Sky Without Stars」
Style: brooding and menacing, deep pulses and ember crackle, slow menace, furnace glow
```
[verse]
Smoke and ember
A sky without stars
The cave glows like a furnace
What crawled in here
Before the world cooled
[chorus]
Still moves in the magma
Do not stop
The dark is hungry
The dark is hot
```

### bgm_dun_03_c — 「The Fire Is Behind Me」
Style: fast driving heat, urgent drums and searing lead, adrenaline chase feel
```
[verse]
I can feel it
Licking at my heels
A river of old anger
The air is a furnace
My blood is a drum
[chorus]
Faster, faster
The fire is behind me
The fire is behind me
```

## 04 毒沼の底 (41-50F)

### bgm_dun_04_a — 「Green Light Glows」
Style: sickly swamp, detuned dissonant pads, bubbling texture, slow crawl, unsettling
```
[verse]
Green light glows
In the black water
The marsh breathes slow
It smells of old rain
[chorus]
The mud takes hold
The air takes hold
Something below
Is wearing a smile
```

### bgm_dun_04_b — 「The Reeds Are Watching」
Style: dissonant and creepy, warped strings and drips, slow lurching rhythm, swamp dread
```
[verse]
The reeds are watching
The frogs have gone silent
Every step leaves a ring
And the ring does not fade
[chorus]
The swamp is patient
The swamp is hungry
It has been waiting
For someone like you
```

### bgm_dun_04_c — 「Walk Soft, Walk Slow」
Style: uneasy mid-tempo swamp stomp, muted brass and bubbles, warning mood
```
[verse]
Walk soft, walk slow
The bottom is not floor
What sinks in the green
Does not come back up
[chorus]
The toads have a song
And the song is a warning
Turn back, turn back
The marsh keeps what it takes
```

## 05 氷の聖堂 (51-60F)

### bgm_dun_05_a — 「Halls of Frozen Light」
Style: cold crystalline cathedral, glassy bells and high strings, spacious and serene with chill
```
[verse]
Halls of frozen light
Where no fire has burned
The ice remembers every word
Spoken in the dark
[chorus]
Cold is a crown
Cold is a law
In the cathedral of ice
Even time stands still
```

### bgm_dun_05_b — 「The Frost Is a Choir」
Style: slow ethereal cold, choir hums and ice chimes, vast emptiness
```
[verse]
The frost is a choir
Singing without breath
The windows are white
The doors are not open
[chorus]
Walk on the glass
Pray on the glass
The saint of the winter
Is listening below
```

### bgm_dun_05_c — 「Breath Like Glass」
Style: crisp mid-tempo cold march, bright arpeggios and cold percussion, resolute
```
[verse]
Breath like glass
Steps like bells
The hall runs long
And the hall runs deep
[chorus]
My blood is a river
The ice is a wall
But the wall must bend
The wall must bend
```

## 06 暗黒の深淵 (61-70F)

### bgm_dun_06_a — 「The Dark Has a Name」
Style: deep abyss, sub-bass drones and sparse low melody, immense pressure, dread
```
[verse]
The dark has a name
But I will not say it
The dark has an eye
And the eye has found me
[chorus]
Deeper, deeper
Than the light has been
In the dark below
Something wears my face
```

### bgm_dun_06_b — 「No Bottom to the Night」
Style: abyssal and slow, low cello and sub drones, dripping silence, vast
```
[verse]
No bottom to the night
No end to the fall
The walls breathe in
And the walls breathe out
[chorus]
I count my torches
They count my heartbeats
Down here, down here
The dark is older than me
```

### bgm_dun_06_c — 「The Eyes Are Counting」
Style: tense low-frequency pulse, creeping staccato, paranoia, mid-tempo dread
```
[verse]
In the black I feel them
On the rock I hear them
A hundred soft steps
None of them mine
[chorus]
The eyes are counting
The eyes are close
Keep walking, keep walking
Do not look down
```

## 07 亡霊王の城塞 (71-80F)

### bgm_dun_07_a — 「The King of Ghosts Still Reigns」
Style: ghostly spectral fortress, reedy flutes and wailing strings, hollow drums, uncanny dignity
```
[verse]
The king of ghosts still reigns
In a castle of cold light
His crown of bone is heavy
His throne is made of night
[chorus]
Bow to the hollow king
The dead do not forgive
The dead do not forget
The dead do not sleep
```

### bgm_dun_07_b — 「A Court of Cold Voices」
Style: spectral and ceremonial, choir whispers and glass bells, slow procession
```
[verse]
A court of cold voices
A hall of pale candles
Every ghost wears a title
Every ghost keeps a grudge
[chorus]
Pass through, traveler
Your name is on the list
The reaper's long shadow
Is shorter now
```

### bgm_dun_07_c — 「The Banners Are Grey」
Style: uneasy mid-tempo ghost march, hollow percussion, spectral brass
```
[verse]
The banners are grey
The horns are of bone
The fortress breathes
In a ghost's slow tone
[chorus]
We walk in the kingdom
Of the ones who are gone
And the gates open wider
The further we go
```

## 08 天使の遺跡 (81-90F)

### bgm_dun_08_a — 「Wings of Marble and Rain」
Style: melancholic ethereal ruins, angelic choir and soft piano, rain texture, sorrow
```
[verse]
Wings of marble and rain
Fallen on the white stone
The angels sang once
Now the ruins moan
[chorus]
What was holy is hollow
What was light is ash
The fallen are watching
From the broken sky
```

### bgm_dun_08_b — 「The Hymn Is Still Playing」
Style: slow sorrowful hymn, strings and distant choir, vast and aching
```
[verse]
The hymn is still playing
In the empty nave
The pews are full of silence
The altar is bare
[chorus]
We were so close to heaven
Now heaven is a room
And the door is sealed
And the door is sealed
```

### bgm_dun_08_c — 「Dust on the Halos」
Style: mid-tempo wistful march, bright minor and soft drums, bittersweet determination
```
[verse]
Dust on the halos
Moss on the swords
The bright ones are buried
Beneath the green
[chorus]
But the light is not gone
It is only sleeping
I will wake the bells
I will wake the bells
```

## 09 魔王の巣窟 (91-99F)

### bgm_dun_09_a — 「The Demon Lord's Den」
Style: demonic and fierce, aggressive low riffs, war drums, sinister choir, high tension
```
[verse]
Ash and iron
Throne of the flame
The demon lord's den
Where the brave become names
[chorus]
Kneel or be broken
The floor is his table
The fire is his tongue
The dark is his smile
```

### bgm_dun_09_b — 「Closer to the Flame」
Style: heavy and menacing, slow crushing tempo, deep brass and sub bass, dread of the finale
```
[verse]
Closer to the flame
Closer to the end
Every step is a vow
Every vow is a wound
[chorus]
The throne room is waiting
The crown is so heavy
Only one of us
Leaves with a heartbeat
```

### bgm_dun_09_c — 「The Last Stair」
Style: frenetic demon march, fast drums and searing leads, desperation and fury
```
[verse]
The last stair, the last stair
The guards do not blink
Their eyes are the fryer's fire
Their hearts are the sink
[chorus]
Break the gate, break the gate
Before the dark closes
One more step
And the legend is ours
```

---

## ボスBGM — bgm_boss.ogg「Hail the Ka-ra-a-ge Emperor」(唐揚げ帝国崇拝アンセム)

ユーザー指定: 歌詞は**唐揚げ帝国にちなんだ崇拝**で盛り上げる。上層階(=100F唐揚げ大魔王への距離)ほど信仰度が上がる=**荘厳な祈りから狂信のクライマックスへ盛り上がる構成**。戦闘BGMとして攻撃的・壮大に。
**T47(09-15)**: 「カラージ」発音修正=歌詞の`Karaage`をモーラ区切り`Ka-ra-a-ge`へ全置換（probe確認済み）。ユーザー指定で**実尺≈2分(=125spec)+シームレスループ**（旧84.5秒は短すぎ）で再生成。

Style: epic fanatical worship anthem, grand war drums and brass, soaring male-choir chanting building to a frenzied climax, sinister grandeur, minor key, aggressive boss battle energy
```
[verse]
Kneel before the golden throne
Where a hundred thousand fryers burn
The Emperor of Crisp and Flame
Whose name no tongue may bear
[chorus]
Hail the Ka-ra-a-ge Emperor
We are the salt upon his wing
Hail the Ka-ra-a-ge Emperor
Our blood is oil, our bones are bread
[verse]
From the deepest dark we climb
Carrying offerings of the brave
Every bone that falls below
Becomes a prayer that will not fade
[chorus]
Hail the Ka-ra-a-ge Emperor
Golden wings above the ash
We will feast when the world is fried
Hail! Hail! Hail!
```
