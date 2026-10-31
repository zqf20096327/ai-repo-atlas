# Tencent-Hunyuan/RepoProbe

⭐ 14 · Python · NOASSERTION · 推送 2026-08-06 · [GitHub](https://github.com/Tencent-Hunyuan/RepoProbe) · 组织维护 · 中文 README

**仓库级代码理解评测基准：500 道源自 GitHub Discussions 的开放题**

腾讯混元团队发布的 ASE 2026 论文配套评测基准：从 50 个仓库的 1.5 类编程语言的 GitHub Discussions 中提取 500 道开放式架构理解问题，答案通过加权检查表协议逐项核验（9 分知识项 + 1 分清晰度项），替代标量 LLM-as-a-Judge 评分。评测以 Docker 隔离的 agent 脚手架运行，50 个上游仓库不随数据分发、需按锁定 commit 自行克隆。论文评估了 20 个模型（13 闭源、7 开源），最佳满分率 27.5%。面向 LLM 研究与评测人员使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 500 道来自真实 GitHub Discussions 的开放性问题，覆盖 50 仓库、15 种语言
- 检查表式核验协议：原子化、加权、可部分给分的技术事实项
- Docker 隔离、脚手架无关的 agent 评测容器契约
- 源码 Apache-2.0，基准数据 CC BY 4.0，含个人数据脱敏处理

## 适用场景

- 评测 LLM/agent 对仓库级架构的理解能力
- 研究流利度与正确性偏差等 LLM 回答质量问题
- 以可核验检查表替代标量 LLM 评分的评测方法参考

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L18: RepoProbe is a discussion-based benchmark for repository-level code understanding. Unlike
> L24: Answers are graded by a **Checklist-Based Verification Protocol** that decomposes each
> L33: |Questions|500 (3–30 per repository, median 8)|

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-Hunyuan/RepoProbe 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5689e28a57b1` · [字段定义](../../DATASET.md)*
