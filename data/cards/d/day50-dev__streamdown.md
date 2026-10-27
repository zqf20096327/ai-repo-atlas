# day50-dev/streamdown

⭐ 363 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/day50-dev/streamdown) · [官网](https://day50.dev) · 组织维护

**终端实时流式 Markdown 渲染库与 CLI，面向 LLM 输出**

以 Python 库与 sd CLI 双形态提供的终端 Markdown 渲染器：支持管道与文件参数、--exec 包装交互式程序（如 llm chat）并保留 readline/方向键操作，针对 LLM 流式输出做实时渲染。支持图片、OSC 8 超链接、OSC 52 剪贴板、CJK 换行、pygments 语法高亮、HSV 调色与 TOML 配置，并带插件系统扩展解析器与渲染器（如 LaTeX 插件）。属 DAY50 AI 工具套件，可与 sidechat 等终端会话工具配合保存/插入代码块。通过 uv tool/pipx/pip/uv 或源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 流式实时渲染，支持管道、文件参数与 --exec 交互式包装
- 图片渲染、OSC 8 超链接、OSC 52 剪贴板与 CJK 排版
- TOML 配置 HSV 调色、PrettyPad/PrettyBroken 等样式选项
- 插件系统可扩展解析器与渲染器（如 LaTeX 表格内数学渲染）

## 适用场景

- 在终端实时查看 LLM 流式输出的 Markdown
- 包装 CLI LLM 工具（如 sd --exec "llm chat"）保留交互操作
- 作为 Python 库嵌入自己的终端渲染流程

## 场景标签

 · 领域:开发者工具/终端渲染

## 证据(README 行号)

> L6: The solution: Streamdown, part of the DAY50 suite of open-source tools for AI workflows, is designed for the wide va
> L10: As both a fast standards-compliant library and a powerful CLI, streamdown supports standard piping and files as arg
> L127: $ sd --exec "llm chat"

## 星数曲线

```mermaid
xychart-beta
    title "day50-dev/streamdown 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 362 --> 365
    line [364, 363, 363]
```

2026-10-18 364 → 2026-10-27 363（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `91c3034f9b91` · [字段定义](../../DATASET.md)*
