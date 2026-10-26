# PromptEngineer48/laya-vs-jev-arena

⭐ 30 · JavaScript · MIT · 推送 2026-09-22 · [GitHub](https://github.com/PromptEngineer48/laya-vs-jev-arena) · 个人维护

**让两个 AI 模型在游戏竞技场实时对战的评测基准**

由 Prompt Engineer 48 视频衍生的模型对比基准：让两个模型（开源本地的 Laya 与 TypeSafe 闭源 API 的 Jev，或任意下拉选择的模型）在贪吃蛇竞速、格斗、Runner、Flappy、Tetris 五个竞技场中实时做决策，每步操作均为模型输出。两侧接收相同输入与问题、共享种子与按较慢方延迟推导的统一节奏以保证公平；导出 JSON 记录得分、decisions/s、p50/p95 延迟与 token 用量。提供 Docker 一键部署与人机对战模式；运行 Jev 需 TypeSafe API key，Laya 首次调用需下载检查点约 30–60 秒。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 贪吃蛇/格斗/Runner/Flappy/Tetris 五个竞技场，每步均为模型真实决策
- 公平规则：同种子、按较慢方延迟共享节奏、开局预热不计加载时间
- 导出 JSON 含得分、decisions/s、p50/p95 延迟与 token 用量
- 支持人机对战与双人同键盘，Docker 一键部署 Human vs Jev

## 适用场景

- 在相同输入下对比两个模型的实时决策能力与延迟
- 自己出种子复现或扩展模型游戏对战实验
- 在自有服务器上人机对战体验模型表现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L70: `server.py` serves the page and exposes two backends that take the **same**
> L75: |`POST /api/laya`|`laya.Router` in-process|`pip install laya`; first call loads the checkpoints|
> L108: `Export JSON` writes score, apples, survival, decisions, decisions/s, p50/p95 latency

## 星数曲线

```mermaid
xychart-beta
    title "PromptEngineer48/laya-vs-jev-arena 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-26 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `68c239bdcc68` · [字段定义](../../DATASET.md)*
