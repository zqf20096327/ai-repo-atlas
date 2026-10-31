# SKKU-ESLAB/ANT-Model-DB

⭐ 17 · Python · Apache-2.0 · 推送 2026-02-10 · [GitHub](https://github.com/SKKU-ESLAB/ANT-Model-DB) · 组织维护

**ANT 框架的 DNN 模型数据库：面向 IoT 设备收录压缩模型**

ANT 框架的模型数据库项目，包含三部分：记录压缩 DNN 模型的模型数据库、基于 TVM 实现的模型 profiler（测量延迟）、以及用 Flask 实现的模型 dashboard 网页（展示数据库中的压缩模型与 kernel 代码）。模型库面向多种 IoT 设备提供 DNN 模型，另含 kernel 数据库用于调优并收集压缩模型的 kernel 代码。通过 python 脚本运行记录器与 dashboard，profiler 依赖 llvm、CUDNN、CUDA。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 记录压缩 DNN 模型并提供给多种 IoT 设备
- 基于 TVM 实现的模型 profiler 测量延迟
- Flask 实现的模型/kernel 数据库 dashboard

## 适用场景

- 为 IoT 设备选型查找可用的压缩 DNN 模型
- 测量 DNN 模型在不同环境的延迟
- 浏览模型库与 kernel 代码收录情况

## 场景标签

 · 领域:IoT/边缘 AI 基础设施

## 证据(README 行号)

> L2: This project includes model database, model profilers, and model dashboard used in ANT framework.
> L4: The model database provides DNN models for various range of IoT devices.

## 星数曲线

```mermaid
xychart-beta
    title "SKKU-ESLAB/ANT-Model-DB 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5f8e30070ce6` · [字段定义](../../DATASET.md)*
