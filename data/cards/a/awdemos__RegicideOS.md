# awdemos/RegicideOS

⭐ 14 · Shell · MIT · 推送 2026-09-13 · [GitHub](https://github.com/awdemos/RegicideOS) · [官网](https://vibecodingagency.com/resources/white-papers/regicide-os/) · 个人维护

**基于 Gentoo/Btrfs/COSMIC 的 Rust 优先不可变 Linux 发行版**

以 Gentoo stage4 为基础构建的 Linux 发行版，默认桌面为 COSMIC，根文件系统为只读 Btrfs，状态数据放独立子卷，更新经离线校验后原子切换并可回滚。提供 Catalyst 与 Dagger 两条构建流水线，产出 stage4、SquashFS、QCOW2 虚拟机镜像与可引导 live ISO；另有 Arch 实验变体及 WSL2 rootfs 管线。系统集成 Rust 编写组件并计划 Rust 化迁移；AI 侧包含已可工作的 BtrMind 代理（Btrfs 优化清理）与规划中的 Portage 优化代理，README 还给出面向 AI 代理的可验证安装步骤。当前处于早期开发阶段（v0.0.1），裸机安装需在现有 Linux live 环境中自行编译安装器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 只读 Btrfs 根 + 原子更新与 regicide-rollback 回滚
- Catalyst/Dagger 流水线产出 stage4/SquashFS/QCOW2/live ISO，六阶段增量缓存
- 内置 BtrMind AI 代理做 Btrfs 优化与清理（Working）
- RegicideOSArch 变体附带 WSL2 rootfs 生成管线

## 适用场景

- 在 VM 或裸机上试用 Rust 化的不可变 Linux 桌面系统
- 从源码自行构建定制的 Gentoo/COSMIC 不可变镜像
- 通过原子更新与快照回滚管理系统变更

## 场景标签

 · 领域:操作系统/系统软件

## 证据(README 行号)

> L14: **A forward-looking Linux distribution with a clear mission:** every component that can be implemented in Rust will
> L51: |AI Agent|BtrMind|BTRFS optimization and cleanup|✅ Working|

## 星数曲线

```mermaid
xychart-beta
    title "awdemos/RegicideOS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d63350ad6525` · [字段定义](../../DATASET.md)*
