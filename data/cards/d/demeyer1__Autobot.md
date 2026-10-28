# demeyer1/Autobot

⭐ 23 · Shell · MIT · 推送 2026-10-02 · [GitHub](https://github.com/demeyer1/Autobot) · [官网](https://demeyer1.github.io/Autobot/) · 组织维护

**在 Mac 上为 ChatGPT/Codex 加载的开源 agent harness**

MIT 开源项目（v0.5.0），以 agent harness 形式加载到 Mac 上 ChatGPT 或 Codex 的本地 Project 中，提供分层磁盘记忆、按关系/用途划分的四档隐私分区（PRIVATE/FAMILY_FRIENDS/WORK/SHARED）、独立于生产者的完成校验器（五阶段证据链与目的地回读）、一分钟存活监督器，以及通过 Computer Use 的洁净外部写入策略。随附 6 个可移植技能。非独立模型或网关，依赖宿主 ChatGPT/Codex 的计划与权限限制；安装通过发布 ZIP 与 INSTALL_FOR_AI.md 完成。

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

- 四档隐私分区，默认不自动跨区共享
- 五阶段证据链 + 独立校验器的完成验证机制
- 磁盘分层记忆与持久检查点，可中断续作
- 对连接器默认只读、写入走第一方应用的 fail-closed 策略

## 适用场景

- 给 Mac 上的 ChatGPT/Codex 加持久记忆与隐私分区
- 长任务可靠完成：阶段证据与目的地回读校验
- 跨天任务中断后由替代 worker 续作

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L59: 2. **The AutoBot workspace:** the operating contract in `AGENTS.md`, privacy zones, selective memory, project statu
> L61: AutoBot is an agent harness, not a separate model, chatbot, or agent gateway. It depends on current ChatGPT and Cod
> L140: An agent harness supplies the operating rules, memory, tools, state and verification around a model. AutoBot adds 

## 星数曲线

```mermaid
xychart-beta
    title "demeyer1/Autobot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `da6a2423fb88` · [字段定义](../../DATASET.md)*
