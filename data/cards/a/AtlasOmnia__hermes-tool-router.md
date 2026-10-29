# AtlasOmnia/hermes-tool-router

⭐ 132 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/AtlasOmnia/hermes-tool-router) · [官网](https://hermesagenttools.com/) · 组织维护 · 中文 README

**Hermes Agent 插件：首轮确定性收敛工具面以降低 token 开销**

面向 Hermes Agent 的独立实验性插件，在首轮对话前通过确定性规则或可选的小型分类器收敛工具 schema，减少发送给主模型的首轮 token 开销；不确定时 fail-open 保留完整工具面，后续按需永久补加工具集，会话粘性不复裁剪。分类器默认关闭，可接入 OpenRouter 做首轮意图分类。README 明确标注实验性质，建议先在独立 profile 测试，且列出多项已知限制（恢复丢弃宿主新增工具、注册表移除后无法按名加载等）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 首轮确定性/可选分类器路由收敛工具 schema
- fail-open：不确定、超时、输出无效时保留完整工具面
- 可选 OpenRouter 小分类器，仅用于首轮分类请求
- 附带 python diagnostics.py 诊断脚本（退出码 0/2 判定路由可用性）

## 适用场景

- 工具集很多的 Hermes Agent 降低首轮 token 与延迟成本
- 在保留模型能力感知（'what can you do?'）前提下裁剪工具面
- 用 /router off 随时关闭路由而不调用模型

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: Experimental standalone Hermes Agent plugin for reducing first-turn tool-schema overhead without repeatedly changing
> L13: The router classifies only the first turn. High-confidence routes send a smaller tool schema to the main model; unc
> L21: OpenRouter is used only for the small first-turn classification request; it does not replace your main Hermes model

## 星数曲线

```mermaid
xychart-beta
    title "AtlasOmnia/hermes-tool-router 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-10-29"]
    y-axis "stars" 131 --> 133
    line [132, 132]
```

2026-10-28 132 → 2026-10-29 132（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bc06f8cf35b1` · [字段定义](../../DATASET.md)*
