# daeryundf2-prog/LAZYANTIGRAVITY

⭐ 14 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/daeryundf2-prog/LAZYANTIGRAVITY) · 个人维护

**给 agent 编程环境的确定性多智能体编排与维护者自动化框架**

面向 Antigravity/Gemini CLI 等 agent 编程运行时的编排框架：提供证据绑定的工作循环（/ulw 实现-测试-修复闭环，完成需文件校验和、exit-0 审计等证据，未验证则失败关闭交人工）、持久工作记忆、15 个组件与 8 个本地 MCP 服务器（git、ast_grep、LSP、媒体转录等）、模型路由提示与会话快照。本地优先：遥测与更新检查默认关闭。符号索引为正则近似，网络出口审计无运行时强制。以 Node 20+ 插件形式安装，无需构建步骤。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 证据绑定 /ulw 工作循环，未验证即失败关闭至人工决策
- 8 个内置本地 MCP 服务器（git/ast_grep/LSP/media/workspace 等）
- 15 个组件 + 24 个共享工作流技能，dist 与源码可复现校验
- LAZYANTIGRAVITY_OFFLINE=1 关闭应用层全部外联路径

## 适用场景

- 在 Antigravity/Gemini CLI 中给 agent 加装证据门与质量闸
- 多目标编排带检查点与断点恢复（/ulw-loop resume）
- 持久化跨会话决策与踩坑记忆供 agent 检索

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: > **Deterministic Multi-Agent Orchestration Framework & Maintainer Automation Layer**
> L11: Originating from concepts in lazycodex and Ouroboros, LAZYANTIGRAVITY provides a model-agnostic, developer-first or
> L93: - **15 components** — rules engine, active memory, quick-lane, adaptive reasoning, comment checker, LSP feedback, U

## 星数曲线

```mermaid
xychart-beta
    title "daeryundf2-prog/LAZYANTIGRAVITY 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `036a2aceb4b3` · [字段定义](../../DATASET.md)*
