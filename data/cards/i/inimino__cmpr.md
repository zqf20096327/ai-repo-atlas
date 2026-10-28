# inimino/cmpr

⭐ 20 · C · MIT · 推送 2026-05-27 · [GitHub](https://github.com/inimino/cmpr) · 个人维护

**面向 LLM agent 的代码数据库与编程框架**

CMPr 是一个代码数据库工具：通过 git clone 源码 make 编译安装，在项目目录初始化后生成 CLAUDE.md，供 Claude 等 agent 通过 cmpr --help 接口查询和使用代码库；同时提供 TUI 界面，用 j/k 滚动浏览代码块。定位为 LLM-enabled programming framework，让 agent 以结构化方式访问代码数据库。README 较简短，更多文档指向 Discord 社区。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 为项目生成 CLAUDE.md 供 Claude agent 引导使用
- agent 通过 cmpr --help 命令接口访问代码数据库
- 提供 TUI 界面浏览代码块

## 适用场景

- 让 Claude agent 在项目中结构化查询代码库
- 开发者用 TUI 管理和浏览代码块
- 为 AI 编程工作流初始化项目配置

## 场景标签

 · 领域:软件开发/AI 工具

## 证据(README 行号)

> L3: Code database.
> L16: Run `cmpr --help` to get started; this is how the agent uses cmpr.

## 星数曲线

```mermaid
xychart-beta
    title "inimino/cmpr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `d21018f5f952` · [字段定义](../../DATASET.md)*
