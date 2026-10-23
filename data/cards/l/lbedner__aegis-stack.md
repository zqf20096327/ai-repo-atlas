# lbedner/aegis-stack

⭐ 145 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/lbedner/aegis-stack) · [官网](https://aegis-stack.io) · 个人维护

**生成生产级 FastAPI 应用的 CLI 脚手架，可增删组件**

基于 Copier 模板的开源 CLI，用 uvx aegis-stack init 生成完整 FastAPI 应用，包含认证、支付、worker、AI 服务与内建控制面 Overseer。组件（数据库、缓存、调度器等）与服务（auth、AI、支付等）可在既有项目上单命令增删，涉及用户已改文件的变更会被合并并标记冲突。AI 能力（PydanticAI/LangChain 跨 7 个 provider、RAG、对话 agent、本地 Ollama 推理）为可选服务；生成项目自带 GitHub Actions CI 与一键 SSH 部署。要求 Python 3.11+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单命令增删组件与服务，变更自动合并并标记冲突
- 可选 AI 服务：对话 agent、RAG、TTS/STT（PydanticAI/LangChain，7 个 provider）
- 内建 Overseer 控制面：组件健康、worker 队列、AI token 用量等一览
- 生成项目预置 GitHub Actions CI 与一键 SSH 部署（含备份与自动回滚）

## 适用场景

- 两周内搭出可上线的 FastAPI 后端骨架
- 按需给现有项目追加数据库、支付、AI 等能力
- 在自管 VPS 上部署并运维生成的应用

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L17: **Aegis Stack is an open-source CLI that scaffolds production-ready FastAPI applications and lets you add, remove, 
> L87: |**AI**|Conversational agents, RAG, model catalog, TTS and STT (PydanticAI / LangChain across 7 providers)|Optional

## 星数曲线

```mermaid
xychart-beta
    title "lbedner/aegis-stack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 144 --> 146
    line [145, 145]
```

2026-10-18 145 → 2026-10-23 145（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `27df13ec66c0` · [字段定义](../../DATASET.md)*
