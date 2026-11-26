# tajirhas9/pdf2epub-ai

⭐ 3 · Python · NOASSERTION · 推送 2026-11-22 · [GitHub](https://github.com/tajirhas9/pdf2epub-ai) · 个人维护

**把数字版/扫描版 PDF 转成可重排 EPUB3 的转换器**

将出生数字或扫描版 PDF 转换为可重排 EPUB3 电子书的工具：先用确定性视觉工具（PaddleOCR/Apple Vision）做版面检测、OCR、跨页拼图与页眉页脚清理，可选接入任意 OpenAI 兼容视觉模型逐页比对原图并返回编辑操作修正 OCR 错误。提供浏览器应用与 CLI 两种使用方式，支持逐页保存进度断点续转，跨 Linux/macOS/Windows 运行，也可用 Docker。许可证为 PolyForm Noncommercial 1.0.0，仅限非商业使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可选 AI 页面审查：OpenAI 兼容视觉模型比对原图返回编辑操作，不直接写标记
- 硬件感知 OCR：NVIDIA GPU CUDA 版 PaddleOCR 或 Mac Neural Engine 上的 Apple Vision
- 逐页保存进度，支持暂停/断电/AI 服务中断后续转
- 混合文字（含 RTL）按行选 OCR 模型并嵌入字体

## 适用场景

- 把扫描版旧书转换成手机/电纸书上可重排阅读的 EPUB
- 转换含图片环绕、跨页插图或混合文字的复杂排版 PDF
- 对干净数字 PDF 用 --no-llm 快速转换

## 场景标签

`OCR` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L4:  Fast vision tools do the heavy lifting; an optional vision LLM checks every page against the original.
> L23: tablet or e-reader. Fast deterministic vision tools do most of the work; an optional vision LLM (any
> L43: - **Optional AI page review** — any OpenAI-compatible vision model (llama.cpp, LM Studio, Ollama,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `ab02d2e8bcf3` · [字段定义](../../DATASET.md)*
