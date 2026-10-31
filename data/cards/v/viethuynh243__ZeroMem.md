# viethuynh243/ZeroMem

⭐ 14 · Python · MIT · 推送 2026-09-05 · [GitHub](https://github.com/viethuynh243/ZeroMem) · 个人维护

**为 Claude Code 提供零 token 长期记忆的确定性检索技能**

独立实现的 Claude Code 技能：索引用户本机的会话转录文件（~/.claude/projects/**/*.jsonl），构建实体-上下文图与时间层级，以 BM25（基于 scipy.sparse）与 numpy 矩阵最近邻等确定性操作完成召回，记忆管线全程无 LLM 调用与网络请求。附加论文之外设计的弃答门控（指出语料不含答案并列出缺失词）、弱结果探针、常驻索引的本地召回守护进程（暖召回约提速 18 倍）与测量报告套件。安装后通过 CLI（build/recall/update/serve）操作，仅依赖 numpy、scipy、regex，稠密编码层为可选。

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

- 记忆管线全程无 LLM 调用：BM25 基于 scipy.sparse、最近邻为 numpy matmul、实体抽取用正则
- 弃答门控：语料不含答案时明确报告并列出缺失词（20/20 不可答问题被弃答，0 次假回答）
- 索引 ~/.claude/projects 只读；摄取时强制脱敏且无关闭开关
- 本地召回守护进程：暖召回 1.7s 对冷启动 34s（约 18×）

## 适用场景

- 让 Claude Code 记住并检索我过往会话中做过的事
- 查询历史会话中的 bug 处理与决策证据
- 要求系统在历史里没有相关信息时直接说不知道

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L18: ZeroMem is an independent, from-scratch Claude Code skill: it indexes your own
> L20: for recall using deterministic, token-free memory operations — **no LLM call
> L43: The only model in the loop is Claude, reading what the pipeline returns.

## 星数曲线

```mermaid
xychart-beta
    title "viethuynh243/ZeroMem 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d65ce4227904` · [字段定义](../../DATASET.md)*
