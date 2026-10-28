# orobix/quadra

⭐ 52 · Python · Apache-2.0 · 推送 2026-05-21 · [GitHub](https://github.com/orobix/quadra) · [官网](https://orobix.github.io/quadra/) · 组织维护

**用 YAML 配置文件组织可复现深度学习实验的框架**

面向研究者和开发者的深度学习实验框架：基于 Hydra、Pytorch Lightning 与 Pytorch，通过单一命令行接口组合 YAML 配置文件运行多组实验，支持分类、分割、自监督学习（如 BYOL）与异常检测（如 PADIM，基于 anomalib）等任务，训练完成保存 torchscript 模型，部分模型支持 ONNX 导出。实验可经 Lightning 集成记录到 Mlflow（默认 logger，需设置 MLFLOW_TRACKING_URI），也可用 csv 记录。以 pip/poetry 安装的 Python 包提供，默认在 GPU 0 运行，可通过 trainer=lightning_cpu 切换到 CPU。

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

- YAML 配置组合实验，单一 CLI 运行多组超参数设置
- 内置分类/分割/SSL/异常检测示例实验
- 训练产出 torchscript 模型，部分模型支持 ONNX 导出
- Mlflow 实验记录集成（也可用 csv logger）

## 适用场景

- 用配置文件管理并对比多组深度学习实验
- 在自有数据集上复用模板配置做分类或分割训练
- 用 Mlflow 跟踪训练指标与模型产物

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L29: `Quadra` aims to simplify deep learning experimenting process, allowing researchers or developers to compare, monit
> L242: - Pytorch and Pytorch Lightning for training and deploying deep learning models. These two libraries are core part

## 星数曲线

```mermaid
xychart-beta
    title "orobix/quadra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-28 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4a3aaefa3867` · [字段定义](../../DATASET.md)*
