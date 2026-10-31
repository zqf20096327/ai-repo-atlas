# valohai/tensorflow-example

⭐ 20 · Python · 推送 2026-05-11 · [GitHub](https://github.com/valohai/tensorflow-example) · [官网](https://valohai.com/) · 组织维护

**Valohai 平台的 TensorFlow 示例项目：手写数字检测全流程**

面向 Valohai MLOps 平台的示例仓库，基于 TensorFlow 实现手写数字检测，演示包含数据预处理、模型训练、批量推理、预测对比与在线推理部署五个步骤的完整流水线。提供四条可运行流水线，包括三路并行训练、带人工审批环节的部署流水线及展示节点复用的 'Broken' 流水线。支持在 Valohai 网页端、终端（valohai-cli）或本地（Python 3.9）运行，本地运行需先完成前置步骤的输出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五步骤 ML 流水线：预处理、训练、批量推理、预测对比、在线部署
- 四条示例流水线，含三路并行训练与人工审批部署流程
- 支持网页端、vh 命令行与本地 Python 三种运行方式
- 基于 TensorFlow 官方手写数字示例实现

## 适用场景

- 学习如何在 Valohai 平台组织 ML 训练与部署流水线
- 体验并行训练、人工审批与部署节点等平台功能
- 参照示例改造自己的 TensorFlow 项目接入 Valohai

## 场景标签

`MLOps` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository serves as an example for the [Valohai MLOps platform][vh]. It implements handwritten digit detection
> L29: If you are just starting out, it is recommended to follow [the learning path][lp] in the Valohai documentation. Thi

## 星数曲线

```mermaid
xychart-beta
    title "valohai/tensorflow-example 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bd472ee5660c` · [字段定义](../../DATASET.md)*
