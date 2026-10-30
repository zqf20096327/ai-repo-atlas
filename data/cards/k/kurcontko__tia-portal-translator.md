# kurcontko/tia-portal-translator

⭐ 16 · Python · MIT · 推送 2026-03-04 · [GitHub](https://github.com/kurcontko/tia-portal-translator) · 个人维护

**面向 TIA Portal 工程师的 Excel 文本批量翻译工具**

读取西门子 TIA Portal 导出的 Excel 文本文件，调用免费 Google Translate、OpenAI/Openrouter API 或任意 OpenAI 兼容服务器（含 Ollama、vLLM、MLX-LM 本地后端）及 DeepL 进行批量翻译，输出回 Excel。支持并发请求（默认 10）、分块处理、指数退避重试、混合缓存（TTL 1 周）、行长度保持与逐项错误记录。以 Python CLI 形式提供，需 Python 3.9+，旧脚本保留在 deprecated/ 目录。

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

- 支持 5 种翻译后端：google-free（无需 API key）、OpenAI/Openrouter、Google、DeepL 及任意 OpenAI 兼容本地服务器
- 异步并发与分块处理，速率限制 10 req/s，Tenacity 指数退避重试
- 混合缓存（默认 TTL 168 小时）与逐项错误写入输出文件
- 可选保持译文行长度与源文本一致（含容差系数）

## 适用场景

- 把 TIA Portal 项目文本从一种语言批量翻译为另一种语言
- 在无 API key 时用 google-free 免费通道完成翻译
- 用本地 LLM（Ollama/vLLM/MLX）离线翻译工程文本

## 场景标签

 · 领域:工业自动化/翻译工具

## 证据(README 行号)

> L2: Modern, async-powered tool for translating TIA Portal texts exported to Excel using
> L3: free Google Cloud Translate, OpenAI/Openrouter API or OpenAI-compatible server, and DeepL APIs. A legacy script and 
> L112: ## Local LLM Backends (Ollama, MLX-LM, vLLM)
> L114: This project can use any OpenAI-compatible server via the `openai` service.

## 星数曲线

```mermaid
xychart-beta
    title "kurcontko/tia-portal-translator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d1f6cf940979` · [字段定义](../../DATASET.md)*
