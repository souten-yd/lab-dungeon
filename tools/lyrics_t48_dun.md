# T48 ダンジョンBGM30曲 — 歌詞・音響指示書（リメイク）

## ユーザー指定（2026-09-16）
T37のダンジョンBGM(30曲・全60〜68s・荘厳/ダーク系)が「**荘厳すぎてちょっと場違い**」。
全30曲(`bgm_dun_00..09_a/b/c`)を再生成:
- テーマ(10F帯)に添いつつ、**割と明るめのテンポの良い歌付き**で(特に1〜50F)
- 感情ライン(冒険の物語に沿って):
  - **1〜30F**: 冒険初心者が意気揚々とダンジョン踏破を夢見て駆け抜ける
  - **31〜50F**: このダンジョンの冒険の辛さが身にしみてくる
  - **51〜70F**: 仲間を失った悲しみをバネに、希望を持って奥に向かっていく
  - **71〜90F**: 色々な苦しみを乗り越え、もうすぐ大きな財宝が手に入る希望を持って進む
  - **91〜100F**: **唐揚げ帝国**に足を踏み入れ、その偉大さに驚愕している
- 全曲: **実尺5分以上(300s+)**・**シームレスループ**・**英語歌詞ボーカル**
- 「Ka-ra-a-ge!」掛け声は**ボス曲専用=ダンジョンBGMには入れない**(ユーザー確認済み)
- 10F帯×3曲=ランダム・各階入場で固定(ゲームコードは現行`themeBgmName`のまま・ファイル名不変)

## 生成パラメータ(全曲共通)
- `instrumental: false`, `vocal_language: "en"`, `loop: true`(シームレスループ)
- `duration_sec: 340`(→実尺300s+目標。T47比=spec125→実110〜135sの法則外挿)
- 出力: `audio/bgm_dun_XX_Y.ogg`(ogg Vorbis 48kHz stereo・既存と同方針)
- 歌詞は本文をそのまま `lyrics` に渡す(`[verse]`/`[pre-chorus]`/`[chorus]`/`[bridge]` マーク付き)
- 5分尺のため**verse2本+bridge+chorus2回**の長尺構成で歌詞量確保(モデルが繰り返して埋める前提)

## QAゲート(全曲)
- 実尺 **300〜400s** / peak < −0.01 dBFS / Vorbis 48kHz stereo
- **ループシーム判定**: 先頭0.5s RMS vs 末尾0.5s RMS の比 0.15〜6.0(フェードアウト→ダウンビート継ぎ目なし)

## テーマ・感情対応表
| XX | 10F帯 | テーマ | 感情ライン | 音響方向 |
|---|---|---|---|---|
| 00 | 1-10F | 地下回廊 | 初心者の意気込み | 明るいフォークロック・跳ねるリズム |
| 01 | 11-20F | 骨の地下墓 | 意気込み(不気味さを軽やかに) | 遊び心のあるロック・クリプト風味 |
| 02 | 21-30F | ゴレムの石殿 | 意気込み(自信の頂) | 打楽器主体の明るいロック |
| 03 | 31-40F | 溶岩洞窟 | 辛さが身にしみる | 駆動する熱いロック(まだ前向き) |
| 04 | 41-50F | 毒沼の底 | 辛さの深化(疲れと執念) | 重い打撃ロック・湿った質感 |
| 05 | 51-60F | 氷の聖堂 | 悲しみをバネに希望へ | 澄んだストリングス+歌・冷たいが温かい芯 |
| 06 | 61-70F | 暗黒の深淵 | 悲しみ→希望の歩行 | 暗いが心臓の鼓動のような前進リズム |
| 07 | 71-80F | 亡霊王の城塞 | 苦難を乗り越えた確信 | 霊的だが力強い行進 |
| 08 | 81-90F | 天使の遺跡 | 大財宝目前の希望 | 輝ける希望の行進・残光の美しさ |
| 09 | 91-100F | 魔王の巣窟(唐揚げ帝国) | 帝国の偉大さに驚愕 | 壮大な驚異・黄金の宮廷の威光(敵意より驚嘆) |

---

## 00 地下回廊 (1-10F) — 冒険の始まり・意気揚々

### bgm_dun_00_a — 「Lantern in the Morning Dark」
Style: bright and bouncy folk-rock dungeon BGM, upbeat major key, jangly guitar, handclaps, warm bass, adventurous and cheerful, a rookie's first descent, lively tempo
```
[verse]
Lantern in my hand
And the world is wide open
A hundred floors below
And I was born to climb them
[pre-chorus]
The stone is cold but my blood is warm
The map says "here be legends"
And I was made for that
[chorus]
Run, little hero, the day is young
Every stair is a song that we haven't sung yet
Down the corridor where the lanterns glow
I'm the bravest one, I'm the bravest one
The legend is me
[verse]
Dust on my boots and a grin on my face
The rats are watching me pass their throne
Some day I'll stand where the big light burns
And this whole dark place will know my name
[bridge]
Step one, step two
The echo claps along
Whatever waits below
Can keep its shadows — I'll bring the morning
[chorus]
Run, little hero, the day is young
Every stair is a song that we haven't sung yet
Down the corridor where the lanterns glow
I'm the bravest one, I'm the bravest one
The legend is me
```

### bgm_dun_00_b — 「A Hundred Floors to Dream」
Style: upbeat indie-rock adventure BGM, bright major key, punchy drums and clean electric guitar, hopeful and energetic, youthful optimism, lively tempo
```
[verse]
They said the dungeon keeps its heroes
I said "then keep me longer"
Packed my bag, sharpened my smile
Signed my name on the door
[pre-chorus]
Forty floors of stone, sixty floors of flame
And I have only just begun
[chorus]
A hundred floors to dream, a hundred floors to run
My shadow and I are just getting started
The dungeon can count its treasures
I'm bringing the luck, I'm bringing the luck
I'm bringing the thunder
[verse]
The first room has a slime and a rusty old sword
The slime has no idea who it's looking at
I tip my hat to the whole underground
The adventure just said "hello"
[bridge]
If I get lost, leave a light on above
If I get tired, I'll sleep on a staircase
I have a hundred floors of reasons
Why I'll be back for more
[chorus]
A hundred floors to dream, a hundred floors to run
My shadow and I are just getting started
The dungeon can count its treasures
I'm bringing the luck, I'm bringing the luck
I'm bringing the thunder
```

### bgm_dun_00_c — 「First Light Below」
Style: cheerful punk-folk dungeon BGM, fast and springy, acoustic and electric guitars, bright major key, playful and daring, a young adventurer sprinting down
```
[verse]
Down, down, the stairs are singing
Up, up, the town is calling
But my boots are already running
And my heart is already winning
[pre-chorus]
No one told me the dark had a heartbeat
Now I'm racing it down the hall
[chorus]
First light below, first light in the deep
I'm the spark that the dungeon can't keep
Every crack in the wall is a window
Every door is a dare
So run, run, little spark
The night is long but I'm the dawn
[verse]
A spider waves, a goblin laughs
A moss slime winks at me
This is the best place on the whole wide earth
And it's three hundred feet below
[bridge]
Somewhere far below the far below
There is a light I haven't seen
And I am going down to meet it
Face to face and grinning
[chorus]
First light below, first light in the deep
I'm the spark that the dungeon can't keep
Every crack in the wall is a window
Every door is a dare
So run, run, little spark
The night is long but I'm the dawn
```

## 01 骨の地下墓 (11-20F) — 意気込み(不気味さを軽やかに)

### bgm_dun_01_a — 「The Bones Tap Their Feet」
Style: playful rock BGM with a crypt flavor, bright but spooky-fun, upbeat major-minor mix, plucked guitar and light percussion, skeletons as an audience, witty and lively
```
[verse]
Ribcage on ribcage, a cathedral of white
The oldest fans in the whole underground
They haven't clapped in a thousand years
But I can swear I hear them tonight
[pre-chorus]
They're keeping time with my boots
Click-clack, click-clack
[chorus]
The bones tap their feet in the bone white hall
The dead are a crowd and the crowd is along
I'll do my best for the gallery below
A thousand years of silence
And now it's a show
[verse]
A skeleton tips its skull at me
A jawbone grins like it knows the score
I'm just a visitor, they're the locals
But tonight the music's mine to play
[bridge]
If I fall, let the choir hum me along
If I win, let the ribcages roar
Whatever happens in this crypt tonight
It's going to be a story
[chorus]
The bones tap their feet in the bone white hall
The dead are a crowd and the crowd is along
I'll do my best for the gallery below
A thousand years of silence
And now it's a show
```

### bgm_dun_01_b — 「Old Friends Down Here」
Style: whimsical mid-tempo rock, warm bass groove, light brass stabs, bright major key with spooky undertone, friendly with the dead, playful confidence
```
[verse]
Hello, hello, to the ones who stayed
You've been down here longer than the dark
I'm passing through, I'm not here to disturb
But I thought I'd say hi to the family
[pre-chorus]
Your silence is so loud
It's got a rhythm to it
[chorus]
Old friends down here in the crypt of bone
We don't have much time to talk
So I'll leave my luck leaning on your wall
And you keep the way lit for the next one
Down the stairs
[verse]
They say the dead keep their grudges
I say the dead keep their seats
Save me the front row when the big ones come
And wave when the legend walks past
[bridge]
When I come back up with the treasure
I'll tell the whole town about you
The quiet ones, the patient ones
The ones who kept the dungeon alive
[chorus]
Old friends down here in the crypt of bone
We don't have much time to talk
So I'll leave my luck leaning on your wall
And you keep the way lit for the next one
Down the stairs
```

### bgm_dun_01_c — 「Dance for the Crypt」
Style: galloping bright rock, energetic drums and bouncing bass, major key, playful spookiness, a daredevil dancing with skeletons, lively tempo
```
[verse]
One step, two steps, the floor goes click
The skulls are swaying in time
This isn't a graveyard, it's a ballroom
And I've just learned the steps
[pre-chorus]
Spin me, dust me
Buried me not
[chorus]
Dance for the crypt, the crypt is awake
A thousand pale feet in a single line
I'll be the last one still on my legs
When the morning finds us
Dancing still
[verse]
A spine stretches out and offers a hand
A femur taps the ground
The dead have been waiting for a partner
I'm honored, I'm in
[bridge]
Let it be said in the town above
That the hero danced with the dead
That the crypt clapped its hollow hands
And the night went on and on
[chorus]
Dance for the crypt, the crypt is awake
A thousand pale feet in a single line
I'll be the last one still on my legs
When the morning finds us
Dancing still
```

## 02 ゴレムの石殿 (21-30F) — 意気込み(自信の頂)

### bgm_dun_02_a — 「Hammer and Heart」
Style: bright percussive rock, stone-strike toms and driving bass, upbeat major key, forge heat turned into rhythm, confident and powerful, lively tempo
```
[verse]
In the stone hall where the anvils rang
The forges went cold a thousand years ago
But the rhythm is still in the walls
And my heartbeat matches the old beat
[pre-chorus]
Strike it, strike it
Like the mountain used to
[chorus]
Hammer and heart, hammer and heart
I'm walking through the forge of giants
And the whole stone hall is ringing out
In my key, in my key
The mountain learned my song
[verse]
The golem sleeps with a fist of granite
The dust hangs still in the air
But I'm not here to wake the sleeper
I'm here to pass through like thunder
[bridge]
They built this hall to outlast the world
The world gave up, the hall is still standing
So am I, so am I
[chorus]
Hammer and heart, hammer and heart
I'm walking through the forge of giants
And the whole stone hall is ringing out
In my key, in my key
The mountain learned my song
```

### bgm_dun_02_b — 「Stone Can't Stop a Song」
Style: determined bright rock, sturdy 4/4 drums, warm guitars, major key with a bit of grit, stubborn optimism, mid-fast tempo
```
[verse]
The walls are forty feet of granite
The door is a boulder with a key
And I'm just a small bright thing
With a song in my chest
[pre-chorus]
Let the stone do its best
I've got something it can't grind
[chorus]
Stone can't stop a song
Stone can't stop a spark
Stone can't hold a dream
That's already learned to run
So stand aside, big hall
I'm passing through with my head up
[verse]
The guardians turn on their stone necks
The floor groans under my feet
But a dungeon is only a door
If you've got the courage to knock
[bridge]
And when I reach the light at the bottom
I'll wave at every wall
You kept the way hard for me
Now keep it open
[chorus]
Stone can't stop a song
Stone can't stop a spark
Stone can't hold a dream
That's already learned to run
So stand aside, big hall
I'm passing through with my head up
```

### bgm_dun_02_c — 「The Forge Is Singing」
Style: warm driving rock, steady stomp rhythm, bright major key, clanging percussion and melodic lead, hopeful momentum, mid tempo
```
[verse]
The forge is singing in a key
That the living forgot
Every hammerhead a cymbal
Every pillar a note
[pre-chorus]
I hum along as I walk
My voice joins the stone
[chorus]
The forge is singing, the mountain is along
A thousand cold fires starting in my chest
If the giants made this place to last
Then I'll be the last one standing here
Still singing
[verse]
Moss on the anvil, lichen on the bell
Time moved in here and left the music
I'm borrowing the beat
And I'll carry it down
[bridge]
Somewhere below the below
The biggest fire of all is waiting
And this little song of mine
Has been climbing toward it for three hundred steps
[chorus]
The forge is singing, the mountain is along
A thousand cold fires starting in my chest
If the giants made this place to last
Then I'll be the last one standing here
Still singing
```

## 03 溶岩洞窟 (31-40F) — 冒険の辛さが身にしみる

### bgm_dun_03_a — 「The Heat Is Real」
Style: driving rock with heat, strong drums and tight guitar riff, tense but forward-moving, major-minor mix, the first real hardship of the journey, mid-fast tempo
```
[verse]
The air has weight now, you can feel it on your shoulders
The road glows like it's alive
I came down here full of songs
And the first real thing this dungeon said
Was "not so fast"
[pre-chorus]
The easy part is over
The real part has begun
[chorus]
The heat is real and the way is long
My water is less and the light is red
But a hero is measured by the floor
That stops trying to break them
So I walk on
[verse]
The fire imp hisses from the ceiling
The ground shifts under my boots
This is where the dream gets heavy
This is where the grin gets earned
[bridge]
I was the bravest one, they said
Now I'm the stubborn one
And if the legend has a price
The price is sweat
[chorus]
The heat is real and the way is long
My water is less and the light is red
But a hero is measured by the floor
That stops trying to break them
So I walk on
```

### bgm_dun_03_b — 「Ember Road」
Style: brooding mid-tempo rock, deep bass pulse and ember-crackle texture, weary but determined, minor key with a driving core, the weight of the journey, mid tempo
```
[verse]
Day one was a storybook
Day ten is a furnace
The map I carried is a lie
Written by someone who never got this hot
[pre-chorus]
The dream is smaller now
The dream is still there
[chorus]
Ember road, ember road
The dust is tasting like smoke
I don't know what I'm walking toward
But I know what I'm walking through
And I'm still walking
[verse]
The lava river keeps its own time
It doesn't care about my schedule
Somewhere up top the town is laughing
At the fool who came down for gold
[bridge]
Let them keep their easy summers
I'm growing roots in the red stone
Everything that breaks down here
Is something I carried that I didn't need
[chorus]
Ember road, ember road
The dust is tasting like smoke
I don't know what I'm walking toward
But I know what I'm walking through
And I'm still walking
```

### bgm_dun_03_c — 「Still Burning, Still Going」
Style: hard-hitting rock, urgent drums and searing lead, exhaustion turned into momentum, minor key, grit and defiance, mid-fast tempo
```
[verse]
My arms remember every swing
My lungs remember every heat
The dungeon took the easy version of me
And handed back the real one
[pre-chorus]
I'm not the kid from the first floor anymore
[chorus]
Still burning, still going
The fire took my shadow and I don't miss it
The road is a river and I'm the stone
That the river can't move
Still burning, still going
[verse]
The lava spider tests the water
The flame spirits count my steps
They can do their worst
The worst is what I'm made of now
[bridge]
There was a boy who dreamed of treasure
There's a man who's earning it
The boy would be proud
The man has no time for pride
[chorus]
Still burning, still going
The fire took my shadow and I don't miss it
The road is a river and I'm the stone
That the river can't move
Still burning, still going
```

## 04 毒沼の底 (41-50F) — 辛さの深化(疲れと執念)

### bgm_dun_04_a — 「Mud and Oath」
Style: heavy stomping rock, slow-driving rhythm, wet textures under tight drums, weary determination, minor key, the deep hardship, mid tempo
```
[verse]
The marsh doesn't fight you, it just takes its time
The mud keeps what it grabs
My pack is heavy, my boots are full of black water
And the dream has a bruise on it
[pre-chorus]
But an oath is a kind of rope
You tie around your own waist
[chorus]
Mud and oath, mud and oath
The bottom of the swamp is not the bottom of me
I gave this place my sweat and my easy years
So I'll give it my stubbornness
And keep going down
[verse]
The poison mist writes its warning in the air
The toads have stopped pretending to be friendly
I've buried a version of myself on every floor
And I'm still standing
[bridge]
Someday the town will ask what it cost
I'll say "it cost me the light"
And I'll be smiling
Because I'll have the treasure
[chorus]
Mud and oath, mud and oath
The bottom of the swamp is not the bottom of me
I gave this place my sweat and my easy years
So I'll give it my stubbornness
And keep going down
```

### bgm_dun_04_b — 「The Slow Water」
Style: heavy mid-tempo rock, sludgy bass and steady drums, dissonant pads under a clear vocal, worn-down but unbroken, minor key, mid tempo
```
[verse]
The slow water takes the sound of your footsteps
So you learn to count your own breath
Forty-one floors of green
And the green is learning your name
[pre-chorus]
The easy heroes are all up top
By now
[chorus]
The slow water rises, the slow water waits
But a slow heart is the last thing to sink
I'm not running anymore, I'm just walking
And walking is a kind of winning
[verse]
The tentacle tests the ankle, the puffer tests the nerve
The swamp has a curriculum
And I am still a student
Passing, barely, but passing
[bridge]
If I ever get a monument
Carve the mud on it
Let them know the water was slow
But it was not the slowest thing down here
[chorus]
The slow water rises, the slow water waits
But a slow heart is the last thing to sink
I'm not running anymore, I'm just walking
And walking is a kind of winning
```

### bgm_dun_04_c — 「Green Warning」
Style: uneasy stomp rock, muted brass and bubbles, warning mood under a steady pulse, dark humor and grit, minor key, mid tempo
```
[verse]
The marsh has a song and the song is a warning
The toads sing it in a key that means "turn back"
I've been hearing it for ten floors now
And I've been answering it with my boots
[pre-chorus]
Turn back, the song says
The song has never been wrong
[chorus]
Green warning, green warning
The bottom of the world has a bottom lip
And it is full of teeth
I came down here for a story
And the story is happening to me
[verse]
The mist rolls in like a slow apology
The floor gives back half of every step
I am learning the swamp's grammar
Subject: the swamp. Verb: keeps. Object: me
[bridge]
But here's the thing the toads don't know
I didn't come for the green
I came for what's under the green
And the green is only the door
[chorus]
Green warning, green warning
The bottom of the world has a bottom lip
And it is full of teeth
I came down here for a story
And the story is happening to me
```

## 05 氷の聖堂 (51-60F) — 悲しみをバネに希望へ

### bgm_dun_05_a — 「Names in the Ice」
Style: cold crystalline rock with a warm heart, clear strings and bright arpeggios over steady drums, aching but hopeful, the grief of lost companions turned into resolve, major key with cold color, mid tempo
```
[verse]
The ice keeps what the fire could not keep
Every name we lost is written in the wall
I press my hand to the cathedral cold
And the cold presses it back
[pre-chorus]
They walked with me this far
So I walk for both of us now
[chorus]
Names in the ice, names in the ice
The winter is not the end of the story
We carried the light down here
And the light is heavier than the dark
So I go on, I go on
[verse]
The frost wolves howl the old songs
The statues watch with patient eyes
I say their names to the empty hall
And the hall says them back
[bridge]
If hope is a fire
Then we are the kind of fire
That the snow doesn't know how to kill
[chorus]
Names in the ice, names in the ice
The winter is not the end of the story
We carried the light down here
And the light is heavier than the dark
So I go on, I go on
```

### bgm_dun_05_b — 「The Cold Is a Witness」
Style: solemn bright rock, glassy bells and steady pulse, grief and hope intertwined, spacious and clear, major key, mid tempo
```
[verse]
The cold is a witness, the cold keeps the record
Of every hand that slipped from mine
The cathedral holds its breath
While I do what the living do
[pre-chorus]
I do not stop. Stopping is for the story
To end
[chorus]
The cold is a witness and I am not alone
A hundred small fires are walking in my chest
Each one a name I will not let go
The winter can keep the dark
I'm keeping the way
[verse]
The ice arches like a spine of the world
The frozen bells are waiting to be rung
Someday someone will ring them
With the news that we made it through
[bridge]
For the ones who stayed in the snow
I am the season that comes after
I am the thaw walking south
[chorus]
The cold is a witness and I am not alone
A hundred small fires are walking in my chest
Each one a name I will not let go
The winter can keep the dark
I'm keeping the way
```

### bgm_dun_05_c — 「Thaw」
Style: crisp mid-tempo rock march, bright arpeggios and cold percussion, resolute and warm, hope breaking through winter, major key, mid-fast tempo
```
[verse]
My breath is glass but my blood is a river
The river has a direction and the direction is down
The cathedral is beautiful and the beautiful
Does not get to keep us
[pre-chorus]
Grief is a door, I'm just going through it
[chorus]
Thaw, thaw, the ice is a season
And seasons have always left
We came down here for a reason
And the reason is still standing
Thaw, thaw, the light is patient
The light was here before the snow
[verse]
The saint of winter turns her statue face
To watch the small warm thing walk past
I tip my hat to the beautiful cold
And keep my feet moving
[bridge]
Everything we lost is a kind of fuel
Now
The fire that left the town
Is burning bigger down here
[chorus]
Thaw, thaw, the ice is a season
And seasons have always left
We came down here for a reason
And the reason is still standing
Thaw, thaw, the light is patient
The light was here before the snow
```

## 06 暗黒の深淵 (61-70F) — 悲しみ→希望の歩行

### bgm_dun_06_a — 「The Dark Has a Pulse」
Style: deep but forward-moving rock, sub-bass pulse like a heartbeat, sparse bright guitar over the dark, determination under pressure, minor key with a driving core, mid tempo
```
[verse]
The dark has a pulse and the pulse has a time
And my boots are learning to walk with it
The abyss is not empty, it's just waiting
With its hands folded in the black
[pre-chorus]
Waiting for me to stop
I don't plan to
[chorus]
The dark has a pulse, I have a name
And the name is the one I came down here to earn
Every shadow that reaches for my lantern
Just shows me how far the light still reaches
[verse]
The walls breathe in, the walls breathe out
The deep has its own slow weather
I carry the cold cathedral's names
Like embers in my coat
[bridge]
The dark can have its silence
The dark can have its deep
The dark does not get to have
The next step
[chorus]
The dark has a pulse, I have a name
And the name is the one I came down here to earn
Every shadow that reaches for my lantern
Just shows me how far the light still reaches
```

### bgm_dun_06_b — 「Keep the Count」
Style: steady mid-tempo rock, ticking rhythm and low grooving bass, quiet intensity, hope kept alive by routine, minor key, mid tempo
```
[verse]
I count my steps the way the dark counts my breath
One for the way, two for the wall
Three for the ones who walked with me
Four for the reason I don't stop
[pre-chorus]
The count is the lamp
The count is the rope
[chorus]
Keep the count, keep the count
The deep is wide but the count is straight
I was small when the town let me go
The count made me something the dark respects
[verse]
The eyes are counting, I know they are
But the count I keep is the one that matters
Every number is a small victory
And I am made of small victories
[bridge]
Somewhere below the count ends
And something begins
I will find out what it is
One number at a time
[chorus]
Keep the count, keep the count
The deep is wide but the count is straight
I was small when the town let me go
The count made me something the dark respects
```

### bgm_dun_06_c — 「Small Warm Thing」
Style: mid-tempo driving rock, warm melodic lead over dark pulse, lonely but unbroken, minor key with bright vocal, mid-fast tempo
```
[verse]
The abyss looks at you like you are a candle
Small, warm, and honestly surprising
It has eaten a thousand candles
And you are still burning
[pre-chorus]
Let it look
I was built for looking
[chorus]
Small warm thing, walking on
The dark is a country and I am the post
Carrying the news that the light
Has not given up on the bottom
Small warm thing, still on
[verse]
The shadow wolves keep a respectful distance
The deep has its etiquette
A candle that doesn't die
Earns a kind of silence
[bridge]
The ones who walked with me are in the wind of it
Their footsteps are in my count
So the dark is looking at more
Than one small flame
[chorus]
Small warm thing, walking on
The dark is a country and I am the post
Carrying the news that the light
Has not given up on the bottom
Small warm thing, still on
```

## 07 亡霊王の城塞 (71-80F) — 苦難を乗り越えた確信

### bgm_dun_07_a — 「The Grey Banners Salute」
Style: spectral but powerful march, hollow drums and bright brass, earned confidence, the ghost king's court acknowledging the survivor, major key with ghostly color, mid-fast tempo
```
[verse]
The fortress opens its grey gates
And for the first time, it opens them early
The ghost king watches from his throne of night
And something in his hollow crown looks like respect
[pre-chorus]
Seventy floors in, I'm not a visitor anymore
[chorus]
The grey banners salute
The cold horns sound my name
The dead have a long memory
And mine is the one they're keeping
I've passed through the fire, the mud, the ice
And I'm still standing in their hall
[verse]
The reaper tips his scythe and steps aside
The ghost soldiers keep a ceremonial distance
This is what it looks like
When the dungeon stops being an obstacle
[bridge]
The town above can keep its stories
I am the story now
And the story has a way
[chorus]
The grey banners salute
The cold horns sound my name
The dead have a long memory
And mine is the one they're keeping
I've passed through the fire, the mud, the ice
And I'm still standing in their hall
```

### bgm_dun_07_b — 「A Court That Nods」
Style: ceremonial mid-tempo rock, glass bells and steady pulse, dignified and warm, quiet triumph, major key, mid tempo
```
[verse]
A court of cold voices has a protocol
For the ones who survive
They stand in their pale rows
And they nod, one at a time
[pre-chorus]
Each nod is a floor I earned
[chorus]
A court that nods, a hall that yields
The ghosts have seen a thousand come
And a thousand go
And I am the one the candles are lit for
[verse]
The king of ghosts keeps his silence
But his silence has changed its key
From "you will not pass"
To "we are watching you pass"
[bridge]
There is a treasure at the bottom
And there is a road that led me here
The road is made of everything
I thought I had lost
[chorus]
A court that nods, a hall that yields
The ghosts have seen a thousand come
And a thousand go
And I am the one the candles are lit for
```

### bgm_dun_07_c — 「The Long Shadow Shortens」
Style: confident mid-fast rock march, hollow percussion and spectral brass, forward momentum, the final stretch in sight, major key, mid-fast tempo
```
[verse]
The long shadow of the reaper
Used to cover my whole road
Now it's only a step behind me
And the step is getting shorter
[pre-chorus]
Twenty floors to go
The treasure is a sound now, almost
[chorus]
The long shadow shortens, the hall runs out
The fortress is only a door from the end
I have worn the dungeon down
And now the dungeon is wearing me thin
Which is the point
[verse]
The grey banners are streaming
The cold court is on its feet
Every ghost is a witness
To the part of the story where the hero arrives
[bridge]
I came down for gold
I'm leaving with something heavier
I'm leaving with the proof
[chorus]
The long shadow shortens, the hall runs out
The fortress is only a door from the end
I have worn the dungeon down
And now the dungeon is wearing me thin
Which is the point
```

## 08 天使の遺跡 (81-90F) — 大財宝目前の希望

### bgm_dun_08_a — 「Dust on the Halos, Light in the Hands」
Style: luminous mid-tempo rock march, bright strings and warm drums, bittersweet triumph, the great treasure just ahead, major key with angelic shimmer, mid-fast tempo
```
[verse]
The ruins of the bright ones are all around
And the light that fell here is still falling
Not gone, just resting
In the marble and the rain
[pre-chorus]
Ten floors and the big light is close enough to feel
[chorus]
Dust on the halos, light in the hands
The treasure is not a thing, it's a distance
And the distance is almost a memory
I've fallen, I've burned, I've frozen
And I'm still climbing toward the glow
[verse]
The fallen archers lower their bows
The broken sky leans in to listen
Someday the bells of this ruin will ring
Not for the ones who fell
But for the one who came through
[bridge]
The town will ask what the treasure looks like
I'll say "like the sun, but it was mine"
[chorus]
Dust on the halos, light in the hands
The treasure is not a thing, it's a distance
And the distance is almost a memory
I've fallen, I've burned, I've frozen
And I'm still climbing toward the glow
```

### bgm_dun_08_b — 「The Hymn Finishes」
Style: soaring mid-tempo rock, distant choir and bright piano, hope at full volume, the final approach, major key, mid-fast tempo
```
[verse]
The hymn that's been playing in the empty nave
For a thousand years, is reaching its last line
The pews are full of silence
And the silence is leaning forward
[pre-chorus]
The last line is mine to sing
[chorus]
The hymn finishes, the light comes down
The broken sky remembers how to shine
Everything I lost is on this floor now
Paid in full, and I am still standing
Ten floors, ten floors
And the great light is waiting
[verse]
The fallen followers cross their arms
And for the first time, they are smiling
The holy shields are picking me up
And setting me down, closer
[bridge]
If the treasure is real
Then it was real from the first floor
And I have just been walking toward it
[chorus]
The hymn finishes, the light comes down
The broken sky remembers how to shine
Everything I lost is on this floor now
Paid in full, and I am still standing
Ten floors, ten floors
And the great light is waiting
```

### bgm_dun_08_c — 「Almost a Memory」
Style: bright driving rock, energetic drums and shimmering leads, elation and relief, the last stretch, major key, mid-fast tempo
```
[verse]
Eighty floors of hard
And the hard has a light at the end of it
The ruins hum with a frequency
That my bones have been waiting for
[pre-chorus]
The treasure is almost a memory
Because it's almost here
[chorus]
Almost, almost, the light is a door
And the door is almost a hand
I have carried this much weight
And the last weight is the good kind
[verse]
The marble is warm under my boots
The rain in the ruins is falling upward
The fallen are watching
And the watching has become a blessing
[bridge]
When I stand in the great light
I will remember every floor
And I will say thank you
To the dark, to the fire, to the ice
[chorus]
Almost, almost, the light is a door
And the door is almost a hand
I have carried this much weight
And the last weight is the good kind
```

## 09 魔王の巣窟 (91-100F) — 唐揚げ帝国に足を踏み入れ・偉大さに驚愕

### bgm_dun_09_a — 「The Golden Empire」
Style: vast and awestruck epic rock, grand brass and shimmering strings over a steady mighty pulse, wonder and awe rather than fear, the golden Karaage Empire revealed, majestic major key, mid tempo
```
[verse]
The last door opens and the dark ends
And the dark was only the hallway
Gold, gold, gold as far as the eye can fry
A hundred thousand lanterns in the dark
And every lantern is a crown
[pre-chorus]
The empire I came to conquer
Is the empire that conquered the dark
[chorus]
The golden empire, the golden empire
I came for treasure and I found a world
The thrones are stacked like the sun is stacked
And the light is so wide
It has no edges
[verse]
The demon guards stand in rows of flame
Not to stop me, but to present it
This is what the dungeon was building
Every floor, every monster, every wall
Was a door for this
[bridge]
My map is a joke, my dream is a seed
The garden it grew into
Has its own weather
[chorus]
The golden empire, the golden empire
I came for treasure and I found a world
The thrones are stacked like the sun is stacked
And the light is so wide
It has no edges
```

### bgm_dun_09_b — 「A Kingdom of Fire and Salt」
Style: majestic mid-tempo epic rock, deep brass fanfare and warm choir, awe and reverence, the scale of the Karaage Empire, major key with dark grandeur, mid tempo
```
[verse]
They built a kingdom where the world gives up
A kingdom of fire and salt and gold
The floors I bled through were the foundation stones
And I am standing in the finished room
[pre-chorus]
This is bigger than the legend
The legend was the doorway
[chorus]
A kingdom of fire and salt
A kingdom no one measured
The demon lord's court is a city of light
And the light is looking back at me
With curiosity
[verse]
The throne room has a weather of its own
The air tastes of embers and something sweet
Every wall is a record of the brave
Who made it this far
[bridge]
I came down here to take
And I am learning, slowly
That some things are here to be witnessed first
[chorus]
A kingdom of fire and salt
A kingdom no one measured
The demon lord's court is a city of light
And the light is looking back at me
With curiosity
```

### bgm_dun_09_c — 「The Fryer's Light」
Style: grand and shimmering epic rock march, mighty drums and soaring leads, awe and wonder, the final approach to the emperor, bright major key, mid-fast tempo
```
[verse]
The light at the bottom of the world
Turns out to have a ceiling
And the ceiling is made of flame
And the flame is made of crowns
[pre-chorus]
Nine hundred steps, and this is what they were for
[chorus]
The fryer's light, the fryer's light
It falls on me like a warm rain
I have walked through a hundred rooms of the dark
To stand in one room of this
[verse]
The empire hums with a billion small fires
The demon court bows to the architecture
Not the emperor — the architecture
As if the building itself is the legend
[bridge]
Someday I will tell the town
And the town will say "that's not possible"
And I will smile
Because I have been told that by every floor
[chorus]
The fryer's light, the fryer's light
It falls on me like a warm rain
I have walked through a hundred rooms of the dark
To stand in one room of this
```

---

## 検証・運用
- probe = `bgm_dun_00_a`(実尺300s+の可否+明るさの方向確認)→ 全30曲blind retry
- 再生成ドライバ: `/tmp/opencode/karaage_regen_run.py` 流用(T48版: QA=300〜400s・ループシーム判定)
- 生成失敗の自動再実行はwatchdog(T47版と同様)
