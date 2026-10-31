# 1596941391qq/anything-to-md

⭐ 19 · Python · MIT · 推送 2026-05-09 · [GitHub](https://github.com/1596941391qq/anything-to-md) · 个人维护 · 中文 README

**把 PDF/Office/音视频等多格式文件转换为 LLM 可用的 Markdown**

统一文档转换层，覆盖 PDF、Office、电子书、图片 OCR、音视频、YouTube 等输入，输出结构化 Markdown。PDF 走 MinerU→MarkItDown→pypdf 三级降级链；视频经 PROBE/DECIDE/EXTRACT/FUSE 四阶段路由，按内嵌字幕/旁白/纯人声等类型选择提取策略，音频转写用 faster-whisper，画面用场景检测加 RapidOCR。以 CLI、MCP Server（4 个工具）、Claude Code Skill 三种方式提供，面向需要向 LLM/Agent 供给文档内容的开发者。MinerU 首次运行需下载约 2GB 模型，视频功能依赖外部 ffmpeg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PDF 三级引擎降级链（MinerU/MarkItDown/pypdf），支持扫描件与中文图文混排
- 视频四阶段智能路由：字幕/音频转写/画面 OCR 按内容类型选路并时间轴融合
- CLI、MCP Server（4 个工具）、Skill 三种使用方式共用一套引擎
- 场景检测+感知哈希将 1 小时视频的关键帧压缩到 50-200 帧

## 适用场景

- 把 PDF 报告、扫描件批量转成 Markdown 喂给 LLM 或知识库
- 在 Claude Code/Cursor 等 MCP 客户端中直接调用文件转换工具
- 把教程视频、讲座录屏转写为带画面文字的文本文档

## 场景标签

`文档解析` `语音识别` `OCR` · 领域:知识与检索

## 证据(README 行号)

> L15: Anything-to-MD 是一个统一转换层：**原始多模态输入 → 结构化、可索引、可总结的 Markdown**。
> L22: |MCP Server|Claude Code / Cursor / AionUI 等 MCP 客户端直接调用|
> L153: ## MCP Server

## 星数曲线

```mermaid
xychart-beta
    title "1596941391qq/anything-to-md 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4ea15d8a936a` · [字段定义](../../DATASET.md)*
