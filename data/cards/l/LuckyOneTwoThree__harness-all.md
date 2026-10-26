# LuckyOneTwoThree/harness-all

⭐ 27 · PowerShell · 推送 2026-07-16 · [GitHub](https://github.com/LuckyOneTwoThree/harness-all) · 个人维护 · 中文 README

**工具无关的 AI 研发治理框架：持久记忆+契约交付+质量门禁**

位于 Agent 运行时之上的本地优先治理与交付协议层，配合 Claude Code、Cursor、Trae、Codex 等 Agent 工具使用，提供跨会话持久项目记忆（knowledge-base.md / progress.md）、领域 SOP、契约式交接（PRD + AC 编号 + API 契约 + SHA-256 清单）与由代码审查技能独占写入了完成状态的质量门禁。现有 harness-pm（产品，84 技能）与 harness-engineering（软件工程，25 技能）两个核心包，通过 git clone 与安装脚本安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 Markdown/YAML/JSON 文件为唯一事实源，Agent 工具可替换
- 契约式 PM→Engineering 交接：AC 编号 + API 契约 + SHA-256 清单
- status:done 仅由 code-review 技能写入，含第 10 次迭代硬熔断
- 109 个技能分布于 PM 与工程两个独立领域包

## 适用场景

- 让 AI Agent 在跨会话、跨工具切换时保留项目记忆与上下文
- PM 与工程之间用结构化契约文档做零信息损失交接
- 以证据门禁约束 Agent 完成判定，避免把生成输出当作完成工作

## 场景标签

`Agent 框架` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: > **A local-first governance & delivery protocol layer for AI product R&D — not another multi-agent runtime.** It si
> L21: harness-all is a **governance & delivery layer** — it decides what long-term R&D process your project follows, what
> L57: **4. Local files are the source of truth; Agent tools are replaceable clients.**

## 星数曲线

```mermaid
xychart-beta
    title "LuckyOneTwoThree/harness-all 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4074e407f822` · [字段定义](../../DATASET.md)*
