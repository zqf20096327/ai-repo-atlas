# hyperspaceai/jevcache

⭐ 78 · 推送 2026-09-19 · [GitHub](https://github.com/hyperspaceai/jevcache) · [官网](https://jevcache.sh) · 组织维护

**Jev 类模型的决策缓存：本地记忆化决策，实现确定性重放**

面向 TypeSafe Jev 类模型的决策缓存 CLI：将决策视为 (model, schema, state) 的纯函数并本地记忆化，recall 只查本地账本、decide 未命中时转发到配置的后端（local|jev|mock）并缓存。状态先经脱敏与规范化再计算指纹，PII 与易变字段不进入键。支持发布/合并缓存包与托管全局索引共享决策，recall 未命中时退出码 3 以便 CI 分支判断。单一 Rust 静态二进制（约 2–3 MB），macOS/Linux arm64/x64 可用；声明与 TypeSafe 无关联。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- recall 仅查本地账本、decide 未命中转发后端并缓存（JEVCACHE_BACKEND=local|jev|mock）
- 状态脱敏与规范化后再取指纹，PII 与易变字段不进入缓存键
- publish/add 以纯 JSON 包共享缓存，托管全局索引仅传输指纹与答案
- 嵌入式零依赖存储（内存 map + 追加日志），单二进制无运行时

## 适用场景

- 重复调用相同 Jev 决策时避免重复计费
- CI 中用 replay 与 fixtures 检测模型漂移
- 团队或社区间共享已产生的决策缓存

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **The decision ledger for Jev-class models.** A Jev decision is (approximately) a pure
> L28: ledger only (never a backend); `decide()` recalls, then on a miss routes to your configured

## 星数曲线

```mermaid
xychart-beta
    title "hyperspaceai/jevcache 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 76 --> 79
    line [77, 78, 78]
```

2026-10-18 77 → 2026-10-27 78（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `6a69676a293b` · [字段定义](../../DATASET.md)*
