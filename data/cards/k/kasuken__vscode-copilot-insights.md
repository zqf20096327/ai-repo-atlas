# kasuken/vscode-copilot-insights

⭐ 38 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/kasuken/vscode-copilot-insights) · [官网](https://marketplace.visualstudio.com/items?itemName=emanuelebartolesi.vscode-copilot-insights) · 个人维护

**VS Code 扩展：查看 GitHub Copilot 配额与 AI 额度使用趋势**

Copilot Insights 是一个 VS Code 扩展，在侧边栏和状态栏本地展示 GitHub Copilot 账户的套餐、配额、重置窗口与 AI 额度消耗。核心机制：记录观测点之间的余额下降形成本地使用时间线（非逐请求日志，项目归因为估算），提供燃尽图、账期对比、加权预测、消耗速率分析与突增提醒；支持个人预算与工作日历配速建议。限制：数据依赖 GitHub 计费延迟，非实时；历史保留默认 7 天且上限 5,000 区间。从 VS Code Marketplace 安装。

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

- 侧边栏展示套餐、配额、重置窗口与超额状态
- 本地使用时间线与每日汇总，支持突增提醒与消耗速率分析
- 按项目/分支归因额度消耗（本地估算）
- Copilot Chat 集成：#copilotQuota 工具与 @insights 参与者问答

## 适用场景

- 随时查看 Copilot AI 额度剩余与重置时间
- 按账期对比额度消耗、判断是否超速使用
- 把额度消耗归因到具体项目与分支
- 导出使用历史做记录或分享

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5:  See your GitHub Copilot plan, quotas, reset window, and AI credit usage trends directly inside VS Code.
> L9: Copilot Insights gives you a fast, local view of the quota and entitlement data already associated with your GitHub 

## 星数曲线

```mermaid
xychart-beta
    title "kasuken/vscode-copilot-insights 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-25 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `89e47127cd05` · [字段定义](../../DATASET.md)*
