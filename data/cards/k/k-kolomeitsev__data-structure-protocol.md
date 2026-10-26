# k-kolomeitsev/data-structure-protocol

⭐ 68 · Python · Apache-2.0 · 推送 2026-08-10 · [GitHub](https://github.com/k-kolomeitsev/data-structure-protocol) · 个人维护

**给 AI 编码 agent 的图结构长期记忆技能，减少重复扫描**

以 agent skill 形式安装到 Claude Code / Cursor / Codex 的代码库结构记忆层：在 .dsp/ 目录以纯文本图存储模块、函数、依赖与公开 API，每条连接带有 why 说明，agent 通过图遍历代替全库扫描获取上下文，支持影响分析（get-parents/get-recipients）。提供 Python CLI（dsp-cli.py）、git hooks（pre-commit/pre-push 图一致性检查）、各 agent 的集成包与全栈样板工程。README 顶部声明本仓库已停止开发，由 dsp-codegen 接替。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- .dsp/ 纯文本图存储实体、依赖与 why 说明，可 git 提交与 diff
- CLI 支持实体创建、搜索、父子遍历与影响分析
- pre-commit / pre-push git hooks 做图一致性检查（无需 LLM）
- 为 Claude Code / Cursor / Codex 提供独立集成包与技能安装脚本

## 适用场景

- 让编码 agent 跨会话记住项目结构，不再每次重新读库
- 重构前查看实体被哪些代码依赖，评估影响范围
- 在存量大型项目上建立可版本化的结构地图

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L26: DSP is a graph-based long-term structural memory stored in `.dsp/`. It gives agents a persistent, versionable map o
> L126: DSP installs as a skill for your agent. Pick your agent and scope.

## 星数曲线

```mermaid
xychart-beta
    title "k-kolomeitsev/data-structure-protocol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-26 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `9a4941efbdcd` · [字段定义](../../DATASET.md)*
