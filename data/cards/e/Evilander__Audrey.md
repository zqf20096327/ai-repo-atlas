# Evilander/Audrey

⭐ 26 · JavaScript · MIT · 推送 2026-09-20 · [GitHub](https://github.com/Evilander/Audrey) · [官网](https://www.npmjs.com/package/audrey) · 个人维护

**给 Codex 与 Claude Code 加持久记忆与行动前核查的本地引擎**

Audrey 以 npm 包安装在 Codex / Claude Code 旁，通过 hooks 形成记忆闭环：会话开始注入记忆简报，提交 prompt 时召回项目事实与偏好，副作用工具执行前 Guard 按精确命令指纹核查既往失败，事后记录结果并关联回执。记忆分层为情节/语义/程序性，保留矛盾标注，支持基于仓库路径与脚本名的 Grounding 校验（audrey ground）、整合（audrey dream）、提升为仓库规则与快照导入导出。要求 Node.js 22.16+ 或 24+，SQLite 内置于 Node，演示场景无需 API key 与网络。默认基础设施故障时 fail-open，可用环境变量切换 fail-closed。

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

- Guard 在 PreToolUse 按精确动作指纹核查既往失败，只读命令静默放行
- audrey ground 校验记忆引用的路径/脚本是否仍存在，失效记忆降置信而非删除
- 记忆分层（情节/语义/程序性）带置信度、来源与矛盾标注
- 一条 npm 全局安装命令接入 Codex / Claude Code，无需 API key 即可运行 demo

## 适用场景

- 让编码 agent 跨会话记住部署命令修复、仓库规范等事实，避免重复犯错
- 在执行有副作用的命令前自动核查是否命中既往失败记录
- 把学到的习惯提升为团队可评审的仓库规则文件

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L22: Audrey sits beside the agent and participates in the work automatically. At the start of a session it brings back a
> L52: |Bash/edit/write is proposed|Checks exact prior failures, trusted rules, procedures, contradictions, and memory hea

## 星数曲线

```mermaid
xychart-beta
    title "Evilander/Audrey 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-29 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `7a3e7cbc8770` · [字段定义](../../DATASET.md)*
