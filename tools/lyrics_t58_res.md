# T58 「死に戻り」テーマ曲 歌詞・スタイル定義

## 指定（ユーザー 2026-09-17）
- 力強い・熱い曲 / **女性ボーカル** / **日本語歌詞** / **約2分**（duration_sec=125 指定）
- テーマ: 死に戻り — 何度死んでも諦めずに立ち上がり、逆境に立ち向かう
- 用途: 死亡→町に戻り、**その後の初回ダンジョン入りのみ**1回だけ再生（`bgm_res.ogg`・loop=trueで階中再生）
- 形式: Ogg Vorbis 48kHz stereo / ~150kbps / peak <-0.01dBFS（既存BGMと同一仕様）

## スタイルプロンプト
```
Powerful J-rock anthem, female lead vocal (passionate, powerful, emotional),
driving drums, distorted electric guitars, soaring chorus, uplifting and hot,
anime opening energy, key of A minor, around 140 BPM.
Theme: dying and coming back — rising again no matter how many times you fall,
facing adversity without giving up.
```

## 歌詞（日本語・vocal_language="ja"）
```
[verse]
また灰となって 街に帰る
失った夢を 数えながら
でも胸の奥 火は消えない
何度折れようと 膝は伸びる

[pre-chorus]
痛みは証 傷は地図
立ち上がるたび 強くなる
今日もまた 刃を研ぐ
倒れた場所から 歩き出す

[chorus]
死に戻りの夜を越えて
何度死んでも 立ち上がれ
燃え尽きた心も 今夜また 火をつけろ
伝説への道は 遠くて険しい
それでも前を向いて 走れ
```

## QAゲート
- 実尺 100〜140s（125spec）
- peak < -0.01dBFS（クリップ0%）
- Ogg Vorbis 48kHz stereo
- ASRで日本語歌詞が正しく歌唱されているか確認
- 音量が既存BGM（peak -0.7〜-2.9dBFS帯）と同等
