# DinoMorphica/safeclaw

⭐ 22 · TypeScript · MIT · 推送 2026-02-19 · [GitHub](https://github.com/DinoMorphica/safeclaw) · [官网](https://safeclaw.io) · 个人维护

**OpenClaw AI agent 的安全管控面板：拦截、监控并控制其系统行为**

运行在 AI agent 与操作系统之间的防火墙式安全面板：以模式黑名单在执行前拦截危险 shell 命令（如 rm -rf、sudo），实时可视化 agent 会话时间线，内置 10 类威胁分析引擎与 200+ 模式及密钥扫描，并可开关 agent 对文件系统、网络、系统命令与 MCP 服务器的访问。面向在本地运行 OpenClaw agent 的开发者，通过 npx safeclaw 启动 Web 面板并自动连接运行中的 agent 实例；开发需 Node.js>=20 与 pnpm>=9。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模式黑名单在执行前拦截危险 shell 命令
- 10 类威胁分析引擎，200+ 模式与密钥扫描，含 OWASP 引用
- 按文件系统/网络/系统命令/MCP 服务器维度开关 agent 访问
- Socket.IO 实时更新的 Web 面板

## 适用场景

- 查看 agent 每次会话到底执行了哪些操作
- 阻止 agent 误删文件或提权执行危险命令
- 限制 agent 可访问的文件系统与网络范围

## 场景标签

`网络安全` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: **Security management dashboard for AI agents** — intercept, monitor, and control what AI agents can do on your syst
> L10: SafeClaw acts as a firewall between AI agents and your operating system. It monitors agent activity in real-time, i
> L16: - **Threat Detection** — 10-category threat analysis engine with 200+ patterns, secret scanning, and OWASP referenc

## 星数曲线

```mermaid
xychart-beta
    title "DinoMorphica/safeclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8e08afeea3ae` · [字段定义](../../DATASET.md)*
