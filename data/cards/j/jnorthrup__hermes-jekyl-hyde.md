# jnorthrup/hermes-jekyl-hyde

⭐ 19 · Python · 推送 2026-08-17 · [GitHub](https://github.com/jnorthrup/hermes-jekyl-hyde) · 个人维护

**Hermes agent 插件：审计会话完成度缺口并生成可验证下一步行动**

面向 hermes-agent 的插件，每 N 个非平凡轮次（默认 7）派生一次性的审计角色：审计克隆产出证据审查，辩护克隆据此提出最小具体续接计划或指认外部阻塞，仲裁者给出 genuine/sandbagged/uncertain 判定（证据不足默认 uncertain）。通过 pre_llm_call、transform_llm_output、post_llm_call 三个钩子注入，提供 arena/silent/mandate/heuristic/full 等六种运行模式与 /hyde 斜杠命令。状态持久化于 $HERMES_HOME/jekyll-hyde/ 下的 JSON/JSONL 文件，含最多 99 条推脱模式池与追加式审计日志。安装方式为 git clone 到插件目录后启用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每 N 轮派生双克隆审计+仲裁者判定 genuine/sandbagged/uncertain
- 六种运行模式：透明注入/静默监控/清洁指令/计划对比/墓碑压缩等
- 状态持久化含 99 条推脱模式池与追加式 JSONL 审计日志
- 仅在可直接观察到安抚承诺+目标转移时升级措辞，辅助判定不足以触发

## 适用场景

- 监控 agent 编码会话中的拖延、配额摊薄与表演性顺从
- 在每轮产出与工具证据间核验完成度缺口
- 以最小具体续接指令推动 agent 完成未竟工作
- 后台静默收集会话审计遥测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: **A Hermes plugin that audits completion gaps and drives verified next actions.**
> L61: Every N-th turn (default 7), the plugin forks disposable audit roles. Clone 1
> L130: |`pre_llm_call`|Before each LLM turn|Ingests mailbox defenses into excuse pool. Checks the turn gate. If activated

## 星数曲线

```mermaid
xychart-beta
    title "jnorthrup/hermes-jekyl-hyde 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2d6bdd19a135` · [字段定义](../../DATASET.md)*
