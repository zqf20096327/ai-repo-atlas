# miunasu/Spore

⭐ 52 · Python · AGPL-3.0 · 推送 2026-09-04 · [GitHub](https://github.com/miunasu/Spore) · 个人维护 · 中文 README

**Windows 桌面 AI Agent：自然语言操作全机文件与系统，可停止/回滚**

面向 Windows 用户的人机交互 Agent 桌面应用：以自然语言下达任务，Agent 读取文件、运行 PowerShell、搜索网页、编辑文档；全程以平实语言记录每一步，可随时停止并从备份面板回滚任意文件改动。安全上采用系统提示约束加执行层后台安全代理（可疑暂停、恶意熔断、一键修复）。支持 Anthropic、OpenAI、DeepSeek 及 OpenAI 兼容端点，含主 Agent、前端 Agent、安全 Agent 多角色分工与多会话/子代理派发。提供安装包、CLI 模式与源码构建（限 Windows 10/11 x64，AGPL-3.0 附商业许可联系渠道）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个被 AI 修改的文件实时逐版本备份，可回滚任意版本或整体回退检查点
- 后台安全代理自动监控命令：可疑暂停询问、恶意熔断并一键修复
- HTML 产物拖入后由前端 Agent 实时理解用户点击/选中并继续修改页面
- GUI 配置所有设置（模型、API key、工具权限、安全策略），无需编辑配置文件

## 适用场景

- 用自然语言让 Agent 帮我整理文件、跑脚本、改文档
- 担心 AI 误操作系统时，依赖逐步日志与文件备份做回滚
- 生成可交互 HTML 学习页，边点边让 Agent 补充讲解与练习

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: AI agent for Windows. Runs on your machine, touches your real files and system, and lets you stop or undo anything i
> L11: Give it a task in plain text. It reads files, runs PowerShell, searches the web, edits documents. The left panel sh
> L63: Works with Anthropic, OpenAI, DeepSeek, and any OpenAI-compatible endpoint. Minimal `.env` for running from source:

## 星数曲线

```mermaid
xychart-beta
    title "miunasu/Spore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-30 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0fe6dcd1e9ca` · [字段定义](../../DATASET.md)*
