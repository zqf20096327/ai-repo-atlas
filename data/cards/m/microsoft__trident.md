# microsoft/trident

⭐ 32 · Rust · MIT · 推送 2026-10-29 · [GitHub](https://github.com/microsoft/trident) · 组织维护

**面向 Azure Linux 的声明式安全优先 OS 生命周期代理**

微软维护的操作系统生命周期代理，面向 Azure Linux 裸金属与虚拟机：支持系统安装、置备、A/B 式更新与运行时配置。核心机制为 Host Configuration API——基于 YAML 的声明式接口，定义机器在存储、OS、网络与固件层的期望状态。能力清单覆盖磁盘分区与镜像、RAID、带 TPM/PCR 的加密卷、dm-verity、引导配置、SELinux 配置、用户管理与自定义钩子。安装与配置指引指向官方文档，README 本身未给出具体安装命令。未提及 AI 相关功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明式 YAML Host Configuration API 定义机器期望状态
- 裸金属安装与置备、A/B 式更新
- 带 TPM/PCR 的加密卷与 dm-verity 支持
- 覆盖磁盘分区、RAID、网络、SELinux、用户管理等生命周期能力

## 适用场景

- 数据中心裸金属节点的自动化安装与置备
- Azure Linux 机器的 A/B 式系统更新
- 通过声明式配置统一管理存储、网络与固件状态

## 场景标签

 · 领域:操作系统/基础设施

## 证据(README 行号)

> L3: **Trident** is a declarative, security-first OS lifecycle agent designed
> L4: primarily for [Azure
> L10: At the heart of Trident is its **Host Configuration API**, a declarative

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/trident 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 30 --> 33
    line [31, 32, 32]
```

2026-10-18 31 → 2026-10-30 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 low · 依据 README sha `c89676f40e04` · [字段定义](../../DATASET.md)*
