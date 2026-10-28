# karayaman/lichess-mcp

⭐ 19 · TypeScript · MIT · 推送 2026-10-12 · [GitHub](https://github.com/karayaman/lichess-mcp) · 个人维护

**让 Claude Desktop 用自然语言操作 Lichess 国际象棋平台的 MCP 服务器**

基于 Model Context Protocol 的服务器，把 Lichess 平台的能力以工具形式暴露给 Claude Desktop 等 MCP 客户端：账户管理、对局与挑战、棋局分析（PGN 导出）、锦标赛/战队、与其他棋手互动，并支持在聊天内打开可交互棋盘（MCP Apps 扩展，无 UI 客户端回退为 FEN/PGN/链接文本）。共约 190 个工具，按 toolset 组织，默认启用约 70 个核心工具以节省上下文，可用 LICHESS_TOOLSETS 环境变量或 enable_toolset 工具按需开启。通过 Lichess API token 鉴权，README 提供四种 token 传递方式并说明权限 scope 限制模型可执行的操作；经 Smithery 或 git clone + npm 手动安装。

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

- 约 190 个工具按 toolset 组织，默认启用约 70 个核心工具
- Claude Desktop 内嵌可交互棋盘（拖动走子、开局树浏览）
- 支持 UCI/SAN 着法格式与 FEN 局面表示
- token 可存放于 OS 密钥库（macOS Keychain / Linux libsecret / 1Password）

## 适用场景

- 在 Claude Desktop 里对弈、发起挑战和分析棋局
- 用自然语言管理 Lichess 账户、参加锦标赛与战队
- 把每日谜题作为交互求解器在聊天中打开

## 场景标签

 · 领域:棋类/AI 工具接入

## 证据(README 行号)

> L5: Speak to Lichess in natural language to interact with the chess platform. Use it with Claude Desktop to play games, 
> L7: Built using the Model Context Protocol.
> L117: The server has about 190 tools. Every enabled tool's description is sent to the model at the start of each session

## 星数曲线

```mermaid
xychart-beta
    title "karayaman/lichess-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-28 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `370a32fa6d8b` · [字段定义](../../DATASET.md)*
