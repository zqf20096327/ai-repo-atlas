# ringger/transcribe-critic

⭐ 26 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/ringger/transcribe-critic) · 个人维护

**多来源转写合并管线：用 LLM 裁决多个 ASR 结果生成更准转写**

从视频/播客 URL 出发的自动转写管线：下载媒体后用多个 ASR 模型（Whisper、Parakeet、Qwen3-ASR）转写，并纳入 YouTube 字幕与人工编辑的外部转写作为独立“证人”，经 wdiff 对齐后由 LLM 以匿名标签逐处裁决差异，合并为单一“批判文本”。借鉴版本校勘学方法（作者有 OCR 领域先前工作）。内置 pyannote 说话人分离、结构化摘要、幻灯片提取、来源存活分析等阶段。默认用 Ollama 本地运行 LLM，无需 API key；各阶段可独立配置不同 LLM 后端（含 Claude API）。限制：不产生异文校勘记或谱系图，目标是单一最佳文本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 ASR 模型 + 字幕 + 外部转写作为独立证人，LLM 匿名裁决合并
- 默认 Ollama 本地 LLM，无需 API key；各阶段可独立指定后端（含 Claude）
- pyannote 说话人分离默认开启，LLM 借视频元数据校正说话人姓名拼写
- Make 式 DAG 管线与检查点续跑，来源存活分析量化各来源贡献

## 适用场景

- 我为长播客生成带说话人标注的高准确度文字稿
- 我有YouTube 讲座和官方外部转写，想交叉合并出更准的版本
- 我在本地用 Ollama 免费跑完整转写+摘要管线

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: Automated pipeline for producing accurate speech transcripts from video URLs. Downloads media, transcribes with mult
> L9: WhisperX improves a single Whisper run with voice-activity-detection (VAD) chunking, word-level timestamps, and spea

## 星数曲线

```mermaid
xychart-beta
    title "ringger/transcribe-critic 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-30 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d5d64d1ec02b` · [字段定义](../../DATASET.md)*
