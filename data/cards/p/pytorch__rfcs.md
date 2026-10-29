# pytorch/rfcs

⭐ 154 · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/pytorch/rfcs) · 组织维护

**PyTorch 官方 RFC 流程文档仓库：功能设计提案的提交与评审规范**

PyTorch 官方维护的 Requests for Comments 仓库，存放向 PyTorch 提议功能变更所需的设计提案文档与流程说明。贡献者 fork 仓库、复制模板填写提案，经 draft/commenting 标签流转获取核心贡献者反馈，达成共识后合并并进入实现阶段；被拒提案以 shelved 标签关闭。RFC 作者无实现义务，任何开发者均可认领已接受 RFC 的实现。流程借鉴 Rust、React 与 Artsy 的 RFC 流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 RFC-0000 模板用于撰写设计提案
- 定义 draft/commenting 标签与核心贡献者评审流转
- shelved 标签标记暂缓评估的提案
- 接受的 RFC 在主仓库关联 issue 跟踪实现

## 适用场景

- 向 PyTorch 提交大型功能或抽象层的设计提案
- 查找已被接受或搁置的 PyTorch 设计提案
- 了解如何认领并实现某个已接受的 RFC

## 场景标签

 · 领域:深度学习框架/开源治理

## 证据(README 行号)

> L1: This page contains instructions on how to propose and implement feature changes to PyTorch.
> L5: To propose a new feature, you’ll submit a Request For Comments (RFC). This RFC is basically a design proposal where 

## 星数曲线

```mermaid
xychart-beta
    title "pytorch/rfcs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 153 --> 155
    line [154, 154]
```

2026-10-18 154 → 2026-10-29 154（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `fd406eb6335a` · [字段定义](../../DATASET.md)*
