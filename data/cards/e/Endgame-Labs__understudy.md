# Endgame-Labs/understudy

⭐ 8 · Rust · MIT · 推送 2026-11-21 · [GitHub](https://github.com/Endgame-Labs/understudy) · 组织维护

**CPU-only LLM 代理：学习重复问题的答案以减少上游调用**

一个部署在应用与上游 System One 模型（Jev、Rune、Clef）之间的 HTTP 代理。转发每个请求的同时，对每个重复问题训练小型 CPU 模型（understudents）；当某个本地模型通过 Wilson 下界等统计门槛后，该问题由本地直接回答，并持续抽样审计，漂移即降级。适用于窄域重复决策（分类、路由、门控、triage），不适用于大状态空间或双文本比较类问题。支持 forward/shadow/serve/race 四种模式，Rust 编写，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 每请求训练小型 CPU 模型，毕业问题由本地直接回答
- 持续抽样审计，Wilson 下界判定毕业与降级
- 四种运行模式：forward/shadow/serve/race
- 11 种 understudent 设计竞争同一问题类型

## 适用场景

- 大规模重复调用上游模型时降低账单开销
- 对支持工单分类、错误检测等窄域决策做本地化应答
- 上游模型缓慢或不可达时继续服务已毕业问题

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: Understudy forwards each request to the lead and trains small CPU models, *understudents*, on the lead's answers: an
> L73:    understudy serve --lead-url <your lead's /v1/systemone URL>

## 星数曲线

```mermaid
xychart-beta
    title "Endgame-Labs/understudy 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-08", "2026-11-28"]
    y-axis "stars" 4 --> 9
    line [5, 7, 8]
```

2026-11-02 5 → 2026-11-28 8（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `77e64697e171` · [字段定义](../../DATASET.md)*
