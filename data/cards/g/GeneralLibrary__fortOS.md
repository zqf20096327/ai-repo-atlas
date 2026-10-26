# GeneralLibrary/fortOS

⭐ 27 · C# · GPL-3.0 · 推送 2026-08-29 · [GitHub](https://github.com/GeneralLibrary/fortOS) · [官网](https://fortos.justerzhu.cn) · 组织维护

**基于 .NET 10 的安全优先 Linux NAS 操作系统**

FortOS 是一个构建于 .NET 10 之上的 Linux NAS 操作系统，可经 Debian 12 ISO 裸金属安装或在 Docker 内评估运行。存储能力覆盖磁盘发现、mdadm RAID、ext4/XFS/Btrfs/ZFS 文件系统、SMART 监控与配额；共享支持 SMB/NFS/FTP；保护机制含快照、rsync/云备份与时间点恢复。管理面统一暴露 REST/gRPC API、终端 CLI 与 Web 仪表盘，Docker 容器与原生存储服务并列为一等公民。安全方面提供 NasToken 能力令牌、细粒度权限与 HMAC 链式审计。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- mdadm RAID 与 ext4/XFS/Btrfs/ZFS 多文件系统支持
- 统一 REST/gRPC API 与终端 CLI、Web 仪表盘
- SMB/NFS/FTP 共享、快照与云备份
- NasToken 能力令牌与 HMAC 链式审计

## 适用场景

- 在 NAS 硬件上裸金属部署一体式存储系统
- 通过 Docker Compose 快速评估系统功能
- 用 CLI 或 REST/gRPC API 自动化管理存储、共享与备份任务

## 场景标签

 · 领域:存储/操作系统

## 证据(README 行号)

> L3:  A modern, security-first Linux NAS operating system , built on .NET 10 .
> L19: |🐳 **Containers**|Agent Catalog, Token Broker, hardened Compose generation|

## 星数曲线

```mermaid
xychart-beta
    title "GeneralLibrary/fortOS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `ac270f00b8fd` · [字段定义](../../DATASET.md)*
