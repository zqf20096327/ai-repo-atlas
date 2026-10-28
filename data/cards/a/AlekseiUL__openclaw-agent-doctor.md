# AlekseiUL/openclaw-agent-doctor

⭐ 25 · Shell · MIT · 推送 2026-10-26 · [GitHub](https://github.com/AlekseiUL/openclaw-agent-doctor) · [官网](https://t.me/Sprut_AI) · 个人维护

**OpenClaw 代理的自诊断技能：检查 7 类系统并给出修复建议**

面向 OpenClaw 用户与维护者的自诊断技能（skill）：对 memory、crons、config、agent 文件、gateway、系统环境与安全共 7 类系统做只读检查，识别 28+ 常见问题并给出带风险评估的修复建议，修复需用户确认。附 10 个使用场景、28 条问题-方案数据库、安装指南与可在终端/CI 运行的 bash 脚本，声明 0 外部依赖，支持 macOS/Linux/Windows。以 git clone 方式安装到 skills 目录。

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

- 7 类系统、28+ 常见问题的只读检查
- 修复建议附风险评估，所有修复需确认
- 附 auto-diagnostic.sh，可脱离代理在终端/CI 运行
- 0 外部依赖，支持每日 cron 定时诊断

## 适用场景

- OpenClaw 更新后做一次全面体检
- 代理行为异常时先诊断再改配置
- 顾问检查客户代理而不导出隐私数据
- 通过 cron 每日定时自检

## 场景标签

 · 领域:AI 代理运维/诊断工具

## 证据(README 行号)

> L28: **Agent Doctor** - an OpenClaw skill that:
> L29: - ✅ Checks 7 system categories (memory, crons, config, files, gateway, system, security)

## 星数曲线

```mermaid
xychart-beta
    title "AlekseiUL/openclaw-agent-doctor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `810976cd7355` · [字段定义](../../DATASET.md)*
