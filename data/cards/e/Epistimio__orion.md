# Epistimio/orion

⭐ 304 · Python · NOASSERTION · 推送 2026-04-11 · [GitHub](https://github.com/Epistimio/orion) · [官网](https://orion.readthedocs.io) · 组织维护

**异步分布式超参数优化框架，供科研调优模型**

Oríon 是面向黑盒函数优化的异步框架，定位为机器学习模型与训练的元优化器和大规模异步优化实验平台。用户在原有命令行脚本上添加一行 orion 命令即可定义搜索空间（如 --mini-batch~'randint(32,256)'），最小侵入研究流程。原生异步、易并行，支持多种既定超参算法、自定义算法插件、本地或远程数据库持久化，语言与配置文件无关。以 pip 安装的 Python 包提供，BSD 3-Clause 许可，含 Zenodo DOI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单行命令包装用户脚本即可开始调参，最小侵入工作流
- 原生异步设计，易于并行化
- 支持既定超参算法并可插件式集成自定义算法
- 本地或远程数据库透明持久化实验结果

## 适用场景

- 为机器学习模型训练做超参数调优
- 在多机/异步环境中并行运行大规模优化实验
- 在不大改现有脚本的前提下接入超参搜索

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L38: Oríon is an asynchronous framework for black-box function optimization.
> L40: Its purpose is to serve as a meta-optimizer for machine learning models

## 星数曲线

```mermaid
xychart-beta
    title "Epistimio/orion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 303 --> 305
    line [304, 304]
```

2026-10-18 304 → 2026-10-22 304（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `96f42a42c3dd` · [字段定义](../../DATASET.md)*
