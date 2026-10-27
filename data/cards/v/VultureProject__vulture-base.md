# VultureProject/vulture-base

⭐ 40 · Shell · LGPL-3.0 · 推送 2026-09-17 · [GitHub](https://github.com/VultureProject/vulture-base) · 组织维护

**Vulture 4 操作系统的基础包与引导脚本**

Vulture4 项目的根软件包：用于加固操作系统、安装 Vulture 所需软件包、部署引导 Vulture 服务与 Jails 的系统脚本。获取方式包括下载含全部软件包的 hypervisor 镜像（QCOW2/RAW/VHD(X)/VMDK）、不含 Vulture 软件包的 HardenedBSD 安装 ISO，以及 base/kernel/ports/src 归档；也可按 Building Guide 从源码构建。README 未描述任何 AI 相关功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 操作系统加固与 Vulture 软件包安装
- 引导 Vulture 服务与 Jails 的系统脚本
- 提供 QCOW2/RAW/VHD(X)/VMDK 四种 hypervisor 镜像格式
- 基于 HardenedBSD，支持从源码自行构建

## 适用场景

- 获取 Vulture 4 操作系统的基础镜像进行部署
- 自行构建定制化的 VultureOS
- 为 Vulture 服务与 Jails 准备引导环境

## 场景标签

 · 领域:操作系统/安全基础设施

## 证据(README 行号)

> L1: # The base package for Vulture 4 Operating System
> L8:  - Harden the operating system
> L10:  - Install system scripts to bootstrap Vulture services and Jails

## 星数曲线

```mermaid
xychart-beta
    title "VultureProject/vulture-base 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-27 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `add595e8e99f` · [字段定义](../../DATASET.md)*
