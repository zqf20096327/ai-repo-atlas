# forester-bt/forester

⭐ 41 · Rust · Apache-2.0 · 推送 2026-09-15 · [GitHub](https://github.com/forester-bt/forester) · [官网](https://forester-bt.github.io/learn) · 组织维护

**行为树 DSL 与 Rust 运行时，编排机器人与 AI agent**

提供一门函数式行为树 DSL 与带类型的 Rust 运行时：用 .tree 文件编写决策逻辑，在应用语言中绑定动作并 tick 执行；运行时处理调度、重试、超时、并行与远程任务，配合 Blackboard 共享状态与指向其中的指针实现 LLM 集成。面向机器人/工业系统与 LLM agent 编排两类用户，支持 ROS Nav2 导出、Webots 仿真、可视化与执行追踪；Python 开发者可经 forester-http-ra-py 通过 HTTP 接入 LangChain/LlamaIndex 工具。提供 f-tree CLI 与 IntelliJ 插件。

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

- 行为树 DSL：高阶树、lambda、类型系统与编译期检查
- 运行时支持同步/异步、本地/远程、并行执行及重试超时
- ROS Nav2 导出与 Webots 仿真器集成
- Python 客户端经 HTTP 执行 LangChain/LlamaIndex 工具

## 适用场景

- 用行为树替代 if/else 链编排 LLM agent 的工具调用
- 机器人在仿真环境中验证控制流后再接入真实硬件
- 对决策逻辑做可视化、追踪与模拟测试

## 场景标签

`Agent 框架` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L4:  A functionally-oriented language and a fast, typed runtime for behavior trees — built to orchestrate robots and AI 
> L42: Structured, inspectable orchestration for LLM-driven systems as an alternative to hand-rolled if/else chains.

## 星数曲线

```mermaid
xychart-beta
    title "forester-bt/forester 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-27 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4b9e286a35df` · [字段定义](../../DATASET.md)*
