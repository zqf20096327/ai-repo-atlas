# stixez/droid-mcp

⭐ 40 · Kotlin · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/stixez/droid-mcp) · [官网](https://stixez.github.io/droid-mcp/) · 个人维护

**Android SDK 与 MCP 服务器：让 LLM 调用手机 157 种工具**

面向 Android 开发者的 Kotlin 库，把日历、联系人、短信、文件、相机、传感器、通知与无障碍 UI 自动化等手机能力封装为 157 个模型可调用的 MCP 工具，分为 53 个独立模块按需引入。支持两种用法：应用内本地模型直接调用工具，或在手机上运行小型 HTTP 服务器，供 Claude Code、Cursor 等桌面 MCP 客户端经 Wi-Fi 连接。默认启用 Bearer 认证、Origin 校验、SSRF 防护、文件沙箱与只读模式等安全机制。要求 Android 9+（API 28），经 JitPack 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 157 个工具、53 个独立模块按需引入，各自声明权限
- 支持端内本地模型直调与手机 HTTP 服务器 + Streamable HTTP 两种方式
- MCP 协议 2025-11-25：typed results、resources、prompts、live list_changed
- 内置 Bearer 认证、SSRF 防护、文件沙箱、只读模式与危险调用确认机制

## 适用场景

- 让端侧 LLM 或桌面 MCP 客户端操作我的 Android 手机功能
- 构建能用自然语言查日历、读短信、做 UI 自动化的 AI 助手应用
- 按模块粒度控制权限与工具暴露范围

## 场景标签

`GUI 自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3:  An Android SDK and MCP server that lets an LLM use the phone.
> L14: droid-mcp turns Android phone capabilities into tools a language model can call, using the Model Context Protocol. 
> L16: - **On-device:** your app runs a local model and calls the tools directly. No server involved.

## 星数曲线

```mermaid
xychart-beta
    title "stixez/droid-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 38 --> 41
    line [39, 40, 40]
```

2026-10-18 39 → 2026-10-29 40（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3143f7d38df1` · [字段定义](../../DATASET.md)*
