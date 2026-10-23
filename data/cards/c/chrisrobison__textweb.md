# chrisrobison/textweb

⭐ 103 · JavaScript · MIT · 推送 2026-03-10 · [GitHub](https://github.com/chrisrobison/textweb) · [官网](https://textweb.net) · 个人维护

**给 AI agent 的文本网格网页渲染器：以文本代替截图看网页**

面向 AI agent 的网页浏览工具：用真实 Chromium 执行 JS 与动态内容，将页面元素的位置、大小、文本与可交互性提取后映射为字符网格文本（约 2-5KB），交互元素以 [ref] 编号标注，LLM 可直接阅读网格并发出 click/type 等指令，无需视觉模型。提供 MCP Server（Claude Desktop/Cursor/Windsurf/Cline 等）、OpenAI/Anthropic 函数调用工具定义、LangChain/CrewAI 工具封装、HTTP API 与 Node.js 库。构建稳定 CSS 选择器策略，支持会话隔离与多步流程的等待/断言工具。另含一个早期的 manifest 驱动运行时 shell 原型。npm 全局安装，需 Playwright Chromium。

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

- 真实 Chromium 渲染后输出保留空间布局的文本网格（约 2-5KB），无需视觉模型
- 交互元素以 [ref] 编号标注，agent 可通过 click/type/select 指令操作
- 提供 MCP Server、函数调用工具定义、LangChain/CrewAI 工具、HTTP API 与 Node.js 库多种接入方式
- 稳定 CSS 选择器策略（id/data-testid/aria-label 等优先级）与 session_id 会话隔离、等待/断言工具

## 适用场景

- 让 AI agent 浏览网页并执行点击、输入等多步操作，替代截图+视觉模型方案
- 通过 MCP 给 Claude Desktop/Cursor 等客户端添加网页浏览能力
- 自动化多步网页流程（如 ATS 招聘系统表单填写）

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: **A text-grid web renderer for AI agents — see the web without screenshots.**
> L5: Instead of taking expensive screenshots and piping them through vision models, TextWeb renders web pages as structur
> L45: TextWeb works with any AI agent framework. Pick your integration:

## 星数曲线

```mermaid
xychart-beta
    title "chrisrobison/textweb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 102 --> 104
    line [103, 103]
```

2026-10-18 103 → 2026-10-23 103（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `a13cf0a42de4` · [字段定义](../../DATASET.md)*
