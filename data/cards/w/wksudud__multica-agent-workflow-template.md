# wksudud/multica-agent-workflow-template

⭐ 18 · MIT · 推送 2026-05-18 · [GitHub](https://github.com/wksudud/multica-agent-workflow-template) · [官网](https://wksudud.github.io/) · 个人维护 · 中文 README

**中文方法论模板：帮你在 Multica 上设计多 agent + skill 工作流**

基于 Multica（managed agents 平台）构建的工作流设计方法论文档集：提供从模型/skill 盘点、agent 数量与分层决策、manager pattern 到 skill router、CLI operator 创建的分步指引，配套文档模板与提示词文件。强调按任务类型、预算与验证环节自行设计而非照抄配置，附作者 7-agent 案例与安全清单。免责声明中说明本库大部分内容由 AI agent 辅助生成，且不是即装即用的软件产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按模型能力/成本/任务类型分层设计 agent 结构的方法论
- 含 skill router、CLI operator、workflow bootstrapper 的提示词模板
- manager pattern 模板与 Delegation→Verification 轻量契约设计
- 声明文档大部分由 AI agent 辅助生成，需自行验证

## 适用场景

- 安装多个 skill 和模型后不知道如何分配任务时做设计参考
- 系统化搭建自己的 Multica 多 agent 工作流
- 把自己的工作流经验整理成可分享的开源模板

## 场景标签

`多智能体` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: > **这不是一份固定配置清单。** 这是一个帮助你设计**你自己的** Multica 多 agent + skill 工作流的方法论模板。
> L158: **使用风险自担。** 本项目是一个工作流方法论文档集，不是即装即用的软件产品。作者不保证：

## 星数曲线

```mermaid
xychart-beta
    title "wksudud/multica-agent-workflow-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `38f825826932` · [字段定义](../../DATASET.md)*
