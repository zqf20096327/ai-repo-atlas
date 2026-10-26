# GabrielOnDelphi/Autopilot-for-Delphi

⭐ 31 · Pascal · NOASSERTION · 推送 2026-10-13 · [GitHub](https://github.com/GabrielOnDelphi/Autopilot-for-Delphi) · [官网](https://www.gabrielmoraru.com/autopilot) · 个人维护

**让 AI 直接操作 Delphi 应用 GUI 的 MCP 工具服务器**

面向 Delphi 开发者的 MCP 服务器：AI 助手（Claude Code、Kai、Claude Desktop、Cursor、Cline）通过其 14 个 autopilot 前缀工具，对运行中的 VCL/FMX 应用进行点击、输入、读取控件状态与截图，实现无人在键盘前的 GUI 测试与调试。要求 Delphi 11/12/13，目标平台为 Windows 32/64 与 Android(FMX)。附带面向 AI 的 AI-INSTRUCTIONS.md 简报文件，复制到项目并在 CLAUDE.md 引用即可（可省略）。采用 SciVance Software License 2.3，每位开发者需购买席位（终身覆盖 2.x 版本，版本 3 需另购）。

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

- 提供 14 个 autopilot 前缀的 MCP 工具，供 AI 操作实时应用界面
- 支持点击、输入、读取控件状态、截图等无人工干预操作
- AI 可自行解析控件名称，用自然语言驱动应用测试
- 附带 AI-INSTRUCTIONS.md 提升 AI 驱动效率（可选）

## 适用场景

- 让 AI 代我启动应用、填表单、点按钮并报告结果
- 调试'某按钮无响应'之类的问题，让 AI 实际运行并定位原因
- 为 Delphi VCL/FMX 应用做自动化 GUI 测试

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L4: Through *Autopilot for Delphi* the AI can click, type, read state, and record screenshots of the live application/fo
> L12: - An AI assistant that speaks MCP: Claude Code, Kai, Claude Desktop, Cursor, Cline.
> L21: claude mcp add autopilot -- C:\Your\Path\McpServer\Autopilot.Mcp.exe

## 星数曲线

```mermaid
xychart-beta
    title "GabrielOnDelphi/Autopilot-for-Delphi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `06ac05527f69` · [字段定义](../../DATASET.md)*
