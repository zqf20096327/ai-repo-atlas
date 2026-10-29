# netresearch/agent-rules-skill

⭐ 88 · Shell · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/netresearch/agent-rules-skill) · 组织维护

**为 AI 编码 agent 生成 AGENTS.md 规范文件的 Agent Skill**

Netresearch 开发的 Agent Skill，按 agents.md 规范生成并维护 AGENTS.md 上下文文件（面向 AI 编码 agent 而非人类的项目说明文档）。机制包括：自动检测子系统（backend/frontend 等）生成分层文件、从 Makefile/package.json/composer.json/go.mod 抽取命令、幂等更新与 agent 维护标记。支持 Go/PHP/TypeScript/Python 及混合项目的模板识别。以 Agent Skills 格式打包，可通过 Claude Code 插件市场、git clone、npx skills add、Composer、npm 等多种途径安装。许可证采用 split licensing（细节未在可见范围展示）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 agents.md 规范生成 AGENTS.md，支持 Claude Code/Cursor/GitHub Copilot 等 agent 平台
- 自动检测子系统并生成分层（scoped）文件，根文件约 30 行
- 从 Makefile、package.json、composer.json、go.mod 自动抽取命令
- 幂等更新：刷新内容同时保留既有结构

## 适用场景

- 为我的项目生成供 AI 编码 agent 读取的 AGENTS.md 文档
- 多语言/多子系统项目中维护分层的 agent 上下文文件
- 更新已有 AGENTS.md 而不破坏手工维护的内容

## 场景标签

 · 领域:AI 开发工具/文档生成

## 证据(README 行号)

> L3: Netresearch AI skill for generating and maintaining AGENTS.md files following the agents.md specification.
> L13: 2. **Agent Skills** - How this skill is packaged and distributed. A portable format for procedural knowledge that w

## 星数曲线

```mermaid
xychart-beta
    title "netresearch/agent-rules-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 87 --> 89
    line [88, 88]
```

2026-10-18 88 → 2026-10-29 88（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ed4fa4c9bf6b` · [字段定义](../../DATASET.md)*
