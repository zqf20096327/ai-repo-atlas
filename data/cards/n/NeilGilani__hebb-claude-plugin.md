# NeilGilani/hebb-claude-plugin

⭐ 15 · Python · Apache-2.0 · 推送 2026-10-03 · [GitHub](https://github.com/NeilGilani/hebb-claude-plugin) · [官网](https://hebb-site.pages.dev) · 个人维护

**让 Claude Code/Codex 从失败命令中学习的记忆插件**

Claude Code 与 OpenAI Codex 的插件：通过 hooks 监听会话中的 shell 命令，当某命令失败且随后有可用替代时，将其记为一条教训；下次会话在命令运行前拦截已知会失败的命令并交给 Claude 可用的替代命令。支持通过自然语言设定硬性命令禁令（按 shell 解析方式匹配，含变体与编码绕过尝试），跨会话记住用户偏好，所有变更记录在 SHA-256 链式日志中可查篡改。默认本地模式（~/.hebb，Claude Code 与 Codex 共享），可选 key 同步团队并在 dashboard 审批；附带的 hebb-memory 研究库可将事实写入冻结开源模型。

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

- 失败命令→可用命令的自动学习与运行前拦截
- 按 shell 解析方式匹配的硬性命令禁令（覆盖 -f/--force、base64、eval 等变体）
- SHA-256 链式本地历史日志，篡改可检测
- 本地模式无需 key，数据留在 ~/.hebb；团队共享需 key 并经审批

## 适用场景

- 让我的编码助手记住这台机器上哪些命令不可用
- 一次设定禁令，阻止助手运行危险命令如 git push --force
- 团队内共享踩坑教训，新成员的助手直接受益

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L13:  Claude Code plugin
> L75: 1. **It watches.** Hooks see every shell command Claude runs and whether it worked.
> L251: |Hebb key (optional)|Leave it empty for local mode. To add or change it, open `/plugin`, pick hebb and update its 

## 星数曲线

```mermaid
xychart-beta
    title "NeilGilani/hebb-claude-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `89ca20c206e8` · [字段定义](../../DATASET.md)*
