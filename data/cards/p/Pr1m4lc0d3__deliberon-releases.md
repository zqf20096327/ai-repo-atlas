# Pr1m4lc0d3/deliberon-releases

⭐ 14 · PowerShell · 推送 2026-09-15 · [GitHub](https://github.com/Pr1m4lc0d3/deliberon-releases) · 个人维护

**Windows 桌面多智能体审议应用：组建 AI 理事会产出决策记录**

面向 Windows 10/11 的成品桌面应用（安装包交付，无源码、无 pip/Docker），由多个带角色分工的 AI 智能体组成"理事会"对用户提交的问题进行多轮审议：智能体独立立论后互相质证，含专属 Critic 对抗智能体、少数派异议保护与迎合检测，最终生成可导出 Markdown/HTML/PDF 的 Decision Record（含 ECDSA P-256 签名）。支持 25 个云/本地模型提供商（BYOK），可在应用内下载 GGUF 本地模型，提供无代码 Agent Designer、28 种审议模式、语音与头像生成及 MCP Server（200+ 工具）。分级一次性买断付费，Free 档可用 3 智能体。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多智能体多轮审议 + Critic 对抗与少数派异议保护，产出签名 Decision Record
- 25 个提供商 BYOK（云/本地混用），应用内直接下载 GGUF 本地模型
- 无代码 Agent Designer：自定义人设、角色原型、语音（VoxCPM2/克隆）与头像
- MCP Server 暴露 200+ 工具供 Claude Code 等编排器程序化驱动

## 适用场景

- 创业者在投入资源前用红队/可行性模式压测商业方案
- 内容创作者生成多人配音的播客、访谈与圆桌节目
- 团队获得留有完整论证与异议记录的可审计决策文档
- 把 Claude Code 等终端 agent 作为理事会成员参与审议

## 场景标签

`多智能体` `语音合成` · 领域:Agent 开发

## 证据(README 行号)

> L26: Deliberon convenes a **structured council of specialised AI agents** to deliberate on your question. Each agent has
> L33: 2. **The council deliberates** — agents form independent positions, then challenge each other across multiple round
> L37: 6. **You receive a Decision Record** — a structured document with the full deliberation history, exportable to Mark

## 星数曲线

```mermaid
xychart-beta
    title "Pr1m4lc0d3/deliberon-releases 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4632cb449d82` · [字段定义](../../DATASET.md)*
