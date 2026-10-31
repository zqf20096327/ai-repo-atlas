# aliyun/pai-python-sdk

⭐ 23 · Python · Apache-2.0 · 推送 2026-01-05 · [GitHub](https://github.com/aliyun/pai-python-sdk) · [官网](https://pai.readthedocs.io/) · 组织维护 · 中文 README

**阿里云 PAI 平台的 Python SDK：用 Python 完成模型训练与部署**

阿里云机器学习平台 PAI 官方 Python SDK，封装 HighLevel API，供机器学习工程师以 Python 代码提交训练任务、部署模型（含预训练大语言模型如 QWen1.5-7b）、提交微调任务，串联完整机器学习流程。要求 Python ≥ 3.8，通过 pip 安装；由阿里云开发，以 Apache-2.0 许可发布，配套 docs 目录文档与 pai-examples 示例仓库，支持通过 GitHub issue 或钉钉群咨询。

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

- 以 Python 提交自定义训练任务（Estimator API）
- 部署 PAI 预训练大语言模型（如 QWen1.5-7b）
- 通过 ModelTrainingRecipe 提交模型微调任务
- pip 安装，支持 Python ≥ 3.8

## 适用场景

- 在 PAI 平台上用代码提交并管理模型训练作业
- 部署预训练大语言模型为在线服务
- 基于 PAI 微调脚本微调预训练模型

## 场景标签

`模型训练` `微调` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: PAI Python SDK是阿里云 机器学习平台 PAI(Platform for Artificial Intelligence) 提供的Python SDK，提供了更易用的HighLevel API，支持机器学习工程师简单地使
> L34: PAI提供了大量预训练模型，可以使用PAI Python SDK轻松部署：

## 星数曲线

```mermaid
xychart-beta
    title "aliyun/pai-python-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `dfe1307aceb9` · [字段定义](../../DATASET.md)*
