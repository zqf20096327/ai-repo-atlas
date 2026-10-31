# 19PINE-AI/programmable-kv

⭐ 16 · Python · Apache-2.0 · 推送 2026-06-29 · [GitHub](https://github.com/19PINE-AI/programmable-kv) · [官网](https://01.me/research/programmable-kv/) · 组织维护

**KV 缓存可编辑可组合机制的论文及复现代码与结果**

arXiv:2606.17107 论文（33 页）的官方仓库，含 LaTeX 源码、交互式配套网站、实验系统（esys/e1/e2）、可独立安装的 editkv 可编辑 KV 模块、用户记忆应用（mem）与全部结果 JSON 记录。研究发现 prefill 阶段模型已把字段相关结论写入下游聚合 token 的 KV 上，据此提出以一行 erratum 就地编辑缓存与 RoPE 重定位复用技能缓存两种操作，并在在线服务场景报告吞吐与 TTFT 数据。面向 LLM 推理与可解释性方向的研究者，实验在单张 RTX PRO 6000 上运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提出 KV 缓存即"记忆化结论笔记本"的机制解释，跨四个模型家族复现
- editkv 模块：就地编辑 + erratum 的可独立安装 Python 包
- 可组合技能缓存：O(L) 时间预编译并 RoPE 重定位到任意上下文
- 提供交互式配套网站与全部结果 JSON 记录供核验

## 适用场景

- 复现论文中缓存编辑与组合实验
- 研究 KV 缓存内部机制与注意力电路
- 基于 editkv 模块构建可编辑上下文的原型

## 场景标签

 · 领域:LLM 推理/可解释性研究

## 证据(README 行号)

> L10: > 📄 **Paper:** arXiv:2606.17107 (33 pp.)
> L54: |`results/`|Result records (JSON) — the source of every number in the paper and on the site; see `results/README.md

## 星数曲线

```mermaid
xychart-beta
    title "19PINE-AI/programmable-kv 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b9c3c572cb2f` · [字段定义](../../DATASET.md)*
