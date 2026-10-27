# mits-pl/wove

⭐ 42 · Go · Apache-2.0 · 推送 2026-06-19 · [GitHub](https://github.com/mits-pl/wove) · 组织维护

**开源自带模型的 AI 编程 agent 桌面应用，本地直连各 AI 提供商**

基于 Wave Terminal（Go + Electron）的桌面 AI 编程 agent：用户以自己的 API key 直连 Anthropic、OpenAI、Google、MiniMax、xAI、Ollama、OpenRouter 或任意 OpenAI 兼容模型，一键切换。能力包括读写代码（读项目规范 WAVE.md/CLAUDE.md）、真实终端中执行命令与测试、CDP 视觉浏览器网页操作、任务拆分与子任务委派、自动发现 MCP 服务器；工具层强制 guardrails（read-before-edit、大文件保护、doom loop 检测等）。API key 存本地加密 keystore。当前提供 macOS DMG（Apple Silicon/Intel），Linux/Windows 构建未发布；源码构建需 Node.js 22、Go 1.25+、Task。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自带模型（BYOK）：直连 7 类提供商，一键切换，支持 OpenAI 兼容自定义端点
- 写码+终端执行+测试运行+CDP 视觉浏览器验证的闭环工作流
- 工具级 guardrails：read-before-edit、大文件保护、doom loop 检测、结构化压缩
- 自动发现 .mcp.json 中的 MCP 服务器，接入数据库 schema/文档/日志

## 适用场景

- 我用自己的 API key 让 AI agent 在本地读写项目代码并跑测试验证
- 在不同模型（含本地 Ollama）间按任务/成本切换，避免厂商锁定
- 让 agent 用内置浏览器测试 Web 应用、抓取文档或调试前端

## 场景标签

`编码 Agent` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: **Open-source AI coding agent. Desktop app. Bring your own model.**
> L9: Wove fixes this. It's a desktop app that connects directly to any AI provider with your own API key. It writes code,
> L33: **It actually does the work.** Wove doesn't just suggest code — it reads your project, writes files, runs tests, op

## 星数曲线

```mermaid
xychart-beta
    title "mits-pl/wove 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-27 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `30ba6cb005ed` · [字段定义](../../DATASET.md)*
