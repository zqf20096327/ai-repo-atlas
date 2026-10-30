# xiaoxu123195/tool_forge

⭐ 65 · TypeScript · GPL-3.0 · 推送 2026-10-10 · [GitHub](https://github.com/xiaoxu123195/tool_forge) · [官网](https://github.com/xiaoxu123195/tool_forge/releases/latest) · 个人维护 · 中文 README

**给程序员的全本地桌面工具箱：46 工具含 AI 问答与用量洞察**

基于 Wails + Go + React + TypeScript 的跨平台桌面工具箱，内置 46 个工具、12 个分类，覆盖 AI 问答/翻译（支持 OpenAI/Anthropic/Gemini/OpenAI 兼容 4 套协议）、AI 用量看板、Claude/Codex 用量洞察、本机 AI 配置总览（Claude Code/Cline/Continue 等）、MCP 工作台，以及取证、编解码、加密、网络调试、真机投屏、磁盘清理等非 AI 工具。全本地运行，AI 调用走用户自配供应商，凭据存 OS Keychain。Windows 提供 Release 安装包，macOS 下载 Universal 包，Linux 需自行构建（Go 1.25+/Node 18+/Wails CLI）。GPL-3.0-or-later（v0.3.0 起，此前 MIT）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 46 个内置工具，12 分类组织，全本地处理
- AI Chat/翻译支持 OpenAI/Anthropic/Gemini/OpenAI 兼容 4 套协议
- AI 用量看板记录 token/时长，含模型/供应商占比
- 本机 AI 配置总览汇总 Claude Code/Codex/Cline/Continue 等家的 MCP、skills 与插件
- MCP 工作台按 schema 生成参数表单直接调用工具

## 适用场景

- 日常开发中查编解码、加密、HTTP 调试、正则等小工具
- 通过一个客户端使用多家 AI 供应商并查看 token 用量统计
- 检查本机 Claude Code/Codex 等 CLI 工具的 MCP 与插件配置状态
- 安卓/iOS 真机取证与投屏操作

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L24: - 🧰 **40+ 内置工具**：覆盖 AI / 编解码 / 加密 / 取证 / 网络 / 文本生成 / 系统等场景，还在持续增加
> L26: - 🤖 **完整的 AI 工作流**：内置 AI Chat（多轮对话、视觉、文件附件、思考折叠）+ AI 翻译，支持 OpenAI / Anthropic / Gemini / OpenAI 兼容 4 套协议
> L32: - ⚡ **轻量启动快**：Windows 版就一个不到 40MB 的 exe（adb 和投屏组件都已内置），常驻内存 < 150MB，远低于 Electron 同类

## 星数曲线

```mermaid
xychart-beta
    title "xiaoxu123195/tool_forge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-30 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `1d9b397acbac` · [字段定义](../../DATASET.md)*
