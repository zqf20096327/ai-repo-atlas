# TauferLab/SOMOSPIE

⭐ 16 · Jupyter Notebook · BSD-3-Clause · 推送 2026-08-26 · [GitHub](https://github.com/TauferLab/SOMOSPIE) · 组织维护

**土壤湿度空间推断引擎：用机器学习生成细粒度土壤湿度预测**

由田纳西大学诺克斯维尔分校与特拉华大学合作开发的 Jupyter Notebook 与机器学习工具套件，读取卫星遥感的粗分辨率土壤湿度数据，结合地形等环境信息，经预处理、ML 建模、可视化与统计分析三个模块化阶段，生成无空缺的细粒度土壤湿度预测，并附带美国三个生态区域的测试用例。支持本地 Debian 环境安装脚本、Jetstream2 虚拟机镜像和 Docker 容器三种运行方式，依赖 Anaconda、Java 11、Spark、R、GDAL 等组件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预处理→ML 建模→分析的模块化三阶段框架
- 由粗分辨率遥感数据生成细粒度无空缺土壤湿度预测
- 提供美国三个生态区域的测试用例与多张预测地图
- 支持本地安装、Jetstream2 VM、Docker 三种运行方式

## 适用场景

- 精准农业中优化灌溉与土地管理决策
- 生态位建模、碳监测等地球系统模型的土壤湿度输入生成
- 研究数据处理选择对土壤湿度预测结果的影响

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L11: **SOMOSPIE is a spatial inference engine consisting of modular stages for processing spatial environmental data,
> L18: This repository contains a suite of tools for tprocessing spatial environmental data, generating fine-grained soil 
> L130: D. Rorabaugh, M. Guevara, R. Llamas, J. Kitson, R. Vargas, and M. Taufer. **SOMOSPIE: A Modular SOil MOisture SPat

## 星数曲线

```mermaid
xychart-beta
    title "TauferLab/SOMOSPIE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9b13149daabf` · [字段定义](../../DATASET.md)*
