# martian56/rook

⭐ 19 · Rust · MIT · 推送 2026-07-28 · [GitHub](https://github.com/martian56/rook) · 个人维护

**终端里的编码 agent：模型读写文件、跑命令改代码**

用 Raven 语言编写的终端编码代理，基于 plumage TUI 与 aviary 模型网关，可对接 OpenAI、Anthropic、Gemini、OpenRouter 等十余家提供商及任意 OpenAI 兼容端点（含本地模型）。模型可读文件、grep 搜索、编辑、多文件批量修改与运行命令；写改与命令需用户逐次或按轮批准，提示中直接展示 diff。支持后台 shell（最多 5 个，可调）、计划模式、任务清单、ask_user 决策、会话自动保存与上下文压缩，读取跨代理的 .agents 目录。提供 Windows/Linux 安装包、一键脚本与源码运行三种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型工具含 read/grep/multi_edit/run_command 与后台 shell 管理（read_shell/kill_shell）
- 所有变更需用户批准，提示内展示红绿 diff
- 通过 aviary 网关支持 20+ 提供商与任意 OpenAI 兼容 base_url
- 计划模式、任务清单、上下文自动压缩与会话恢复

## 适用场景

- 在终端让 AI 代理读取、修改并测试我的代码
- 让代理启动 dev server 并根据日志继续调整
- 在改动仓库前先让模型给出分步计划再执行

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L11: rook streams a real model's reply token by token, and the model can read,
> L15: aviary model gateway, so it speaks to
> L172: ## Tools

## 星数曲线

```mermaid
xychart-beta
    title "martian56/rook 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2ea843ddf16b` · [字段定义](../../DATASET.md)*
