# apposed/appose

⭐ 19 · Python · BSD-2-Clause · 推送 2026-10-20 · [GitHub](https://github.com/apposed/appose) · [官网](https://apposed.org) · 组织维护

**跨语言进程协作库：Java 调用 Python 环境并共享内存**

Appose 是一个进程间协作库，提供基于社区标准（pixi/mamba/uv）构建环境、以独立 worker 进程运行脚本、通过命名共享内存缓冲区零拷贝传递 NDArray 数据的能力。它最初为在 Java 中免拷贝张量地执行 Python 深度学习而编写，支持 Java 与 Python 实现（JavaScript 为规划中）。Worker 通过 stdin/stdout 的单行 JSON 协议通信（HELLO/LAUNCH/UPDATE/COMPLETION/CANCELATION/FAILURE），内置 Python 与 Groovy worker，任何遵守该 worker 进程契约的程序均可接入。设计原则为简单与自包含，FAQ 中明确拒绝传输层抽象与插件化扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨进程共享内存零拷贝传递 NDArray
- 基于 pixi/mamba/uv 标准构建依赖环境
- stdin/stdout 单行 JSON 的 worker 进程契约，可接入任意遵守契约的程序
- 内置 Python 与 Groovy worker，Java/Python 双语言实现

## 适用场景

- 在 Java 应用中执行 Python 深度学习脚本且避免张量拷贝
- 按需构建隔离依赖环境并在其中异步运行脚本
- 跨语言进程间共享大型数组数据

## 场景标签

 · 领域:跨语言进程间通信/运行时基础设施

## 证据(README 行号)

> L13: Appose is a library for interprocess cooperation with shared memory.
> L17: Appose was written to enable **easy execution of Python-based deep learning
> L22: * Create a Service linked to a *worker*, which runs in its own process.

## 星数曲线

```mermaid
xychart-beta
    title "apposed/appose 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-30 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6eab6ac1102e` · [字段定义](../../DATASET.md)*
