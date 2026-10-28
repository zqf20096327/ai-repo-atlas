# Arcadi4/balatro-agent

⭐ 21 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/Arcadi4/balatro-agent) · [官网](https://www.nexusmods.com/balatro/mods/927) · 个人维护 · 中文 README

**让 MCP AI 代理直接游玩 Balatro 的游戏模组与服务器**

Balatro 游戏模组（依赖 Lovely Injector 与 Steamodded）加原生 MCP 服务器：将运行中游戏的实时状态、Balatro Wiki 查询暴露为 MCP 资源，并提供选盲注、出牌弃牌、购买小丑牌、开启新一局等文本工具调用，使任意 MCP 兼容客户端（Claude Code、Cursor 等）的 AI 代理可完整游玩游戏，无需屏幕截图或视觉模型。安装方式含 Nexus Mods / GitHub Releases 解压到 Mods 目录，或 npx -y balatro-mcp 启动服务器。README 声明 v1.1 游戏发布后的版本不保证兼容 v1.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 MCP 工具调用读取实时状态并执行盲注、出牌、商店购买等操作
- 无需屏幕截图或视觉模型，纯文本工具调用
- 实时状态与 Balatro Wiki 以 MCP 资源形式暴露
- 支持 --no-auto-context 模式适配代码型客户端（Codex/OpenCode 等）

## 适用场景

- 让 Claude Code、Cursor 等 MCP 客户端里的 AI 代理替我打 Balatro
- 研究 AI 代理在卡牌构筑游戏中的决策表现
- 通过自然语言指令开启指定卡组与难度的游戏对局

## 场景标签

 · 领域:游戏/AI agent 工具

## 证据(README 行号)

> L7: Let an AI agent play Balatro. Balatro Agent connects any MCP-compatible AI client to a running game. The agent can r
> L52:   "mcpServers": {

## 星数曲线

```mermaid
xychart-beta
    title "Arcadi4/balatro-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `606ccd68e15f` · [字段定义](../../DATASET.md)*
