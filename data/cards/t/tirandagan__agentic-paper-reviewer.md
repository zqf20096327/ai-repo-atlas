# tirandagan/agentic-paper-reviewer

⭐ 3 · Python · MIT · 推送 2026-11-20 · [GitHub](https://github.com/tirandagan/agentic-paper-reviewer) · [官网](https://github.com/tirandagan/agentic-paper-reviewer/blob/main/docs/USER_GUIDE.md) · 个人维护

**为论文作者在 Claude Code 中生成有据可查的审稿报告**

以 Claude Code 插件形式安装运行，读取用户的论文 PDF，执行 10 阶段流水线：全文读取、生成 arXiv 查询、检索相关工作、按相关度筛选、收集证据、按固定模板起草审稿意见、强制批判性修订、7 维度打分后经 ICLR 2025 人类评分拟合的 rescale 校准，输出 Markdown 审稿报告与分数 JSON。每条弱点须引用原文语句或 arXiv ID（grounding gate），支持文献截止日期与自排除。运行需 python3（3.8+，仅标准库）与 arXiv 访问，无需 API key。定位为作者自查工具，非同行评审替代品。

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

- 10 阶段 agentic 流水线：PDF 读取→arXiv 检索→证据收集→起草→批判→打分
- grounding gate：每条弱点须引用原文短语或 arXiv ID，无法溯源则丢弃或标注
- 7 维度锚定 1–10 打分，经 14 篇 ICLR 2025 论文拟合的 rescale 映射到人类评分尺度
- 文献截止（literature cutoff）防止引用评审时点之后的工作

## 适用场景

- 投稿前自查论文的过强声明、缺失基线与未引用的竞争工作
- 修改稿后重跑，查看各评分维度的变化
- 被拒后获得一份更详细的第三方视角解读

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L28: This plugin brings that approach into Claude Code, so an author can run it on
> L107: It needs `python3` (3.8 or later; standard library only) and access to


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `e36e289a388c` · [字段定义](../../DATASET.md)*
