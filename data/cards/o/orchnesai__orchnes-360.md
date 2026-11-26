# orchnesai/orchnes-360

⭐ 3 · Shell · MIT · 推送 2026-11-23 · [GitHub](https://github.com/orchnesai/orchnes-360) · [官网](https://orchnes.com) · 个人维护

**面向 AI agent 的端到端业务技能包（26 个 SKILL.md）**

按开放 Agent Skills 格式（YAML frontmatter + Markdown）组织的 26 个技能文件夹，覆盖创业全流程：市场调研、公司设立、品牌与知识产权、产品构建、基础设施规划、安全运维、增长运营、日常助理等。每个技能仅在需要时加载指令，平时只占技能名与描述的上下文；设计原则要求每条流程以可核查结果收尾、不依赖特定模型或工具。安装方式是把技能文件夹复制到各 AI 编码工具的 skills 目录，或通过 Claude Code 插件市场安装；不支持 skills 的工具可用指令文件回退方案，配套 Rust CLI 可代为生成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 26 个 SKILL.md 技能，覆盖从想法到运营的业务全流程
- 按需加载设计：仅技能名与描述进入上下文
- 多工具兼容：Codex/Cursor/Copilot/Gemini CLI/Windsurf/Cline 原生 skills 路径
- 不支持 skills 的工具提供 AGENTS.md 等指令文件回退与 orchnes CLI

## 适用场景

- 给 AI 编码工具补充创业、合规、增长等业务流程技能
- 让 agent 团队按成本路由任务并记录决策
- 跨会话/跨工具维护持久记忆与状态

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L12: Each skill is a folder with a `SKILL.md` following the open **Agent Skills** format
> L51: These are standard **Agent Skills** (agentskills.io spec), so most AI coding agents load them natively.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `2b208ba9c734` · [字段定义](../../DATASET.md)*
