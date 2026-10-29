# j0hanz/filesystem-mcp

⭐ 26 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/j0hanz/filesystem-mcp) · [官网](https://github.com/j0hanz/filesystem-mcp#readme) · 个人维护

**给 AI 助手提供安全本地文件操作工具的 MCP 服务器**

运行在本机的 Model Context Protocol 服务器，向 Claude、Cursor、VS Code 等 MCP 客户端的 AI 提供 14 个文件工具：列出、按名/glob 查找、RE2 正则内容搜索、按行读取、diff 比较、创建/编辑/打补丁/批量替换/移动/删除及 undo。安全机制包括文件夹沙箱（含符号链接解析）、.env 与密钥等敏感文件默认屏蔽、删除或覆盖前需用户确认、--read-only 移除全部写工具、RE2 线性时间正则防挂起。支持 stdio 与 HTTP 传输，跨 macOS/Linux/Windows，无遥测。需 Node.js 24+，可通过 npx、npm 全局安装、Docker 或 Claude Desktop 一键扩展安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 个文件工具，含 grep 式 RE2 内容搜索、unified diff 应用与批量替换
- 文件夹沙箱与敏感文件（.env、密钥、云凭证）默认屏蔽
- 删除非空文件夹/覆盖文件前需用户确认，--read-only 可移除全部写工具
- 支持 stdio 与 HTTP 传输，可从自有代码作为客户端调用

## 适用场景

- 让 Claude/Cursor/VS Code 中的 AI 在指定项目文件夹内查找、读取、修改代码
- 以只读模式让 AI 安全检索本地文件
- 为自己的 agent、编辑器插件或 CI 脚本接入文件操作能力

## 场景标签

 · 领域:AI 工具接入/文件系统

## 证据(README 行号)

> L20: Filesystem MCP is an MCP server: a small program that runs on your computer
> L21: and gives the AI 14 tools for working with files. You choose which folders it
> L50: - It works with any MCP client, over stdio or HTTP, on macOS, Linux, and

## 星数曲线

```mermaid
xychart-beta
    title "j0hanz/filesystem-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-29 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `118f44c06909` · [字段定义](../../DATASET.md)*
