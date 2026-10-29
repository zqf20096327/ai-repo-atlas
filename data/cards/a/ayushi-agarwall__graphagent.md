# ayushi-agarwall/graphagent

⭐ 33 · Python · MIT · 推送 2026-04-14 · [GitHub](https://github.com/ayushi-agarwall/graphagent) · 个人维护

**零依赖的极简 AI agent 编排框架（<100 行核心）**

基于图论的异步优先 agent 编排框架，核心用 Python 标准库实现、少于 100 行代码、零依赖。以 Node（原子工作单元）、State（线程安全状态容器）、Flow（DSL 解析的图编排器）为原语，提供 6 种边运算符（顺序、并行、条件成功/失败、循环、分组）组合执行流；支持多 agent 并行、工作流自动化、RAG 管道、Graph of Thoughts、MoE、自纠错循环等架构。声称零供应商锁定，可接入任意 LLM。安装方式为 git clone 源码安装或直接复制单文件；PyPI 发布标注 coming soon；执行追踪与 GNN 优化功能为规划中未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 核心少于 100 行 Python，零依赖（仅标准库）
- DSL 边运算符（>>、&、?、|、<N>）表达顺序/并行/条件/循环编排
- asyncio.gather 实现节点并行执行，表达式解析缓存
- 输入校验（缺失节点、非法语法、循环流）与重试/超时支持

## 适用场景

- 用轻量 DSL 组合多个 agent 的并行与条件执行流
- 搭建自纠错循环（生成器+校验器）的多 agent 流程
- 在无第三方依赖要求的环境中运行 agent 编排

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L9: A zero-dependency, async-first agent orchestration framework built on graph theory.
> L13: GraphAgent is a minimal, production-ready framework for building AI agents and complex multi-agent orchestrations. 

## 星数曲线

```mermaid
xychart-beta
    title "ayushi-agarwall/graphagent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-29 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `0eb93d7acb53` · [字段定义](../../DATASET.md)*
