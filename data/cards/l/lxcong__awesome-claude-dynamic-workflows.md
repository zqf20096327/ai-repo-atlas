# lxcong/awesome-claude-dynamic-workflows

⭐ 30 · Shell · MIT · 推送 2026-06-02 · [GitHub](https://github.com/lxcong/awesome-claude-dynamic-workflows) · 个人维护

**Claude Code 多智能体工作流实例的社区策展清单**

社区维护的 Claude Code Dynamic Workflows 目录：收录实际生产环境中使用的工作流脚本，安装后成为斜杠命令（放入 ~/.claude/workflows/ 或项目 .claude/workflows/，Claude Code 自动发现，无需插件或注册）。提供 install.sh 一键安装单个工作流或从克隆安装全部。首个展示条目 TradingFlow 为多智能体股票分析工作流（并行分析师→多轮辩论→评级），已独立成仓库；其余多个分类尚待贡献。使用需 Claude Code v2.1.154+、付费计划并启用该功能。

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

- 工作流文件放入目录即被 Claude Code 自动发现为斜杠命令，无需插件或清单注册
- install.sh 支持按名称安装单个工作流或批量安装（用户/项目两种作用域）
- 收录 TradingFlow：4 分析师并行→多轮辩论→5 档评级的多智能体股票分析工作流
- 多智能体编排模式：并行扇出、顺序辩论、评审面板

## 适用场景

- 为 Claude Code 查找生产环境验证过的多智能体工作流
- 参考并行扇出、辩论、评审面板等编排模式构建自己的工作流
- 分享自己在生产中运行的工作流给社区

## 场景标签

`精选清单` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: A community-curated list of real-world Dynamic Workflows in Claude Code —
> L16: a tutorial — it's a directory of battle-tested examples.

## 星数曲线

```mermaid
xychart-beta
    title "lxcong/awesome-claude-dynamic-workflows 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-31 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f78eb9f5a9bd` · [字段定义](../../DATASET.md)*
