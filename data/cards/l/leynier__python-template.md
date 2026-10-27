# leynier/python-template

⭐ 37 · Jinja · MIT · 推送 2026-10-01 · [GitHub](https://github.com/leynier/python-template) · [官网](https://python-template.leynier.dev) · 个人维护

**Copier 模板：按层组合生成 Python 与 AI 生产级项目**

基于 Copier 的项目模板生成器：通过 12 个可编辑预设或逐层选择，组合工作负载（库/CLI/API/MCP/agent/RAG/训练/推理）、框架（FastAPI、FastMCP、LangGraph、LlamaIndex 等）、模型提供商、数据层、训练与部署目标，生成带 src/ 布局、测试、CI、安全策略的完整工程。组件目录含 126 个条目并标注支持层级（stable/platform/experimental）。生成后可用 uvx copier update 跟随模板更新。也提供无 AI 依赖的小型方案。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 126 个组件目录，按工作负载/框架/模型提供商等分层组合
- 12 个预设（如 langgraph-anthropic-api、litellm-gateway、hf-finetuning）
- 14 个部署目标（Docker、Fly.io、AWS ECS 等），云端目标可生成 Pulumi/Terraform
- 生成项目含 uv.lock、Ruff/pytest/CI/安全策略等完整工程配置

## 适用场景

- 快速搭建带工程规范的 AI agent 或 RAG 项目
- 生成训练或推理服务脚手架并直接部署到云平台
- 用统一模板初始化纯 Python 库、CLI 或 FastAPI 服务

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L12: Generate production-ready Python and AI stacks by combining frameworks, data engines, tooling, and cloud deployment
> L47: |Workload|library, CLI, API, web, TUI, MCP, agent, RAG, inference, training, hybrid|
> L48: |Framework|FastAPI, Flask, FastMCP, Pydantic AI, LangGraph, LlamaIndex, Lingo, Transformers|

## 星数曲线

```mermaid
xychart-beta
    title "leynier/python-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-27 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `70920bf43ed8` · [字段定义](../../DATASET.md)*
