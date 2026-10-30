# civyk-official/civyk-winwright

⭐ 20 · PowerShell · NOASSERTION · 推送 2026-07-31 · [GitHub](https://github.com/civyk-official/civyk-winwright) · [官网](https://github.com/civyk-official/civyk-winwright) · 组织维护

**给 AI agent 的 Windows 自动化 MCP 工具服务器**

面向 Model Context Protocol 的 Windows 自动化工具服务器：提供 52 个工具，覆盖桌面（WPF/WinForms/Win32，基于 UIA）、系统管理（进程/注册表/服务等）与 Chrome/Edge 浏览器（CDP），供 AI agent 调用；MCP 被封锁时可用 CLI 模式驱动。支持录制 AI 会话为 JSON 脚本后脱离 AI 确定性回放，并提供选择器自愈。仅限 Windows 10/11，以自包含单二进制分发，无需 .NET 运行时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 52 个 MCP 工具：桌面 33、系统 8、AI agent 辅助 7、浏览器 4
- AI 会话可录制为 JSON 脚本，CI 中无 AI 确定性回放
- CLI 模式（winwright call）在 MCP 被封锁环境下可用
- 运行时权限防护、AD 组覆盖与 JSONL 审计日志

## 适用场景

- QA 工程师用自然语言让 AI 生成并回放 WinForms/WPF UI 测试
- 让 AI agent 操控桌面完成跨应用表单填写与数据搬运
- 从无 API 的遗留企业应用中通过 UI Automation 抽取数据

## 场景标签

`GUI 自动化` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L8: Windows automation server for the Model Context Protocol.
> L260: WinWright is not an RPA platform. It's a tool server that gives AI agents access to Windows.

## 星数曲线

```mermaid
xychart-beta
    title "civyk-official/civyk-winwright 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `6fa93b48b9fc` · [字段定义](../../DATASET.md)*
