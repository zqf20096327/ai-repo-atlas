# microsoft/What-I-Did-Copilot

⭐ 51 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/microsoft/What-I-Did-Copilot) · 组织维护

**GitHub Copilot 使用量与影响力报告生成工具**

读取本机的 Copilot CLI 与 VS Code Copilot Chat 会话日志，生成 HTML 影响力报告：产出物分类统计、20+ 角色的技能增益映射、9 种工作模式分布、活动热力图、基于 13 篇同行评审文献的人力估算方法，以及引用 Anthropic/OpenAI/GitHub 指引的额度消耗模式检测。本地优先，无遥测；AI 语义分析为可选（经 gh CLI 调用 GitHub Models API，无 API 时退化为本地启发式估算）。提供 Copilot CLI 插件、VS Code 聊天插件与源码克隆三种运行方式，核心代码仅依赖 Python 标准库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取本地 Copilot 会话日志生成 HTML 影响力报告
- 基于 13 篇同行评审来源的工时/杠杆估算方法
- 额度消耗模式检测，每个检测项引用 Anthropic/OpenAI/GitHub 已发布指引
- 本地优先：无遥测、无云端上传，AI 分析可选并有本地启发式回退

## 适用场景

- 查看过去 7/14/30 天我与 Copilot 协作做了什么
- 向管理层展示 Copilot 席位的产出与杠杆
- 定位额度消耗模式以优化使用习惯

## 场景标签

 · 领域:开发者工具/AI 使用分析

## 证据(README 行号)

> L5: ### One command. See everything you built with Copilot — and the leverage you're getting from your seat.
> L92: |📐 **Estimation evidence**|Transparent methodology grounded in 13 peer-reviewed sources. *Why should anyone trust t
> L133: - **Reads only local files** &mdash; session logs from `~/.copilot/session-state/` (Copilot CLI) and `<AppData>/Co

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/What-I-Did-Copilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-25 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `1952e3598e5b` · [字段定义](../../DATASET.md)*
