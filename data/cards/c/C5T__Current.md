# C5T/Current

⭐ 98 · C++ · 推送 2025-11-18 · [GitHub](https://github.com/C5T/Current) · [官网](https://medium.com/dima-korolev/current-for-realtime-machine-learning-4f04aa8ab81a) · 组织维护

**C++ 实时机器学习框架，含类型系统、流式持久化与优化引擎**

面向 C++ 开发者的实时机器学习基础框架，MIT 许可，累计超过 1000 个 PR。核心组件包括：内建反射的 TypeSystem、JSON/二进制序列化与命令行参数库（Bricks）、HTTP 服务与内存消息队列（Blocks）、append-only 不可变持久层 Stream、内存事务对象存储 Storage、类型演化框架、流式数据管道语言 RipCurrent、凸优化引擎 FnCAS 及 1+ GB/s 吞吐的 CompactTSV。2024 年起转向 cmake，通过复制 Makefile 并 make 即可构建用户项目；测试与覆盖率工具链完备。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内建反射的 C++ 类型系统（支持模板）
- append-only 不可变持久层与发布订阅机制
- 内存事务对象存储，支持最终一致只读副本扩展
- 凸优化引擎 FnCAS 与 1+ GB/s 的 CompactTSV 持久层

## 适用场景

- 构建需要低延迟持久化与流式处理的 C++ 实时系统
- 搭建基于 HTTP 服务与内存消息队列的后端组件
- 使用凸优化引擎进行实时数值优化

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L1: # Current C++ MIT license
> L28: #### TypeSystem
> L46: #### RipCurrent

## 星数曲线

```mermaid
xychart-beta
    title "C5T/Current 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 97 --> 99
    line [98, 98]
```

2026-10-18 98 → 2026-10-29 98（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `5d1dcec0b06f` · [字段定义](../../DATASET.md)*
