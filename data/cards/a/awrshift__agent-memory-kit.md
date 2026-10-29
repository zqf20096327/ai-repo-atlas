# awrshift/agent-memory-kit

⭐ 34 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/awrshift/agent-memory-kit) · 个人维护

**给 Claude Code 加显式确认记忆的插件：代理提议、你批准、逐行带日期**

Claude Code 插件，为编码代理提供基于纯文本文件的记忆系统：代理在 MEMORY.md 中写入带日期的单行事实并告知用户，任何内容在用户批准前不会成为规则或知识条目；会话结束时提炼模式、写交接笔记，下次启动由 hook 自动加载。内含 7 个 hooks（含 git/密钥守卫）、10 个 skills、4 个 agents 及子代理协作方法。无数据库、无服务、无 API key，声明非 Anthropic 官方项目。

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

- 记忆以带日期纯文本行存储，升级为规则/知识需用户逐项批准
- 7 个 hooks：会话启动加载记忆、压缩前保护、git/密钥守卫等
- 提供子代理协作方法：先写 spec 文件，报告视为待验证输入
- 每客户独立文件夹，记忆与工作文档分离

## 适用场景

- 让 Claude Code 跨会话记住客户偏好与项目上下文
- 多客户工作时代理按客户文件夹隔离读取文档
- 对子代理产出做事实核查再采信

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: Claude Memory Kit is a Claude Code plugin that gives your coding agent a memory made of plain text files in your own
> L26: How Claude Memory Kit works: you talk, the agent writes plain files in your folder, hooks load them at the next sta
> L42: /plugin marketplace add awrshift/agent-memory-kit

## 星数曲线

```mermaid
xychart-beta
    title "awrshift/agent-memory-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-29 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d8734c2d4fa0` · [字段定义](../../DATASET.md)*
