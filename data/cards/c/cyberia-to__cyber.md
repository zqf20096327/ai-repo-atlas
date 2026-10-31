# cyberia-to/cyber

⭐ 54 · Nushell · NOASSERTION · 推送 2026-10-30 · [GitHub](https://github.com/cyberia-to/cyber) · [官网](https://cyber.page) · 组织维护

**面向开发者的去中心化"超级智能"协议节点软件**

Cyber 是一个基于 Cosmos SDK/CosmWasm 技术栈的区块链协议节点（Rust 编写，版本 0.8.0），通过签名、质押的链接构建称为 cybergraph 的共享知识图谱，参与者因"教授"图谱而获得代币奖励。仓库提供 cyber 产品二进制、配置与协议图，支持从源码 cargo 构建并运行本地节点（init/auth enable/node），提供网络端点固定、遗留存储迁移、发布构建脚本等功能；文档中标注验证者共识与分布式最终性仍处分阶段交付状态，当前 token 与 state 为测试网。另有 cyb 机器人二进制（macOS/Android）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Rust 节点二进制：init/auth/node CLI 流程，签名本地发布
- 链接即挖矿的 cybergraph 共识机制（白皮书含数学证明）
- 发布脚本生成二进制、校验和与依赖清单，提供 macOS/Linux ARM64/x64 构建
- 支持遗留 home 存储迁移与端点 network pin 固定

## 适用场景

- 构建并运行本地 Cyber 节点参与协议网络
- 开发基于签名链接知识图谱的应用
- 跟踪该协议的白皮书与测试网（spacepussy-test）进展

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L20: [[superintelligence]] is Type I infrastructure: every agent on a planet — human, machine, sensor, organism — teache
> L37: This repository owns the `cyber` product binary, its configuration, and the
> L92: version 0.8.0.

## 星数曲线

```mermaid
xychart-beta
    title "cyberia-to/cyber 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-31 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `3c7d69d4e5c2` · [字段定义](../../DATASET.md)*
