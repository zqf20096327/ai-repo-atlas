# truffle-ai/dexto

⭐ 661 · TypeScript · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/truffle-ai/dexto) · [官网](https://dexto.ai) · 组织维护

**Agent 编排框架：帮开发者构建可持久运行、调用工具的 AI agent**

Dexto 提供一个 agent harness，即把 LLM 编排为有状态 agent 的中间层：以 YAML 配置定义 agent，内置会话管理、持久记忆、工具编排、多模态与多 agent 子代理机制，通过 MCP 协议连接外部工具服务器。自带可立即使用的编码 agent，支持 CLI 交互、headless 运行与 Discord/Telegram 集成；另提供 @dexto/core SDK 以编程方式构建 agent，并可启动 REST/SSE API 服务器。支持 50+ 模型与多云/本地后端切换，需 Node.js 20+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YAML 配置驱动定义 agent，可会话中途切换模型
- MCP 集成连接 30+ 工具服务器
- 持久会话与记忆，支持多 agent 子代理协作
- 提供 CLI、@dexto/core SDK 与 REST/SSE API 三种使用方式

## 适用场景

- 用 CLI 内置编码 agent 读写代码并执行测试
- 以 SDK 构建嵌入自家应用的 agent 后端
- 通过 YAML 配置组合 LLM、工具与存储，构建多 agent 系统
- 本地模型运行以保持数据不出本机

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L53: Dexto is an **agent harness**—the orchestration layer that turns LLMs into reliable, stateful agents that can take 
> L61: |**Dexto**|Operating System|Orchestration, state, tools, recovery|

## 星数曲线

```mermaid
xychart-beta
    title "truffle-ai/dexto 星数(近 7 点)"
    x-axis ["2026-10-24", "2026-10-30", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-26"]
    y-axis "stars" 656 --> 662
    line [657, 659, 657, 659, 660, 661, 661]
```

2026-10-24 657 → 2026-11-26 661（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `d22140bb68c1` · [字段定义](../../DATASET.md)*
