# dermatologist/kedro-multimodal

⭐ 24 · Python · Apache-2.0 · 推送 2026-04-03 · [GitHub](https://github.com/dermatologist/kedro-multimodal) · [官网](https://nuchange.ca) · 个人维护

**医疗多模态机器学习 Kedro 项目模板：融合报告/表格/图像**

基于 Kedro 框架（0.18.4 生成）的多模态机器学习项目模板，面向医疗场景，支持将文本报告、表格数据与图像按早融合/晚融合等方法组合训练；其他融合方法与图数据为开发中。可与 Kubeflow、Vertex AI 配合使用，实验性支持 BERT。功能组件来自 kedro-tf-image、kedro-tf-text、kedro-tf-utils 等仓库，可选 DICOM 处理与 DGL 图构建；训练后的融合模型可导出供 TF Serving 部署（附 REST 客户端示例与 Docker 启动脚本）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 报告/表格/图像多数据类型任意组合，支持早融合与晚融合
- 融合模型可导出 TF Serving 签名（含 b64 图像输入）
- 实验性支持 BERT 模型
- 可选组件：DICOM 处理（kedro-dicom）、DGL 图数据（kedro-graph）、FHIR 展平（fhiry）

## 适用场景

- 以模板快速搭建医疗多模态 ML 流水线
- 训练并部署融合报告、表格与图像的模型到 TF Serving
- 在 Kubeflow / Vertex AI 上运行 Kedro 流水线

## 场景标签

`多模态` `MLOps` · 领域:感知与多模态

## 证据(README 行号)

> L5: This is a *template* for **multi-modal machine learning in healthcare** using the Kedro framework. You can combine r
> L9: * This is a template repository. Generate a new repository with the same directory structure by clicking the **Use t

## 星数曲线

```mermaid
xychart-beta
    title "dermatologist/kedro-multimodal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `66583bca4f9b` · [字段定义](../../DATASET.md)*
