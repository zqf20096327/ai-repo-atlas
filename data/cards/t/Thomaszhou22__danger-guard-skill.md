# Thomaszhou22/danger-guard-skill

⭐ 10 · Shell · MIT · 推送 2026-11-15 · [GitHub](https://github.com/Thomaszhou22/danger-guard-skill) · 个人维护 · 中文 README

**AI agent 危险命令拦截与告警的安全防护技能**

以 SKILL.md/配置文件形式部署的 agent 安全层：在命令执行前按黑名单分级拦截（Tier 1 拦截并要求密码验证，Tier 2 需确认），覆盖 rm -rf、dd 写盘、fork 炸弹、git push --force、DROP TABLE 等模式，并识别中英文自然语言删除指令；通过 Feishu/Telegram/Discord 等消息通道发送告警，提供 account-hacked 紧急协议与白名单机制。安装后自动写入 MEMORY.md/AGENTS.md 形成三层防护，另提供 shell 包装脚本与 git hooks。限制：依赖 agent 加载或配置文件生效，无独立运行形态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两级拦截规则（密码验证 / 确认）覆盖文件系统、磁盘、权限、RCE 等类别
- 中英文自然语言危险指令的语义检测
- 安装后自动写入 MEMORY.md/AGENTS.md/配置 JSON 的三层加固
- 提供 OpenClaw/Claude Code/Codex/Cursor/Copilot 等工具的配置文件与 git hooks

## 适用场景

- 防止被盗的消息账号指挥 agent 执行破坏性命令
- 为多个 AI 编码工具统一配置危险命令防护
- 为 force push、SQL 删除等操作增加确认环节
- 账号疑似被盗时记录命令并触发紧急告警

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: AI agent safety shield. Intercepts dangerous commands before execution, requires password verification, and sends al
> L51: |**OpenClaw**|`SKILL.md`|`~/.openclaw/skills/danger-guard/`|

## 星数曲线

```mermaid
xychart-beta
    title "Thomaszhou22/danger-guard-skill 星数(近 2 点)"
    x-axis ["2026-11-23", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-23 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 mid · 依据 README sha `3f321584d038` · [字段定义](../../DATASET.md)*
