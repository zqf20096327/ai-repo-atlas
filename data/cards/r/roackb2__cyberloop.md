# roackb2/cyberloop

⭐ 15 · TypeScript · NOASSERTION · 推送 2026-04-12 · [GitHub](https://github.com/roackb2/cyberloop) · 个人维护

**给 AI Agent 加中间件控制层的 TypeScript 框架**

CyberLoop 是用 TypeScript 编写的 agent 中间件框架：将任意 agent 包装进可组合的中间件栈，通过 beforeStep/afterStep 钩子（洋葱模型）在每一步观察、注释并纠正行为，而无需修改 agent 核心逻辑。内置预算控制、遥测日志、评测中间件，以及基于控制论与微分几何的三个几何控制中间件（EKF+PID 运动学、流形 PCA、Grassmann 子空间跟踪），并附 Wikipedia 导航 Demo（嵌入+PID，无 LLM）。安装方式为 git clone 源码 + yarn install，需配置 OPENAI_API_KEY。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 中间件栈以 beforeStep/afterStep 钩子包装任意 agent，洋葱模型执行
- 预算/步数/token/费用停止控制与结构化遥测
- 三个几何控制中间件：kinematics/manifold/grassmannian，基于 AICL 研究项目
- 三层 API：Opaque / Steppable / Advanced（含嵌入与参考轨迹的漂移检测）

## 适用场景

- 给已有 agent 加预算、日志与护栏等控制行为
- 通过漂移检测与轨迹跟踪监控 agent 执行过程
- 用嵌入+PID 做无 LLM 的导航类任务实验

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: **CyberLoop** is a TypeScript middleware framework for AI agents. It wraps any agent
> L141: Each middleware hooks into the step with `beforeStep` / `afterStep`. Metadata flows

## 星数曲线

```mermaid
xychart-beta
    title "roackb2/cyberloop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `06a90688fb33` · [字段定义](../../DATASET.md)*
