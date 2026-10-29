# thinkingmachines/unicef-ai4d-poverty-mapping

⭐ 24 · Jupyter Notebook · MIT · 推送 2026-02-24 · [GitHub](https://github.com/thinkingmachines/unicef-ai4d-poverty-mapping) · [官网](https://thinkingmachines.github.io/unicef-ai4d-poverty-mapping) · 组织维护

**东南亚九国相对财富（贫困）预测的开源数据集与机器学习模型**

Thinking Machines 与 UNICEF AI4D 合作的贫困制图项目：开放数据集、训练好的模型及复现脚本，基于 DHS 调查数据、EOG 夜间灯光等公开地理空间数据构建相对财富估计模型，覆盖东南亚九国。训练与全国范围预测通过 Jupyter notebook 复现：有 DHS 数据的四国走单国 rollout，其余五国走跨国 rollout。原始 DHS 数据因使用条款不随仓库分发，需用户自行向 DHS 申请；EOG 夜光数据需注册账号；数据缓存需 40-50GB 磁盘空间。提供 conda/make 本地环境搭建和 Docker 镜像两种运行方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 开放数据集、训练模型与复现 notebook（单国/跨国两种 rollout 路径）
- 读取 DHS 调查数据、EOG 夜间灯光等地理空间数据构建特征
- 提供 ghcr.io Docker 镜像，支持交互式全国范围模型 rollout
- 依赖 pip-tools 管理依赖，miniconda 安装 GDAL

## 适用场景

- 复现或扩展东南亚国家的相对财富预测模型
- 用新年度夜光/Ookla 数据对其他国家做模型 rollout
- 获取区域贫困制图的开源数据集与训练产物

## 场景标签

 · 领域:地理空间机器学习/社会发展

## 证据(README 行号)

> L8: The UNICEF AI4D Relative Wealth Project aims to develop open datasets and machine learning (ML) models for poverty m
> L21: * For countries with available DHS training data (Cambodia, Myanmar, Philippines, and Timor-Leste), please refer to
> L23: * For the other countries without DHS training data (Indonesia, Laos, Malaysia, Thailand, and Vietnam), please refe

## 星数曲线

```mermaid
xychart-beta
    title "thinkingmachines/unicef-ai4d-poverty-mapping 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6579aaa9abe2` · [字段定义](../../DATASET.md)*
