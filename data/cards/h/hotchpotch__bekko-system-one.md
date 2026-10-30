# hotchpotch/bekko-system-one

⭐ 37 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/hotchpotch/bekko-system-one) · 个人维护

**17M–400M 小型决策模型套件：选择/判否/打分/重排及训练工具**

训练并运行极小型 System One 决策模型的实验性项目，v0 家族覆盖 17M/68M/400M 参数，将指令、上下文与候选项转为带概率的类型化决策（Choice/Noul/Score/Reranking）。提供基于 Sentence Transformers 的训练工具链（支持全量微调、LoRA、软标签）、独立 Python 推理（CPU 或 CUDA）及 ONNX 导出（Node.js/浏览器，含 WebGPU 浏览器应用）。README 明示 v0 泛化有限，训练与评测清单共享 77 个子集，S1MB 评测覆盖 137 个基准。训练环境针对 Linux x86_64 与 Python 3.12，源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Choice/Noul/Score/Reranking 四类类型化决策输出
- 17M/68M/400M 三档模型，Python CPU/CUDA 推理与 ONNX 导出
- 支持全量微调、LoRA、软标签的自定义数据训练
- 浏览器应用支持 CPU 与 WebGPU 本地推理

## 适用场景

- 路由工单到指定部门或对候选做二选一判断
- 按自定义 0–4 标度给请求打分
- 对检索段落做重排（reranking）
- 用自己的 JSONL 数据训练小型决策模型并导出 ONNX 部署

## 场景标签

`微调` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L10: Bekko System One is an **experimental project for training and running very
> L13: spans 17M to 400M parameters. These models turn instructions, context, and
> L25: passages. It provides training and inference with Sentence Transformers, plus

## 星数曲线

```mermaid
xychart-beta
    title "hotchpotch/bekko-system-one 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-30"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-19 37 → 2026-10-30 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `32d4a22e6831` · [字段定义](../../DATASET.md)*
