# imprvhub/mcp-claude-spotify

⭐ 53 · TypeScript · MPL-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/imprvhub/mcp-claude-spotify) · 个人维护

**让 Claude Desktop 通过 MCP 操作 Spotify 的服务器**

面向 Claude Desktop 的 MCP 服务器，以 Node.js 子进程形式运行，通过 Spotify Web API 提供认证、搜索曲目/专辑/艺术家/歌单、播放控制、完整歌单管理（创建/更新/删除/排序/封面）以及热门曲目与最近播放读取等工具。采用 OAuth 回调认证（CSRF state 保护、token 文件仅属主可读、回调仅监听 loopback），支持 Smithery 一键安装或手动 git clone，可选 Windows/macOS/Linux 自启动脚本。需 Node.js 20+、Spotify API 凭据；get-recommendations 工具因 Spotify API 弃用已在 0.6.0 移除。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OAuth 认证含 CSRF state 保护与 loopback-only 回调
- 歌单全生命周期管理（创建/更新/删除/排序/封面上传）
- 支持 Smithery 自动安装或 git clone 手动安装
- 0.6.0 因 Spotify API 弃用移除 get-recommendations 工具

## 适用场景

- 在 Claude Desktop 中用对话控制 Spotify 播放与搜索
- 通过 Claude 管理歌单：增删曲目、排序、换封面
- 让 Claude 查看我的热门曲目与最近播放记录

## 场景标签

 · 领域:AI 工具集成/音乐服务

## 证据(README 行号)

> L10:  An integration that allows Claude Desktop to interact with Spotify using the Model Context Protocol (MCP).
> L213: The MCP server runs as a child process managed by Claude Desktop. When Claude is running, it automatically starts 

## 星数曲线

```mermaid
xychart-beta
    title "imprvhub/mcp-claude-spotify 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 51 --> 54
    line [52, 53, 53]
```

2026-10-18 52 → 2026-10-27 53（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a2597dc1a82c` · [字段定义](../../DATASET.md)*
