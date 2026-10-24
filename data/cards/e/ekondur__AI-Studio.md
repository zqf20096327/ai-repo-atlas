# ekondur/AI-Studio

⭐ 52 · C# · MIT · 推送 2026-09-18 · [GitHub](https://github.com/ekondur/AI-Studio) · [官网](https://marketplace.visualstudio.com/items?itemName=ekondur.AI-Studio) · 个人维护

**Visual Studio 扩展：右键调用 AI 完成生成、重构、注释与单元测试**

面向 Visual Studio 2022/2026 的 VSIX 扩展，通过编辑器右键菜单提供 8 个 AI 命令：Code It 生成实现、加注释、生成 XML 摘要、重构、解释、安全检查、生成单元测试（支持 xUnit/NUnit/MSTest 定制）与新对话。支持 OpenAI、Azure AI、Anthropic Claude 与 Ollama（本地或云端）四个内置 provider，也可指向任意 OpenAI 兼容端点；回复先在 Chat 窗口预览，经 diff 确认后才写回文件。从 Marketplace 安装或源码构建 VSIX。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 右键菜单 8 个 AI 命令：生成代码/注释/摘要/重构/解释/安全检查/单元测试/新对话
- 内置 OpenAI、Azure AI、Anthropic、Ollama 四个 provider，可切换
- 支持任意 OpenAI 兼容自托管端点
- 单元测试生成可配置测试框架、命名规则与 mock 偏好

## 适用场景

- 在 Visual Studio 内右键为方法生成单元测试或 XML 文档注释
- 让 AI 重构选中代码并经 diff 预览后应用
- 用本地 Ollama 模型在 IDE 内做代码解释与安全检查

## 场景标签

`代码生成` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: AI Studio is a Visual Studio 2022, 2026 extension that adds AI-assisted code generation, refactoring, documentation,
> L17: - Supports **OpenAI**, **Azure AI**, **Anthropic (Claude)**, and **Ollama** (local or cloud) — switch provider from

## 星数曲线

```mermaid
xychart-beta
    title "ekondur/AI-Studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-24 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6962f43df799` · [字段定义](../../DATASET.md)*
