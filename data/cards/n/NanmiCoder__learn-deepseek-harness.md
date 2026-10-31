# NanmiCoder/learn-deepseek-harness

⭐ 14 · TypeScript · MIT · 推送 2026-08-17 · [GitHub](https://github.com/NanmiCoder/learn-deepseek-harness) · [官网](https://learn-dsh.vercel.app) · 个人维护 · 中文 README

**DeepSeek Harness 插件开发交互式教程：20 节课带可跑 demo**

面向会写代码但没做过 agent 框架的开发者的交互式教程工作台：用 20 节课、7 个阶段讲解 DeepSeek Harness（DSH）的搭法，从「模型只会说话」讲到写出能装进真实 DSH 的插件。课程代码来自 demo/ 下可运行的两个工程——与真实 DSH 结构同构的最小 Harness 和一个最小 DSH 插件；提供 npm 本地运行、npm run demo 查看真实输出、课程数据体检命令，以及写作规范（判据/手法/禁用词表）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20 节 7 阶段课程，从基础概念到写出可装进真实 DSH 的插件
- 教程代码全部来自 demo/ 下可运行的最小 Harness 与最小插件示例
- npm run demo 展示完整运行过程（插件装配、工具执行、危险动作拦截）
- 课程数据体检（npm run check）含内容边界拦截与图数据校验

## 适用场景

- 系统学习 agent harness 与插件系统的工作原理
- 动手写出并排查第一个 DSH 插件
- 按写作约定扩展或修改教程课程内容

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L17: 一个交互式教程工作台，把 DeepSeek Harness（DSH）是怎么搭起来的讲清楚。写给会写代码、但没做过 agent 框架的人：不需要先懂插件系统、依赖注入、事件总线，从「大模型只会说话」讲起。
> L21: - 说清 DeepSeek Harness 是什么、和 Claude Code 什么关系
> L62: - `demo/mini-harness/` —— 一个能跑的最小 Harness，和真实的 DeepSeek Harness **结构同构，规模不同**：一样的插件模型、服务与依赖、环绕式拦截、事件日志派生历史。差的是规模，不是

## 星数曲线

```mermaid
xychart-beta
    title "NanmiCoder/learn-deepseek-harness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `fc4803dd5b16` · [字段定义](../../DATASET.md)*
