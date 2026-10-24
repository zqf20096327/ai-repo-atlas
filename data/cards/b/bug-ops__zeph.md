# bug-ops/zeph

⭐ 65 · Rust · MIT · 推送 2026-10-22 · [GitHub](https://github.com/bug-ops/zeph) · [官网](https://bug-ops.github.io/zeph/) · 组织维护

**记忆优先的长期任务 AI agent：本地/云/去中心化运行**

单个约 12 MB 的 Rust 二进制，面向跨天、跨会话的长期工作：分四层记忆（工作上下文/情景/语义/图），以类型化知识图谱记录决策及其因果关系，支持多跳召回。可接入 Ollama、Claude、OpenAI、Gemini、OpenAI 兼容端点、Candle 及去中心化网络，按五种路由策略在多模型间分配任务。技能以 SKILL.md 文件定义并可热重载，失败后由 LLM 反思生成改进版本。提供 CLI、TUI、聊天机器人部署、MCP/ACP/A2A。安全机制含 age 加密 vault、沙箱、提示注入检测与 SSRF 防护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四层记忆栈（工作上下文/情景/语义/图）记录决策因果，支持多跳召回
- 八类开箱可用 provider 与五种路由策略（EMA/Thompson Sampling/Cascade 等）
- SKILL.md 技能热重载，失败驱动自我改进并自动回滚
- 提示规模 O(K)：50 个技能仅加载约 5 个相关技能（约 2,500 tokens）

## 适用场景

- 跨会话维护项目上下文的编码助手（读取仓库、运行命令、搜索代码）
- 部署到 Telegram/Discord/Slack 作为团队助手
- 通过 Ollama 完全本地离线运行，数据不出机器
- 长任务自动化：研究循环、文档 RAG、计划与子 agent

## 场景标签

`多智能体` `聊天机器人` `知识图谱` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L17: Point it at your code, your documents, or your team chat, and it keeps working across days and sessions — recalling
> L55: |Provider freedom|Ollama, Claude, OpenAI, Gemini, Candle, any OpenAI-compatible endpoint, plus decentralized networ

## 星数曲线

```mermaid
xychart-beta
    title "bug-ops/zeph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-24 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `18141c509e46` · [字段定义](../../DATASET.md)*
