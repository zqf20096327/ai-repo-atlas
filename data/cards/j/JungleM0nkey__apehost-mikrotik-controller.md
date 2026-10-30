# JungleM0nkey/apehost-mikrotik-controller

⭐ 22 · TypeScript · MIT · 推送 2025-11-05 · [GitHub](https://github.com/JungleM0nkey/apehost-mikrotik-controller) · 个人维护

**带 AI 诊断助手的 MikroTik 路由器 Web 管理面板**

面向 MikroTik RouterOS 的自托管 Web 管理界面：提供实时指标仪表盘（WebSocket 更新）、网络管理（接口/IP/路由/ARP）、WireGuard VPN 配置（自动生成密钥、QR 码）。内置 AI 诊断助手，含 14 个 MCP 工具做防火墙路径分析、连通性测试、安全检测等，支持自然语言提问，输出带置信度与严重度分级的建议。AI 后端可在 Anthropic Claude、Cloudflare Workers AI、LM Studio 本地推理之间选择。前后端均为 Node/TypeScript，从源码运行。README 自声明处于开发中、不适用于生产环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AI 诊断助手含 14 个专用 MCP 工具（防火墙路径测试、连通性诊断、安全审计、测速）
- 多 AI 供应商支持：Claude / Cloudflare Workers AI / LM Studio 本地推理
- WireGuard VPN 管理：自动密钥生成、peer 管理、移动端 QR 码
- 实时 WebSocket 指标更新与点击复制的网络值展示

## 适用场景

- 用 Web 面板集中管理 MikroTik 路由器的接口、路由与 ARP
- 让 AI 助手诊断网络连通性问题并定位防火墙阻断规则
- 配置和管理 WireGuard VPN 远程访问

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L15: Web-based management interface for MikroTik routers with AI-powered network diagnostics and troubleshooting capabil
> L27: AI-powered network troubleshooting with automated issue detection, severity classification, confidence scoring, and

## 星数曲线

```mermaid
xychart-beta
    title "JungleM0nkey/apehost-mikrotik-controller 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-30 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `051cfeeba850` · [字段定义](../../DATASET.md)*
