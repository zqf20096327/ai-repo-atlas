# axisvela/peiravela-open

⭐ 12 · HTML · Apache-2.0 · 推送 2026-11-16 · [GitHub](https://github.com/axisvela/peiravela-open) · 组织维护

**自主系统实验控制平面的开源 SDK/UI 层**

本仓库是 PEIRAVELA 可能世界实验控制平台三层的 Apache-2.0 SDK/UI 层：发布由 OpenAPI 规范生成的 TypeScript/JavaScript 客户端、公共 Go SDK（SUT 适配器 SPI）、Studio 前端、示例与预编译 AGPL 核心二进制。控制面核心（AGPL-3.0）与企业版（专有）分属另外两个仓库。定位为原始证据生产者：记录事实而不做通过/失败判定，证据包仅用 tar+SHA-256 即可独立核验。面向需要在部署前做可复现场景与反事实分支实验的自主系统团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAPI 生成的 TS/JS 客户端与公共 Go SDK（SUT 适配器 SPI）
- Studio 控制台前端源码以 Apache-2.0 发布，可主题化与嵌入
- 证据包仅用 tar + SHA-256 标准工具即可独立核验
- 提供 Linux amd64 与 Windows amd64 预编译核心二进制

## 适用场景

- 在代码中驱动仿真世界、运行与证据查询
- 为自主系统实现自定义 SUT 适配器接入实验平台
- 以外部评估者身份独立核验仿真证据包

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: > This repository (`peiravela-open`) is one of PEIRAVELA's three tiers: the
> L22: runs, or leaves no verifiable trace. PEIRAVELA gives operators a governed loop —
> L64: - **Extensible by design** — provider SPI, SUT adapter SPI (Digital/Process/

## 星数曲线

```mermaid
xychart-beta
    title "axisvela/peiravela-open 星数(近 3 点)"
    x-axis ["2026-10-25", "2026-11-19", "2026-11-22"]
    y-axis "stars" 10 --> 13
    line [11, 12, 12]
```

2026-10-25 11 → 2026-11-22 12（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `6ed6ce423a77` · [字段定义](../../DATASET.md)*
