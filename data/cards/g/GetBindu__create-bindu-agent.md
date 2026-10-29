# GetBindu/create-bindu-agent

⭐ 32 · Python · MIT · 推送 2026-03-13 · [GitHub](https://github.com/GetBindu/create-bindu-agent) · [官网](http://docs.getbindu.com) · 组织维护

**AI agent 项目脚手架模板：快速生成支持 A2A 等协议的 agent 服务**

基于 cookiecutter 的 Python 项目模板，配合 uv 做依赖管理。运行一条 uvx 命令并回答项目名、agent 框架（Agno/LangChain/CrewAI 等）、许可证等提示后，生成一个可部署的 agent 服务项目，预配置 A2A、AP2、X402 三种协议，本地运行后监听 8030 端口。生成的项目附带 CI/CD、pytest、ruff/mypy、MkDocs 文档、Docker/Podman 容器化及 Phoenix/Langfuse/Jaeger 可观测性支持。面向需要快速搭建可接入 Internet of Agents 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- cookiecutter 模板一键生成 agent 项目，uv 管理依赖
- 生成项目预配置 A2A/AP2/X402 协议与 agent_config.json
- 支持自选框架：Agno、LangChain、CrewAI、LlamaIndex、FastAgent 等
- 附带 CI/CD、测试、文档、容器化与可观测性配置

## 适用场景

- 快速搭建符合 A2A 协议的可部署 agent 服务
- 为新 agent 项目生成带工程化配置的脚手架
- 让自研 agent 接入多 agent 通信与支付协议生态

## 场景标签

`Agent 框架` `代码生成` · 领域:Agent 开发

## 证据(README 行号)

> L34: **Create Bindu Agent** is the fastest way to build production-ready AI agents that speak the language of the Intern
> L44: uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
> L108: This Cookiecutter template scaffolds a complete Bindu Agent project with everything you need:

## 星数曲线

```mermaid
xychart-beta
    title "GetBindu/create-bindu-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-29 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `ebcb4dfe32f8` · [字段定义](../../DATASET.md)*
