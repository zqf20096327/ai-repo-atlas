# DozaVisuals/doza-assist

⭐ 56 · Python · MIT · 推送 2026-09-22 · [GitHub](https://github.com/DozaVisuals/doza-assist) · [官网](https://doza.ai) · 组织维护

**本地优先的 Mac AI 剪辑助手：从采访素材生成粗剪**

面向纪录片与采访类视频剪辑师的本地 AI 助手：拖入视频后在本地转录（Apple Silicon 上用 NVIDIA Parakeet TDT，多语言用 WhisperX large-v3），基于本地 Gemma/Ollama 模型做故事结构分析、对话式选片与故事搭建，并按用户已剪作品学习个人剪辑风格（多档案、可导出 JSON）。粗剪可一键导出为 FCPXML/FCP7 XML/EDL 供 Final Cut Pro、Premiere Pro、DaVinci Resolve 使用。MIT 开源，素材不上传；可自选接入 Anthropic/OpenAI API key 走云端分析。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地转录：Parakeet TDT（Apple Silicon/MLX）+ WhisperX large-v3（99+ 语言），词级时间戳
- 从已剪作品学习个人剪辑风格的 Editorial DNA 多档案系统，含演化追踪与导入导出
- Story Builder 从素材自动选段组装叙事弧线，附每段编辑理由
- 一键导出 FCPXML / Final Cut Pro 7 XML / CMX 3600 EDL 至三大 NLE

## 适用场景

- 把几小时的采访素材先过一遍 AI，找出故事节拍和金句
- 按我的剪辑风格生成粗剪时间线再导入 NLE 精修
- 客户不用注册就能通过公开链接听素材、做高亮标注

## 场景标签

`AI 助手` `语音识别` `图像视频处理` · 领域:对话与助手

## 证据(README 行号)

> L15: Drop in an interview. Get back a rough cut shaped by your editorial voice, ready for **Final Cut Pro**, **Premiere 
> L76: - Uses NVIDIA Parakeet TDT (via MLX) on Apple Silicon for fast English transcription, WhisperX large-v3 for 99+ lan
> L99: **AI Analysis** (powered by Ollama — free, local)

## 星数曲线

```mermaid
xychart-beta
    title "DozaVisuals/doza-assist 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 54 --> 57
    line [55, 56, 56]
```

2026-10-18 55 → 2026-10-31 56（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `06201ff9f865` · [字段定义](../../DATASET.md)*
