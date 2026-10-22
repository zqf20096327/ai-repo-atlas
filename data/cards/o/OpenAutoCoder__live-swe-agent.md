# OpenAutoCoder/live-swe-agent

⭐ 467 · MIT · 推送 2026-01-19 · [GitHub](https://github.com/OpenAutoCoder/live-swe-agent) · 组织维护

**运行时自我演化的软件工程 agent 脚手架，供 LLM 评测**

构建在 mini-swe-agent 框架之上的软件工程 agent 脚手架：在处理真实 issue 时于运行时扩展与修订自身能力。用于在 SWE-bench Verified 与 SWE-Bench Pro 上评测各 LLM，附带排行榜与可下载的完整轨迹、补丁和结果数据集。安装方式为先安装 mini-swe-agent，再以自定义 YAML 配置（livesweagent.yaml）运行 mini 命令。作者团队来自学术界（arXiv 预印本署名）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 运行时自我扩展/修订自身能力的 agent 脚手架
- 对 SWE-bench Verified 与 SWE-Bench Pro 的完整评测轨迹、补丁与结果可下载
- 统一脚手架下对不同模型做对比评测的排行榜
- 以 mini-swe-agent 配置文件形式使用

## 适用场景

- 在统一脚手架下评测不同 LLM 的软件工程能力
- 复现 SWE-bench 上的完整运行轨迹与补丁
- 向社区排行榜提交模型评测结果

## 场景标签

`Agent 框架` `编码 Agent` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L13: Live-SWE-agent is the **first *live*, runtime self-evolving software engineering agent** that expands and revises i
> L27: Live-SWE-agent not only demonstrates that a minimal, open, and live scaffold already has the ability to outperform 
> L39: We built Live-SWE-agent on top of the popular mini-swe-agent framework with very minimal modifications.

## 星数曲线

```mermaid
xychart-beta
    title "OpenAutoCoder/live-swe-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 466 --> 468
    line [467, 467]
```

2026-10-18 467 → 2026-10-21 467（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `755ea72cab05` · [字段定义](../../DATASET.md)*
