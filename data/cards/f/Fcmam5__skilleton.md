# Fcmam5/skilleton

⭐ 14 · TypeScript · MIT · 推送 2026-09-03 · [GitHub](https://github.com/Fcmam5/skilleton) · [官网](https://www.npmjs.com/package/skilleton) · 个人维护

**面向团队的 AI 技能依赖管理 CLI：像 npm 一样管理 skill**

用 npm 式工作流管理 SKILL.md 格式 AI agent 技能的命令行工具：通过 skilleton add/install/update/list/describe 等命令，将技能引用解析为 git 仓库与子路径，生成 skilleton.json 清单与 skilleton.lock.json 锁文件，实现确定性安装（团队与 CI 拉取相同 commit）。技能直接从 git 安装，无全局注册表，依赖本地 git 与 git ls-remote，支持私有仓库凭据；无遥测。另提供 Node 包 API 供脚本调用，audit 命令目前为占位符。

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

- 清单+锁文件实现确定性技能安装（同 commit 复现）
- 支持根仓库与 monorepo 子路径两种技能指定方式
- 经 git ls-remote 从 git 安装，支持私有仓库，零共享状态
- 提供表格式/JSON 输出与程序化包 API

## 适用场景

- 团队把 AI 技能与代码一起版本化管理
- CI 中按锁文件复现一致的技能安装
- 在 monorepo 中按子路径引用并安装技能

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Deterministic AI skill dependency management for teams**
> L5: Manage AI skills like npm packages - with project manifests, lockfiles, and reproducible installations.
> L47: > **Note**: Skilleton resolves skill refs via `git ls-remote` and requires a local git installation. It respects yo

## 星数曲线

```mermaid
xychart-beta
    title "Fcmam5/skilleton 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `1d5352d9cfe7` · [字段定义](../../DATASET.md)*
