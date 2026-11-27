# LukshinVI/game-of-the-day

⭐ 7 · Python · MIT · 推送 2026-11-22 · [GitHub](https://github.com/LukshinVI/game-of-the-day) · 个人维护

**为 0–3 岁家庭每日推送 LLM 生成并经校验的儿童游戏**

生产运行的消息推送服务：每天为照护者生成一个适龄儿童发展活动，经确定性门槛（schema、年龄技能带、危险词、去重）与小模型安全审查双线校验后经 Telegram/VK 投递，并收集按钮/文字/语音反馈。小模型从反馈中抽取带逐字引文的观察项，代码构建儿童画像用于次日选题。LLM 只提议，交付状态机、幂等、重试、安全策略均由确定性代码持有。语音经 Whisper 转写。README 声明非医疗/诊断产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双线安全校验：确定性门槛 + 小模型年龄清单审查，被拒候选不投递
- LLM 仅提议，状态机/幂等/重试/画像由确定性代码持有
- 反馈抽取的每条观察须含逐字引文并通过代码核验
- 选题 evals 支持多模型对比，记录每次模型调用的时延/成本/结果

## 适用场景

- 每天给孩子收到一个适龄的家庭活动建议
- 在 Telegram/VK 里一键反馈，让后续游戏跟着调整
- 学习 LLM 生产工作流的架构参考

## 场景标签

`工作流自动化` `模型评测` `语音识别` · 领域:效率与自动化

## 证据(README 行号)

> L6: A small production service that sends a caregiver one safe, age-appropriate developmental activity for a young child
> L128: **LLMs are used for:**
> L131: - **Safety review:** a small model reviews each activity that passed the deterministic gate against an age checkli

## 星数曲线

```mermaid
xychart-beta
    title "LukshinVI/game-of-the-day 星数(近 3 点)"
    x-axis ["2026-11-19", "2026-11-20", "2026-11-27"]
    y-axis "stars" 5 --> 8
    line [6, 7, 7]
```

2026-11-19 6 → 2026-11-27 7（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `108f462f7794` · [字段定义](../../DATASET.md)*
