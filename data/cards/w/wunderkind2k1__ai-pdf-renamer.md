# wunderkind2k1/ai-pdf-renamer

⭐ 22 · Go · MIT · 推送 2026-02-16 · [GitHub](https://github.com/wunderkind2k1/ai-pdf-renamer) · 个人维护

**离线批量 PDF 智能重命名工具：用本地 Ollama 模型按内容生成文件名**

基于 Go 的命令行工具，通过本地运行的 Ollama 模型分析 PDF 内容并生成描述性文件名。默认视觉模式用 qwen2.5vl:7b 将页面转为图像分析（最多 3 页，经 Ghostscript 转换），失败或指定 -novision 时回退到 OCR 模式（ocrmypdf 提取文本后由 gemma3:1b 或 llama3.3 处理）。支持 glob 批量匹配、自定义提示词、输出目录与文件名长度限制，全程无需联网或外部 API。运行依赖 ocrmypdf、curl、jq、Ghostscript 及本地 Ollama 服务（端口 11434），可从 release 下载或用 Go 1.21+ 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 默认视觉模式（qwen2.5vl:7b）+ OCR 回退（ocrmypdf + gemma3:1b/llama3.3）双处理模式
- 完全离线运行，无需互联网或外部 API
- 支持 glob 批量处理、自定义提示词、自动重命名与文件名长度限制（默认 64 字符）
- 跨平台支持 Linux/macOS/Windows，提供 release 下载与 Go 源码构建两种获取方式

## 适用场景

- 批量重命名下载的论文、发票、合同等 PDF 为有意义的文件名
- 整理杂乱的 Downloads 文件夹，让文件可检索
- 在无网络或注重隐私的环境下自动整理 PDF 文档库

## 场景标签

 · 领域:文件管理/自动化工具

## 证据(README 行号)

> L5: **AI PDF Renamer** is a powerful tool that automatically renames PDF files based on their content using AI. By lever
> L27: - Generates concise, descriptive filenames using Ollama's AI models
> L177: Vision mode uses the qwen2.5vl:7b vision-language model to analyze PDF pages directly as images. This mode:

## 星数曲线

```mermaid
xychart-beta
    title "wunderkind2k1/ai-pdf-renamer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-30 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e0600e83ae0b` · [字段定义](../../DATASET.md)*
