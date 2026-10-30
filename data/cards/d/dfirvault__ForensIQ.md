# dfirvault/ForensIQ

⭐ 18 · Python · MIT · 推送 2026-01-17 · [GitHub](https://github.com/dfirvault/ForensIQ) · [官网](https://dfirvault.com) · 个人维护

**数字取证应急响应工具：用本地 Ollama LLM 分析日志生成发现**

面向事件响应人员与 DFIR 分析师的取证自动化工具，基于 Streamlit Web UI 运行：上传单个/多个日志文件或指向本地文件夹后自动识别并排队分析，支持多格式文件与系统日志（含 Windows 事件日志解析依赖 python-evtx），输出 JSON 结构化报告、CSV 摘要与审计日志。AI 机制为通过本地或远程 Ollama 服务调用 LLM（README 提供 qwen-long Modelfile 配置流程），配合 LangChain、ChromaDB、sentence-transformers 等依赖。限制：仅支持 Windows，需 Python 3.11+ 并自行搭建 Ollama 服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用本地/远程 Ollama LLM 对日志生成自动化分析发现
- 支持单文件、多文件与文件夹批量日志排队分析
- 输出 JSON 报告、CSV 摘要与可复现审计日志
- 提供 qwen-long Modelfile 配置与启动批处理脚本

## 适用场景

- 应急响应时快速从系统日志生成取证发现
- DFIR 分析师批量处理日志并导出结构化报告
- 事件调查中留存可审计的分析日志

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: **ForensIQ** is a fast, accurate, and modern digital forensics automation tool designed for incident responders, DFI
> L29: pip install --upgrade langchain langchain-community langchain-ollama langchain-huggingface sentence-transformers ch
> L78: - **JSON Reports:** Structured forensic data.

## 星数曲线

```mermaid
xychart-beta
    title "dfirvault/ForensIQ 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `ed9b6a79a93d` · [字段定义](../../DATASET.md)*
