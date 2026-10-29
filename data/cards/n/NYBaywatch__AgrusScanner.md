# NYBaywatch/AgrusScanner

⭐ 39 · C# · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/NYBaywatch/AgrusScanner) · [官网](https://github.com/NYBaywatch/AgrusScanner/releases/latest) · 个人维护

**Windows 网络扫描器：发现内网中的 AI/ML 服务与 MCP 服务器（影子 AI 探测）**

C#/.NET WPF 编写的 Windows 网络侦察工具，面向安全团队、IT 管理员与研究者：提供 ping 扫描、端口扫描与主机名解析，并通过 116 个探测定义识别 70+ 种 AI/ML 服务（LLM 推理、图像/语音生成、RAG、向量库、MCP 服务器等），主动调用服务 API 提取模型名、GPU 与容器信息。检测签名经签名后自动更新，可关闭。应用自身可运行于 MCP 服务器模式供 Claude Code、OpenClaw 等 agent 调用，另有跨平台 Docker/stdio 控制台版本。仅支持 Windows 10/11 桌面版。

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

- 116 个探测定义识别 70+ 种 AI/ML 服务与 MCP 服务器
- 签名与引擎分离，签名经 CI 签名自动滚动更新（可关闭、可离线）
- 桌面版可 --mcp-only 运行为 Streamable HTTP MCP 服务器，供 agent 调用
- 提供跨平台 Docker/stdio MCP 服务器构建（无 UI，非回环监听需 MCP_TOKEN）

## 适用场景

- 安全团队盘点内网中未经批准的影子 AI 与 LLM 部署
- IT 管理员发现内网 GPU 基础设施与 AI 容器
- 让 Claude Code 等 AI agent 把扫描作为工具自主执行网络探测

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L19: It also runs as an MCP server, so AI agents like Claude Code and OpenClaw can use it as a tool — scan networks, pro
> L58: - **AI Service Detection** - 116 probe definitions identifying 70+ AI/ML services and MCP servers
> L64: - **MCP Server** - Expose scanning tools to AI agents via Model Context Protocol

## 星数曲线

```mermaid
xychart-beta
    title "NYBaywatch/AgrusScanner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-29 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2151187e9390` · [字段定义](../../DATASET.md)*
