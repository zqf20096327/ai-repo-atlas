# guguzea/MC-AI-Coding-Assistant-Tool

⭐ 20 · HTML · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/guguzea/MC-AI-Coding-Assistant-Tool) · 个人维护 · 中文 README

**为 AI 编程助手提供 Minecraft 模组开发全流程知识库与 MCP 工具包**

面向使用 Cursor / Claude Code 等 AI 编程助手的 Minecraft 模组开发者：提供覆盖 Forge/Fabric/NeoForge/Quilt/LiteLoader/Rift/ModLoader/基岩版/Paper/Spigot 的版本化规则树、文档检索数据（javadoc/javap 核实签名）与反模式知识库，通过 stdio MCP Server（89 个工具）接入宿主 IDE。机制上强调人在环：写盘、Gradle 构建、上传等高风险操作须用户确认；Agent 代劳决策须按五要素解释模板说明并给出可核对出处。还提供脚手架生成、崩溃分诊与两段式真机测试 loop（含进程内 playtest driver）。要求 Node.js >= 22.5。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- stdio MCP Server 含 89 个工具，文档检索/版本门禁/崩溃分诊/脚手架生成
- 多平台多版本规则树与构件级 API 签名核实表（javap 直读）
- 人在环机制：高风险操作须确认，代劳决策须按五要素解释模板并附出处
- 两段式模组真机测试 loop，支持进程内 driver 剧本测试与取证

## 适用场景

- 让 Cursor / Claude Code 等 AI 助手在正确的 MC 版本与 API 下写模组
- 查各加载器各版本的官方文档与已核实的 API 签名
- 让 Agent 代跑构建-启动游戏-读崩溃日志的迭代测试流程

## 场景标签

`代码生成` `编码 Agent` `知识库管理` · 领域:编码与开发

## 证据(README 行号)

> L10: 让 AI 编程助手（Cursor / Claude Code 等）能更好地编写 Minecraft 模组的完整工具包。
> L125: > 将 AUTO_SETUP.md 拖入当前 AI IDE / CLI。Agent 应识别宿主（Cursor / Claude Code / VS Code / Continue / Trae / OpenCode / Code
> L126: > 要求 **Node.js >= 22.5**（**22.5–22.12 与 23.0–23.3 必须加 `--experimental-sqlite` 启动**——内置 `node:sqlite` 在 22.13 / 23.

## 星数曲线

```mermaid
xychart-beta
    title "guguzea/MC-AI-Coding-Assistant-Tool 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-29 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `3be352779117` · [字段定义](../../DATASET.md)*
