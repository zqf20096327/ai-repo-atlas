# ideos/gloe

⭐ 114 · Python · Apache-2.0 · 推送 2026-09-05 · [GitHub](https://github.com/ideos/gloe) · [官网](https://gloe.ideos.com.br) · 组织维护

**将 Python 代码表达为类型安全数据流（DAG）的通用库**

Gloe 是一个通用 Python 库，引导开发者把代码表达为 flow：即具有单源单汇的 DAG，由称为 transformer 的原子、隔离、可扩展、可追踪单元通过 >> 运算符连接组成。提供类型检查（配合 Mypy 与 IDE 报告不兼容连接）、执行期输入输出校验、同步/异步混用、流程图可视化（开发中）等能力。适用于数据科学与机器学习管道、服务器、脚本等场景。声明自身不是工作流编排器，不提供调度后端、专用执行环境，也不直接提升执行速度或可扩展性。以 pip/conda 安装，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用 >> 运算符连接 transformer 组成 DAG 型数据流
- 类型安全管道，Mypy 与 IDE 报告畸形连接
- 同步与异步代码混用，无需关心并发性质
- 管道可视化绘图生成文档（该功能开发中）

## 适用场景

- 把数据科学或机器学习管道组织为可读、可维护的类型安全流程
- 在服务器或脚本中用小单元明确职责地组织业务逻辑
- 通过流程图快速文档化既有管道

## 场景标签

 · 领域:软件工程/数据管道

## 证据(README 行号)

> L36: **Where can I use it?** Anywhere! Gloe is particularly useful for data science and machine learning pipelines, as w
> L42: - Write **type-safe** pipelines with pure Python.

## 星数曲线

```mermaid
xychart-beta
    title "ideos/gloe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 113 --> 115
    line [114, 114]
```

2026-10-18 114 → 2026-10-27 114（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `fc7f7424a717` · [字段定义](../../DATASET.md)*
