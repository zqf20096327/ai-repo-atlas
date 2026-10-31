# waitdeadai/llm-dark-patterns

⭐ 22 · Shell · Apache-2.0 · 推送 2026-07-26 · [GitHub](https://github.com/waitdeadai/llm-dark-patterns) · [官网](https://github.com/waitdeadai/llm-dark-patterns/blob/main/METHODOLOGY.md) · 组织维护

**Claude Code 钩子套件：在文本边界拦截 LLM 输出中的暗模式行为**

面向 Claude Code 高级操作者的伞形仓库，聚合一组单一职责的 Stop/事件钩子与规则包，在模型输出文本边界以确定性代码（非 LLM 裁判）检测并拦截谄媚、家长式口吻、虚假成功、许可循环、过早收尾等暗模式。提供英/西/波兰语 locale 包、破坏性命令面规则包（7 面 56 模式）、证据二进制白名单（200+），用户可用 .txt 文件免 fork 扩展；另含 Rust 物理引擎的收尾检测适配器。已在 MAD 数据集上做 F1 实证评估并公开结果与失效分析；明确声明仅捕捉文本签名而非底层倾向。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性代码裁判在 Claude Code 钩子边界检查输出文本，非另一次 LLM 调用
- 规则包覆盖 locale、破坏性命令面（56 模式）、证据二进制白名单（200+）
- 13 个检测钩子映射 MAST 14 种失效模式中的 8 种，含 MAD 数据集 F1 实证结果
- 用户放置 .txt 文件即可免 fork 扩展覆盖面

## 适用场景

- 长会话中拦截模型过早收尾或虚假成功声明
- 守护 kubectl/terraform/force-push 等破坏性操作面的收尾文本
- 按 MAST 分类对照排查多智能体系统失效模式

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L8: > A suite of single-purpose Claude Code hooks that suppress LLM dark-pattern defaults — sycophancy, paternalism, fal
> L23: The shared architecture is out-of-band textual enforcement at Claude Code hook
> L58: The **LLM Dark Patterns Hooks** suite is the out-of-band complement: deterministic judges that inspect the model's 

## 星数曲线

```mermaid
xychart-beta
    title "waitdeadai/llm-dark-patterns 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f5fda81aaee5` · [字段定义](../../DATASET.md)*
