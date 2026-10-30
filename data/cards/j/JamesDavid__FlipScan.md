# JamesDavid/FlipScan

⭐ 16 · Python · NOASSERTION · 推送 2026-08-01 · [GitHub](https://github.com/JamesDavid/FlipScan) · 个人维护

**把翻书视频/照片/PDF 转成校对过的电子书与有声书的本地工具**

面向个人用户的图书数字化应用：从翻书视频抽帧、聚类选页，用视觉 LLM（本地 Ollama、Anthropic API 或混合）逐页转录，重建页序与插图，逐章校对后生成 EPUB/PDF/Markdown，并可 narrate 成带章节的 .m4b 有声书（本地语音模型与声音克隆）。提供手机可访问的本地 Web GUI，含重拍清单、目录编辑、图表裁剪等管理界面。除可选 Anthropic 后端外数据不出本机。Docker Compose 或 pip 安装，基础安装需 ffmpeg，LaTeX PDF 输出需额外安装 pandoc/XeLaTeX。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 翻书视频抽帧聚类选页，视觉 LLM 逐页转录
- 逐章非破坏式校对层，歧义项人工确认后生效
- 生成本地声音克隆旁白的章节化 .m4b 有声书
- 弱页生成重拍清单而非静默丢弃；任务持久化后台执行

## 适用场景

- 把手头的纸质书拍成视频转成 EPUB 自读
- 整理已有扫描 PDF 或 EPUB 并重新排版到电子墨水设备
- 把校对完的书 narrate 成有声书在通勤时听

## 场景标签

`OCR` `文档解析` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L3: Turn a phone video of flipping through a book — or a stack of page photos, or a PDF — into a clean, proofread EPUB. 
> L5: Everything runs through a local web GUI you can drive from your phone on the same network. Nothing about the digitiz

## 星数曲线

```mermaid
xychart-beta
    title "JamesDavid/FlipScan 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6ce27408d997` · [字段定义](../../DATASET.md)*
