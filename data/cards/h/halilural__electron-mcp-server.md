# halilural/electron-mcp-server

⭐ 71 · TypeScript · MIT · 推送 2026-08-06 · [GitHub](https://github.com/halilural/electron-mcp-server) · [官网](https://www.npmjs.com/package/electron-mcp-server) · 个人维护

**让 AI 助手通过 CDP 自动化操控 Electron 应用的 MCP 服务器**

面向 AI 助手（Claude、Cursor、VS Code 等）的 MCP 服务器，通过 Chrome DevTools Protocol 连接任意 Electron 应用（需 --remote-debugging-port=9222），无需修改应用代码。提供 7 个工具：启动/关闭/构建应用、获取窗口信息、截图、发送 UI 交互与 eval 命令（click_by_text、fill_input、get_page_structure 等）、读取主进程/渲染进程/控制台日志。内置 strict/balanced/permissive/development 四级安全级别，默认阻止 eval、文件系统访问与网络请求。以 npm 包形式分发。

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

- 通过 CDP 连接任意 Electron 应用，零应用改动
- 提供点击、填表、键盘快捷键、get_page_structure 等 UI 交互命令
- 四级安全级别控制 UI 交互/DOM 查询/函数调用权限
- 支持启动、关闭、构建 Electron 应用与实时日志流读取

## 适用场景

- 让 AI 助手用自然语言操控我的 Electron 应用做 UI 自动化
- 把手工测试步骤转为 AI 执行的 E2E 测试流程
- 在聊天中直接查看 Electron 应用的控制台日志与页面结构进行调试

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L11: **Control any Electron app with natural language.** An MCP server that lets AI assistants (Claude, Cursor, VS Code,
> L28: **The 4 tools it exposes:** `get_electron_window_info`, `take_screenshot`, `send_command_to_electron` (UI interacti

## 星数曲线

```mermaid
xychart-beta
    title "halilural/electron-mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 69 --> 72
    line [70, 71, 71]
```

2026-10-18 70 → 2026-10-30 71（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `186ea6da47b4` · [字段定义](../../DATASET.md)*
