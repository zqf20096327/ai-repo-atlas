# luongnv89/asm

⭐ 976 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/luongnv89/asm) · [官网](https://luongnv.com/asm) · 个人维护

**面向 AI 编码 agent 的技能安装与管理 CLI**

agent-skill-manager（asm）是一个 Node.js CLI，用于跨 21 个提供方（Claude Code、Codex、Cursor 等）安装、搜索、审计与组织 agent 技能。所有命令支持 --json 与 --yes 以供脚本与 agent 非交互调用；提供安装前安全扫描、重复与语义重叠审计、上下文驻留成本统计（--tokens）、免安装的 asm get 引用模式，以及技能脚手架与发布流水线。目录收录 7,267 个技能，MIT 许可、无遥测，要求 Node.js 22+ 与 git 2.20+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨 21 个 provider 的统一技能清单与去重审计（asm list / audit / overlap）
- 上下文注意力预算管理：stats --tokens 与 residency audit 量化驻留成本
- asm get 免安装读取技能正文，配合 --json/--yes 供 agent 脚本化调用
- 安装前安全扫描：shell 执行、网络访问、凭据暴露检测

## 适用场景

- 为多个 AI 编码工具统一管理技能安装，避免散落的重复副本
- 在 CI 或 agent 工作流中以 JSON 输出自动化技能的安装与审计
- 控制技能对 agent 上下文窗口的 token 驻留成本
- 按标签检索与浏览 6,000+ 技能目录后按需安装

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L10: # CLI to install and manage agent skills
> L12: **agent-skill-manager** (`asm`) is a scriptable CLI built for AI agents and automation — install, search, audit, an
> L34: |**Agent-ready CLI**|`--json`, `--yes`, `--machine` on list, search, install, audit, eval|

## 星数曲线

```mermaid
xychart-beta
    title "luongnv89/asm 星数(近 19 点)"
    x-axis ["2026-10-25", "2026-10-28", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 958 --> 978
    line [959, 960, 959, 961, 962, 959, 966, 971, 972, 974, 975, 974, 973, 974, 975, 976, 977, 976, 976]
```

2026-10-25 959 → 2026-11-27 976（+17）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `466f803c2a3c` · [字段定义](../../DATASET.md)*
