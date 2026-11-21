# vadympetryshyn/effort-pilot

⭐ 9 · TypeScript · MIT · 推送 2026-11-20 · [GitHub](https://github.com/vadympetryshyn/effort-pilot) · 个人维护

**按轮次自动设置 Claude Code 推理强度的插件**

以 Claude Code 插件形式分发：每轮发送前由 Haiku 小模型读取消息并分类到计划/分析/构建/问答等阶段，对应设置 high/medium/low 推理强度，不可回退操作（push/deploy）固定为 high；支持口语切换模型与强度、按阶段命名模型的流水线、子代理独立强度、状态条展示选择原因，以及 /effort-pilot report 对比统计。作者自测称快问最多快约 2 倍、token 至多省 10%，并注明数据来自其自身会话、需自行测量。依赖较新的 Claude Code 版本；在部分模型/网关场景下自动停用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每轮按消息内容自动选择推理强度（Haiku 分类，约 $0.0004/轮）
- 自然语言切换模型与强度，支持分阶段流水线与子代理独立强度
- /effort-pilot report 输出成本/速度/质量对比图表
- 在会破坏 prompt cache 的场景自动停用（stand aside）

## 适用场景

- 让 Claude Code 会话中计划用高强度、问答用低强度
- 用一句话为长任务不同阶段指定不同模型与强度
- 统计插件对 token 消耗与响应速度的影响

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L34: /plugin marketplace add vadympetryshyn/effort-pilot
> L62: Before each turn a small, fast model (Haiku, ≈ $0.0004 a turn) reads your message and picks the effort:
> L110: |`managedModels`|`opus,fable`|models whose effort it sets (never where effort is one setting per request: see abov

## 星数曲线

```mermaid
xychart-beta
    title "vadympetryshyn/effort-pilot 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-12", "2026-11-21"]
    y-axis "stars" 7 --> 10
    line [8, 9, 9]
```

2026-11-08 8 → 2026-11-21 9（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `43ccb4efacc3` · [字段定义](../../DATASET.md)*
