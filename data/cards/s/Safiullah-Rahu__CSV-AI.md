# Safiullah-Rahu/CSV-AI

⭐ 341 · Python · MIT · 推送 2026-05-20 · [GitHub](https://github.com/Safiullah-Rahu/CSV-AI) · [官网](https://csv-ai.streamlit.app/) · 个人维护

**与 CSV 文件对话、总结与分析的 Streamlit AI 应用**

基于 Streamlit 的 CSV 分析应用 v2 重写版：提供对话问答（schema 与样本感知、流式输出）、单次调用总结、以及确定性 pandas 统计与 LLM 分析并排展示（含图表、缺失值、相关性）。LLM 层为 provider 无关设计，支持 OpenAI、Anthropic 或本地 Ollama，通过环境变量/.env/Streamlit secrets 配置。可部署到 Streamlit Community Cloud、本地运行或 Docker Compose；服务层为纯 Python，预留未来 FastAPI API 拆分。采用 MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多提供商支持：OpenAI、Anthropic、本地 Ollama
- 对话/总结/分析三种模式，pandas 确定性统计与 LLM 叙述并列
- 模块化 app/ 包结构，服务层无 Streamlit 依赖
- 支持 Streamlit Cloud、本地、Docker Compose 部署

## 适用场景

- 上传 CSV 后通过对话提问获取数据洞察
- 生成 CSV 的结构化总结概览
- 查看确定性统计与 AI 分析并排的数据报告

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Modernized AI-powered CSV analysis** — chat with, summarize, and analyze your CSV files using OpenAI, Anthropic, o
> L9: - **💬 Chat** — schema- and sample-aware Q&A with token-streaming.
> L12: - **🔌 Multi-provider** — OpenAI, Anthropic Claude, or local Ollama.

## 星数曲线

```mermaid
xychart-beta
    title "Safiullah-Rahu/CSV-AI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 339 --> 342
    line [340, 341, 341]
```

2026-10-18 340 → 2026-10-29 341（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `d47345006fa5` · [字段定义](../../DATASET.md)*
