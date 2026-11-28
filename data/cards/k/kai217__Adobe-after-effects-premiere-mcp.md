# kai217/Adobe-after-effects-premiere-mcp

⭐ 3 · JavaScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/kai217/Adobe-after-effects-premiere-mcp) · 个人维护

**让 Claude/ChatGPT 通过自然语言控制 After Effects、Premiere 与 Illustrator 的 MCP server**

一个本地 MCP server，把正在运行的 Adobe After Effects、Premiere Pro 和 Illustrator 接入 Claude 或 ChatGPT 桌面客户端：AI 请求经文件队列与两座桥（CEP+ExtendScript、Premiere 的 UXP 插件）下发到应用内执行，生成可撤销、可编辑的 comp/图层/剪辑。提供约数十个工具（ae_/pr_/il_/uxp_/media_/kai_ 系列）覆盖时间线、字幕、调色、MOGRT、矢量绘制与转录；面板内可实时查看步骤并批准/拒绝高风险操作，编辑带 expected_project 保护与 JSONL 日志。仅 Windows 实测，macOS 路径未验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 CEP/ExtendScript 与 Premiere UXP 双桥同时驱动三个 Adobe 应用
- KAI MCP Bridge 面板实时展示 AI 计划与步骤，含 Proceed/Deny 审批按钮
- expected_project 校验与一键命名 Undo 防止误改项目
- 面板内置 Chat 模式，用本机 Claude Code 登录态运行，无需 API key

## 适用场景

- 用自然语言在 Premiere 里完成粗剪、字幕与调色
- 让 Claude 生成可编辑的 AE 动态图形工程而非成品视频
- 从 Illustrator 图稿一键转到 AE comp 再进 Premiere 序列

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L4: Lets Claude or ChatGPT work inside your running **After Effects, Premiere Pro and Illustrator** in the background (n
> L6: One server, three apps, two bridges: ExtendScript through the CEP bridge (every app) and modern **UXP** for Premiere
> L28: Other MCP clients (Cursor, VS Code, Claude Code...): point them at `node <install folder>\server.js` over stdio.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 low · 依据 README sha `bf7143028186` · [字段定义](../../DATASET.md)*
