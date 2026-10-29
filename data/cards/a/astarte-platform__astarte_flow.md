# astarte-platform/astarte_flow

⭐ 18 · Elixir · Apache-2.0 · 推送 2026-07-17 · [GitHub](https://github.com/astarte-platform/astarte_flow) · [官网](https://docs.astarte-platform.org/flow/snapshot/) · 组织维护

**构建可复用数据处理管道的 IoT 流处理引擎**

Astarte 生态的流处理组件：用户将算法封装为容器 Block，组合成可复用、可共享的 Pipeline，在不同计算场景中以不同配置复用。支持 Lua 编写组件，通过 Container SDK 以 Python 实现并部署算法容器，生产环境推荐使用 Astarte Kubernetes Operator 运行。面向 IoT 数据科学与实时处理场景的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Block/Pipeline 模型实现管道复用与共享
- 算法以 Docker 容器形式打包部署
- Container SDK 支持 Python 实现算法
- 推荐通过 Astarte Kubernetes Operator 运行

## 适用场景

- 为 IoT 设备数据搭建实时处理管道
- 将自研算法封装为容器并在管道中复用
- 在不同配置下复用同一管道处理多种计算场景

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: Astarte Flow lets you create reusable Blocks and Pipelines. This way, you can reuse the same pipeline in countless c
> L10:  * Container SDK - Implement and deploy your algorithm as a Docker Container. Available for
> L11:  Python

## 星数曲线

```mermaid
xychart-beta
    title "astarte-platform/astarte_flow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `c6f772dd6842` · [字段定义](../../DATASET.md)*
