# c2dc/AB-TRAP

⭐ 59 · Jupyter Notebook · 推送 2025-12-30 · [GitHub](https://github.com/c2dc/AB-TRAP) · 组织维护

**五步流程的网络入侵检测系统 ML 开发框架**

面向网络入侵检测系统（NIDS）开发的机器学习框架，定义五个步骤：攻击数据集生成、bonafide 数据集生成（基于 MAWILab）、ML 模型训练（Jupyter Notebook）、模型落地（LAN 场景以 LKM 嵌入内核态，Internet 场景以 Python 用户态实现）与部署后的性能评估。提供 LAN 与 Internet 两套示例，利用虚拟机与容器支撑数据集生成。目标设备为 Raspberry Pi 4，通过 pip 安装依赖。附论文引用与 NeurIPS 2021 数据中心 AI Workshop Lightning Talk。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖数据集生成→训练→落地→评估的完整五步流程
- 内核态（LKM）与用户态（Python）两种模型实现路径
- LAN 与 Internet 两套环境示例，利用虚拟化生成数据集
- bonafide 数据集基于 MAWILAB 构建

## 适用场景

- 按流程构建网络入侵检测系统并部署到目标设备
- 生成攻击与正常流量数据集用于 ML 训练
- 评估 ML 模型在真实设备上的部署性能

## 场景标签

`网络安全` `MLOps` · 领域:学习与行业

## 证据(README 行号)

> L2: The AB-TRAP framework is applicable to the development of Network Intrusion Detection Systems (NIDS), it enables the
> L13: * `/3_Training models`: contains the Jupyter Notebooks to pre-process the data, and generate the ML models (LAN and

## 星数曲线

```mermaid
xychart-beta
    title "c2dc/AB-TRAP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-30 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `0c4a99df7a22` · [字段定义](../../DATASET.md)*
