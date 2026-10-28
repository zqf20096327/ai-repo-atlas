# XucroYuri/how-to-make-script

⭐ 22 · Python · MIT · 推送 2026-08-24 · [GitHub](https://github.com/XucroYuri/how-to-make-script) · 个人维护 · 中文 README

**面向写作者与 AI agent 的剧本创作知识基础设施**

开源的编剧知识库 monorepo，同时供人类写作者与 LLM agent 使用：按意图、媒介、阶段与输出类型对请求分类路由，按需加载协议、评分量规与知识原子，产出结构化剧本工件并自检。内容含 29 个子技能、114 个知识原子、33 个工作流协议、31 个评分量规与 119 条路由 fixture，覆盖叙事、商业定制与互动剧本。以 git clone 方式安装，可挂载为 Claude Code 技能或 Codex 等平台的本地技能；运行时执行尚未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按 intent×medium×stage×output 分类并按需加载知识
- 29 个子技能、33 个工作流协议、31 个评分量规
- 119 条路由 fixture 与 19 个测试模块做路由验证
- 中英双语文档（17 对）

## 适用场景

- 作家用它做结构化剧本开发与自检审阅
- agent 构建者把它挂载为 Claude Code/Codex 技能获得显式路由逻辑
- 查找 beat sheet、场景草稿、互动分支图等输出的生成流程

## 场景标签

`AI 写作` `知识库管理` · 领域:内容生成

## 证据(README 行号)

> L3:  Open-source screenwriting knowledge infrastructure for writers and agents.
> L53: This repository isn't a prompt library or a single-method writing course. It's durable, composable screenwriting in
> L57: If you're a writer: it's a structured development and review toolkit. If you're building agent workflows: it's expl

## 星数曲线

```mermaid
xychart-beta
    title "XucroYuri/how-to-make-script 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-28 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0baacb7ac0c1` · [字段定义](../../DATASET.md)*
