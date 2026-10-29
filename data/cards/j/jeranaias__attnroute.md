# jeranaias/attnroute

⭐ 30 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/jeranaias/attnroute) · 个人维护

**给 Claude Code 用户的上下文注入工具：自动预选相关代码文件**

以 Python 包与 CLI 形式提供的 Claude Code hook 系统：追踪文件交互热度（指数衰减）、学习文件共激活模式、用 tree-sitter 依赖图上的 PageRank 排序，在每条 prompt 前自动注入预算内（默认约 6K tokens）的三级上下文（HOT 全文/大纲、WARM 符号、COLD 不注入）。附 4 个行为插件：VerifyFirst 读后写校验、LoopBreaker 循环干预、BurnRate token 预算监控、ContextGuard 压缩恢复。搜索策略含 BM25/语义/图/关键词四级降级；基准（对全量拼接的理论上限）报告 97-99% 压缩率，但 README 自述预测 F1 仅 0.35-0.42，真实节省取决于工作流。核心零依赖安装，Python 3.10+。

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

- 每条 prompt 前注入预算内上下文（默认约 6K tokens，延迟 95-309ms）
- 热度衰减 + 共激活学习 + 依赖图 PageRank 的文件排序机制
- 内置 4 个行为插件（读后写校验、循环检测、token 预算、压缩恢复）
- 核心零依赖，pip 安装后 attnroute init 即用，无需重启

## 适用场景

- 在大型代码库上使用 Claude Code 时自动注入相关文件上下文
- 监控 token 消耗与速率限制，避免超预算
- 拦截 Claude 编辑未读文件、陷入重复失败编辑等行为

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L75: attnroute is a **hook system for Claude Code** that automatically injects smart context into every prompt. Instead 
> L342: After running `attnroute init`, just use Claude Code normally:

## 星数曲线

```mermaid
xychart-beta
    title "jeranaias/attnroute 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-29 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `39c39feae105` · [字段定义](../../DATASET.md)*
