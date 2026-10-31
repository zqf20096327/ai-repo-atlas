# Dedeep007/browse_code

⭐ 21 · JavaScript · MIT · 推送 2026-08-04 · [GitHub](https://github.com/Dedeep007/browse_code) · 个人维护

**把网页版 AI 聊天变成本地自主编程代理的 CLI+浏览器扩展**

由本地 Python 服务器（bc 命令）与浏览器扩展组成：服务器通过安全本地 API 暴露文件系统与终端，扩展将代理工具注入 ChatGPT、Claude、Gemini、HuggingFace Chat 的网页界面，使网页版模型无需 API key 即可读取文件、正则搜索、行级编辑代码并执行终端命令（含后台进程监控），利用现有免费或订阅账户。安装方式为 pip 安装后运行 bc，首次运行引导加载浏览器扩展并以认证密钥配对。MIT 许可。

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

- 本地 Python 服务器 + 浏览器扩展双组件架构，无需 API key
- 工具集：view_dir/search_code/read_lines/replace/write/terminal_run/terminal_bg
- 支持 Chrome/Edge/Brave/Firefox 等浏览器的扩展加载
- 行级精确编辑以减少幻觉，附终端内 diff 显示

## 适用场景

- 用 ChatGPT/Claude/Gemini 网页版免费额度驱动本地编程代理
- 让网页 AI 直接在自己的工作区读写代码并运行命令
- 不想为 Devin/Cursor 等 API 计费工具付费的自主编程场景

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L35: 1. **A Local Python Server** (`bc`): Exposes your file system and terminal to the AI via a secure local API.
> L36: 2. **A Chrome Extension**: Injects agent capabilities and hidden tools directly into the AI chat interface, passing

## 星数曲线

```mermaid
xychart-beta
    title "Dedeep007/browse_code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e66bfc60fb12` · [字段定义](../../DATASET.md)*
