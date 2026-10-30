# tanbro/uiautomator2-mcp-server

⭐ 54 · Python · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/tanbro/uiautomator2-mcp-server) · 个人维护 · 中文 README

**让 AI 通过 MCP 控制安卓设备的工具服务器**

基于 uiautomator2 与 fastmcp 的 MCP 服务器，向 Claude/GPT 等 AI 助手暴露 70+ 个安卓设备操作工具（点击、滑动、输入、应用管理、截图等），支持多设备连接、XPath 过滤 UI 元素以节省 token、按标签过滤工具。提供 STDIO 与 HTTP 两种运行模式，TOML/YAML/JSON 配置文件自动发现，内置 AI 驱动的 UI 测试框架。前置要求 Python 3.11+、adb 与开启 USB 调试的安卓设备；提供预编译二进制（Linux x64/macOS arm64/Windows x64），也可 uvx 直接运行或 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 70+ 安卓设备控制工具，支持多设备
- XPath 过滤 UI 元素与标签化工具过滤
- STDIO/HTTP 双运行模式，TOML/YAML/JSON 配置自动发现
- 可用 PyInstaller/Nuitka 打包为独立可执行文件

## 适用场景

- 用自然语言让 AI 助手操作安卓手机完成任务
- 通过对话式指令做安卓应用 UI 自动化测试
- 远程查看设备 UI 层级与截图进行调试

## 场景标签

`GUI 自动化` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L18: An MCP server that provides tools for controlling Android devices using uiautomator2.
> L69:     AI[AI Assistant<br/>Claude/GPT/etc.] --> MCP[MCP Protocol]
> L70:     MCP --> Server[u2mcp Server]

## 星数曲线

```mermaid
xychart-beta
    title "tanbro/uiautomator2-mcp-server 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29", "2026-10-30"]
    y-axis "stars" 51 --> 55
    line [52, 53, 54, 54]
```

2026-10-18 52 → 2026-10-30 54（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `c69b6688e7fe` · [字段定义](../../DATASET.md)*
