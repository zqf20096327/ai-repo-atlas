# claude-did-this/MCPControl

⭐ 331 · TypeScript · MIT · 推送 2025-12-02 · [GitHub](https://github.com/claude-did-this/MCPControl) · 组织维护

**Windows 自动化 MCP 服务器：让 AI 模型控制鼠标键盘与屏幕**

基于 Model Context Protocol 的 Windows 控制服务器，为 AI 模型（如 Claude 客户端）提供对系统的程序化控制：鼠标移动点击、键盘输入与组合键、窗口管理（列出/聚焦/调整）、屏幕截图与剪贴板操作。通过 npm 全局安装，支持 SSE 传输（默认端口 3232）与 HTTPS/TLS。提供 keysender（默认）、PowerShell、AutoHotkey v2 三种自动化后端，可按操作类型混配。仅支持 Windows；安装需要 VC++ Build Tools、Python 与 Node.js 以编译原生模块；官方建议在 1280x720 分辨率的虚拟机中运行以获得点击精度。README 声明该软件为实验性质，存在 AI 直接控制计算机的风险。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 鼠标/键盘/窗口管理/屏幕截图/剪贴板五类控制工具
- SSE 传输（默认 3232 端口）与 HTTPS/TLS 支持，可远程部署
- 三种自动化后端（keysender/PowerShell/AutoHotkey v2），可按操作混配
- npm 全局安装，配置到 Claude 类 MCP 客户端使用

## 适用场景

- 让 Claude 在虚拟机中代为操作桌面完成 UI 测试或表单填写
- 跨应用工作流自动化与演示录制
- 测试 AI 的视觉推理与界面导航能力

## 场景标签

`GUI 自动化` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: Windows control server for the Model Context Protocol, providing programmatic control over system operations includi
> L276: - @modelcontextprotocol/sdk - MCP SDK for protocol implementation

## 星数曲线

```mermaid
xychart-beta
    title "claude-did-this/MCPControl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 330 --> 332
    line [331, 331]
```

2026-10-18 331 → 2026-10-24 331（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c0f513c3ddcd` · [字段定义](../../DATASET.md)*
