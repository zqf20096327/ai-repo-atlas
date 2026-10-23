# helixml/helix

⭐ 822 · Go · NOASSERTION · 推送 2026-10-22 · [GitHub](https://github.com/helixml/helix) · [官网](https://helix.ml) · 组织维护

**私有部署的编码 Agent 舰队平台：每 Agent 独立 GPU 桌面**

Helix 是面向团队的自托管 AI 编码 Agent 编排平台：将 Claude Code、Codex、Gemini CLI、Qwen Code 等 Agent harness 以并行舰队方式运行在自有基础设施上，每个 Agent 获得独立 GPU 加速沙箱桌面（浏览器、终端、GUI 应用），通过规格驱动的看板管理 Backlog 到 PR 的任务流。附带完整私有 GenAI 栈：RAG、MCP 工具、追踪观测、多租户 OIDC、计量计费。支持 Docker 安装器与 Kubernetes Helm 部署；许可证类似 Docker Desktop，大企业商用需购买许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个 Agent 独立 GPU 加速沙箱桌面，任务并行运行
- 规格任务看板：规划→审核→实施→PR 全流程
- 支持多 Agent harness 与自托管 OpenAI 兼容端点（含 vLLM），可中途切换
- 内置 RAG、追踪观测、多租户与计费计量

## 适用场景

- 团队在自有服务器上并行运行多个编码 Agent 并审阅 PR
- 按规格描述驱动 Agent 完成代码变更
- 私有化、可气隙隔离的全栈 GenAI 部署

## 场景标签

`编码 Agent` `多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L16: Helix runs those agents as a **fleet** — many in parallel, each in its own isolated sandbox with a full desktop (br
> L18: It runs with the agent harnesses you already use (Claude Code, Codex, Gemini CLI, Qwen Code, or any ACP-compatible 
> L73: Helix is a full private GenAI stack, so the pieces you'd expect are here too:

## 星数曲线

```mermaid
xychart-beta
    title "helixml/helix 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 821 --> 823
    line [822, 822]
```

2026-10-18 822 → 2026-10-23 822（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `f46f5a086f7e` · [字段定义](../../DATASET.md)*
