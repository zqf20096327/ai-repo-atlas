# CarlosCaPe/octorato

⭐ 18 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/CarlosCaPe/octorato) · [官网](https://www.dataqbs.com/octorato) · 个人维护

**给 AI 编程助手提供持久记忆与规则约束的纯文本 Agent OS**

一个由纯文本文件组成的开源文件夹（~/.claude），为 Claude Code 和 Cursor 等 AI 编程助手提供跨会话记忆、house rules、按客户隔离的密封文件夹（arm）以及每次运行的回执（provenance footer）。内含 240+ 技能指南与 160+ 角色卡，每条规则绑定由 hook 执行的自动检查；v8 内核为每次运行提供身份、日志与步数/时长上限，v9 引入由第二助手判定完成度的裁决机制。安装为 git clone 后运行一条 quickstart 命令，无需写代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯文本规则/技能/角色卡文件夹，AI 助手每次启动读取
- 每条规则绑定 hook 自动检查，无检查的规则不计入
- 按客户隔离的密封 arm 文件夹与推送到回执机制
- v8 内核提供运行身份、追加日志与步数/分钟上限

## 适用场景

- 多项目/多客户工作者让 AI 助手跨会话记住偏好与禁令
- 按客户隔离工作内容，防止信息串漏
- 记录每次运行的依据、改动与验证方式并控制成本

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: Free and open source (MIT). Runs on Claude Code and Cursor today. No code to write to start using it.
> L19: - **What it is.** A folder (`~/.claude`) of rules, how-to guides and role descriptions, all plain text. Your AI ass
> L87: |Hook|An automatic check that runs before or after the assistant acts. It can refuse the action.|

## 星数曲线

```mermaid
xychart-beta
    title "CarlosCaPe/octorato 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `0df051b80def` · [字段定义](../../DATASET.md)*
