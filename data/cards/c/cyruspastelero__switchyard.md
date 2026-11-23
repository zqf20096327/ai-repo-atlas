# cyruspastelero/switchyard

⭐ 11 · TypeScript · Apache-2.0 · 推送 2026-11-21 · [GitHub](https://github.com/cyruspastelero/switchyard) · 个人维护

**多 Claude Code agent 的实时监控面板：状态、成本、指令注入**

一个面向 Claude Code 多 agent 工作流的 Web 监控面板：通过向 Claude Code 写入 hooks（PreToolUse/PostToolUse/Stop）采集 agent 活动，在浏览器仪表盘中实时展示每个 agent 的状态、工具调用、diff 统计与文件改动；从 JSONL 会话日志读取 token 用量并按模型定价计算 API 成本；提供任务板、反模式告警（STUCK/LOOP/SPIRAL/ERRORS/MARATHON）与手机端（同 WiFi）查看。限制：指令通过 hook 在下次工具调用时才送达，且仅支持 Claude Code。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 Claude Code hooks 实时采集每个 agent 的工具调用与状态
- 读取 JSONL 会话日志计算真实 token 成本与模型级费用分解
- 向运行中的 agent 注入指令（stderr 送达，下次工具调用生效）
- STUCK/LOOP/SPIRAL 等反模式检测与浏览器桌面通知

## 适用场景

- 同时运行多个 Claude Code agent 时在一个页面监控全部状态
- 查看团队/个人 agent 的 API 成本与上下文窗口健康度
- 发现卡住或循环改文件的 agent 并从仪表盘/手机发指令干预

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L26: **Mission Control** gives you a real-time command center for all your Claude Code agents. One browser tab. Every ag
> L59: And it's **2 dependencies** (`better-sqlite3` + `ws`). No React. No build step. One command to start.
> L89: This adds hooks to `~/.claude/settings.json` so Claude Code reports activity to Mission Control. You only need to d


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `963b9d92581a` · [字段定义](../../DATASET.md)*
