# devoidfury/hotdog

⭐ 22 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/devoidfury/hotdog) · 个人维护

**零依赖的本地开源权重 AI agent 运行框架**

面向本地开源权重模型的 agent harness（框架）：连接 llama.cpp、llama-swap、vllm 或任意 OpenAI 兼容端点，在自有硬件上运行 agent 栈。运行时完全由仓库内 TypeScript 构成，无 npm 依赖、无构建步骤，仅需 Bun >= 1.4.2（源码运行）或可选 npm 安装 @read-receipt/hotdog。功能含工具调用、MCP 客户端、扩展架构、profile、子 agent 与工作流图、上下文压缩等。默认防护栏较少，建议在容器/VM 中运行；macOS/Windows 未测试。

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

- 零运行时依赖，源码即运行时，支持 git clone 直跑与 npm 发布双途径
- 工具调用、MCP 客户端（HTTP+stdio）、扩展架构、profile 组合配置
- 子 agent、工作流图、上下文自动压缩与 JSONL 会话日志
- 工具执行隔离：进程外执行器、可选 bubblewrap jail、userGate 审批

## 适用场景

- 用本地 llama.cpp/vllm 等后端运行编码与任务 agent
- 按需扩展工具与系统提示，组装自定义 agent
- 对供应链敏感、希望可审计源码的用户运行 agent 栈

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **agent harness built for local, open-weight models.** Point it at llama.cpp, llama-swap, vllm, or any OpenAI-compat
> L5: **Zero dependencies** - bring your own Bun and hotdog will run from source code. No `npm install`, no `node_modules`

## 星数曲线

```mermaid
xychart-beta
    title "devoidfury/hotdog 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b2e457098b66` · [字段定义](../../DATASET.md)*
