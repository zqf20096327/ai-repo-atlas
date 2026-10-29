# jyjeanne/ditacraft

⭐ 19 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/jyjeanne/ditacraft) · [官网](https://marketplace.visualstudio.com/items?itemName=JeremyJeanne.ditacraft) · 个人维护

**VS Code 的 DITA 编辑发布扩展：可视化编辑、校验与 AI 辅助**

面向 DITA 技术文档作者的 Visual Studio Code 扩展：提供可视化编辑器（页面与 XML 并排、每次修改为最小文本编辑）、实时预览、LSP 语言服务（补全/悬停/重命名/43 条 DITA 规则校验的 13 阶段管线）、DITA 1.3 键空间解析、重构工具与 DITA-OT 一键发布。AI 为其中功能集：@ditacraft 聊天参与者、AI Quick Fix、AI 补全与地图重构，支持 Copilot/Anthropic/OpenAI/Ollama 级联；另含供外部 AI agent 使用的 MCP 服务器。诊断与界面提供英/法语本地化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可视化编辑器与 XML 双向同步，修改以最小文本编辑落盘
- 13 阶段校验管线：DTD + 可选 RelaxNG + 43 条 DITA 规则 + 自定义规则
- AI 功能（聊天参与者/AI Quick Fix/AI 补全/地图重构）支持 Copilot→Anthropic→OpenAI→Ollama 级联
- MCP 服务器供 opencode、Claude Desktop、Cursor、Continue 等外部 AI agent 接入

## 适用场景

- 在 VS Code 中可视化编写与校验 DITA 主题和地图
- 通过 AI 解释校验错误并生成修复建议
- 一键经 DITA-OT 发布 HTML5/PDF/EPUB 等格式
- 让外部 AI agent 通过 MCP 操作 DITA 工作区

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L10: DITA Craft is a comprehensive Visual Studio Code extension for editing and publishing DITA (Darwin Information Typi
> L112: 🤖 **AI-Powered Features** - `@ditacraft` chat participant, AI Quick Fix, AI Completion, map restructuring (Copilot
> L113: 🔌 **MCP Server** - Model Context Protocol server for external AI agents (opencode, Claude Desktop, Cursor, Continu

## 星数曲线

```mermaid
xychart-beta
    title "jyjeanne/ditacraft 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0d4e34c8d080` · [字段定义](../../DATASET.md)*
