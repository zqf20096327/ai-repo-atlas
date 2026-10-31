# Leanmcp-Community/music-composer-webmcp

⭐ 45 · TypeScript · 推送 2026-03-25 · [GitHub](https://github.com/Leanmcp-Community/music-composer-webmcp) · [官网](https://music.leanmcp.live) · 组织维护

**WebMCP 协议演示：AI agent 通过工具调用操作网页音乐音序器**

一个用于演示 WebMCP 协议（待定标准）的功能性示例项目：网页音频音序器将自身能力以工具形式注册到浏览器或连接的 AI agent，agent 通过 WebMCP 工具调用自主编排音序器完成复杂工作流。面向关注 agent 与浏览器上下文交互的开发者与体验者。本地运行需要 Node.js、Google Chrome Canary（需在 chrome://flags 启用 WebMCP 实验特性，否则走 polyfill）以及 LeanMCP API Token 和账户额度；通过 npm 安装依赖并以 Vite 开发服务器运行，另有在线 demo。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 网页音序器将 UI 能力暴露为 WebMCP 工具供 LLM 调用
- agent 通过工具调用自主完成音序器编排工作流
- Chrome Canary 原生 WebMCP 支持，不满足时回退 polyfill
- 提供免费在线 demo 与本地 Vite 运行路径

## 适用场景

- 体验 AI agent 通过 WebMCP 协议操作浏览器内应用
- 了解 Web 应用向 agent 注册工具的协议机制
- 作为 WebMCP 协议开发的参考示例

## 场景标签

 · 领域:AI agent/浏览器协议演示

## 证据(README 行号)

> L3: This project is a functional demonstration of the WebMCP Protocol, illustrating how AI agents can interact with loca
> L10: WebMCP (Web Model Context Protocol) is PENDING standard allowing web applications to register "tools" directly with
> L53: 4. Use the interface to initiate an agent run. You'll observe the underlying WebMCP runtime expose the UI's capabil

## 星数曲线

```mermaid
xychart-beta
    title "Leanmcp-Community/music-composer-webmcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-31 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4bddc0fb3d46` · [字段定义](../../DATASET.md)*
