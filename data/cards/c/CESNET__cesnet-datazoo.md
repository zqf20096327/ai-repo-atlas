# CESNET/cesnet-datazoo

⭐ 53 · Python · BSD-3-Clause · 推送 2026-03-23 · [GitHub](https://github.com/CESNET/cesnet-datazoo) · [官网](https://cesnet.github.io/cesnet-datazoo/) · 组织维护

**面向流量分类研究的加密网络流量数据集工具集**

CESNET 维护的网络流量数据集工具包：提供统一 API 下载、配置并加载四个公开加密流量数据集（CESNET-TLS22/QUIC22/TLS-Year22/QUICEXT-25，TLS 与 QUIC 协议），支持训练/验证/测试时间段选择、应用类已知/未知划分、特征缩放等配置，内置缓存机制加速重复实验，数据集提供 XS-L 多种规模（默认 S 含 2500 万样本）。数据可经 Pandas DataFrame 或 PyTorch DataLoader 读取，配套示例 notebook、预训练模型与迁移学习代码库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 API 下载/配置/加载 4 个加密流量数据集（最大超 5 亿样本）
- 训练/验证/测试划分与已知/未知应用类拆分配置
- 缓存机制与多档数据集规模（XS-L）
- 支持 Pandas DataFrame 与 PyTorch DataLoader 读取

## 适用场景

- 开展加密流量分类模型实验
- 获取大规模 TLS/QUIC 真实骨干网流量数据集
- 复现论文中的流量分类迁移学习实验

## 场景标签

 · 领域:计算机网络/流量分类

## 证据(README 行号)

> L1: The goal of this project is to provide tools for working with large network traffic datasets and to facilitate resea
> L3: - A common API for downloading, configuring, and loading of four public datasets of encrypted network traffic.
> L18: The `cesnet-datazoo` package currently provides four datasets with details in the following table (you might need t

## 星数曲线

```mermaid
xychart-beta
    title "CESNET/cesnet-datazoo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 51 --> 54
    line [52, 53, 53]
```

2026-10-18 52 → 2026-10-29 53（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `89c114c68ee3` · [字段定义](../../DATASET.md)*
