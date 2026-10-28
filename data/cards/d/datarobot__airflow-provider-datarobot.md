# datarobot/airflow-provider-datarobot

⭐ 29 · Python · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/datarobot/airflow-provider-datarobot) · [官网](https://pypi.org/project/airflow-provider-datarobot/) · 组织维护

**将 DataRobot 接入 Apache Airflow 的算子与传感器集成包**

DataRobot 官方维护的 Apache Airflow provider 包，提供 operators、sensors 和 hook，用于在 Airflow DAG 中编排 DataRobot 流水线：创建项目、训练模型、部署模型并对部署的模型进行预测评分。要求 Apache Airflow >= 2.3 与 DataRobot Python API Client >= 3.2.0，通过 pip 安装，并在 Airflow 连接中配置 API Key 与 endpoint。开发流程基于 Docker Desktop 与 Astronomer CLI，代码以专有许可发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 operators、sensors 与 hook 三类组件
- 覆盖创建项目、训练、部署、评分的 DataRobot 流水线编排
- 通过 Airflow 连接配置 API Key 与 endpoint
- 依赖 Airflow >= 2.3 与 DataRobot Python API Client >= 3.2.0

## 适用场景

- 在 Airflow DAG 中编排 DataRobot 的建模与部署流程
- 对已部署的 DataRobot 模型定时执行预测评分
- 将 DataRobot 纳入现有数据流水线进行 MLOps 自动化

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L7: This package provides operators, sensors, and a hook to integrate DataRobot into Apache Airflow.
> L8: Using these components, you should be able to build the essential DataRobot pipeline - create a project, train model


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f1db03d31ec0` · [字段定义](../../DATASET.md)*
