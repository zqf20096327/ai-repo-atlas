# fundwotsai2001/MIDI-SAG

⭐ 33 · Python · Apache-2.0 · 推送 2026-05-30 · [GitHub](https://github.com/fundwotsai2001/MIDI-SAG) · 组织维护 · 中文 README

**论文官方代码：由人声旋律生成全曲伴奏轨的生成管线**

MIDI-SAG 论文的官方代码：以人声旋律 MIDI 为条件生成伴奏轨（钢琴、贝斯、鼓、合成器等），串联节拍检测、GAME 人声转 MIDI、AccoMontage2 和弦编配与 MuseControlLite（基于 Stable Audio Open 1.0）。提供三种模式：Detected（仅人声音频）、Ground-truth（人声音频+现成 MIDI）、ComposeFlow（从歌词端到端生成整首歌：CSL-L2M 歌词转旋律、SoulX-Singer 歌声合成，作者声明该部分为自行实现的开源版本）。通过 shell 脚本配置参数运行，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 以人声旋律 MIDI 为条件的全曲伴奏生成，支持结构感知（intro/verse/chorus 等分段）
- 和弦风格、每小节和弦数、调性等参数可控
- ComposeFlow 模式从歌词文本端到端生成完整歌曲（旋律、歌声、伴奏）

## 适用场景

- 给我的人声清唱自动编配和弦并生成伴奏
- 从歌词文本生成含歌声与伴奏的完整歌曲小样
- 按指定和弦风格（流行/暗色等）生成钢琴贝斯鼓合成器伴奏

## 场景标签

 · 领域:音乐生成/音频 AI

## 证据(README 行号)

> L10: MIDI-SAG is a compositional pipeline that generates backing tracks (piano, bass, drums, synth, etc.) conditioned on
> L16: - **ComposeFlow** -- input is a lyrics text file. End-to-end pipeline from text to full song: lyrics-to-melody (CSL

## 星数曲线

```mermaid
xychart-beta
    title "fundwotsai2001/MIDI-SAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-29 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a5b8f4a1bb12` · [字段定义](../../DATASET.md)*
