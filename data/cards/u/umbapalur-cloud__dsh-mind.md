# umbapalur-cloud/dsh-mind

⭐ 4 · JavaScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/umbapalur-cloud/dsh-mind) · 个人维护 · 中文 README

**为 DeepSeek Shell/Cordis 提供记忆、自我觉知与上下文压缩插件**

面向 DeepSeek Shell / Cordis 框架的插件，整合自我觉知、经验库与压缩引擎三部分：压缩前把日记、状态、原文存档写入 `~/.dsh/mind` 下不被压缩触及的文件，压缩后可通过 `mind_expand`/`mind_search` 取回被折叠的原文；经验库只注入命中的手写准则（最多 3 条）；`mind_intend` 让模型声明当前追求。提供 7 个工具，需手动在 profile 层接线替换宿主压缩引擎，跨会话记忆已拆分至 `dsh-strand`（软依赖）。Windows junction 方式安装，MIT 许可，零运行时依赖。

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

- 压缩前落盘日记/状态/存档，压缩后可按 seq 取回原文
- 经验库条件匹配注入，最多 3 条，命中才进上下文
- 7 个 mind_* 工具：声明追求、查看窗口、搜索压缩存档、主动排队压缩
- 662 项回归测试与反向验证脚本，测试硬隔离在临时目录

## 适用场景

- 让 DSH/Cordis agent 在上下文压缩后仍保留自我状态与可回取的原文
- 为 agent 手写条件性经验准则并按信号命中注入
- 排查「记忆没生效」：查看注入情况、预算与开关

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: 把 **跨会话脉络**、**经验库**、**自我觉知** 合成一个插件 —— 一套状态、一条注入、一条推送、一个预算。
> L111:   name: dsh-mind/compaction    # 从 @deepseek-ai/dsh-compaction-basic 换成这个

## 星数曲线

```mermaid
xychart-beta
    title "umbapalur-cloud/dsh-mind 星数(近 3 点)"
    x-axis ["2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-25 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `b0ea68b2f4d2` · [字段定义](../../DATASET.md)*
