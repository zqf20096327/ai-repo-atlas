# a4webdev/tiacommander-mcp

⭐ 50 · NOASSERTION · 推送 2026-09-07 · [GitHub](https://github.com/a4webdev/tiacommander-mcp) · [官网](https://tiacommander.com/) · 组织维护

**连接 MCP AI 助手与西门子 TIA Portal 的 MCP 服务器**

基于 .NET Framework 4.8 的 MCP 服务器（stdio 协议），通过西门子 Openness API 将 MCP 兼容的 AI 客户端接入 TIA Portal V17–V20，支持 SCL/LAD/FBD/STL 块的创建导入导出、硬件与网络配置、报警文本 XLSX 导入导出、交叉引用分析、编译与 PLC 下载上传等 19 个工具共 230 个动作，面向使用 S7-1200/1500 的自动化工程师。以便携 zip 与 Claude Desktop 的 .mcpb 扩展包形式分发，需本机已安装并启用 Openness 组件的 TIA Portal。许可证为专有（免费 beta）；仅 V19 经过完整测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 19 个工具、230 个动作覆盖 TIA Portal 项目全生命周期
- 支持 Claude Desktop/Claude Code/VS Code Copilot/Cursor/Windsurf/Codex CLI/Gemini CLI 客户端
- 便携 zip 分发，无安装器、无注册表改动；另有 .mcpb 扩展包安装方式
- 新增 technology_objects 工具：15 个技术对象读写/参数/导入导出动作

## 适用场景

- 通过自然语言让 AI 助手完成 PLC 块编写、编译与部署
- 在 AI 客户端中做硬件配置、报警文本与交叉引用分析
- 读取运行中控制器的实时值与 CPU 诊断

## 场景标签

 · 领域:工业自动化/PLC 工程

## 证据(README 行号)

> L17: TiaCommander is an MCP server that connects AI assistants to Siemens TIA Portal via the Openness API. It enables AI
> L19: **Tested AI clients:** Claude Desktop, Claude Code, VS Code (Copilot), Cursor, Windsurf, Codex CLI, Gemini CLI.

## 星数曲线

```mermaid
xychart-beta
    title "a4webdev/tiacommander-mcp 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25", "2026-10-27"]
    y-axis "stars" 47 --> 51
    line [48, 49, 50, 50]
```

2026-10-18 48 → 2026-10-27 50（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `344af434c489` · [字段定义](../../DATASET.md)*
