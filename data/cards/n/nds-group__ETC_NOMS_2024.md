# nds-group/ETC_NOMS_2024

⭐ 22 · Python · 推送 2026-02-02 · [GitHub](https://github.com/nds-group/ETC_NOMS_2024) · [官网](https://ieeexplore.ieee.org/document/10575394/) · 组织维护

**在可编程交换机内以 P4+随机森林实现线速加密流量分类**

NOMS 2024 论文的配套代码：提出 ETC 框架，仅基于包长与包到达时间特征训练随机森林，并将训练好的模型编码到 P4 可编程交换机的数据平面，实现线速、低延迟的加密流量分类。仓库含两个目录：In_switch_ETC 提供 RF 训练与 P4 编码所需的 Python 与 P4 代码，Offline_ETC 提供离线数据分析与建模代码。覆盖 QUIC 五分类、即时通讯应用指纹六分类、VPN 七分类三个用例，代码以即时通讯用例为主，其余用例沿用同一方法。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 仅用包长与包到达时间特征训练随机森林
- 训练好的 RF 模型编码进 P4 可编程交换机数据平面
- 提供在线（交换机内）与离线两条代码路径
- 支持 QUIC/即时通讯/VPN 三类加密流量分类用例

## 适用场景

- 在可编程交换机上对加密流量做实时分类
- 复现论文的即时通讯应用指纹识别实验
- 研究特征选择与模型到 P4 的编码方法

## 场景标签

 · 领域:网络/流量分类

## 证据(README 行号)

> L3: This repository contains the source code for our work on Encrypted Traffic Classification (ETC) in programmable swit
> L8: This work leverages recent advances in data plane programmability to achieve real-time ETC in programmable switches 

## 星数曲线

```mermaid
xychart-beta
    title "nds-group/ETC_NOMS_2024 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0ebbf83adf81` · [字段定义](../../DATASET.md)*
