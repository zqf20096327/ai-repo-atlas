# MedX-PKU/OneEHR

⭐ 10 · Python · MIT · 推送 2026-05-25 · [GitHub](https://github.com/MedX-PKU/OneEHR) · [官网](https://medx-pku.github.io/OneEHR/) · 组织维护 · 中文 README

**EHR 纵向预测实验的 Python 一站式库**

面向纵向电子健康记录（EHR）实验的 Python 包：以标准化三表 CSV 输入和 TOML 实验配置驱动预处理、训练、测试、分析与绘图全流程。内置 42 种模型架构（表格 ML、循环/非循环 DL、不规则时间、多模态、KG 增强、EHR 专用、生存分析），并提供 MIMIC-III/IV、eICU 数据集转换器、ICD/CCS/ATC 医学编码工具、公平性与校准分析模块，每次实验输出独立运行目录（检查点、预测、指标、图表）。需要 Python 3.12+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 42 种内置模型架构，覆盖 ML/DL/EHR 专用/生存分析等 8 类
- TOML 配置驱动的 preprocess→train→test→analyze→plot CLI 工作流
- MIMIC-III/IV、eICU 数据集转换器与 ICD-9/10 编码工具
- 公平性、校准、bootstrap 置信区间等分析模块与多类图表输出

## 适用场景

- 在 MIMIC 数据上做死亡率等临床预测任务实验
- 用统一配置对比多种 EHR 模型并生成图表与分析报告
- 处理 ICD 编码分组与医学代码映射
- 做带公平性与校准评估的临床预测研究

## 场景标签

`科研工具` `MLOps` · 领域:学习与行业

## 证据(README 行号)

> L8: OneEHR is a Python package for longitudinal EHR experiments. It uses standardized EHR tables and a TOML experiment c
> L13: - **42 built-in model architectures**: tabular ML, recurrent and non-recurrent DL, irregular-time, multimodal, KG-e


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `7b0ad4a6200d` · [字段定义](../../DATASET.md)*
