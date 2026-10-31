# Dicklesworthstone/source_to_prompt_tui

⭐ 23 · TypeScript · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/Dicklesworthstone/source_to_prompt_tui) · 个人维护

**把源码文件组合成 LLM 提示词的终端界面工具**

面向开发者交互式选取项目源码文件，生成结构化 XML 类标签的 LLM 提示词。功能包括带文件大小与行数的树状文件浏览器（vim 风格按键）、实时语法高亮预览、基于 tiktoken(cl100k_base) 的 token 计数与 API 成本估算、128K 上下文窗口用量条、预设保存/加载、JS/TS/CSS/HTML 代码压缩与多语言注释剥离、递归 .gitignore 支持。由 Bun 编译为单二进制分发，安装脚本提供 macOS/Linux/Windows 预编译产物，其他平台回退到源码构建（需 git + Bun）。

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

- 树状文件浏览器 + 实时语法预览的 TUI 选文件流程
- tiktoken(cl100k_base) 实时 token 计数、成本估算与 128K 上下文用量条
- XML 类结构化输出（preamble/goal/project_structure/files 元数据标签）
- Terser/csso/html-minifier 压缩与多语言注释剥离，可降低 30-50% token

## 适用场景

- 把项目代码上下文整理成结构化提示词发给 LLM
- 在发送前确认所选文件是否超出模型上下文窗口与预算
- 跨多次会话用预设复用同一批文件选择

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L8: A world-class terminal UI for combining source code files into LLM-ready prompts. Features a tree explorer with file
> L32: Modern AI-assisted development often requires sharing code context with large language models. But getting that con
> L52: - **Uses structured XML-like output** that LLMs parse reliably and consistently

## 星数曲线

```mermaid
xychart-beta
    title "Dicklesworthstone/source_to_prompt_tui 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-31 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `1a989dd07b55` · [字段定义](../../DATASET.md)*
