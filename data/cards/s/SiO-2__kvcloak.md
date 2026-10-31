# SiO-2/kvcloak

⭐ 22 · Python · Apache-2.0 · 推送 2026-02-28 · [GitHub](https://github.com/SiO-2/kvcloak) · 组织维护

**LLM 推理 KV-cache 隐私保护的攻击与防御研究代码**

NDSS 2026 论文 "Shadow in the Cache" 的官方实现，面向安全研究人员：包含三种从 KV-cache 还原用户输入的攻击实现（Inversion/Collision/Injection）及配套防御机制 KV-Cloak（对 KV-cache 加密保护），支持攻击准确率评估与性能基准测试。在 Llama-3.2-1B 上测试，防御后攻击指标显著下降，保护开销低于 AES 加密路径。攻击脚本需显式传 --i-understand-risks 才能运行。提供 conda/pip 环境搭建流程与 pytest 测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种 KV-cache 攻击实现：Inversion、Collision、Injection
- KV-Cloak 防御对 KV-cache 加密，附性能基准（与 AES/DP 对比）
- 攻击脚本需 --i-understand-risks 显式确认才能执行
- 提供路径校验等安全工具函数与 pytest 测试

## 适用场景

- 评估 LLM 推理系统 KV-cache 的隐私泄露风险
- 研究并复现论文中的攻击与防御实验
- 对比 KV-cache 加密方案的防护效果与开销

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L25: KV-CLOAK is a privacy-preserving protection mechanism for Key-Value (KV) caches in Large Language Model (LLM) infer
> L27: - **Inversion Attack**: Reconstructs input tokens from KV-cache
> L29: - **Injection Attack**: Injects malicious prompts to extract information

## 星数曲线

```mermaid
xychart-beta
    title "SiO-2/kvcloak 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6469c30d565a` · [字段定义](../../DATASET.md)*
