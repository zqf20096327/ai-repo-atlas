# tomlin7/biscuit

⭐ 266 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/tomlin7/biscuit) · [官网](https://biscuit.tomlin7.com) · 个人维护

**轻量原生 Python 代码编辑器，内置 AI 编程 agent**

基于 Tkinter 的原生代码编辑器，安装包体积 <20MB，通过 pip/uv 秒装即用。核心能力包括：接入 Gemini/Anthropic API 的规划型 agent（12 种文件/终端/搜索工具）、tree-sitter 代码高亮与补全、LSP 语言服务器（经扩展注册）、ripgrep 快速搜索、Git 分屏 diff 与基础操作、断点调试（内置 Python 调试器）、GUI 扩展管理与扩展市场。本地 LLM 的 ollama 扩展已弃用、重写中。系统需预装 Tkinter，Python 3.10+。面向偏好轻量工具的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 接入 Gemini/Anthropic API 的规划 agent，含 12 种文件/终端/搜索工具
- tree-sitter 解析、代码补全、符号导航与 LSP 扩展机制
- ripgrep 快速搜索、Git 分屏 diff、内置 Python 调试器
- GUI 扩展安装管理与扩展市场，<20MB 体积

## 适用场景

- 想要一个秒装轻量编辑器做日常编码
- 在编辑器内用 agent 读写文件、跑终端命令完成编程任务
- 通过扩展市场添加语言服务器、格式化器等能力

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L10: `biscuit` is a fast, extensible, native code editor with agents. lightweight <20 mb in size. install and start usin
> L45: - [x] gemini, anthropic API support (`claude-4-5-opus/sonnet/haiku`, `gemini-2-5-flash/pro`)

## 星数曲线

```mermaid
xychart-beta
    title "tomlin7/biscuit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 265 --> 267
    line [266, 266]
```

2026-10-18 266 → 2026-10-24 266（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a32c711c93c1` · [字段定义](../../DATASET.md)*
