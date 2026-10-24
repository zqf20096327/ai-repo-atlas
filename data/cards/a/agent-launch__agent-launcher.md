# agent-launch/agent-launcher

⭐ 261 · TypeScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/agent-launch/agent-launcher) · 组织维护 · 中文 README

**桌面端工作台：统一配置并运行多种编码 agent CLI**

基于 Electron 的本地桌面应用，面向使用编码 agent CLI 的开发者：检测并链接系统已安装的 CLI（Claude Code、Codex CLI、OpenCode、Pi、Gemini CLI、Hermes Agent），缺失的一键安装，管理多 provider 配置（账号或 API），在嵌入终端或聊天视图中运行会话。读取各 CLI 自身的本地会话历史（JSONL/SQLite），支持 MCP server 与 Skills 查看、用量统计。限制：API key 以明文存储于 ~/.agent-launcher/config.json；未签名构建会触发系统警告。

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

- 检测并链接系统已装的 6 种编码 agent CLI，缺失可一键安装
- 每 agent 多 provider 配置档案，用最小模型请求预检端点与凭据
- 读取并恢复各 CLI 本地会话（JSONL/SQLite），含 MCP/Skills 查看与用量面板
- macOS DMG/ZIP、Windows NSIS、Linux AppImage 三平台发布

## 适用场景

- 在一个桌面应用里管理并切换多个编码 agent CLI
- 为不同 CLI 配置多套账号/API 档案并预检连通性
- 查看各 CLI 的本地会话历史与 token 用量

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L10: Agent Launcher is a local desktop workspace for coding-agent CLIs. It detects and links CLIs already installed on y
> L22: |Agent|CLI source|Configuration and runtime|

## 星数曲线

```mermaid
xychart-beta
    title "agent-launch/agent-launcher 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 260 --> 262
    line [261, 261]
```

2026-10-18 261 → 2026-10-24 261（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `cbf128fe7199` · [字段定义](../../DATASET.md)*
