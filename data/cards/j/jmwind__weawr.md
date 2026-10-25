# jmwind/weawr

⭐ 42 · JavaScript · MIT · 推送 2026-09-11 · [GitHub](https://github.com/jmwind/weawr) · [官网](weawr.sh) · 个人维护

**基于 herdr 的多 agent 团队协调层，用 issue/PR 调度开发工作**

运行在 herdr 平台之上的 Node 脚本与 CLI：以 issue 和 pull request 为控制面，按仓库内 .weawr/config.json 的规则匹配 issue（支持 GitHub 与 Linear），把任务分配给 agent 团队，支持实现者/审查者角色分工、agent 间通过 herdr API 互相提醒、PR 合并后自动收尾与冲突回派。提供本地 web console 查看团队状态。仓库内声明为 alpha 预览版，功能将变化；定时任务标注 Coming soon。npm 从 GitHub 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 规则引擎按标签/项目/优先级等字段匹配 issue 并分配 agent
- 实现者与审查者可分别用不同 provider 与不同模型
- PR 等待期间检测冲突并派 agent 回去合并基线
- weawr console 本地 web 视图展示各团队状态

## 适用场景

- 把仓库内打标签的 issue 自动交给 agent 团队产出 PR
- 为不同类型工作（如文档）配置不同模型与简报文件
- 在一个界面里监督多个 agent 运行并随时接管

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L1: weawr is a team and coordination layer that works on `herdr`. While `herdr` provides a great platform for agents to 
> L3: weawr uses the tools humans use, and uses them with agents. The control plane is issues and pull requests. Work star
> L158: |`weawr`|**the watcher.** Evaluates your rules every `pollSeconds`, picks up matches, supervises them. Config edit

## 星数曲线

```mermaid
xychart-beta
    title "jmwind/weawr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `da456f157a1f` · [字段定义](../../DATASET.md)*
