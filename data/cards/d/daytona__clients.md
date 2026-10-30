# daytona/clients

⭐ 15 · Python · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/daytona/clients) · [官网](https://daytona.io) · 组织维护

**Daytona 平台的官方 SDK、API 客户端与 CLI/MCP 工具集**

Daytona（面向运行 AI 生成代码的安全弹性基础设施）的客户端仓库：提供 TypeScript、Python、Ruby、Go、Java 五种语言的 SDK 与生成的 API 客户端，以及 CLI 与 MCP 工具。CLI 可经 Homebrew 安装或从 GitHub Releases 下载二进制（带 SLSA 构建来源证明，可用 GitHub CLI 验证）。使用需设置 DAYTONA_API_KEY。仓库内部用 yarn/poetry/bundle 管理开发依赖，基于 OpenAPI 规范生成本地客户端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五种语言的 SDK 与生成的 API 客户端
- CLI 提供 Homebrew 安装与平台二进制下载
- 发布二进制携带 GitHub artifact attestation（SLSA 构建证明）
- 提供 MCP 工具

## 适用场景

- 在自己的应用中集成 Daytona 沙箱代码执行环境
- 通过 CLI 或 MCP 工具管理 Daytona 实例
- 用官方 SDK 构建 AI agent 的代码执行后端

## 场景标签

 · 领域:AI 基础设施/代码执行沙箱

## 证据(README 行号)

> L1: # Daytona Clients
> L3: SDKs, generated API clients, and the CLI/MCP tools for Daytona.

## 星数曲线

```mermaid
xychart-beta
    title "daytona/clients 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `281c178cd401` · [字段定义](../../DATASET.md)*
