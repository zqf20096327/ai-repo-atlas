# lveillard/factorio-ai-companion

⭐ 14 · Lua · MIT · 推送 2026-09-13 · [GitHub](https://github.com/lveillard/factorio-ai-companion) · 个人维护

**Factorio 2.x 的 AI 伙伴模组：经 MCP 用自然语言驱动游戏内角色**

由 Factorio Lua 模组、TypeScript 网桥服务与 Web 面板组成：通过 RCON 连接游戏，暴露 51 个 RCON 命令与工具契约，内置 Codex app-server 用 ChatGPT 订阅驱动伙伴进行采矿、合成与建造；也可作为 MCP 服务器接入 Claude Code 或 Codex CLI 等自有 harness，以自然语言下达任务。世界观测为有界采样而非完整地图。需 Bun 1.4.2+ 与 Factorio 2.0.77+，启用 RCON 并主持多人游戏；支持 Docker 远程部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 Codex app-server 复用 ChatGPT 订阅，无需 API key
- 同一 MCP 端点可接入 Claude Code / Codex CLI 等自有 harness
- 51 个 RCON 命令与由配置文件生成的一致工具契约
- 提供 docker compose 远程部署与设备码登录

## 适用场景

- 在 Factorio 游戏或浏览器里与 AI 伙伴对话，让其采矿、合成、建造
- 通过 Claude Code 等既有 agent harness 用自然语言控制游戏角色
- 把 Factorio 作为 MCP 工具环境远程部署体验

## 场景标签

 · 领域:游戏/AI 工具

## 证据(README 行号)

> L45: **MCP:** `/mcp` uses Streamable HTTP with `Authorization: Bearer <COMPANION_ACCESS_TOKEN>`. Locally, an automatical
> L51: For **Claude Code**, keep the HTTP service running with `bun run start`, then run `bun run claude` from another ter
> L64: Set that environment variable to the service token before starting Codex. Codex uses its own ChatGPT login; no dash

## 星数曲线

```mermaid
xychart-beta
    title "lveillard/factorio-ai-companion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b63a6992021d` · [字段定义](../../DATASET.md)*
