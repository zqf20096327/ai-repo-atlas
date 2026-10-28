# vulture-s/arkiv

⭐ 78 · Python · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/vulture-s/arkiv) · [官网](https://vulture-s.github.io/arkiv/) · 个人维护 · 中文 README

**给独立 DIT 与小团队的本地优先媒体资产管理器，AI 元数据与语义搜索**

面向独立 DIT 和小型摄制团队、本地自托管的素材管理层：摄入素材后生成 AI 元数据（Whisper large-v3-turbo 转写带四层防幻觉保护、qwen2.5vl 视觉描述、自动标签），提供中/英/日语义搜索与库内对话（RAG）；同时覆盖现场 DIT 流程——多目标并行卸载卡、逐文件哈希校验、ASC MHL v2 清单、摄影机报告 CSV。通过 DaVinci Resolve 插件、EDL/FCPXML 导出、REST API 与只读 MCP 接入剪辑流程。读取 Sony XAVC sidecar、EXIF 等专业相机元数据，360 素材（Insta360/GoPro Max）先重投影再索引。许可为 PolyForm Perimeter（source-available，任何用途含商用免费）。macOS/Windows 提供安装包，仍需 FFmpeg 与 Ollama。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Whisper large-v3-turbo 转写 + 四层防幻觉保护（VAD→no_speech→空/重复过滤→LLM 纠正）
- 中/英/日三语语义搜索与带会话记忆的库内 Chat（RAG）
- 多目标并行卸载 + 哈希校验 + ASC MHL v2 清单，卸载过程不删源卡
- DaVinci Resolve 插件：库内搜索、带片段颜色导入、打帧标记；另有 EDL/FCPXML/CSV 导出与 REST API/只读 MCP

## 适用场景

- 海量素材里用自然语言（中/英/日）找到想要的镜头
- 现场 DIT 做卡备份、校验与 MHL 哈希清单
- 把 AI 标签、评分和相机元数据带进 DaVinci Resolve 剪辑流程

## 场景标签

`语义搜索` `语音识别` · 领域:知识与检索

## 证据(README 行号)

> L14: arkiv sits between your media drive and DaVinci Resolve: it ingests your footage, attaches AI-generated metadata (t
> L16: Designed for solo DITs and small crews who own their data: local-first, self-hosted, source-available (PolyForm Per
> L61: - Card offload: parallel multi-destination copy + per-file hash verify + resumable, and it **never deletes the sour

## 星数曲线

```mermaid
xychart-beta
    title "vulture-s/arkiv 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-28 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `c11ce1909f3a` · [字段定义](../../DATASET.md)*
