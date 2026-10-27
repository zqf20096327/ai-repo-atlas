# thetobysiu/Deepstory

⭐ 103 · Python · 推送 2025-11-23 · [GitHub](https://github.com/thetobysiu/Deepstory) · [官网](https://blog.thetobysiu.com) · 个人维护

**把文本变成角色说话视频的应用（GPT-2 生成+TTS+动画）**

结合 GPT-2 文本生成、DC-TTS 语音合成、语音驱动动画与 First Order Motion Model 图像动画的 Flask Web 应用：输入文本或续写故事，按句子映射说话人，合成语音并生成角色开口说话的视频。支持 transformers 与 pytorch-dctts 模型，提供网页界面与后端。需 nvidia GPU（≥4GB VRAM）、ffmpeg 与 spacy 英文模型；项目自称 5 年前的技术，作者称将更新为更现代模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GPT-2 续写故事并支持交互式分批生成
- 句子到说话人的映射系统
- 文本→语音→角色动画视频的完整流水线
- Flask Web 界面与 Colab 演示版本

## 适用场景

- 把小说或同人文本生成角色开口讲述的视频
- 基于原书文本续写故事并配音动画
- 在网页界面中交互式创作多说话人故事

## 场景标签

`语音合成` `视频生成` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L2: Deepstory is an artwork that incorporates Natural Language Generation(NLG) w/GPT-2, Text-to-Speech(TTS) w/Deep Convo
> L4: To put it simply, it turns a text/generated text into a video where the character is animated to speak your story us

## 星数曲线

```mermaid
xychart-beta
    title "thetobysiu/Deepstory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 102 --> 104
    line [103, 103]
```

2026-10-18 103 → 2026-10-27 103（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `73a3d05a6aa8` · [字段定义](../../DATASET.md)*
