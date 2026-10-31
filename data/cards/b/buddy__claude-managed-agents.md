# buddy/claude-managed-agents

⭐ 16 · TypeScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/buddy/claude-managed-agents) · [官网](https://buddy.works/docs/ai-agents/claude-managed-agents) · 组织维护

**在 Buddy Sandboxes 上自托管 Claude Managed Agents 执行层的控制平面**

为想在自有基础设施上运行 Claude Managed Agents（CMA）的开发者提供部署方案：Anthropic 负责代理循环与会话状态，本仓库提供编排器沙箱（webhook 或轮询两种触发模式）与每会话一个的 worker 沙箱（预装 ant CLI，经 `ant beta:worker run` 运行内置工具集）。以 Node 24+ 与 npm 脚本交付，bootstrap 命令自动完成环境创建、快照构建与部署，仅在生成环境密钥和注册 webhook 两处需在 Anthropic Console 手动操作（轮询模式可省去后者）。凭据边界上 worker 仅接收可撤销的加密环境密钥。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 编排器沙箱支持 webhook 与轮询两种触发模式，切换仅需改 TRIGGER_MODE
- npm run bootstrap 自动化部署并把生成的 id 写回 .env
- 内置 janitor 清扫停止的 worker 沙箱并支持崩溃恢复
- 凭据边界设计：worker 仅接收可撤销的加密环境密钥，不接触管理员 API key

## 适用场景

- 在自有 Buddy 沙箱上运行 Claude Managed Agents 的执行层
- 不暴露公网入站端点的场景下用轮询模式接入 CMA 工作队列
- 验证会话端到端是否真的在 worker 沙箱内执行了命令

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Run the self-hosted Claude Managed Agents (CMA) path on Buddy Sandboxes.
> L5: work queue. Buddy runs the execution layer: one **orchestrator** sandbox (control
> L6: plane) and one **worker** sandbox per session that runs the built-in CMA toolset

## 星数曲线

```mermaid
xychart-beta
    title "buddy/claude-managed-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `652016a65ac3` · [字段定义](../../DATASET.md)*
