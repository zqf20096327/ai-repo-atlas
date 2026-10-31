# r-uben/deepseek-ocr-cli

⭐ 14 · Python · MIT · 推送 2026-06-06 · [GitHub](https://github.com/r-uben/deepseek-ocr-cli) · 个人维护

**本地 OCR 命令行工具：用 DeepSeek 视觉模型识别文档与图片**

Python 编写的命令行 OCR 工具，调用 DeepSeek 视觉模型将 PDF 与多种图片（JPG/PNG/WEBP/GIF/BMP/TIFF）转换为 Markdown，支持 Ollama（本地）与 vLLM（GPU 服务器、OpenAI 兼容 API）两种后端，无云端依赖。输出遵循 ocr-output-contract：按输入相对路径分目录存放，生成每文档 metadata.json 与根索引；支持目录树批量处理、增量续跑（输入/模型/后端/提示词变更时自动重跑）、截断检测、指数退避重试与 --dry-run 预览。也提供 Python API 编程调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ollama 本地与 vLLM 服务器双后端，零云端依赖
- 目录树批量 OCR 与增量续跑（按输入/模型/后端/提示词指纹判断）
- 遵循 ocr-output-contract 的规范化 Markdown 与双 metadata.json 输出
- 截断页标记 partial/failed，不静默记为完成

## 适用场景

- 把本地 PDF 和图片批量转成 Markdown 文本
- 在无云端依赖的环境用 Ollama 跑 OCR
- 批量文档处理中断后增量续跑，只补未完成的文档

## 场景标签

`OCR` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L7: Command-line tool for OCR using DeepSeek vision models. Supports Ollama (local) and vLLM (GPU server) backends.
> L11: - **Multi-backend**: Ollama (local, free) and vLLM (OpenAI-compatible API)
> L13: - Canonical output via the shared `ocr-output-contract`: one `<root>/<rel/dir>/<stem>/<stem>.md` per document under

## 星数曲线

```mermaid
xychart-beta
    title "r-uben/deepseek-ocr-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c70968f0d377` · [字段定义](../../DATASET.md)*
