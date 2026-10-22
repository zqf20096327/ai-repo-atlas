# SAP-samples/sap-rpt-1-oss

⭐ 192 · Python · Apache-2.0 · 推送 2026-06-16 · [GitHub](https://github.com/SAP-samples/sap-rpt-1-oss) · 组织维护

**表格上下文学习模型 sap-rpt-1-oss 的推理实现**

SAP 发布的深度学习模型实现，即论文 ConTextTab: A Semantics-Aware Tabular In-Context Learner 的推理管线，原名 ConTextTab，模型与功能不变。模型对表格数据做上下文学习（ICL），支持分类与回归任务，接受 pandas DataFrame 或 NumPy 数组输入，无需预处理：列名与单元格值由后台运行的 LLM 自动嵌入，缺失值自动处理。使用不同模态的专用嵌入并在大规模真实表格数据上训练。模型检查点托管在 Hugging Face，需登录下载；推荐 80GB 显存 GPU 与 8192 上下文，也可降低上下文与 bagging 因子减少资源占用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 表格上下文学习，支持分类与回归
- 输入 pandas/NumPy，无需预处理，LLM 自动嵌入列名与单元格值
- 检查点托管 Hugging Face，运行时自动下载
- 可调节上下文大小与 bagging 因子适配不同 GPU 资源

## 适用场景

- 在小样本表格数据上直接做分类或回归预测
- 需要利用表格语义与世界知识的预测任务
- 复现论文 ConTextTab 的实验结果

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L9: Implementation of the deep learning model with the inference pipeline described in the paper "ConTextTab: A Semantic
> L18: With the aim to combine the best of both these worlds, we introduce **sap-rpt-1-oss** (formerly known under the nam
> L47: The model supports both classification and regression tasks. It accepts input data in the form of a pandas DataFram

## 星数曲线

```mermaid
xychart-beta
    title "SAP-samples/sap-rpt-1-oss 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 191 --> 193
    line [192, 192]
```

2026-10-18 192 → 2026-10-22 192（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `023d21767400` · [字段定义](../../DATASET.md)*
