# imlrz/InMind

⭐ 18 · Python · 推送 2026-07-30 · [GitHub](https://github.com/imlrz/InMind) · 组织维护

**面向长记忆 agent 的 125 任务评测基准**

InMind 是一个评测长期记忆 agent 的基准数据集：检验 agent 能否在后续查询仅通过世界知识与某条用户事实间接关联时，正确调用该事实（即“隐式关联盲点”）。125 个任务、10 个领域、全合成用户事实，每任务包含直接回忆查询与语义距离较远的应用查询配对，以分离存储、检索、路由与端到端记忆使用等失败原因。数据以 JSON Lines 格式提供并附 JSON Schema，仓库含评测脚本、judge 提示词、agent 技能清单与 arXiv 论文；基线适配器与仓库许可证尚在路线图中未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 125 任务、10 领域，用户事实全部合成
- 直接/间接查询配对设计，分离存储、检索、路由、应用四类失败
- 含固定 LongMemEval-s 背景轨迹、middle-injection 工具与 judge 提示词
- 提供 coding agent 可执行的 SKILL.md 集成清单

## 适用场景

- 评测我的记忆系统的隐式关联检索能力
- 诊断错误回答究竟出在存储、检索还是路由环节
- 在研究中引用该基准对比记忆系统表现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8: InMind is a 125-task benchmark for evaluating whether long-term-memory agents can apply a previously stated user fac
> L74: ```bash
> L77: wc -l benchmark/dataset/inmind.jsonl

## 星数曲线

```mermaid
xychart-beta
    title "imlrz/InMind 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a4fef1504f58` · [字段定义](../../DATASET.md)*
