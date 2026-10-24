# HRNPH/AIwaifu

⭐ 519 · Python · GPL-2.0 · 推送 2026-07-07 · [GitHub](https://github.com/HRNPH/AIwaifu) · 个人维护

**自托管可定制的 AI 虚拟伴侣（waifu）平台，可对话/直播**

受 neuro-sama 启发的开源 AI waifu 项目：为用户提供可自行微调、定制人格与数据集的虚拟伴侣基础平台，基于开源 AI 模型自托管部署。技术栈为 Pygmalion1.3b 语言模型生成对话，经 Facebook/nllb-600m 翻译为日语后由 VITS 模型做语音合成，配合 VTube Studio 桌面程序呈现虚拟形象并支持直播。架构分为推理 HTTP 服务器与客户端两部分。需自行编译 monotonic_align 模块，作者在 README 中标注部分功能可能不稳定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Pygmalion1.3b 对话模型 + nllb-600m 翻译 + VITS 语音合成
- 支持自定义人格、数据集微调与形象修改
- 推理服务器与客户端分离架构，支持外置服务器部署
- 通过 VTube Studio 与 VTS 桌面音频插件联动，支持直播

## 适用场景

- 我想拥有一个可自定义人格的自托管 AI 虚拟伴侣
- VTuber 直播中运行 AI 角色进行对话互动
- 在自有数据集上微调并打造专属 waifu 角色

## 场景标签

`聊天机器人` `微调` · 领域:对话与助手

## 证据(README 行号)

> L11: aiwaifu is an Open sourced finetunable customizable simpable AI waifu inspired by neuro-sama
> L89: > - The Language model we're using is Pygmalion1.3b

## 星数曲线

```mermaid
xychart-beta
    title "HRNPH/AIwaifu 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 517 --> 520
    line [518, 519, 519]
```

2026-10-18 518 → 2026-10-24 519（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `54620409afd0` · [字段定义](../../DATASET.md)*
