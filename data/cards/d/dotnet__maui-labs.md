# dotnet/maui-labs

⭐ 229 · C# · MIT · 推送 2026-10-28 · [GitHub](https://github.com/dotnet/maui-labs) · [官网](https://dot.net/maui) · 组织维护

**.NET MAUI 的实验性工具与预发布包合集（CLI、UI 框架、调试与 AI 集成）**

Microsoft dotnet 组织维护的 .NET MAUI 实验性项目集合，包含 10 个产品：maui 全局 CLI（环境诊断、SDK/模拟器管理、设备管理、AI 引导初始化）、Comet MVU UI 框架、单文件应用服务器 Go、DevFlow 应用自动化/调试与 MCP 工具集、源生成式 AI 工具绑定 AI Extensions、macOS AppKit 与 WPF 后端、基于 Apple Intelligence 的端上 AI API Essentials.AI 等。以 NuGet 预发布包分发，nightly 构建发布至 dotnet10 feed。仓库自身声明实验性质：API 可能变更，不受 .NET MAUI 支持政策覆盖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- maui CLI 提供环境诊断（maui doctor）、Android/Apple SDK 与模拟器管理、设备管理
- DevFlow 提供应用运行时自动化、可视化树检查、网络监控与 MCP server 供 AI agent 接入
- maui ai init 一站式安装 MAUI 技能、DevFlow 技能、Copilot agent 定义与 MCP 配置
- Essentials.AI 通过 Apple Intelligence 提供端上 chat/embedding/tool calling

## 适用场景

- 搭建与诊断 .NET MAUI 开发环境，管理 Android SDK 与模拟器
- 在应用开发中用 DevFlow 做自动化测试、UI 检查与性能分析
- 让 AI agent（Copilot 等）通过 MCP 接入 MAUI 应用调试与自动化
- 用 WPF/AppKit 后端在 Windows/macOS 桌面运行 MAUI 应用

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: Experimental packages and tooling for .NET MAUI. This repository hosts pre-release projects that are in active devel
> L33: - **DevFlow app automation** (`maui devflow`) — visual tree inspection, element interaction, screenshots, WebView/C
> L77: - **MCP server** for AI agent integration (via `maui devflow mcp`)

## 星数曲线

```mermaid
xychart-beta
    title "dotnet/maui-labs 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 227 --> 230
    line [228, 229, 229]
```

2026-10-18 228 → 2026-10-28 229（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c4d33575bf4b` · [字段定义](../../DATASET.md)*
