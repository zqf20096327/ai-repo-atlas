# eyecan-ai/pipelime-python

⭐ 19 · Python · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/eyecan-ai/pipelime-python) · [官网](https://pipelime-python.readthedocs.io/) · 组织维护

**数据处理与数据流构建的 Python 框架，面向数据科学**

pipelime 是一个模块化的数据科学框架：通过 SamplesSequence 读取、操作数据集并写回磁盘，内置并行化与 yaml/json 序列化，并提供 pytorch 等集成；Piper 管理和执行有向无环图（DAG）数据流并反馈进度；Choixe 提供带变量、导入、循环和参数扫描的配置管理；还可为自定义命令生成 CLI 并将其作为数据流节点使用。支持 Underfolder 基于文件系统的数据集格式，覆盖图像、numpy 数组、yaml/json 等多种文件类型。以 Python 包形式经 pip 安装，绘制数据流图需可选的 draw 变体和系统安装 Graphviz。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SamplesSequence 数据集读写管线，并行化开箱即用，可序列化为 yaml/json
- Piper 执行 DAG 数据流并通过 socket 或回调反馈进度
- Choixe 迷你配置语言：变量、符号导入、循环、switch、参数扫描
- 自定义命令自动获得 CLI 与数据流节点双重身份

## 适用场景

- 读写与转换基于文件系统的数据集
- 构建和管理数据处理 DAG 工作流
- 为数据处理脚本快速生成命令行接口

## 场景标签

`工作流自动化` `MLOps` · 领域:效率与自动化

## 证据(README 行号)

> L10: `pipelime` is a full-fledge **framework** for **data science**: read your datasets,
> L16: - **data processing scripts**: use the powerful `SamplesSequence` and create your own data processing pipelines, wi
> L19: - **command line interface**: `pipelime` can remove all the boilerplate code needed to create a beautiful CLI for y

## 星数曲线

```mermaid
xychart-beta
    title "eyecan-ai/pipelime-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `54b9a46d8210` · [字段定义](../../DATASET.md)*
