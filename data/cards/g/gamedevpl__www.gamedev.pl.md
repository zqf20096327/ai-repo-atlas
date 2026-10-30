# gamedevpl/www.gamedev.pl

⭐ 15 · TypeScript · GPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/gamedevpl/www.gamedev.pl) · [官网](https://www.gamedev.pl) · 组织维护

**AI agent 构建浏览器游戏并发布目录的开放平台**

gamedev.pl 的开源平台代码：用户写下几句话的游戏描述，平台托管构建器或经 MCP 接入自有编码 agent（Cursor、Claude Code、Codex 等），由 agent 生成真实代码并经 QA 门禁、人类审核后发布到游戏仓库，在浏览器中游玩，部分游戏支持手机当手柄。平台大部分代码也由编码 agent 编写。提供远程 MCP 端点与 gamedevpl CLI；本地可用 npm run dev 运行（Node.js ≥20.19），但无云端密钥时提交仅排队。游戏创建功能处于封闭测试，需申请创作者账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 远程 MCP 服务器，Claude 可作为插件安装（pl.gamedev/creator）
- QA 门禁先提问澄清再生成代码，CI 从源码派生验证触屏可玩性
- 游戏在无 allow-same-origin 的沙箱 iframe 中运行，隔离 cookies 与认证端点
- gamedevpl CLI（REPL 模式，无本地模型）与五分钟本地开发流程

## 适用场景

- 用自然语言描述游戏并由自己的 Cursor/Claude Code agent 构建
- 在浏览器游玩 agent 生成的多人游戏，用手机作手柄
- 研究 agent 驱动的软件交付流水线与 MCP 工具设计

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L15: can hand the brief to the platform builder or connect your own coding agent over MCP. The
> L54: **MCP.** The server is remote and needs no install: point an MCP-capable client at
> L60: The tools cover one build round: opening or rejoining it, reading the brief and the engine

## 星数曲线

```mermaid
xychart-beta
    title "gamedevpl/www.gamedev.pl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `808c4c72ffa6` · [字段定义](../../DATASET.md)*
