# CrayLabs/SmartRedis

⭐ 58 · C++ · BSD-2-Clause · 推送 2026-03-25 · [GitHub](https://github.com/CrayLabs/SmartRedis) · 组织维护

**面向 HPC 的多语言 RedisAI 客户端库：连接模拟与 ML 模型**

SmartRedis 是一组支持 RedisAI 能力的 Redis 客户端库，提供 Python、C++、C、Fortran 四种语言接口，并在 Redis 之上为高性能计算（HPC）应用增加数据存储、脚本执行与模型评估等功能。它是 SmartSim 库的底层客户端，用于把数值模拟连接到 Redis 数据库（或集群），使 PyTorch、TensorFlow 等 ML 库可在超算规模的模拟工作流中使用；也可脱离 SmartSim 独立作为 RedisAI 客户端使用。依赖 NumPy、Hiredis 与 Redis-plus-plus，安装说明托管于 SmartSim 文档，PyPI 提供 Wheel。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 RedisAI 能力的多语言客户端（Python/C++/C/Fortran）
- 连接数值模拟与 Redis 数据库，支持数据存储、脚本执行与模型评估
- 可脱离 SmartSim 独立用于任意 Python/C++/C/Fortran 项目
- 面向超算 HPC 模拟工作流，兼容 PyTorch/TensorFlow 等 ML 库

## 适用场景

- 在 HPC 数值模拟中调用部署于 RedisAI 的 ML 模型
- 在 Python/C++/C/Fortran 项目中作为 RedisAI 客户端使用
- 通过 SmartSim 在超算上编排模拟与机器学习工作流

## 场景标签

 · 领域:HPC/科学计算基础设施

## 证据(README 行号)

> L17: SmartRedis is a collection of Redis clients that support
> L29: SmartRedis is used in the SmartSim library.
> L33: data storage, script execution, and model evaluation. While SmartRedis

## 星数曲线

```mermaid
xychart-beta
    title "CrayLabs/SmartRedis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-26 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `6803cc9aa921` · [字段定义](../../DATASET.md)*
