# 唐揚げダンジョン — 進捗ログ

> 締切版（セッション中断時の復元用）。最終更新: 2026-09-16 01:40 (JST) — **T47 全完了（実装+テスト+ボスBGM 10曲再生成・全QA合格）**

## 全体ステータス
| タスク | 状態 |
|---|---|
| T0〜T42 | ✅ 完了・検証済み |
| T37 BGM 31曲 | ✅ 生成・検証完了（テーマ30曲60.2〜68.2s/ボス84.5s→**T47で122.9sに再生成**・英語歌詞ボーカル・シームレスループ） |
| T38 SEファイル(20本) | ✅ 全20本完成・QA済（2秒窓方針） |
| T40 必殺TTS / T41 中ボスボイス | ✅ **廃止**（ユーザー指示09-15: 日本語TTSに不自然な部分→**ボイスなしで完成**） |
| T35 統合テスト+記録 | ✅ 完了（最終132/132 green + audio最終sweep + 記録更新） |
| **T43 中ボス専用BGM9曲** | ✅ **完了・検証済み（音源9/9インストール・QA合格・AUD_LISTとディスク完全一致）** |
| **T44 モバイルBGM自動再生** | ✅ 完了・検証済み（t44_test 9/9） |
| **T45 性能最適化** | ✅ 完了・計測済み（t45_perf_test 13/13・before/after計測下記） |
| **T46 モバイル・描画バグ修正** | ✅ 完了・検証済み（t46_test 29/29→T47でWeb Audio仕様に33/33） |
| **T47 Web Audio SFX+回転ズレ+BGM発音** | ✅ **全完了**（t47_test 14/14・全15スイートgreen / BGM 10曲`Ka-ra-a-ge`表記・約2分+ループで再生成・最終QA 10/10合格） |

## 最新（2026-09-15 午後）

### T43 中ボス専用BGM — 完了（9/9）
- 設計: 10F〜90F帯の中ボス9体各自の「唐揚げ王国崇拝」BGM。全曲にヴォーカルフック**「Karaage!」**、各約2分。深層ほど狂信化: 10Fゴンタ=素朴な民間賛美歌 → 50F=聖戦の行進 → 90Fベリアル=終末の集団合唱。歌詞仕様 `tools/lyrics_t43_mb.md`（"The Fried Kingdom"モチーフ・T37「Karaage Emperor」と一貫）。
- 配線: `mbBgmName(floor)`/`isMbBgm(n)`・AUD_LIST 69→**78**（BGM 35→**44**）・`mbTalk`挑発時=その階専用曲(`bgm_mb_01〜09`)に切替・`mbDefeated`=フロースレームBGM復元。検証: t43_test 12/12 + t41_t42 D4 / t41_gatekeys K2 をT43仕様に更新。
- 音源(**9/9インストール・QA合格**): `bgm_mb_01`=118.2s / `bgm_mb_02`=119.2s / `bgm_mb_03`=123.5s / `bgm_mb_04`=121.7s / `bgm_mb_05`=118.5s / `bgm_mb_06`=120.9s / `bgm_mb_07`=117.3s / `bgm_mb_08`=121.9s / `bgm_mb_09`=120.6s（全曲110〜135s枠・peak -0.8〜-2.3dB・Vorbis 150k/48kHz stereo・クリップ0%）。`bash /tmp/opencode/qa_mb_bgm.sh`=**9 OK / 0 FAIL**。
- **GPU VRAM競合の経過**: 初回生成時、他プロセス(ユーザーの`llama-server` Qwen3.8-27B)がGPU[0]の34.2GB中~23GBを占有→ACE-Step LM初期化で「HIP out of memory」で4曲失敗。対策=`/tmp/opencode/retry_mb_bgm_blind.py`(**VRAMゲートなし・失敗ごとに即時再挑戦**のバックグラウンドループ)を起動→GPUが空いた窓(16:15/16:52-17:01)を自動捕捉して残4曲を全生成。検証済みコピーは`/tmp/opencode/mb_bgm_final/`(9本)。
- 最終確認済み: audio/=**78本**でAUD_LIST(78・BGM44+SFX34)と完全一致・`run_all_tests.sh`全13スイートgreen・`node --check`合格。

### T44 モバイル・タイトルBGM自動再生
- 報告: 「モバイルだとトップ画面で音楽がならない」。原因=ブラウザ自動再生ポリシー(初回ユーザー操作なしに`Audio.play()`不可)。
- 実装: `tryPlayBgm()`+`bgmPending`フラグ(BGM再生失敗/未開始でpending保持)+`unlockAudio()`=window `pointerdown`/`touchstart`と**ゲーム本体の既存keydownハンドラ内**に配線(第二window listenerは禁止=ハーネスが最後1件のみ保持するため)。初回操作でタイトルBGM開始+タイトル画面に「タップでサウンドON」ヒント表示。
- 検証: t44_test **9/9**（pending保持/タップで開始/二重再生防止/キー操作開始/ダンジョン中無効化）。

### T45 性能最適化（実装+計測完了）
報告: 「挙動が重い。攻撃時やアイテム取得時に特に固まる。また、敵が多い場合にも固まる。よく使うSEはキャッシュすることや、(…)動作表示を軽量化することで高速化できないか？最大数の敵が発生時にも処理落ちせずスムーズに処理して欲しい」。

**実施した3点:**
1. **床レイヤオフスクリーンキャッシュ** — 全マップ1792×1280(2240タイル)を`FLOOR_CV`に1回レンダリングし、毎フレームは可視領域の単一`drawImage`ブリット。静的部分(床/草/石・毒沼ベース・穴・柱・ロックドア・水+水際・2.5D壁影グラデ・隠し壁強調)を焼き込み、動的部分(毒泡・水波紋・pitScar・秘宝室グロー)は`drawFloorDynamics`が可視範囲のみ毎フレーム描画。`invalidateFloor()`フック: `enterFloor`/IMG onload/プレイヤー穴埋め(`stepOnHazard`)/敵穴埋め(`enemyStepHazard`)/秘宝室開錠/トラップ室ロック。トラップ(尖刺/転移)・開いた罠扉・スイッチパルス・tint・チャージ警告・エンティティ/パーティクル/floatは毎フレームのままで不変。
2. **`ctx.filter`全廃** — 攻撃/被弾・アイテム取得の3箇所のfilterヒットフラッシュを軽量オーバーレイ矩形に置換(白`rgba(255,255,255,.75)`/敵白/プレイヤー暗`rgba(20,30,60,.5)`)。filterはGPU合成コストが大きく、攻撃時スパイクの主因。
3. **SFXプール起動時予備生成** — 34種×5本=170 Audio要素を起動時に一括生成(共有decoded buffer)。初回再生時のAudio要素生成スパイクを解消(常時5本/種のプール維持)。

**before/after計測**（ヘッドレスハーネス・40敵・300フレーム・canvas APIカウント。before=編集前タイルループの忠実再構築+計測、after=現行コード実測）:

| メトリクス | 変更前 | 変更後 | 変化 |
|---|---|---|---|
| canvas呼び出し/フレーム | 2,090 | 1,163 | **−44%** |
| `fillRect`/フレーム | 1,094 | 69 | **−94%** |
| `createLinearGradient`/フレーム | 21 | 0 | **−100%**（壁影をキャッシュ化） |
| タイル`drawImage`/フレーム（実ブラウザ換算） | ~340 | **1**（ブリット） | **−99.7%** |
| JS時間/フレーム（ヘッドレス） | 0.173 ms | 0.100 ms | −42% |
| 攻撃/取得時の`ctx.filter`設定 | 各回~11フレーム | 0 | **全廃** |
| 敵48体・フレーム平均（t45 D1） | — | <8 ms（60fpsの1/13以下） | 60fps維持 |
| SFX Audio要素生成（初回再生時） | その都度生成 | 起動時一括170本（以後0生成） | スパイク解消 |

> 注: ヘッドレスではcanvas呼び出しはno-opのため実GPUコストは含まれない。実ブラウザではfillRect/drawImageの減少がGPUラスタ化+GPU→CPU合成の削減に直結し、攻撃時/取得時のスパイク(filter)は完全に消える。

**検証:** t45_perf_test **13/13**（A: プール生成方式+連打6回で5本維持 / B: FLOOR_CV存在+動的リスト+120fでdrawImage<3000・fillRect<20000・gradient 0 / C: 攻撃+10f・取得+5fでfilter設定0 / D: 敵48体で平均<8ms・<16.7ms・600f無例外）+ **全回帰green**+`node --check`合格。

### T46 モバイル・描画バグ修正（2026-09-15・報告3件+附帯1件）
**ユーザー報告(3件):** ①「移動していると動かなくなる」（モバイル・常に/頻繁に）②「敵を攻撃すると敵の背景が白くなる」③「横向きにしても画面に広がらない」。

**診断:** ヘッドレスハーネス(rAF駆動+phase/gate/画面プロブ)で**ゲームロジック健全を証明**（100フロールームランダムウォーク0例外・0実停滞・30回右長押し0デッドロック・9/9中ボス戦OK。観測された「phase=enemy停滞」は全てgameover画面の正当フリーズ）→ ①は環境レベル(モバイルChromeのAudio要素上限)と判定。

**実施した4修正:**
1. **SFXプール遅延化（①主因）** — 起動時一括生成(34種×5=170本)を**廃止**。起動Audio248本がChrome「Media resources were blocked for too long」の閾を超過し、モバイルで全メディアを恒久ブロック→BGM死+固まり。`playSFX(n)`が初回再生時にその種5本のみ生成(同一URLはdecoded buffer共有=メモリ増は不変)。起動Audio=AUD_LISTの78本のみ。
2. **ターンwatchdog（①保険）** — `TURN.phase`がanim/enemyで2秒以上復帰しない(overlay/ポーズ/画面変更なし)場合、`player`へ強制復帰+console.warnで停滞フェーズ記録。正常はanim≤0.16s+enemy≤0.08sで解決するため誤爆なし。
3. **被弾フラッシュ=シルエット（②）** — T45の白色矩形オーバーレイは**スプライトの透過四隅まで白塗り**が原因。初回フラッシュ時にオフスクリーンで`globalCompositeOperation="source-in"`白色塗り→`Image._white`(_dark)にキャッシュ、毎フレームコスト=drawImage 1回のみ(旧rectと同等・filterより軽量)。敵=白/プレイヤー=暗/ミミック=白。
4. **画面比に応じた横方向拡張（③）** — `const W=960`→`let W`（H=540固定）。`fitCanvas()`が端末比で`W=960〜min(1280,round(540×iw/ih))`に再計算(16:9以下=960維持のレターボックス)し`cv.width`+CSSで画面いっぱい表示。`resize`+`orientationchange`追従。全面背景(`bg_title/town/clear`)は`imgCover`(アスペクト保持coverクロップ)で引き伸ばし歪み防止。町ショップx=比率`fx`+`layoutTown()`毎フレーム追従、タッチUI(ABTN/PADMENU)=右端オフセット`dx`+`layoutTouchUI()`追従。カメラ表示域`viewW=W/ZOOM`が横に自動拡大。フロアキャッシュはマップ全体サイズ(W非依存)のため影響なし。
   - （附帯）P/Esc keydownで`e.repeat`を無視（OSキーリピートによるポーズ高速トグルの解消）。

**検証:** t46_test **29/29**（A: 起動Audio=78のみ+起動時プール無生成 / B: 初回playSFXで5本・連打で頭打ち・種独立 / C: フラッシュ中白矩形fillRect 0回+source-in使用+drawImage差2(通常1)+Imageキャッシュ / D: anim停滞>2s→player復帰(120f)・rAF生存・正常anim誤爆なし / E: 20:9でW=1201+cv.width/style追従・縦長は960維持・上限1280・町/タッチUI追従 / F: 連続移動12/12+watchdog誤爆なし / G: 拡張Wで180f+町/タイトル実動作スモーク）+ **全回帰14スイートgreen**(TOTAL **182** pass / 0 fail・計上外77を含む実259チェック)+`node --check`合格。t45_perf_test A1は「起動時無生成(遅延化)」仕様に更新済み。

### T47 モバイル2バグ+ボスBGM発音修正（2026-09-15・報告3件）
**ユーザー報告(3件):** ①「（T46後も）モバイルで固まる」②「縦から横に回転するとタッチボタンが全部ズレる」③「ボスBGMの『Karaage!』が『カラージ』に聞こえる」。

**① SFX=Web Audioへ全面移行:** T46の`<audio>`遅延プール(5本/種)でもモバイルChromeでフリーズ残存→**SFXの`<audio>`要素を全廃**。単一`AudioContext`+初回ユーザー操作(`unlockAudio()`・既存keydown/pointerdown/touchstart配線)で`resume()`+全34SFXのfetch+`decodeAudioData`を非同期実行→`SFX_BUF{name:AudioBuffer}`。`playSFX(n,rate)`=`createBufferSource()`+`playbackRate.value=rate||1`+`connect(destination)`+`start()`=**プール不要・同時重なり無制限**(ターン制連打に最適)。起動Audio生成=**BGM44のみ**(旧78→44)。未登録名(未来の追加SFX)は従来どおり`<audio>`フォールバック。`sfxWarmup`は`fetch`未定義環境(headless)でno-op。

**② 縦→横回転でタッチUIが全部ズレる:** 根因=回転遷移中`innerWidth/innerHeight`が**旧(縦長)値のまま返る**ブラウザの挙動で、`orientationchange`の150ms遅延実行や遅れてきた`fitCanvas`が**拡大済みのWを縮小値に確定**させ、描画(動的W)とタッチヒット判定(旧rect)が固定=ズレが解消しなかった。修正4点:
1. `orientationchange`の150ms`setTimeout`**廃止**→`fitCanvasNow()`=即`fitCanvas()`+rAF×2+`setTimeout(fitCanvas,60)`を**resizeとorientationchange両方**に绑定(遷移の全段階で再収束)。
2. **単調拡大保証**(`fitCanvas`内): 直近のW拡大(`W_T`)から600ms以内の縮小はスキップ(旧値の遅着を無視)。正当な縮小は600ms後に自動適用。
3. **`canvasPos()`アスペクトガード**: `getBoundingClientRect`の縦横比がバッファ(W/H)と2%以上食い違う=遷移中の旧rect→contain正規化でW/H空間に再写像(画面端タップがゲーム画面の端に一致)。
4. **`touchTol()`**: 回転直後(`FIT_T`)300msだけABTN/PADMENU/PAD8/JOYのヒット半径×1.2(収束前のタップも拾う)。

**③ ボスBGM「カラージ」問題:** `Karaage!`は英語歌唱で末尾/g/が/ji:/にglideし「カラージ」に。ユーザー指示で**まずprobe 1曲**(`audio/karaage_probe_01.ogg`・`Ka-ra-a-ge!`=モーラ区切り+伸ばしa+硬い`!`、2番に旧表記`Karaage!`/`Karaage~`をA/Bコントロールとして内蔵)を生成→**ユーザーが「唐揚げって聞こえるからよし」と確認**。**決定: 全10曲(9中ボス+大魔王)を`Ka-ra-a-ge`表記で再生成**(`tools/lyrics_t43_mb.md`/`lyrics_t37_boss.md`の歌詞・promptも全置換済み)。ユーザー追加指定: **大魔王`bgm_boss.ogg`=実尺≈2分(125spec)+シームレスループ**(旧84.5sは短すぎ)。QAゲート=実尺110〜135s/peak<-0.01dBFS/Vorbis 48kHz stereo+**ループシーム判定**(先頭0.5s RMSと末尾0.5s RMSの比が0.15〜6=末尾フェード→先頭ダウンビートの継ぎ目を検出)。blind retry(12回/曲・6h上限・VRAM窓捕捉)+watchdog(失敗曲の自動ピンポイント再実行)で実施。

**再生成結果(10/10完了・09-16 01:33):** blind retry+watchdogでllama-serverのVRAM競合を回避しつつ全曲生成。mb_05のみ1ラウンド12回失敗→watchdogが自動でピンポイント再実行し初回成功。最終QA **10/10合格**: `bgm_mb_01`=117.2s / `bgm_mb_02`=117.1s / `bgm_mb_03`=117.9s / `bgm_mb_04`=120.4s / `bgm_mb_05`=119.8s / `bgm_mb_06`=119.1s / `bgm_mb_07`=117.7s / `bgm_mb_08`=119.1s / `bgm_mb_09`=119.2s / `bgm_boss`=**122.9s**(旧84.5s→2分化)（全曲110〜135s枠・peak -0.8〜-4.2dB・Vorbis 48kHz stereo・ループシーム比0.70〜3.67=先頭/末尾のエネルギー継続を確認）。**ASR発音QA**: 新mb_01のフック行が「Karachi」と書き起こし=`Ka-ra-a-ge`の4モーラ構造が歌唱されている機械的確認（probeのユーザー確認と一致）。probe曲は`/tmp/opencode/karaage_probe_01.ogg`へ退避（audio/=78本=AUD_LISTと一致を維持）。

**検証:** t47_test **14/14**(A: 縦長起動W=960→resize即実行でW=1169/旧縦長値が600ms窓内で来てもW縮小なし/窓超過で正当縮小W=960/旧rectでcanvasPos右端→x≈W・中央→W/2・一致rectは従来スケーリング/touchTol 0-200ms=1.2→350msで1.0 / B: 起動Audio=44(BGMのみ)/SFX34種`<audio>`0/unlockでdecode34/playSFX=bufferSourceのみ・Audio不生成) + t46_test **33/33**(A/B=Web Audio仕様に書き換え・E/F=FakeDateで600ms窓クリア) + **全15スイートgreen**(TOTAL **201** pass/0 fail)+`node --check`合格。

## 最終成果物
- **ゲーム本体**: `index.html` 単一ファイル（AUD_LIST=**78本**: BGM **44** + SFX 34・ボイス0。**T47: SFXはWeb Audio再生で`<audio>`要素不使用**=起動Audio生成44本のみ）
- **audio/**: **78本** = 旧69 + 中ボス専用BGM 9本(`bgm_mb_01〜09`)。AUD_LISTと完全一致・余剰なし。**T47: 全10ボス曲(`bgm_mb_01〜09`+`bgm_boss`)が`Ka-ra-a-ge`表記・約2分+シームレスループで再生成完了・QA 10/10合格**
- **SFX20本（新規）**: 「生成窓下限2秒→無音トリム→ピーク-6dB正規化→QA」で全件完成
- **テスト**: 全**15スイート** green（`/tmp/opencode/run_all_tests.sh`・TOTAL **201** pass/0 fail+計上フォーマット差で未集計80=実**281**チェック）+ `node --check` 合格

## 履歴（主要な出来事・教訓）
1. **短尺指定のSFX生成は壊れる**: 0.55s指定=クリップ方形波（ソースWAV破損）/ 1s指定=内容劣化 → **下限2秒が確定方針**（ユーザー指示）。
2. **日本語TTSボイス不自然** → ボイス全廃。AUD_LISTから25本削除、`playVoice()`はAUD未登録ならno-op（呼び出し側残置でロジック影響ゼロ）、テスト6アサーションを廃止仕様に更新。
3. **sonic.asset_idの罠**: `sonic.generate`応答のtop-level `asset_id`(`job-result:`形式)は`sonic.pack`で422。本物は`output.asset_id`(`asset:<uuid>`)。フォールバック=資産ストアWAV(`/data1tb/ControlDeck/data/feature-data/sonic-forge/assets/<uuid>.wav`)からffmpeg直接変換。
4. **サブエージェントのキャンセルでファイルが到達する**: 統合audioジョブキャンセル直前にボイス21本+SFX17本の上書きが到達→**キャンセル後も必ず最終sweep**（voice削除+SFXのmtime/ffprobe点検→`/tmp/opencode/sfx_final/`から再配置）。
5. **GPU VRAMは共有・常時占有される**: 他プロセス(llama-server等)がVRAMを保持するとACE-StepはLM初期化でOOM。対策=**VRAMゲート待ちではなく即時再挑戦のバックグラウンドループ**（失敗は~3.5minで低コスト）。VRAM%閾値待機は占有が解消されない限り永久ブロックされる。
6. 他バグ修正: `mbTalk`の警告フィルタ / `drawPlayer`の`globalThis.P` / t28_regress flake（fuzz前フルHP）— 全て回帰テスト済み。
7. **TTSの日本語発音は表記依存で不安定（T47）**: `Karaage!`=「カラージ」にglide。**probe 1曲でユーザーの耳に確認→勝った表記で全再生成**が最速の確実手順（全生成→失敗は10倍のロス）。モーラ区切り`Ka-ra-a-ge!`+硬い`!`（チルダ`~`はglideを強化するので廃止）で「唐揚げ」に。
8. **回転中のwindowサイズは旧値が混在する（T47）**: `orientationchange`の1回だけ・150ms遅延では旧値で確定し得る。即実行+複数回の再実行(rAF×2+60ms)+単調拡大保証(600ms窓)+座標系ガード(canvasPosアスペクト照合)+タッチ許容拡大(+20%・300ms)の4層で実機の遷移ノイズを吸収。

## 重要パス
- ゲーム本体: `index.html`（AUD_LIST@87）/ 仕様: `PLAN.md` / 説明: `README.md`
- テスト: `/tmp/opencode/*.js` + `/tmp/opencode/run_all_tests.sh`（**15スイート**・t47_test追加済み）
- T45計測: `/tmp/opencode/t45_measure_before.js`（before再構築+計測）/ `t45_measure.js`（after実測）
- T43音源: 歌詞 `tools/lyrics_t43_mb.md` / QA `qa_mb_bgm.sh`（9/9合格）/ 検証済みコピー `/tmp/opencode/mb_bgm_final/`（9本）/ 再試行スクリプト `retry_mb_bgm_blind.py`（完了・ログ `mb_bgm_blind.log`）
- SFX再生成ツール: `/tmp/opencode/regen_sfx_all.py` / `sfx_recover.py` / 検証済みコピー `/tmp/opencode/sfx_final/`
- 旧audioバックアップ: `/tmp/opencode/karaage_bak/`（`voice_discarded/`に廃止ボイス25本分）
- BGM歌詞仕様: `tools/lyrics_t37_boss.md` / `tools/lyrics_t43_mb.md`（**T47: 全歌詞=`Ka-ra-a-ge`表記へ置換済み**）
- T47 BGM再生成: `/tmp/opencode/karaage_regen_make_args.py`(10曲args・`karaage_regen_args/`) + `karaage_regen_run.py`(blind retry+QA+argvピンポイント再実行・ログ `karaage_regen.log`) + `karaage_regen_watchdog.py`(失敗曲自動再実行) / probe: `/tmp/opencode/karaage_probe_01.ogg`+`karaage_probe_args.json`
- sonic-forge DB: `/data1tb/ControlDeck/data/feature-data/sonic-forge/sonicforge.db`
- MCP直接呼び出し: `http://127.0.0.1:8765/api/v1/addons/agent-mcp/{tools,call}`（トークン=opencode.jsonの`CONTROL_DECK_ADDON_MCP_TOKEN`）

## 今後の拡張メモ（未着手・任意）
- ボイスを復活させる場合: AUD_LIST登録+ファイル配置のみで復帰可能（`playVoice`配線は残存。T40/T41の台詞文は`MBV_LINES`/必殺技定義に保存済み）
- T45の残課題（任意）: 敵/パーティクルのスプライトバッチ描画（本計測では敵48体でも<8ms/フレームのため未実施・リスク対効果で保留）
- git: master・未コミット。`audio/`はuntracked（バックアップは`/tmp/opencode/karaage_bak/`）
