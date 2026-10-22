# LearnPrompt/cc-harness-skills

⭐ 239 · Python · MIT · 推送 2026-07-10 · [GitHub](https://github.com/LearnPrompt/cc-harness-skills) · 组织维护 · 中文 README

**面向编码 Agent 的六件套便携技能包：记忆/压缩/验证/路由**

从一个公开镜像的 CC 编码 Agent 代码库中提炼并重写的六个可安装技能，以 SKILL.md 便携包形式分发，可在 Claude Code、Codex、OpenClaw 三种宿主运行时中安装，不依赖私有运行时内部结构。技能覆盖记忆索引整合、持久记忆抽取、完成验证门、多 Agent 分工协调、长会话九段续接摘要与轻量主动任务。提供 npx 一键安装、手动复制与检查/发布脚本。Codex 侧仅验证了包结构，运行时冒烟测试因本地认证未完成。

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

- 六个技能包：记忆整合/记忆抽取/验证门/群体协调/上下文压缩/主动任务
- 跨 Claude Code、Codex、OpenClaw 三种宿主运行时安装
- npx skills add 一键安装，或手动复制 skills 目录
- 每个包含 SKILL.md、prompt 模板、源注与脚本

## 适用场景

- 给 Claude Code / Codex / OpenClaw 加一层共享的记忆与验证能力
- 长会话压缩与交接时保留用户修正
- 多 Agent 分工执行大型任务且不污染主上下文

## 场景标签

`Agent 记忆` `多智能体` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L12: Portable agent skills distilled from a publicly mirrored `CC` coding-agent codebase, then rewritten so they can be 
> L113: |CC Dream Memory|`dream-memory`|Consolidates logs, recent sessions, and topic memories into a short durable memory
> L115: |CC Verification Gate|`verification-gate`|Runs a read-only challenge pass after implementation to distinguish veri

## 星数曲线

```mermaid
xychart-beta
    title "LearnPrompt/cc-harness-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 237 --> 239
    line [238, 238]
```

2026-10-18 238 → 2026-10-22 238（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d59510211c0a` · [字段定义](../../DATASET.md)*
