# ntua-unit-of-control-and-informatics/jaqpotpy

⭐ 21 · Python · MIT · 推送 2026-07-13 · [GitHub](https://github.com/ntua-unit-of-control-and-informatics/jaqpotpy) · [官网](https://jaqpot.org) · 组织维护

**Jaqpot 平台的 Python 客户端：上传部署模型并获取预测**

面向 Jaqpot 平台（app.jaqpot.org）的 Python 客户端库：用 pandas DataFrame 训练的模型（示例为 sklearn RandomForestRegressor）可通过 deploy_on_jaqpot 函数上传部署到平台，获得模型 ID 后可在 Web 界面查看文档、分享模型，并通过 API 在线或以编程方式获取预测。使用需 Python 3.10 与平台账号，通过 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- deploy_on_jaqpot 函数将训练好的模型上传至 Jaqpot 平台
- 部署后可在 Web 界面管理、记录文档并分享模型
- 支持通过 Jaqpot API 在线或编程方式获取预测

## 适用场景

- 把 sklearn 等训练的模型部署到 Jaqpot 平台
- 通过 API 以编程方式获取已部署模型的预测
- 在团队内共享模型及配套文档

## 场景标签

`推理引擎` `MLOps` · 领域:训练与推理

## 证据(README 行号)

> L5: The jaqpotpy library enables you to upload and deploy machine learning models to the Jaqpot platform. Once uploaded,
> L27: 	2. Deploy the trained model using the deploy_on_jaqpot function.

## 星数曲线

```mermaid
xychart-beta
    title "ntua-unit-of-control-and-informatics/jaqpotpy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3961cf1736b4` · [字段定义](../../DATASET.md)*
