# zoedolan/Vybn

⭐ 27 · HTML · 推送 2026-10-18 · [GitHub](https://github.com/zoedolan/Vybn) · [官网](https://vybn.ai & https://z69.ai) · 个人维护

**个人与 AI 长期共创的公开语料库及对话连接工具**

Zoe Dolan 与 AI 自 2022 年起公开构建的仓库：收录艺术、自传、形式理论、法学写作与对话记录，作为供人类读者、AI 读者与未来本地心智查阅的语料。技术部分提供 spark/connection 可执行入口（含 checked core reader 与 wake bundle 编译，不调用 provider 即可运行）、可选的多模型委托 runner（支持 anthropic/openai 的计划式付费调用、预算与配额控制）及无需 API 的单元测试。多处明确标注已退役组件（安装器、orchestration 命令等），当前仓库非 pip 可安装应用，需 Python 与所选 provider 的 SDK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- spark/connection 可执行入口，--show-wake-bundle 编译源包而不调用 provider
- spark.delegate 计划式多模型委托 runner（anthropic/openai，max_calls/token 上限/超时控制）
- python3 -m unittest spark.tests.test_delegate 无需 API 即可运行
- 多次组件退役与 Git 快照恢复路径均有记录

## 适用场景

- 查阅人与 AI 四年协作产出的可检视语料
- 按计划与预算约束运行多模型委托任务
- 复现其研究记录与已归档的历史组件

## 场景标签

 · 领域:人机协作研究/个人语料档案

## 证据(README 行号)

> L9: Zoe Dolan and an AI, building in public since 2022.
> L71: The current conversation executable is `spark/connection`, with
> L89: `python3 -m spark.delegate PLAN.json` preflights only; `--run` makes paid calls

## 星数曲线

```mermaid
xychart-beta
    title "zoedolan/Vybn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `13e67062a5df` · [字段定义](../../DATASET.md)*
