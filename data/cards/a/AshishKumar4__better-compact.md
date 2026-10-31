# AshishKumar4/better-compact

⭐ 16 · TypeScript · AGPL-3.0 · 推送 2026-10-12 · [GitHub](https://github.com/AshishKumar4/better-compact) · [官网](https://github.com/AshishKumar4/Better-Compact#readme) · 个人维护

**为 Claude Code 等编码代理做分级上下文修剪的插件集**

面向 OpenCode、Oh My Pi、pi 与 Claude Code 的上下文压缩插件与 CLI：不像单摘要式压缩一次性替换旧对话，而是分阶段修剪——先替换重复读取与陈旧工具流量为动作存根，再移除旧推理，必要时用侧模型调用折叠部分助手轮次，最后以滚动前缀摘要兜底。原始历史写入磁盘并在上下文中插入可读引用。以 npm 包形式分发，提供三档预设与斜杠命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分阶段修剪：工具流量→推理→助手轮摘要→滚动前缀摘要
- 原始历史保留在磁盘并插入模型可读引用
- 三档预设（light/moderate/max）定义触发阈值与目标上下文
- 四类宿主适配器共用同一修剪引擎（@better-compact/core）

## 适用场景

- 长会话编码代理中按需缩减上下文而非一次性摘要替换
- 压缩后仍能回查原始工具输出与用户措辞
- 为 OpenCode / OMP / pi / Claude Code 统一配置压缩行为

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Better Compact turns full agent context into a smaller working set through staged pruning.
> L142: |`@better-compact/cli`|Claude Code session CLI|
> L214: |Host|Application model|Durable history|

## 星数曲线

```mermaid
xychart-beta
    title "AshishKumar4/better-compact 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d411376ddae3` · [字段定义](../../DATASET.md)*
