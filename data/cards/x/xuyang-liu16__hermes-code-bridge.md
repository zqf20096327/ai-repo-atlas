# xuyang-liu16/hermes-code-bridge

⭐ 41 · Python · MIT · 推送 2026-07-22 · [GitHub](https://github.com/xuyang-liu16/hermes-code-bridge) · 个人维护 · 中文 README

**让 Hermes Agent 调度本地编码 CLI（Codex/Claude Code 等）的插件与技能**

Hermes Agent 的插件+技能（SKILL.md），把 Hermes 变成本地编码代理的调度层：用户向 Hermes 发一条请求，它按请求路由到 Codex、Kimi Code、Claude Code、OpenCode、Gemini CLI 等已安装的本地 CLI，并复用既有会话、分发结构化提示词、监控后台任务、核验 git diff 与测试输出后汇报命令、改动、失败与风险。支持 tmux 会话与 CCB 桥接作为后端。以 hermes plugins install 一行命令或单独安装 SKILL.md 两种方式提供，MIT 许可。

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

- 按用户指名调用真实的本地 CLI（指定 Codex 就运行 Codex）
- 会话优先路由：按仓库目录、会话 ID、角色与历史匹配既有会话
- 证据核验流程：git diff/status、原始测试输出、远程回读状态
- 支持 Codex、Kimi Code、Claude Code、OpenCode、Gemini CLI、tmux 与 CCB 后端

## 适用场景

- 让一个实现代理编码、另一个代理只读评审的循环
- 把模糊需求转成带成功标准与测试命令的结构化代理任务
- 离开工位前下发任务，回来后查看各代理的命令、改动与风险汇总

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L17: ### Turn Hermes Agent into a command center for Codex, Kimi Code, Claude Code, OpenCode, Gemini CLI, and other loca
> L19: Stop copy-pasting prompts between terminals. Give Hermes one request; it can route the work to Codex, Kimi Code, Cl

## 星数曲线

```mermaid
xychart-beta
    title "xuyang-liu16/hermes-code-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-26 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8f9ce754ad9e` · [字段定义](../../DATASET.md)*
