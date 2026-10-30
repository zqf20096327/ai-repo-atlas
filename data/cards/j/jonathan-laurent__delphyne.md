# jonathan-laurent/delphyne

⭐ 22 · Python · MIT · 推送 2026-07-31 · [GitHub](https://github.com/jonathan-laurent/delphyne) · [官网](https://jonathan-laurent.github.io/delphyne/) · 个人维护

**给开发者的 LLM 应用构建框架：策略与策略解耦的可靠编程**

Delphyne 是一个构建 LLM 应用的 Python 编程框架：用户将高层解题策略写成含未决选择点的程序，由独立的策略（policy）驱动 LLM 在搜索树中导航；提供专用演示语言以交互式、测试驱动方式编写少样本示例，并以静态类型与测试 DSL 保证策略修改不破坏演示。附带标准库（结构化输出、工具调用、思维链等）、请求缓存以复现实验、VSCode 扩展与 CLI。要求 Python 3.12（不支持 3.13+），经 git clone 源码 pip 安装。

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

- 策略（strategy）与搜索策略（policy）分离，策略可独立迭代
- 专用演示语言支持交互式测试驱动开发少样本示例
- 静态类型与测试 DSL 保证修改 policy 不破坏 demonstrations
- 资源感知的组合子语言，按构造防止预算超支

## 适用场景

- 构建需要验证与回退的 LLM 推理管线
- 对少样本示例做测试驱动的编写与维护
- 在预算约束下复现与调优 LLM 实验

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: Delphyne is a programming framework for building _reliable_ and _modular_ LLM applications. It offers a powerful app
> L10: Users can describe high-level problem solving _strategies_ as arbitrary programs with unresolved choice points. _Po

## 星数曲线

```mermaid
xychart-beta
    title "jonathan-laurent/delphyne 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-30 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `7457585350c6` · [字段定义](../../DATASET.md)*
