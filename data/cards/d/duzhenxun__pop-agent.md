# duzhenxun/pop-agent

⭐ 151 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/duzhenxun/pop-agent) · [官网](https://pop.xs25.cn/) · 个人维护 · 中文 README

**给本地编码 agent 提供可实时观察与中途介入的 Web UI**

本地运行的 Web 前端，将已安装的编码 agent（pi、Codex、Claude Code、opencode、DSH）的执行过程可视化：思考块、工具调用、变更文件、token 与费用流式展示，并支持回合中途插入纠正。不重建引擎、不用数据库与会话上云，直接读取引擎自身的 JSONL/threads 会话文件。带模板/快捷命令/Think 输入辅助、语音输入与 TTS、cron 定时任务、macOS 辅助功能层面的电脑控制、任务画布、Web Push 与带密码的远程访问。macOS 提供 .dmg，其他平台经 npm 或安装脚本。

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

- 流式展示 agent 思考块、工具调用与变更文件，支持回合中途纠正
- 每个引擎走各自原生循环（SDK/JSON-RPC/ACP），按能力矩阵隐藏不可用按钮
- 语音输入默认 macOS 本地识别，TTS 与事件提示音可离线
- 定时任务默认拒绝写操作，超出 watchdog 中断并记录为失败

## 适用场景

- 在浏览器里围观编码 agent 的推理与工具调用过程
- 手机上远程查看和继续本地 agent 会话
- 用 cron 让 agent 每天早晨自动检查仓库
- 把任务计划画成节点依赖图逐步推进

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L19: **What it is**: a front end that lays an agent's *process* open — thinking blocks, tool calls, changed files, token
> L21: **What it isn't**: not another agent engine, and not a SaaS that moves your sessions to the cloud. It doesn't rewri
> L97: |**pi** (default)|native SDK|full plugin / skill ecosystem, lazy tool loading, approval gate, subagents, **native s


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `457dc071033a` · [字段定义](../../DATASET.md)*
