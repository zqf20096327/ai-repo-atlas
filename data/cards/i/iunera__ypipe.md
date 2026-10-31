# iunera/ypipe

⭐ 14 · PowerShell · 推送 2026-08-31 · [GitHub](https://github.com/iunera/ypipe) · [官网](https://ypipe.ai) · 组织维护

**企业本地 AI 客户端与 MCP 编排引擎（Java 单体）**

iunera 开发的本地桌面应用：内置自带的推理引擎，在 CPU/GPU 上运行 GGUF 模型（800M 至 31B+），无需外部推理引擎或 Python 依赖；提供自然语言 Agentic 聊天、可视化 DAG 工作流构建器（SmartPipes）、模型/运行时管理器（含硬件评估与 Hugging Face 模型下载），以及 MCP 服务器一键安装与编排（含内置 Druid MCP Server）。支持 OpenAI 兼容 API、SQLite/Apache Druid 查询与 Kubernetes 部署。当前为专属技术预览：可免费使用但禁止再分发/修改，未来可能引入商业许可层级。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自包含 Java 可执行文件：内置推理引擎，无需 Ollama 等外部引擎或 Python 依赖
- SmartPipes 可视化 DAG 工作流，可发布为 WebForm 或 REST 端点
- MCP 服务器零依赖一键安装与编排，内置 Druid MCP Server
- Gearbox 自动评估 CPU/GPU/RAM 并推荐模型与运行时

## 适用场景

- 在离线/airgapped 环境运行本地 LLM 并编排多智能体工作流
- 将本地模型接入本地数据库（SQLite/Druid）与企业系统执行数据工作流
- 以 OpenAI 兼容端点替代云端 API，实现数据不出本机

## 场景标签

`多智能体` `工作流自动化` `推理引擎` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L9: **Y̊pipe** is an easy-to-use local AI client and MCP orchestration engine—a secure, **local desktop application** th
> L49: * **Self-Contained Inference:** No external inference engines (like Ollama) need to be installed. Everything is ful
> L105: * **Zero-Dependency Setup:** One-click installation of MCP servers. Ypipe handles the environment, runtimes, and c

## 星数曲线

```mermaid
xychart-beta
    title "iunera/ypipe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `bac03c57617b` · [字段定义](../../DATASET.md)*
