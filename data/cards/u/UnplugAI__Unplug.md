# UnplugAI/Unplug

⭐ 45 · Python · Apache-2.0 · 推送 2026-10-16 · [GitHub](https://github.com/UnplugAI/Unplug) · [官网](https://unplug-ai.org) · 组织维护

**LLM 应用安全 SDK：注入检测、来源追踪与工具调用管控**

面向 LLM 应用的 agent 运行时安全 Python SDK：以 TaintedText 追踪文本来源（用户/检索/工具输出），用正则+规范化做离线注入检测，可选 ML span 模型 unplug-tiny-v1 提升召回；在工具调用前执行策略检查（破坏性操作阻断、污点内容转人工审查），并以 span 级脱敏替代整体拦截。README 给出基准数据与局限：正则路径 F1 0.52，加 ML 模型后 F1 0.97；在更广的良性语料上误报率最高达 34%，需自调阈值。检测当前仅针对英语调优。另提供 MCP server、GitHub Action 与规划中的自托管 API（付费层）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- TaintedText 来源追踪与会话污点管理
- 正则+规范化注入检测（离线、零 ML 依赖）与可选 ML span 模型
- 工具调用策略执行：破坏性操作阻断、污点转审查
- span 级脱敏与流式/长文档滑动窗口扫描

## 适用场景

- 在 agent 流水线中扫描并包裹不可信内容防注入
- 工具调用前做策略检查阻断破坏性操作
- 对含敏感信息的输出做 span 级脱敏

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: Unplug is agent runtime security for LLM applications. It tracks where text came from (user vs retrieved vs tool out
> L32: App and agent code imports from the top-level package (`from unplug import Guard`).

## 星数曲线

```mermaid
xychart-beta
    title "UnplugAI/Unplug 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-30 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1fd0e2ec3fcd` · [字段定义](../../DATASET.md)*
