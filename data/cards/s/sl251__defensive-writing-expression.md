# sl251/defensive-writing-expression

⭐ 3 · Python · MIT · 推送 2026-11-19 · [GitHub](https://github.com/sl251/defensive-writing-expression) · 个人维护 · 中文 README

**给中文用户制造 GPT 式过度防御性表达的 Agent Skill**

面向支持 Agent Skills 客户端的中文使用者，以 SKILL.md 为入口的写作风格 Skill：将用户输入的文字改写或回答为带分级免责、边界限定的防御性表达，支持 0–5 级防御强度、五种防御逻辑、荒诞度与自知度参数，覆盖 Rewrite/Respond/Task 三种任务模式并可叠加角色融合。默认不主动启用，需明确请求。仓库含 64 条测试场景与基于 Python 标准库的评测脚本；项目自述为刻意夸张的写作风格实验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 0–5 级防御强度与五种防御逻辑（可混合）
- Rewrite/Respond/Task 三种任务模式，可叠加 Persona 角色融合
- 64 条测试场景与 Python 标准库评测脚本（无额外依赖）
- 多轮继承与退出，说“不要防御性”即切到 0 级

## 适用场景

- 把一句话改写成多级防御性的表达用于娱乐
- 在角色扮演中让角色带防御性说话习惯
- 按评测脚本检验输出的防御标记与重复情况

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: 一个专门制造 **GPT 式过度防御性表达** 的中文 Agent Skill。
> L27: |**0–5 级防御强度**|从正常直说到连免责声明都要免责，默认三级|
> L46: 将仓库完整复制或克隆到支持 Agent Skills 的客户端的 Skills 目录，确保 `SKILL.md` 与 `references/`、`scripts/`、`tests/` 等文件保持原有相对位置。

## 星数曲线

```mermaid
xychart-beta
    title "sl251/defensive-writing-expression 星数(近 2 点)"
    x-axis ["2026-11-20", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-20 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `b552bd9e5085` · [字段定义](../../DATASET.md)*
