# tianji-qingtian/AI-Native-Code

⭐ 38 · 推送 2026-05-06 · [GitHub](https://github.com/tianji-qingtian/AI-Native-Code) · 个人维护 · 中文 README

**面向 Claude Code 用户的 AI-native 开发工作流方法论文档集**

一套以文档为主的开发方法论仓库：核心为 4-Phase 框架（意图凝练→契约骨架→机器可读契约网络→意图驱动多 Agent），区分空项目与已有源码两种接入场景，并附反模式速查表与按场景标注的加速数据（30-50% / 10-30%）。面向以 Claude Code 或同类 AI agent CLI 为主力工具的工程师与 tech lead。附带可执行的 Claude Code skill（复制到 ~/.claude/skills 后自动加载并引导流程）。声明为 v0.1 初版，将随试点结果更新。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 4-Phase 框架：意图凝练→契约骨架→契约网络→意图驱动多 Agent
- 空项目（前瞻）与已有源码（考古）两种接入场景
- 反模式速查表与机器可读契约（pytest/mypy/linter）作为真相源
- 提供可复制安装的 Claude Code skill 自动引导流程

## 适用场景

- 用 Claude Code 开新项目时按 4-Phase 流程组织多 Agent 协作
- 在已有代码库上以考古模式接入该工作流并建立契约网络
- 查阅反模式清单避免 AI 协作开发中的常见坑

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: > AI-native 开发的工程方法论——核心不是"让 AI 自主"，是让多 Agent 在共享契约下并行干活。
> L22: |`AI-Native-开发工作流方法论.md`|方法论本体：4-Phase 框架 + 空项目 / 已有源码两种场景 + 反模式速查|
> L23: |`skills/ai-native-code/`|Claude Code skill：方法论的可执行版本，Claude 自动加载并引导 4-Phase 流程|

## 星数曲线

```mermaid
xychart-beta
    title "tianji-qingtian/AI-Native-Code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-26 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0697bda278f1` · [字段定义](../../DATASET.md)*
