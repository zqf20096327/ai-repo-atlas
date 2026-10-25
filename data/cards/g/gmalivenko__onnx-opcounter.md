# gmalivenko/onnx-opcounter

⭐ 95 · Python · Apache-2.0 · 推送 2026-09-06 · [GitHub](https://github.com/gmalivenko/onnx-opcounter) · 个人维护

**统计 ONNX 模型参数量与 MACs 的 Python 库/CLI 工具**

读取 ONNX 模型文件并统计参数数量与 MACs（乘加运算量）的实用工具，提供命令行和 Python API 两种使用方式。MACs 计算默认依赖 ONNX 形状推断；对形状推断失败的少数模型，会回退到实际运行模型来获取中间形状，此时需额外安装 onnxruntime（pip install onnx_opcounter[runtime]）。要求 Python 3.12 或 newer。README 标注 WIP，许可证为 Apache 2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 统计 ONNX 模型的参数数量与 MACs
- 提供 CLI 与 Python API 两种调用方式
- 形状推断失败时回退到运行模型获取中间形状（需 onnxruntime）

## 适用场景

- 评估模型部署前的计算量与参数规模
- 对比不同 ONNX 模型的算力开销
- 在脚本中集成模型复杂度统计

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: Counts number of parameters / MACs for ONNX models.
> L37: ### Using API

## 星数曲线

```mermaid
xychart-beta
    title "gmalivenko/onnx-opcounter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-18 95 → 2026-10-25 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ab52f88ca399` · [字段定义](../../DATASET.md)*
