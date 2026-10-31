# nestchao/ai-studio-bridge

⭐ 14 · Python · MIT · 推送 2026-03-14 · [GitHub](https://github.com/nestchao/ai-studio-bridge) · 个人维护

**用 Playwright 把 Google AI Studio 网页封装成可编程 API 的 Python 库**

非官方、线程安全的 Python 库，通过 Playwright 驱动浏览器自动化操作 Google AI Studio 网页界面：发送 Gemini 提示词、上传文件并提取文本、查询/切换模型、设置 Thinking 级别，并以纯文本或 Markdown 返回结果。内部用专用工作线程与命令队列串行处理调用，适配 FastAPI/Flask 等后端集成。首次运行需手动登录 Google 账号，会话保存在本地 profile；依赖特定 CSS 选择器，Google 更新 UI 后需自行维护。

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

- 专用工作线程 + 命令队列，支持多调用串行排队
- 浏览器 stealth 配置与屏蔽重媒体资源加载
- 文件上传后自动等待处理并提取文本
- 可切换 Gemini 模型与 Thinking 级别（High/Low）

## 适用场景

- 在脚本或 Web 后端中调用 Gemini 而不使用官方 API
- 批量向 Gemini 发送提示词并获取结构化结果
- 通过 UI 上传 PDF 等文件并提取文本

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: An unofficial, thread-safe Python bridge for automating Google AI Studio using Playwright.
> L5: This library turns the Google AI Studio web interface into a programmable API. It is designed for developers who wan

## 星数曲线

```mermaid
xychart-beta
    title "nestchao/ai-studio-bridge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `20c0f049f0c4` · [字段定义](../../DATASET.md)*
