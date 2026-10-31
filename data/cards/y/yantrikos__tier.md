# yantrikos/tier

⭐ 14 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/yantrikos/tier) · [官网](https://zenodo.org/records/19228710) · 个人维护

**按模型规模自适应路由工具的 Python SDK，提升小模型工具调用准确率**

面向 AI agent 开发者的工具路由 SDK：将工具按模型参数规模分为 S/M/L/XL 四档，自动检测模型 tier 并以不同粒度呈现工具定义——小模型用 Hybrid 策略（少量详细+其余仅名称，省 97% token），大模型用相关性重排，超大模型呈现全量。工具导出为 OpenAI/Ollama 原生格式，注册时校验各档描述与参数完整性。基准基于 Ollama /api/chat 的 1,000+ 次原生工具调用（4 模型、80 工具）；另以 OpenClaw 插件形式提供生产集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按模型规模分四档（S/M/L/XL）自适应工具呈现策略
- Hybrid 策略在小模型上减少 97% 工具 token
- 工具导出为 OpenAI/Ollama 原生格式，适配 /api/chat
- ClawHub 提供 OpenClaw 网关集成插件

## 适用场景

- 在小参数模型上运行多工具 agent 时降低工具 token 消耗
- 同一套工具定义适配从 0.8B 到 35B+ 的异构模型
- 复现工具路由基准（80 工具、50 提示、4 模型）

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L59: **Adapt the interface, not the model.** Different model sizes get different tool presentations:
> L165: The `TierRouter` selects the best strategy per tier:
> L215: The Tier plugin is available on ClawHub as a code plugin. It integrates the SDK with OpenClaw's gateway, automatic

## 星数曲线

```mermaid
xychart-beta
    title "yantrikos/tier 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `49ef2db9a7e5` · [字段定义](../../DATASET.md)*
