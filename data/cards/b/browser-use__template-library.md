# browser-use/template-library

⭐ 25 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/browser-use/template-library) · 组织维护

**browser-use CLI 的项目模板集合，供 init 命令加载**

browser-use 官方模板库：以 templates.json 作为模板注册表，记录每个模板的文件、描述、安装后步骤与作者信息，由主仓库以 git submodule 引入，通过 `browser-use init --template` 命令加载生成项目（如 shopping、job-application、agentmail 等）。另含 Browser Use Cloud 启动示例（Playwright/Puppeteer over CDP、v4 agent API 等）。面向为浏览器自动化 agent 编写与贡献模板的开发者，文档规定模板结构、featured 标记、AGENTS.md 约定与贡献清单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- templates.json 注册表定义模板文件、next_steps、featured 等字段
- 由 browser-use CLI 的 init 命令按模板名加载（uvx browser-use init --template）
- cloud-starters 目录含 Browser Use Cloud 运行示例（CDP、并行浏览器、TOTP 登录等）
- 每个模板附带 AGENTS.md，供 Codex、Cursor 等编码 agent 读取运行说明

## 适用场景

- 用现成模板快速初始化浏览器自动化 agent 项目
- 为 Browser Use Cloud 编写并测试 CDP/agent 示例
- 向模板库贡献自定义模板并按 checklist 自查

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: Template collection for the `browser-use` CLI init command.
> L18: This repository is used as a git submodule by the main browser-use repository.

## 星数曲线

```mermaid
xychart-beta
    title "browser-use/template-library 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c13b39d42e19` · [字段定义](../../DATASET.md)*
